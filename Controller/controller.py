from Modelle.gekochtergericht import GekochterGericht
from Modelle.getrank import Getrank
from Modelle.kunde import Kunde
from Modelle.bestellung import Bestellung


class RestaurantController:
    def __init__(self, gericht_repo, getrank_repo, kunde_repo, bestellung_repo):
        self.gericht_repo = gericht_repo
        self.getrank_repo = getrank_repo
        self.kunde_repo = kunde_repo
        self.bestellung_repo = bestellung_repo


    def hinzufugen_gericht(self, name, portionsgrosse, preis, zubereitungszeit, gericht_id):
        gericht = GekochterGericht(id=gericht_id, name=name, portionsgrosse=portionsgrosse, preis=preis,zubereitungszeit=zubereitungszeit)
        self.gericht_repo.add_cooked_dish(gericht)   # se adauga mancare nou in date
        return gericht


    def hinzufugen_getrank(self, name, portionsgrosse, preis, alkoholgehalt, getrank_id):
        getrank = Getrank(id=getrank_id, name=name, portionsgrosse=portionsgrosse, preis=preis,alkoholgehalt=alkoholgehalt)
        self.getrank_repo.add_drink(getrank)   #se adauga bautura noua in date
        return getrank


    def hinzufugen_kunde(self, kunden_id, name, adresse):
        new_customer = Kunde(id=kunden_id, name=name, adresse=adresse)
        self.kunde_repo.add_customer(new_customer)  # se adauga clientul nou in date
        return new_customer


    def suche_kunde_teilname(self, teilname):
        kunden = self.kunde_repo.load()   # incarca lista de clienți
        gefunden = list(filter(lambda kunde: teilname.lower() in kunde.name.lower(), kunden))    # filtrare dupa o parte a numelui
        if not gefunden:
            print("Kunde nicht gefunden.")
            return
        print("Kunde gefunden:")
        for kunde in gefunden:
            print(f"ID: {kunde.id}, Name: {kunde.name}, Adresse: {kunde.adresse}")


    def suche_kunde_teiladresse(self, teiladresse):
        kunden = self.kunde_repo.load()  # incarca lista de clienți
        gefunden = list(filter(lambda kunde: teiladresse.lower() in kunde.adresse.lower(), kunden))  # filtrare dupa o parte a adresei
        if not gefunden:
            print("Kunde nicht gefunden.")
            return
        print("Kunde gefunden:")
        for kunde in gefunden:
            print(f"ID: {kunde.id}, Name: {kunde.name}, Adresse: {kunde.adresse}")


    def aktualisiere_kunden_name(self, kunden_id, neuer_name):
        kunden = self.kunde_repo.load()  # incarca lista de clienți
        for kunde in kunden:
            if kunde.id == kunden_id:
                kunde.name = neuer_name
                break
        self.kunde_repo.save(kunden)    # actualizează numele clientului
        print("Kundenname erfolgreich aktualisiert")


    def platziere_bestellung(self, bestellungs_ids, kunden_id, gericht_ids, getrank_ids):
        gesamtkosten = Bestellung.berechnen_kosten(gericht_ids, getrank_ids, self.gericht_repo, self.getrank_repo)    # calculeaza costul total al comenzii
        neue_bestellung = Bestellung(id=bestellungs_ids, kunden_id=kunden_id, gericht_ids=gericht_ids, getrank_ids=getrank_ids, gesamtkosten=gesamtkosten)  #creeaza o noua comanda
        self.bestellung_repo.add_order(neue_bestellung)
        rechnung_string = neue_bestellung.generiere_rechnung_string(self.gericht_repo, self.getrank_repo)  # genereaza și returneaza factura
        return rechnung_string


    def zeige_bestellungs_rechnung(self, bestellungs_id):
        bestellung = self.bestellung_repo.find_bestellung_by_id(bestellungs_id)   # gasește comanda in date
        if bestellung:
            bestellung.display_invoice(self.gericht_repo, self.getrank_repo)  # afișeaza factura
        else:
            print("Bestellung nicht gefunden.")

    def delete_kunde(self, kunden_id):
        kunden = self.kunde_repo.load()
        kunde = self.kunde_repo.del_kunden_id(kunden_id, kunden)
        if kunde:
            kunden.remove(kunde)   # stergem  clientul cu ID dat de la tastatura
            self.kunde_repo.save(kunden)
            return True
        return False

    def delete_bestellung(self, bestellung_id):
        bestellungen = self.bestellung_repo.load()
        bestelung = self.bestellung_repo.del_bestellung_id(bestellung_id,bestellungen)
        if bestelung:
            bestellungen.remove(bestelung)   # stergem comanda cu ID dat de la tastatura
            self.bestellung_repo.save(bestellungen)
            return True
        return False

    def delete_gericht(self, gericht_id):
        gerichte = self.gericht_repo.load()
        gericht = self.gericht_repo.del_gericht_id(gericht_id,gerichte)
        if gericht:
            gerichte.remove(gericht)   # stergem mancarea cu ID dat de la tastatura
            self.gericht_repo.save(gerichte)
            return True
        return False

    def delete_getrank(self, getrank_id):
        getranken = self.getrank_repo.load()
        getrank = self.getrank_repo.del_getrank_id(getrank_id,getranken)
        if getrank:
            getranken.remove(getrank)  # stergem bautura cu ID dat de la tastatura
            self.getrank_repo.save(getranken)
            return True
        return False

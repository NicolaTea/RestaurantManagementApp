from Modelle.identifizierbar import  Identifizierbar
from functools import reduce


class Bestellung(Identifizierbar):
    def __init__(self, id, kunden_id, gericht_ids, getrank_ids, gesamtkosten):
        super().__init__(id)
        self.kunden_id = kunden_id
        self.gericht_ids = gericht_ids
        self.getrank_ids = getrank_ids
        self.gesamtkosten = gesamtkosten

    @staticmethod
    def berechnen_kosten(gericht_ids, getrank_ids, gericht_repo, getrank_repo):
        gerichte_preise = [gericht_repo.find_by_id(gericht_id).preis for gericht_id in gericht_ids if gericht_repo.find_by_id(gericht_id) is not None]
        getranke_preise = [getrank_repo.find_by_id(getrank_id).preis for getrank_id in getrank_ids if getrank_repo.find_by_id(getrank_id) is not None]
        gesamtpreis = reduce(lambda x, y: x + y, gerichte_preise + getranke_preise, 0)
        return gesamtpreis

    def generiere_rechnung_string(self, gericht_repo, getrank_repo):
        invoice_string = "Rechnung:\n"
        for gericht_id in self.gericht_ids:
            gericht = gericht_repo.find_by_id(gericht_id)
            if gericht:
                invoice_string += f"{gericht.name} - {gericht.preis} lei\n"
            else:
                print(f"Gericht mit ID {gericht_id} nicht gefunden.")

        for getrank_id in self.getrank_ids:
            getrank = getrank_repo.find_by_id(getrank_id)
            if getrank:
                invoice_string += f"{getrank.name} - {getrank.preis} lei\n"
            else:
                print(f"Getränk mit ID {getrank_id} nicht gefunden.")

        invoice_string += f"Gesamtkosten: {self.gesamtkosten} lei\n"
        return invoice_string

    def display_invoice(self, gericht_repo, getrank_repo):
        invoice_string = self.generiere_rechnung_string(gericht_repo, getrank_repo)
        print(invoice_string)


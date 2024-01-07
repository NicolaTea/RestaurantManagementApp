
class Restaurant_ui:
    def __init__(self, controller):
        self.controller = controller

    def display_gericht(self):
        gerichte = self.controller.gericht_repo.load()
        print("=== Gerichte ===")
        for gericht in gerichte:
            print(f"ID: {gericht.id}, Name: {gericht.name}, Portionsgröße: {gericht.portionsgrosse} g, Preis: {gericht.preis} lei, Zubereitungszeit: {gericht.zubereitungszeit} min")

    def display_getrank(self):
        getranke = self.controller.getrank_repo.load()
        print("=== Getränke ===")
        for getrank in getranke:
            print(f"ID: {getrank.id}, Name: {getrank.name}, Portionsgröße: {getrank.portionsgrosse} ml, Preis: {getrank.preis} lei, Alkoholgehalt: {getrank.alkoholgehalt}%")

    def display_kunde(self):
        kunden = self.controller.kunde_repo.load()
        print("=== Kunden ===")
        for kunde in kunden:
            print(f"ID: {kunde.id}, Name: {kunde.name}, Adresse: {kunde.adresse}")

    def display_bestellung(self):
        bestellungen = self.controller.bestellung_repo.load()
        print("=== Bestellungen ===")
        for bestellung in bestellungen:
            print(f"ID-Bestellung: {bestellung.id}, ID-Kunde: {bestellung.kunden_id}, Gerichte: {bestellung.gericht_ids}, Getränke: {bestellung.getrank_ids}, Cost total: {bestellung.gesamtkosten} lei")



    def menu(self):
        return '''
        === Menü ===
        1-Gericht hinzufügen
        2-Getränk hinzufügen
        3-Kunde hinzufügen
        4-Kunde suchen nach Teilnamen
        5-Kunde suchen nach Teiladresse
        6-Kundenname aktualisieren
        7-Bestellung aufgeben
        8-Rechnung generieren
        9-Display Gericht
        10-Display Getrank
        11-Display Kunde
        12-Display Bestellung
        13-Delete Gericht   
        14-Delete Getrank
        15-Delete Kunde
        16-Delete Bestellung
        0-Beenden
        '''

    def run(self):
        while True:
            print(self.menu())
            option = int(input('Bitte wählen Sie eine Option: '))

            if option == 1:
                gericht_id = int(input("Geben Sie die ID des Gerichts ein: "))
                name = input('Name eingeben: ')
                portionsgrosse = float(input('Portionsgröße eingeben: '))
                preis = float(input('Preis eingeben: '))
                zubereitungszeit = float(input("Zubereitungszeit eingeben: "))
                new_gericht = self.controller.hinzufugen_gericht(name, portionsgrosse, preis, zubereitungszeit, gericht_id)
                print(f"Gericht hinzugefügt: ID - {new_gericht.id},Name - {new_gericht.name}, Portionsgröße - {new_gericht.portionsgrosse}, Preis - {new_gericht.preis}, Zubereitungszeit - {new_gericht.zubereitungszeit}")

            elif option == 2:
                getrank_id = int(input("Geben Sie die ID des Getränks ein: "))
                name = input('Name eingeben: ')
                portionsgrosse = float(input("Portionsgröße eingeben: "))
                preis = float(input("Preis eingeben: "))
                alkoholgehalt = float(input("Alkoholgehalt eingeben: "))
                new_getrank = self.controller.hinzufugen_getrank(name, portionsgrosse, preis, alkoholgehalt, getrank_id)
                print(f"Getränk hinzugefügt: ID - {new_getrank.id},Name - {new_getrank.name}, Portionsgröße - {new_getrank.portionsgrosse}, Preis - {new_getrank.preis}, Alkoholgehalt - {new_getrank.alkoholgehalt}")

            elif option ==3:
                gerichte = int(input("Kunden-ID: "))
                name = input('den Name eingeben: ')
                adresse = input('die Adresse eingeben: ')
                new_kunde = self.controller.hinzufugen_kunde(gerichte, name, adresse)
                print(f"Kunde hinzugefügt: ID - {new_kunde.id}, Name - {new_kunde.name}, Adresse - {new_kunde.adresse}")

            elif option == 4:
                teilname = input("Teilname: ")
                matching_kunden = self.controller.suche_kunde_teilname(teilname)
                if matching_kunden:
                    print("Kunden gefunden:")
                    for kunde in matching_kunden:
                        print(f"Kunde: ID - {kunde.id}, Name - {kunde.name}, Adresse - {kunde.adresse}")

            elif option == 5:
                teiladresse = input("Teiladresse: ")
                matching_kunden = self.controller.suche_kunde_teiladresse(teiladresse)
                if matching_kunden:
                    print("Kunden gefunden:")
                    for kunde in matching_kunden:
                        print(f"Kunde: ID - {kunde.id}, Name - {kunde.name}, Adresse - {kunde.adresse}")

            elif option == 6:
                gerichte = int(input("Kunden-ID: "))
                new_name = input("Neuer Name: ")
                self.controller.aktualisiere_kunden_name(gerichte, new_name)
                print('Name erfolgreich aktualisiert')

            elif option == 7:
                bestellung_ids=int(input("Bestellungs-ID: "))
                gerichte = int(input("Kunden-ID: "))
                gerichte_ids = [int(id) for id in input("Gericht-ID: ").split()]
                getranke_ids = [int(id) for id in input("Getränk-ID: ").split()]
                gesamtkosten = self.controller.platziere_bestellung(bestellung_ids,gerichte, gerichte_ids, getranke_ids)
                print(f"Bestellung aufgegeben: Gesamtkosten - {gesamtkosten}")

            elif option == 8:
                bestellung_id = int(input("Bestellungs-ID: "))
                rechnung = self.controller.zeige_bestellungs_rechnung(bestellung_id)
                print(rechnung)

            elif option == 9:
                self.display_gericht()

            elif option == 10:
                self.display_getrank()

            elif option == 11:
                self.display_kunde()

            elif option == 12:
                self.display_bestellung()

            elif option == 13:
                gericht = int(input("Geben Sie die zu löschende Gericht-ID ein: "))
                self.controller.delete_gericht(gericht)
                print(f"Gericht mit ID  {gericht} wurde gelöscht.")

            elif option == 14:
                getrank = int(input("Geben Sie die zu löschende Getrank-ID ein: "))
                self.controller.delete_getrank(getrank)
                print(f"Getrank mit ID  {getrank} wurde gelöscht.")

            elif option == 15:
                gerichte = int(input("Geben Sie die zu löschende Kunden-ID ein: "))
                self.controller.delete_kunde(gerichte)
                print(f"Kunde mit ID  {gerichte} wurde gelöscht.")

            elif option == 16:
                bestellung_id = int(input("Geben Sie die zu löschende Bestellungen-ID ein: "))
                self.controller.delete_bestellung(bestellung_id)
                print(f"Bestellung mit ID  {bestellung_id} wurde gelöscht.")

            elif option == 0:
                break

            else:
                print('Ungültige Option')
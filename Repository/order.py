from Repository.repository import PickleRepo
from Modelle.bestellung import Bestellung


class OrderRepo(PickleRepo):

    def add_order(self, new_order):
        existing_data = self.load()
        existing_data.append(new_order)
        self.save(existing_data)

    def find_bestellung_by_id(self, bestellung_id):
        bestellungen = self.load()
        for bestellung in bestellungen:
            if bestellung.id == bestellung_id:
                return bestellung
        print(f"Bestellung mit ID {bestellung_id} nicht gefunden.")

    def del_bestellung_id(self, bestellungen_id, bestellungen):
        for bestellung in bestellungen:
            if bestellung.id == bestellungen_id:
                return bestellung
        return None

    def convert_to_string(self, objekte):

        return '\n'.join([f"{o.id},{o.kunden_id},{','.join(map(str, o.gerichte_ids))},{','.join(map(str, o.getraenke_ids))},{o.gesamtkosten}" for o in objekte])

    def convert_from_string(self, string):

        lines = string.split('\n')
        bestellungen = []
        for line in lines:
            if line:
                o_id, kunden_id, gerichte_ids, getraenke_ids, gesamtkosten = line.split(',')
                bestellung = Bestellung(id=int(o_id), kunden_id=int(kunden_id),
                                        gericht_ids=list(map(int, gerichte_ids.split(','))),
                                        getrank_ids=list(map(int, getraenke_ids.split(','))),
                                        gesamtkosten=float(gesamtkosten))
                bestellungen.append(bestellung)
        return bestellungen




from Repository.repository import PickleRepo
from Modelle.gekochtergericht import GekochterGericht


class CookedDishRepo(PickleRepo):

    def add_cooked_dish(self, new_cooked_dish):
        existing_data = self.load()
        existing_data.append(new_cooked_dish)
        self.save(existing_data)

    def find_by_id(self, dish_id):
        dishes = self.load()
        for dish in dishes:
            if dish.id == dish_id:
                return dish

        return None

    def del_gericht_id(self, gericht_id, dishes):
        for gericht in dishes:
            if gericht.id == gericht_id:
                return gericht
        return None

    def convert_to_string(self, objekte):

        return '\n'.join([f"{d.id},{d.name},{d.portionsgroesse},{d.preis},{d.zubereitungszeit}" for d in objekte])

    def convert_from_string(self, string):

        lines = string.split('\n')
        gerichte = []
        for line in lines:
            if line:
                d_id, name, portionsgrosse, preis, zubereitungszeit = line.split(',')
                gericht = GekochterGericht(id=int(d_id), name=name, portionsgrosse=float(portionsgrosse),
                                    preis=float(preis), zubereitungszeit=float(zubereitungszeit))
                gerichte.append(gericht)
        return gerichte



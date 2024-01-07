from Repository.repository import PickleRepo
from Modelle.getrank import Getrank


class DrinkRepo(PickleRepo):

    def add_drink(self, new_drink):
        existing_data = self.load()
        existing_data.append(new_drink)
        self.save(existing_data)

    def find_by_id(self, drink_id):
        drinks = self.load()
        for drink in drinks:
            if drink.id == drink_id:
                return drink
        return None
    def del_getrank_id(self, getrank_id, drinks):
        for getrank in drinks:
            if getrank.id == getrank_id:
                return getrank
        return None



    def convert_to_string(self, objekte):

        return '\n'.join([f"{d.id},{d.name},{d.portionsgrosse},{d.preis},{d.alkoholgehalt}" for d in objekte])

    def convert_from_string(self, string):

        lines = string.split('\n')
        getranke = []
        for line in lines:
            if line:
                d_id, name, portionsgrosse, preis, alkoholgehalt = line.split(',')
                getrank = Getrank(id=int(d_id),name=name, portionsgrosse=float(portionsgrosse),preis=float(preis), alkoholgehalt=float(alkoholgehalt))
                getranke.append(getrank)
        return getranke


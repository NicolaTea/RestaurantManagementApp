from Modelle.gericht import Gericht


class Getrank(Gericht):
    def __init__(self, id, name, portionsgrosse, preis, alkoholgehalt):
        super().__init__(id, portionsgrosse, preis)
        self.name = name
        self.alkoholgehalt = alkoholgehalt

    def __str__(self):
        return f"Getrank: {self.id}, {self.name}, {self.portionsgrosse} ml, {self.preis} lei, {self.alkoholgehalt}%"

from Modelle.gericht import  Gericht


class GekochterGericht(Gericht):
    def __init__(self, id, name, portionsgrosse, preis, zubereitungszeit):
        super().__init__(id, portionsgrosse, preis)
        self.name = name
        self.zubereitungszeit = zubereitungszeit

    def __str__(self):
        return f"GekochterGericht: {self.id},{self.name},{self.portionsgrosse} g, {self.preis} lei, {self.zubereitungszeit} min"






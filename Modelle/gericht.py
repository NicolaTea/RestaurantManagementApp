from Modelle.identifizierbar import Identifizierbar


class Gericht(Identifizierbar):
    def __init__(self, id, portionsgrosse, preis):
        super().__init__(id)
        self.portionsgrosse = portionsgrosse
        self.preis = preis





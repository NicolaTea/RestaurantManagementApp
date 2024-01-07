from Modelle.identifizierbar import Identifizierbar


class Kunde(Identifizierbar):

    def __init__(self, id, name, adresse):
        super().__init__(id)
        self.name = name
        self.adresse = adresse

    def __str__(self):
        return f"Kunde: {self.id}, {self.name}, {self.adresse}"




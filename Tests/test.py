import unittest
from Controller.controller import RestaurantController

from Modelle.bestellung import Bestellung
from Modelle.getrank import Getrank
from Modelle.gekochtergericht import GekochterGericht
from Repository.drink import DrinkRepo
from Repository.order import OrderRepo
from Repository.customer import CustomerRepo
from Repository.cookeddish import CookedDishRepo



class Test(unittest.TestCase):
    def setUp(self):  #functie utilizata pentru a initializa orice resurse teste
        gericht_repo = CookedDishRepo('test_gericht.txt')
        getrank_repo = DrinkRepo('test_getrank.txt')
        kunde_repo = CustomerRepo('test_kunde.txt')
        bestellung_repo = OrderRepo('test_bestellung.txt')
        self.controller = RestaurantController(gericht_repo,getrank_repo,kunde_repo,bestellung_repo)


    def test_hinzufugen_gericht(self):  #trebuie in controller schimbata metoda add_cooked-dish cu save ca altfel nu merge cand se adauga prima data

        new_gericht = self.controller.hinzufugen_gericht('Mamaliga', 400, 30, 45, 7)
        found_gericht = self.controller.gericht_repo.find_by_id(new_gericht.id)
        self.assertIsNotNone(found_gericht, f"Gericht mit ID {new_gericht.id} ist nicht gefunden.")              # verifica ca found_gericht nu este None
        self.assertEqual(new_gericht.name, found_gericht.name, "Der Name des Gerichts stimmt nicht überein.")    # verifica ca doua valori sunt egale in cazul nostru numele mancarii

    def test_hinzufugen_getrank(self):  #trebuie in controller schimbata metoda add_drink cu save ca altfel nu merge cand se adauga prima data
        new_getrank=self.controller.hinzufugen_getrank('Vin',250,35,20,6)
        found_getrank = self.controller.getrank_repo.find_by_id(new_getrank.id)
        self.assertIsNotNone(found_getrank, f"Getrank mit ID {new_getrank.id} ist nicht gefunden.")             # verifica ca found_getrank nu este None
        self.assertEqual(new_getrank.name, found_getrank.name, "Der Name des Getrankes stimmt nicht überein.")  # verifica ca doua valori sunt egale in cazul nostru numele bauturii

    def test_aktualisiere_kunden_name(self):
        kunden_id = 3  # presupunem că exista un client cu ID 3
        name = "Bern Himmel"
        adresse = "Koln str3"
        self.controller.hinzufugen_kunde(kunden_id, name, adresse)
        new_name = "Luka Blau"
        self.controller.aktualisiere_kunden_name(kunden_id, new_name)
        updated_customer = self.controller.kunde_repo.find_kunden_id(kunden_id)
        self.assertEqual(updated_customer.name, new_name, "Der neue Kundenname wurde nicht korrekt aktualisiert.")

    def test_suche_kunde_teilname(self):
        kunden_id = 3  #adaugam un client nou
        name = "Franz Schoko"
        adresse = "Hamburg str1878"
        new_customer = self.controller.hinzufugen_kunde(kunden_id, name, adresse)
        self.assertIsNotNone(new_customer, "Der richtige Kunde wurde nicht hinzugefügt.")  #verificare adaugare client
        teilname = "Franz"
        self.controller.suche_kunde_teilname(teilname)  #cautam clientul dupa numele partial

    def test_suche_kunde_teiladresse(self):
        kunden_id = 4
        name = "Abelard Gunther"
        adresse = "Nurnberg str3567"
        new_customer = self.controller.hinzufugen_kunde(kunden_id, name, adresse)
        self.assertIsNotNone(new_customer, "Der richtige Kunde wurde nicht hinzugefügt.")   #verificare adaugare client
        teiladresse = "Nurnberg"
        self.controller.suche_kunde_teiladresse(teiladresse)   #cautam clientul dupa adresa partiala

    def test_generiere_rechnung_string(self):
        self.gericht_repo=CookedDishRepo('test_gericht.txt')
        self.getrank_repo=DrinkRepo('test_getrank.txt')
        self.gericht_repo.add_cooked_dish(GekochterGericht(id=1, name="Schnitzel", preis=20, portionsgrosse=345, zubereitungszeit=24))  #adaugam o mancare noua
        self.getrank_repo.add_drink(Getrank(id=3, name="Cola", preis=5, portionsgrosse=250, alkoholgehalt=0)) #adaugam o bautura noua
        gericht_ids = [1]
        getrank_ids = [3]
        gesamtkosten = 25
        bestellung = Bestellung(1, 1, gericht_ids, getrank_ids, gesamtkosten)  #creeam comanda
        bestellung.gericht_repo = self.gericht_repo
        bestellung.getrank_repo = self.getrank_repo
        rechnung_string = bestellung.generiere_rechnung_string(bestellung.gericht_repo,bestellung.getrank_repo) #generam factura
        self.assertIn("Schnitzel - 20 lei", rechnung_string)
        self.assertIn("Cola - 5 lei", rechnung_string)
        self.assertIn("Gesamtkosten: 25 lei", rechnung_string)




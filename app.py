from Ui.ui import Restaurant_ui
from Repository.cookeddish import CookedDishRepo
from Repository.drink import DrinkRepo
from Repository.customer import CustomerRepo
from Repository.order import OrderRepo
from Controller.controller import RestaurantController


def main():
    gericht_repo = CookedDishRepo('gerichte.txt')
    getrank_repo = DrinkRepo('getranke.txt')
    kunde_repo = CustomerRepo('kunden.txt')
    bestellung_repo = OrderRepo('bestellungen.txt')

    controller = RestaurantController(gericht_repo, getrank_repo, kunde_repo, bestellung_repo)
    ui = Restaurant_ui(controller)
    ui.run()


main()

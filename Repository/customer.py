from Repository.repository import PickleRepo
from Modelle.kunde import Kunde


class CustomerRepo(PickleRepo):

    def add_customer(self, new_customer):
        existing_data = self.load()
        existing_data.append(new_customer)
        self.save(existing_data)

    def find_kunden_id(self, kunden_id):
        kunden = self.load()
        for kunde in kunden:
            if kunde.id == kunden_id:
                return kunde

        return None

    def del_kunden_id(self, kunden_id, kunden):
        for kunde in kunden:
            if kunde.id == kunden_id:
                return kunde
        return None

    def convert_to_string(self, objekte):

        return '\n'.join([f"{k.id},{k.name},{k.adresse}" for k in objekte])

    def convert_from_string(self, string):

        lines = string.split('\n')
        kunden = []
        for line in lines:
            if line:
                k_id, k_name, k_adresse = line.split(',')
                kunde = Kunde(id=int(k_id), name=k_name, adresse=k_adresse)
                kunden.append(kunde)
        return kunden
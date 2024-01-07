import pickle
from abc import ABC, abstractmethod


class Datarepo(ABC):
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def save(self, objekte):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_to_file(self, string):
        pass

    @abstractmethod
    def convert_to_string(self, objekte):
        pass

    @abstractmethod
    def convert_from_string(self, string):
        pass

class PickleRepo(Datarepo):
    def save(self, objekte):
        with open(self.file, 'wb') as file:
            pickle.dump(objekte, file)

    def load(self):
        try:
            with open(self.file, 'rb') as file:
                data = pickle.load(file)
                if not isinstance(data, list):
                    data = [data]  # asigura ca întotdeauna întoarce o lista chiar și pentru un singur obiect
                return data
        except FileNotFoundError:
            return []

    def read_file(self):
        with open(self.file, 'r') as file:
            content = file.read()
            return content

    def write_to_file(self, string):
        with open(self.file, 'w') as file:
            file.write(string)

    def convert_to_string(self, objekte):
        pass

    def convert_from_string(self, string):
        pass



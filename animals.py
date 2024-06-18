from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class anjing(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "guuukkk!"

class kucing(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Meow!"

class bebek(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "kuek!"

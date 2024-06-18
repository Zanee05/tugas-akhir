from animals import anjing, kucing, bebek

def make_animal_sound(animal):
    return animal.make_sound()

animals = [anjing("budi"), kucing("jono"), bebek("joni")]

for animal in animals:
    print(f"{animal.name} berbunyi {make_animal_sound(animal)}")     

# Interface
class animal2:
    def print_info(self):
        pass

class anjing(animal2):
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"{self.name} adalah seekor anjing")

class kucing(animal2):
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"{self.name} adalah seekor kucing")

class bebek(animal2):
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"{self.name} adalah seekor bebek")

animals = [anjing("budi"), kucing("jono"),bebek("joni")]

for animal in animals:
    animal.print_info()

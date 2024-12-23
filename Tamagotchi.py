class Tamagotchi:
    def __init__(self):
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger += 10

    def pet(self):
        self.happiness += 10

    def update(self):
        self.hunger -= 0.1
        self.happiness -= 0.1
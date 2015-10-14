class Animal:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def get_noise(self):
        print("growl")

    def get_move(self):
        print("runs")

class Cheetah(Animal):
    def __init__(self, name, food, noise, move):
        super().__init__(name, food)
        self.noise = noise
        self.move = move

    def get_noise(self):
        return self.noise

    def get_move(self):
        return self.move
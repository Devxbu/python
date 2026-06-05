#!/usr/bin/env python3


class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def grow(self):
        self.height += 0.8

    def age_up(self):
        self.age += 1

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height)
        self.color = color
        self.bloomed = False

    def bloom(self):
        if not self.bloomed:
            print(f"{self.name} has not bloomed yet")
            print("[asking the rose to bloom]")
            self.bloomed = True
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is already blooming!")

    def show(self):
        super().show()
        print(f"Color: {self.color}")


class Tree(Plant):
    def __init__(self, name, age, height, trunk_diameter):
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade", end=" ")
        print(f"of {self.height:.1f}cm", end=" ")
        print(f"long and {self.trunk_diameter:.1f}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, age, height, harvest_season):
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self):
        super().grow()
        self.nutritional_value += 1

    def age_up(self):
        super().age_up()
        self.nutritional_value += 1

    def grow_for_days(self, days):
        for _ in range(days):
            self.grow()
            self.age_up()

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":

    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 10, 15.0, "red")
    rose.show()
    rose.bloom()

    print("\n=== Tree")
    oak = Tree("Oak", 365, 200.0, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 10, 5.0, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow_for_days(20)
    tomato.show()

#!/usr/bin/env python3


class Plant:

    class Stats:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0
            self.shade_count = 0

        def show(self):
            print(f"Stats: {self.grow_count} grow,", end=" ")
            print(f"age {self.age_count},", end=" ")
            print(f"show {self.show_count}")
            if self.shade_count or self.shade_count == 0:
                pass

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.stats = Plant.Stats()

    @staticmethod
    def is_older_than_year(days):
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0, 0.0)

    def grow(self):
        self.height += 8.0
        self.stats.grow_count += 1

    def age_up(self):
        self.age += 1
        self.stats.age_count += 1

    def show(self):
        self.stats.show_count += 1
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height)
        self.color = color
        self.bloomed = False

    def bloom(self):
        if not self.bloomed:
            print(f"{self.name} has not bloomed yet")
            print(f"{self.name} is blooming beautifully!")
            self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if not self.bloomed:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, age, height, trunk_diameter):
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        self.stats.shade_count += 1
        print(f"Tree {self.name} now produces a shade", end=" ")
        print(f"of {self.height:.1f}cm", end=" ")
        print(f"long and {self.trunk_diameter:.1f}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Seed(Flower):
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        if self.bloomed:
            self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


def show_statistics(plant):
    print(f"[statistics for {plant.name}]")
    plant.stats.show()
    if hasattr(plant.stats, "shade_count"):
        print(f"{plant.stats.shade_count} shade")


if __name__ == "__main__":

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 10, 15.0, "red")

    rose.show()
    print(f"[statistics for {rose.name}]")
    show_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()

    rose.show()
    print(f"[statistics for {rose.name}]")
    show_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 365, 200.0, 5.0)

    oak.show()
    print(f"[statistics for {oak.name}]")
    show_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print(f"[statistics for {oak.name}]")
    show_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 45, 80.0, "yellow")

    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_up()
    sunflower.bloom()

    sunflower.height = 110.0
    sunflower.age = 65

    sunflower.show()
    print(f"[statistics for {sunflower.name}]")
    show_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()

    print(f"[statistics for {unknown.name}]")
    show_statistics(unknown)

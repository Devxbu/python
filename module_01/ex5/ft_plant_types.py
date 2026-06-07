#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self.age = age
        self.height = height

    def grow(self) -> None:
        self.height += 0.8

    def age_up(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, age: int, height: float, color: str) -> None:
        super().__init__(name, age, height)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        if not self.bloomed:
            print(f"{self.name} has not bloomed yet")
            print("[asking the rose to bloom]")
            self.bloomed = True
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is already blooming!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")


class Tree(Plant):
    def __init__(
        self, name: str, age: int, height: float, trunk_diameter: float
    ) -> None:
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade", end=" ")
        print(f"of {self.height:.1f}cm", end=" ")
        print(f"long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, age: int, height: float, hs: str) -> None:
        super().__init__(name, age, height)
        self.harvest_season = hs
        self.nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age_up(self) -> None:
        super().age_up()
        self.nutritional_value += 1

    def grow_for_days(self, days: int) -> None:
        for _ in range(days):
            self.grow()
            self.age_up()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
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


if __name__ == "__main__":
    main()

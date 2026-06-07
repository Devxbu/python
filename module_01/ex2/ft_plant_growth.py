#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self.age_days = age
        self.height = height

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}:", end=" ")
        print(f"Height: {round(self.height, 1)}cm", end=" ")
        print(f"Age: {self.age_days} days old")


def main() -> None:
    plant: Plant = Plant("Rose", 30, 25)
    height: float = plant.height

    print("=== Garden Plant Growth ===")
    plant.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()

    growth = plant.height - height
    print(f"Growth this week: {round(growth, 1)}cm")


if __name__ == "__main__":
    main()

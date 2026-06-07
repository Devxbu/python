#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height

    def show(self) -> str:
        return f"{self.name}: {round(self.height, 1)}cm, {self.age} days old"


def main() -> None:
    print("=== Plant Factory Output ===")

    plants: list[Plant] = [
        Plant("Rose", 30, 25.0),
        Plant("Oak", 365, 200.0),
        Plant("Cactus", 90, 5.0),
        Plant("Sunflower", 45, 80.0),
        Plant("Fern", 120, 15.0),
    ]

    for plant in plants:
        print(f"Created: {plant.show()}")


if __name__ == "__main__":
    main()

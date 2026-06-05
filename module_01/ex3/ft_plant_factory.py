#!/usr/bin/env python3


class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def show(self):
        return f"{self.name}: {round(self.height, 1)}cm, {self.age} days old"


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plants = [
        Plant("Rose", 30, 25.0),
        Plant("Oak", 365, 200.0),
        Plant("Cactus", 90, 5.0),
        Plant("Sunflower", 45, 80.0),
        Plant("Fern", 120, 15.0),
    ]

    for plant in plants:
        print(f"Created: {plant.show()}")

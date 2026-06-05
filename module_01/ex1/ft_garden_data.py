#!/usr/bin/env python3


class Plant:
    def __init__(self, name, age_days, height):
        self.name = name
        self.age_days = age_days
        self.height = height

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 30, 25)
    plant2 = Plant("Sunflower", 45, 80)
    plant3 = Plant("Cactus", 120, 15)
    plant1.show()
    plant2.show()
    plant3.show()

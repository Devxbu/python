#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, age_days: int, height: int):
        self.name = name
        self.age_days = age_days
        self.height = height

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    plant1: Plant = Plant("Rose", 30, 25)
    plant2: Plant = Plant("Sunflower", 45, 80)
    plant3: Plant = Plant("Cactus", 120, 15)
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self._age = age
        self._height = height

    def show(self) -> str:
        return f"{self.name}: {round(self._height, 1)}cm, {self._age} days old"

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {age} days")

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height


def main() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 30, 25.0)
    print(f"Plant created: {plant.show()}")

    plant.set_height(20)
    plant.set_age(10)
    plant.set_height(-10)
    plant.set_age(-10)
    plant.show()
    print(f"Current age: {plant.get_age()} days old")
    print(f"Current height: {plant.get_height()}cm")


if __name__ == "__main__":
    main()

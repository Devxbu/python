#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_garden_operations() -> None:
    test_plant_error()
    test_water_error()


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        test_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("\nTesting WaterError...")
        test_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        test_plant_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        test_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()

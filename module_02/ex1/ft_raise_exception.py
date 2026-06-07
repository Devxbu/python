#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp = int(temp_str)

    if temp >= 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp <= 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

    return temp


def test_temperature(value: str) -> None:
    try:
        temp = input_temperature(value)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


def main() -> None:
    print("=== Garden Temperature ===")

    test_temperature("25")
    test_temperature("abc")
    test_temperature("100")
    test_temperature("-50")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()

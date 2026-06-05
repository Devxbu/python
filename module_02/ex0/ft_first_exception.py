#!/usr/bin/env python3


def input_temperature(temp_str):
    print(f"Input data is '{temp_str}'")
    return int(temp_str)


def test_temperature(value):
    try:
        temp = input_temperature(value)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")

    test_temperature("25")
    test_temperature("abc")

    print("All tests completed - program didn't crash!")

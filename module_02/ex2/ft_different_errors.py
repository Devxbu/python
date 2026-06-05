#!/usr/bin/env python3


def garden_operations(operation_number):
    print(f"Testing operation {operation_number}...")
    if operation_number == 0:
        return int("abc")
    elif operation_number == 1:
        return 1 / 0
    elif operation_number == 2:
        return open("/non/existent/file", "r")
    elif operation_number == 3:
        return "test" + 1
    else:
        return


def test_error_types(operation_number):
    try:
        garden_operations(operation_number)
    except ValueError as v:
        print(f"Caught ValueError: {v}")
        pass
    except ZeroDivisionError as z:
        print(f"Caught ZeroDivisionError: {z}")
        pass
    except FileNotFoundError as f:
        print(f"Caught FileNotFoundError: {f}")
        pass
    except TypeError as t:
        print(f"Caught TypeError: {t}")
        pass


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types(0)
    test_error_types(1)
    test_error_types(2)
    test_error_types(3)
    test_error_types(4)
    print("All error types tested successfully!")

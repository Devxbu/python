#!/usr/bin/env python3
import sys


def parse_item(item: str) -> tuple[str | None, str | None]:
    key = ""
    value = ""
    i = 0
    found = False

    while i < len(item):
        if item[i] == ":":
            found = True
            i += 1
            break
        key = key + item[i]
        i += 1

    if not found:
        print(f"Error - invalid parameter '{item}'")
        return None, None

    while i < len(item):
        value = value + item[i]
        i += 1

    return key, value


def to_int(s: str) -> int:
    result = 0
    i = 0

    if len(s) == 0:
        return 0

    while i < len(s):
        c = s[i]
        if c < "0" or c > "9":
            return 0
        result = result * 10 + (ord(c) - ord("0"))
        i += 1

    return result


def main() -> None:
    print("=== Inventory System Analysis ===")

    cli = sys.argv[1:]
    inventory: dict[str, int] = {}

    i = 0
    while i < len(cli):
        item = cli[i]
        key, value_str = parse_item(item)
        if key is None or value_str is None:
            i += 1
            continue

        keys_list = list(inventory.keys())
        j = 0
        duplicate = False
        while j < len(keys_list):
            if keys_list[j] == key:
                duplicate = True
                break
            j += 1

        if duplicate:
            print(f"Redundant item '{key}' - discarding")
            i += 1
            continue

        value = to_int(value_str)

        inventory[key] = value
        i += 1

    if len(inventory) == 0:
        print("Empty inventory")
        return

    total = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of {len(inventory)} items: {total}")

    keys = list(inventory.keys())

    most_key = keys[0]
    least_key = keys[0]

    i = 0
    while i < len(keys):
        key = keys[i]
        value = inventory[key]

        if value > inventory[most_key]:
            most_key = key
        if value < inventory[least_key]:
            least_key = key

        print(f"Item: {key} represents {round((value / total) * 100, 1)}%")

        i += 1

    print(f"Item most abundant: {most_key}", end=" ")
    print(f"with quantity {inventory[most_key]}")

    print(f"Item least abundant: {least_key}", end=" ")
    print(f"with quantity {inventory[least_key]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()

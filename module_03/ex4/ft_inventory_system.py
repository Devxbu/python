#!/usr/bin/env python3
import sys


def generate_inventory(cli):
    key = ""
    value = ""
    inventory = {}
    for i in cli:
        splited = i.split(":")
        if len(splited) != 2:
            print(f"Error - invalid parameter '{i}'")
            continue
        key = splited[0]
        value = splited[1]
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            value = int(value)
        except ValueError as e:
            print(f"Quantity error for'{key}': {e}")
            continue
        inventory[key] = value

    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    cli = sys.argv[1:]
    inventory = generate_inventory(cli)
    total = sum(inventory.values())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of {len(inventory)} items: {total}")
    for i in inventory.items():
        print(f"Item: {i[0]} represents {round((i[1] / total) * 100, 1)}%")
    print(f"Item most abundant: {max(inventory, key=inventory.get)}", end=" ")
    print(f"with quantity {max(inventory.values())}")
    print(f"Item least abundant: {min(inventory, key=inventory.get)}", end=" ")
    print(f"with quantity {min(inventory.values())}")
    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")

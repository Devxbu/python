#!/usr/bin/env python3
import math


def get_player_pos():
    while True:
        position = input("Enter new coordinates as floats in format 'x,y,z': ")
        pos = position.split(",")

        if len(pos) != 3:
            print("Invalid syntax")
            continue

        try:
            coords = []

            for value in pos:
                coords.append(float(value.strip()))

            return tuple(coords)

        except ValueError:
            for value in pos:
                try:
                    float(value.strip())
                except ValueError:
                    print(f"Error on parameter '{value.strip()}':", end=" ")
                    print("could", end=" ")
                    print(f"not convert string to float: '{value.strip()}'")
                    break


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos = get_player_pos()

    print(f"Got a first tuple: {pos}")
    print(f"It includes: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")

    dist = math.sqrt(pos[0] ** 2 + pos[1] ** 2 + pos[2] ** 2)
    print(f"Distance to center: {dist:.4f}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()

    dist_between = math.sqrt(
        (pos[0] - pos2[0]) ** 2 + (pos[1] - pos2[1]) ** 2 + (pos[2] - pos2[2]) ** 2
    )

    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")

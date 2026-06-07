#!/usr/bin/env python3
import math


def parse_float(s: str, i: int) -> tuple[float, int]:
    sign = 1
    if s[i] == "-":
        sign = -1
        i += 1

    result = 0.0

    while i < len(s) and "0" <= s[i] <= "9":
        result = result * 10 + (ord(s[i]) - ord("0"))
        i += 1

    if i < len(s) and s[i] == ".":
        i += 1
        divisor = 1
        frac = 0

        while i < len(s) and "0" <= s[i] <= "9":
            frac = frac * 10 + (ord(s[i]) - ord("0"))
            divisor *= 10
            i += 1

        result += frac / divisor

    return sign * result, i


def get_player_pos() -> tuple[float, float, float]:
    while True:
        position = input("Enter new coordinates as floats in format 'x,y,z': ")

        coords: list[str] = []
        i = 0
        current = ""

        while i < len(position):
            if position[i] == ",":
                coords = coords + [current]
                current = ""
            else:
                current = current + position[i]
            i += 1

        coords = coords + [current]

        if len(coords) != 3:
            print("Invalid syntax")
            continue

        try:
            result: list[float] = []
            j = 0

            while j < 3:
                value = coords[j]
                num, _ = parse_float(value, 0)
                result = result + [num]
                j += 1

            return (result[0], result[1], result[2])

        except ValueError:
            print("Invalid number format")


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos = get_player_pos()

    print(f"Got a first tuple: {pos}")
    print(f"It includes: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")

    dist = math.sqrt(pos[0] ** 2 + pos[1] ** 2 + pos[2] ** 2)
    print(f"Distance to center: {round(dist, 4)}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()

    p1 = pos[0] - pos2[0]
    p2 = pos[1] - pos2[1]
    p3 = pos[2] - pos2[2]
    dist_between = math.sqrt(p1 * p1 + p2 * p2 + p3 * p3)

    print("Distance between the 2 sets of", end=" ")
    print(f"coordinates: {round(dist_between, 4)}")


if __name__ == "__main__":
    main()

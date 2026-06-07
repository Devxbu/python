#!/usr/bin/env python3
import random


def to_title_manual(name: str) -> str:
    if len(name) == 0:
        return name

    first = name[0]
    rest = ""

    if "a" <= first <= "z":
        first = chr(ord(first) - 32)

    i = 1
    while i < len(name):
        ch = name[i]
        if "A" <= ch <= "Z":
            ch = chr(ord(ch) + 32)
        rest += ch
        i += 1

    return first + rest


def is_title_manual(name: str) -> bool:
    if len(name) == 0:
        return False

    first = name[0]
    if not ("A" <= first <= "Z"):
        return False

    i = 1
    while i < len(name):
        if "A" <= name[i] <= "Z":
            return False
        i += 1

    return True


def bubble_sort_desc(items: list[tuple[str, int]]) -> list[tuple[str, int]]:
    arr = items[:]
    n = len(arr)

    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if arr[j][1] < arr[j + 1][1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            j += 1
        i += 1

    return arr


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    arr = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]

    print("Initial list of players:", arr)

    capitalized_arr = []
    i = 0
    while i < len(arr):
        capitalized_arr.append(to_title_manual(arr[i]))
        i += 1

    print("New list with all names capitalized:", capitalized_arr)

    filtered_arr = []
    i = 0
    while i < len(arr):
        if is_title_manual(arr[i]):
            filtered_arr.append(arr[i])
        i += 1

    print("New list of capitalized names only:", filtered_arr, "\n")

    score_dict = {}
    i = 0
    while i < len(arr):
        score_dict[arr[i]] = random.randint(0, 1000)
        i += 1

    print("Score dict:", score_dict)

    total = sum(score_dict.values())
    avg = round(total / len(score_dict), 2)
    print("Score average is:", avg)

    items = []
    for k in score_dict:
        items.append((k, score_dict[k]))

    sorted_items = bubble_sort_desc(items)
    print("High scores:", sorted_items[:3])


if __name__ == "__main__":
    main()

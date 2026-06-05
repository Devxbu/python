#!/usr/bin/env python3
import random


if __name__ == "__main__":
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

    print(f"Initial list of players: {arr}")
    capitalized_arr = [name.capitalize() for name in arr]
    print(f"New list with all names capitalized: {capitalized_arr}")
    filer_arr = [name for name in arr if name.istitle()]
    print(f"New list of capitalized names only: {filer_arr}\n")
    score_dict = {name: random.randint(0, 1000) for name in arr}
    print(f"Score dict: {score_dict}")
    print(f"Score average is: {round(sum(score_dict.values()) / len(score_dict), 2)}")
    print(
        f"High scores: {sorted(score_dict.items(), key=lambda x: x[1], reverse=True)[:3]}"
    )

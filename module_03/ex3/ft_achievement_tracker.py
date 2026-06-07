#!/usr/bin/env python3
import random

all_achievements = (
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
)


def gen_player_achievements() -> set[str]:
    count = random.randint(1, len(all_achievements))
    return set(random.sample(all_achievements, count))


def main() -> None:
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    common_achievements = set.intersection(alice, bob, charlie, dylan)
    all_distinct = alice | bob | charlie | dylan
    common_achievements = alice & bob & charlie & dylan

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")
    print(f"All distinct achievements: {all_distinct}")
    print(f"Common achievements: {common_achievements}\n")
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}\n")
    print(f"Alice is missing: {set(all_achievements) - alice}")
    print(f"Bob is missing: {set(all_achievements) - bob}")
    print(f"Charlie is missing: {set(all_achievements) - charlie}")
    print(f"Dylan is missing: {set(all_achievements) - dylan}")


if __name__ == "__main__":
    main()

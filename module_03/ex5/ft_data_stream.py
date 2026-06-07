#!/usr/bin/env python3

import random
import typing

players = ("Bahri", "Can", "Irmak", "Verda")

actions = (
    "run",
    "eat",
    "grab",
    "sleep",
    "move",
    "climb",
    "jump",
    "sing",
    "sleep",
    "think",
    "move",
    "climb",
    "climb",
    "climb",
    "climb",
    "swim",
    "jump",
    "sing",
    "sleep",
)


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:

    i = 0
    while i < len(events):
        yield events[i]
        i += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()

    i = 0
    while i < 1000:
        event = next(event_stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
        i += 1

    ten_events = []
    i = 0
    while i < 10:
        ten_events += [next(event_stream)]
        i += 1

    print("Built list of 10 events:", ten_events)

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()

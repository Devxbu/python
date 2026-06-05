#!/usr/bin/env python3

import random

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


def gen_event():
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events):
    while events:
        item = random.choice(events)
        events.remove(item)
        yield item


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    event_stream = gen_event()
    for i in range(1000):
        event = next(event_stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    ten_events = [next(event_stream) for _ in range(10)]
    print("Built list of 10 events:", ten_events)

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")

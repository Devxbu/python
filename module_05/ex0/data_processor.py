#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self._data: list[str] = []
        self._counter = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise Exception("No data available")

        value = self._data.pop(0)
        result = (self._counter, value)
        self._counter += 1
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, (int, float)):
            data = [data]

        self._data.extend(str(x) for x in data)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, str):
            data = [data]

        self._data.extend(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def valid_dict(item: Any) -> bool:
            return (
                isinstance(item, dict)
                and "log_level" in item
                and "log_message" in item
                and isinstance(item["log_level"], str)
                and isinstance(item["log_message"], str)
            )

        if valid_dict(data):
            return True

        if isinstance(data, list):
            return all(valid_dict(item) for item in data)

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        if isinstance(data, dict):
            data = [data]

        self._data.extend(f"{d['log_level']}: {d['log_message']}" for d in data)


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    num = NumericProcessor()

    print("\nTesting Numeric Processor...")

    print(f"Trying to validate input '42': {num.validate(42)}")
    print(f"Trying to validate input 'Hello': {num.validate('Hello')}")

    print("\nTest invalid ingestion of string 'foo' without prior validation:")

    try:
        num.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")

    numeric_data = [1, 2, 3, 4, 5]

    print(f"\nProcessing data: {numeric_data}")

    num.ingest(numeric_data)

    print("\nExtracting 3 values...")

    for _ in range(3):
        idx, value = num.output()
        print(f"Numeric value {idx}: {value}")

    text = TextProcessor()

    print("\nTesting Text Processor...")

    print(f"Trying to validate input '42': {text.validate(42)}")

    text_data = ["Hello", "Nexus", "World"]

    print(f"\nProcessing data: {text_data}")

    text.ingest(text_data)

    print("\nExtracting 1 value...")

    idx, value = text.output()
    print(f"Text value {idx}: {value}")

    log = LogProcessor()

    print("\nTesting Log Processor...")

    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")

    log_data = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]

    print(f"\nProcessing data: {log_data}")

    log.ingest(log_data)

    print("\nExtracting 2 values...")

    for _ in range(2):
        idx, value = log.output()
        print(f"Log entry {idx}: {value}")

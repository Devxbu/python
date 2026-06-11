#!/usr/bin/env python3

from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: object) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: object) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self._data) == 0:
            return (-1, "")

        value = self._data.pop(0)
        result = (self._counter, value)
        self._counter += 1
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: object) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)

        return False

    def ingest(self, data: object) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, (int, float)):
            data = [data]

        assert isinstance(data, list)

        self._data.extend(str(x) for x in data)


class TextProcessor(DataProcessor):
    def validate(self, data: object) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)

        return False

    def ingest(self, data: object) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, str):
            data = [data]

        assert isinstance(data, list)

        self._data.extend(data)


class LogProcessor(DataProcessor):
    def validate(self, data: object) -> bool:
        def valid(item: object) -> bool:
            if not isinstance(item, dict):
                return False
            return (
                "log_level" in item
                and "log_message" in item
                and isinstance(item["log_level"], str)
                and isinstance(item["log_message"], str)
            )

        if valid(data):
            return True

        if isinstance(data, list):
            return all(valid(x) for x in data)

        return False

    def ingest(self, data: object) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, dict):
            data = [data]

        assert isinstance(data, list)
        temp = (f"{d['log_level']}: {d['log_message']}" for d in data)
        self._data.extend(temp)


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    num = NumericProcessor()

    print("\nTesting Numeric Processor...")
    print(f"Validate 42: {num.validate(42)}")
    print(f"Validate 'Hello': {num.validate('Hello')}")

    try:
        num.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")

    numeric_data = [1, 2, 3, 4, 5]
    print(f"\nProcessing: {numeric_data}")

    num.ingest(numeric_data)

    print("\nExtracting 3 values...")
    i = 0
    while i < 3:
        idx, value = num.output()
        print(f"Numeric value {idx}: {value}")
        i += 1

    text = TextProcessor()

    print("\nTesting Text Processor...")
    text_data = ["Hello", "Nexus", "World"]

    text.ingest(text_data)

    idx, value = text.output()
    print(f"Text value {idx}: {value}")

    log = LogProcessor()

    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]

    log.ingest(log_data)
    i = 0
    while i < 2:
        idx, value = log.output()
        print(f"Log entry {idx}: {value}")
        i += 1


if __name__ == "__main__":
    main()

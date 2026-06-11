#!/usr/bin/env python3

from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._counter: int = 0
        self._total_processed: int = 0

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

    @property
    def total_processed(self) -> int:
        return self._total_processed

    @property
    def remaining(self) -> int:
        return len(self._data)


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
        self._total_processed += len(data)


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
        self._total_processed += len(data)


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

        self._total_processed += len(data)


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[object]) -> None:
        for element in stream:
            processed = False

            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break

            if not processed:
                print(
                    "DataStream error - Can't process element in stream:",
                    element,
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if len(self._processors) == 0:
            print("No processor found, no data")
            return

        for proc in self._processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")

            print(
                f"{name}: total {proc.total_processed} items processed, "
                f"remaining {proc.remaining} on processor"
            )

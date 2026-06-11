#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._counter: int = 0
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise Exception("No data")

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

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, (int, float)):
            data = [data]

        self._data.extend(str(x) for x in data)
        self._total_processed += len(data)


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, str):
            data = [data]

        self._data.extend(data)
        self._total_processed += len(data)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        def ok(d: Any) -> bool:
            x = isinstance(d, dict) and "log_level" in d and "log_message" in d
            return x

        if ok(data):
            return True
        if isinstance(data, list):
            return all(ok(x) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        if isinstance(data, dict):
            data = [data]

        formatted = [f"{d['log_level']}: {d['log_message']}" for d in data]

        self._data.extend(formatted)
        self._total_processed += len(data)


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None: ...


class CSVExportPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        for _, value in data:
            print(value)


class JSONExportPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items = {f"item_{i}": value for i, (_, value) in enumerate(data)}
        print("{")
        for k, v in items.items():
            print(f'  "{k}": "{v}"')
        print("}")


class DataStream:

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            handled = False

            for p in self._processors:
                if p.validate(item):
                    p.ingest(item)
                    handled = True
                    break

            if not handled:
                print(f"Can't process element: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for p in self._processors:
            name = p.__class__.__name__
            print(
                f"{name}: total {p.total_processed} items processed, "
                f"remaining {p.remaining} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for _ in range(nb):
            batch: list[tuple[int, str]] = []

            for p in self._processors:
                if p.remaining > 0:
                    batch.append(p.output())

            if batch:
                plugin.process_output(batch)


def main() -> None:

    print("=== Code Nexus - Data Pipeline ===")

    stream = DataStream()

    print("Initialize Data Stream...")
    stream.print_processors_stats()

    num = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    print("\nRegistering Processors")
    stream.register_processor(num)
    stream.register_processor(txt)
    stream.register_processor(log)

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("\nSend first batch of data on stream:", batch)
    stream.process_stream(batch)

    stream.print_processors_stats()

    csv_plugin = CSVExportPlugin()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, csv_plugin)

    stream.print_processors_stats()

    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE", "log_message": "expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print("\nSend another batch of data:", batch2)
    stream.process_stream(batch2)

    stream.print_processors_stats()

    json_plugin = JSONExportPlugin()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json_plugin)

    stream.print_processors_stats()


if __name__ == "__main__":
    main()

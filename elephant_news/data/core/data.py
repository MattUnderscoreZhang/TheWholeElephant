from dataclasses import dataclass
from dataclasses_json import dataclass_json
from uuid import UUID


@dataclass_json
@dataclass
class Data:
    uuid: UUID
    title: str
    content: str
    summary: str = ""
    publishedAt: str = ""


# to be added to log.py when ready
"""
    def read_article(self, filepath: Path) -> Data:
        try:
            with open(filepath) as f:
                return Data.from_json(f.read())
        except IsADirectoryError:
            self.log_fn(f"Path is a directory: {filepath}\n", Colors.info)
        except FileNotFoundError:
            self.log_fn(f"File not found: {filepath}\n", Colors.info)
        return Data()

    def set_data(self, data: Data) -> None:
        self.data = data
        self.messages = []
        self.log_fn(f"You are now discussing \"{self.data.title}\".\n")
"""

from dataclasses import dataclass

@dataclass
class TodoData:
    title: str
    description: str
    is_completed: bool = False
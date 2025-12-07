from dataclasses import dataclass
from typing import Optional


@dataclass
class TodoData:
    title: str
    description: str = ""
    is_completed: bool = False


@dataclass
class TodoUpdateData:
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

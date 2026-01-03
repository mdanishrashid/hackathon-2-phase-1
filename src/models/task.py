from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    """
    Represents a to-do item in the application
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
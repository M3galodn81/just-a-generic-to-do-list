from enum import Enum

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class UserTask:
    def __init__(
        self,
        title: str,
        description: str,
        priority: Priority = Priority.LOW
    ):
        self.title = title
        self.description = description
        self.priority = priority
        self.is_done = False

    def mark_done(self):
        self.is_done = True

    def __str__(self):
        return f"{self.title} [{self.priority.name}]"






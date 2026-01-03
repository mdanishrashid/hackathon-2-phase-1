from typing import List, Optional
from src.models.task import Task
from src.lib import utils
import sys

class TaskManager:
    """
    Manages in-memory storage and operations for tasks
    """

    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task with auto-incremented ID
        """
        # Validate title
        if not utils.validate_title(title):
            raise ValueError("Title cannot be empty and must be 1-255 characters")

        # Validate description
        if description and not utils.validate_description(description):
            raise ValueError("Description must be 0-1000 characters")

        # Create new task with auto-incremented ID
        task = Task(
            id=self.next_id,
            title=title.strip(),
            description=description.strip() if description else None,
            completed=False
        )

        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks
        """
        return self.tasks
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        if title is not None:
            if not utils.validate_title(title):
                raise ValueError("Title cannot be empty and must be 1-255 characters")
            task.title = title.strip()

        if description is not None:
            if not utils.validate_description(description):
                raise ValueError("Description must be 0-1000 characters")
            task.description = description.strip() if description else None

        return True
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        self.tasks.remove(task)
        return True
    
    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        task.completed = True
        return True
    
    def mark_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        task.completed = False
        return True
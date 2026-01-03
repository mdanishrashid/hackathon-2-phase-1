import pytest
from src.models.task import Task

class TestTaskModel:
    """
    Unit tests for the Task model
    """
    
    def test_task_creation(self):
        """Test creating a Task instance"""
        task = Task(
            id=1,
            title="Test Task",
            description="Test Description",
            completed=False
        )
        
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False
    
    def test_task_default_values(self):
        """Test Task creation with default values"""
        task = Task(
            id=2,
            title="Test Task",
        )
        
        assert task.id == 2
        assert task.title == "Test Task"
        assert task.description is None
        assert task.completed is False
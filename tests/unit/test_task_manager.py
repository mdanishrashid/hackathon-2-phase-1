import pytest
from src.models.task import Task
from src.services.task_manager import TaskManager

class TestTaskManager:
    """
    Unit tests for the TaskManager service
    """
    
    def setup_method(self):
        """Set up a fresh TaskManager for each test"""
        self.task_manager = TaskManager()
    
    def test_initial_state(self):
        """Test that TaskManager starts with no tasks and next_id is 1"""
        assert len(self.task_manager.get_all_tasks()) == 0
        assert self.task_manager.next_id == 1
    
    def test_add_task(self):
        """Test adding a task"""
        task = self.task_manager.add_task("Test Task")
        
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description is None
        assert task.completed is False
        
        # Verify the task was added to the list
        tasks = self.task_manager.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0] == task
    
    def test_add_task_with_description(self):
        """Test adding a task with description"""
        task = self.task_manager.add_task("Test Task", "Test Description")
        
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False
    
    def test_auto_increment_id(self):
        """Test that IDs are auto-incremented"""
        task1 = self.task_manager.add_task("Task 1")
        task2 = self.task_manager.add_task("Task 2")
        task3 = self.task_manager.add_task("Task 3")
        
        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3
    
    def test_get_all_tasks(self):
        """Test getting all tasks"""
        # Add some tasks
        task1 = self.task_manager.add_task("Task 1")
        task2 = self.task_manager.add_task("Task 2")
        
        tasks = self.task_manager.get_all_tasks()
        
        assert len(tasks) == 2
        assert task1 in tasks
        assert task2 in tasks
    
    def test_get_task_by_id(self):
        """Test getting a specific task by ID"""
        task = self.task_manager.add_task("Test Task")
        
        found_task = self.task_manager.get_task_by_id(1)
        assert found_task == task
        
        # Test getting non-existent task
        not_found_task = self.task_manager.get_task_by_id(999)
        assert not_found_task is None
    
    def test_update_task(self):
        """Test updating a task"""
        task = self.task_manager.add_task("Original Title", "Original Description")
        
        # Update title and description
        result = self.task_manager.update_task(task.id, "New Title", "New Description")
        assert result is True
        
        # Verify the task was updated
        updated_task = self.task_manager.get_task_by_id(task.id)
        assert updated_task.title == "New Title"
        assert updated_task.description == "New Description"
    
    def test_update_task_partial(self):
        """Test updating only the title or description"""
        task = self.task_manager.add_task("Original Title", "Original Description")
        
        # Update only title
        result = self.task_manager.update_task(task.id, "New Title")
        assert result is True
        
        updated_task = self.task_manager.get_task_by_id(task.id)
        assert updated_task.title == "New Title"
        assert updated_task.description == "Original Description"  # Unchanged
        
        # Update only description
        result = self.task_manager.update_task(task.id, description="New Description")
        assert result is True
        
        updated_task = self.task_manager.get_task_by_id(task.id)
        assert updated_task.title == "New Title"  # Unchanged
        assert updated_task.description == "New Description"
    
    def test_delete_task(self):
        """Test deleting a task"""
        task = self.task_manager.add_task("Task to Delete")
        
        # Verify task exists
        assert self.task_manager.get_task_by_id(task.id) is not None
        
        # Delete the task
        result = self.task_manager.delete_task(task.id)
        assert result is True
        
        # Verify task no longer exists
        assert self.task_manager.get_task_by_id(task.id) is None
        assert len(self.task_manager.get_all_tasks()) == 0
    
    def test_mark_complete(self):
        """Test marking a task as complete"""
        task = self.task_manager.add_task("Test Task")
        assert task.completed is False
        
        result = self.task_manager.mark_complete(task.id)
        assert result is True
        
        updated_task = self.task_manager.get_task_by_id(task.id)
        assert updated_task.completed is True
    
    def test_mark_incomplete(self):
        """Test marking a task as incomplete"""
        task = self.task_manager.add_task("Test Task")
        
        # Mark as complete first
        self.task_manager.mark_complete(task.id)
        assert self.task_manager.get_task_by_id(task.id).completed is True
        
        # Mark as incomplete
        result = self.task_manager.mark_incomplete(task.id)
        assert result is True
        
        updated_task = self.task_manager.get_task_by_id(task.id)
        assert updated_task.completed is False
    
    def test_validation_on_add(self):
        """Test validation during task addition"""
        with pytest.raises(ValueError):
            self.task_manager.add_task("")  # Empty title
        
        with pytest.raises(ValueError):
            self.task_manager.add_task("   ")  # Only whitespace
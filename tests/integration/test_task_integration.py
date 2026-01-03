import pytest
from src.models.task import Task
from src.services.task_manager import TaskManager

class TestTaskManager:
    """
    Integration tests for TaskManager covering all user stories
    """
    
    def setup_method(self):
        """Set up a fresh TaskManager for each test"""
        self.task_manager = TaskManager()
    
    def test_add_task_user_story_1(self):
        """Test User Story 1: Add a new task"""
        # Add a task with title only
        task1 = self.task_manager.add_task("Test task 1")
        assert task1.id == 1
        assert task1.title == "Test task 1"
        assert task1.description is None
        assert task1.completed is False
        
        # Add a task with title and description
        task2 = self.task_manager.add_task("Test task 2", "This is a description")
        assert task2.id == 2
        assert task2.title == "Test task 2"
        assert task2.description == "This is a description"
        assert task2.completed is False
        
        # Verify auto-increment ID
        assert len(self.task_manager.get_all_tasks()) == 2
    
    def test_view_tasks_user_story_2(self):
        """Test User Story 2: View all tasks"""
        # Add tasks
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2", "Description for task 2")
        
        # Get all tasks
        tasks = self.task_manager.get_all_tasks()
        
        # Verify we have 2 tasks
        assert len(tasks) == 2
        
        # Verify task details
        assert tasks[0].id == 1
        assert tasks[0].title == "Task 1"
        assert tasks[0].description is None
        assert tasks[0].completed is False
        
        assert tasks[1].id == 2
        assert tasks[1].title == "Task 2"
        assert tasks[1].description == "Description for task 2"
        assert tasks[1].completed is False
    
    def test_mark_complete_user_story_3(self):
        """Test User Story 3: Mark task as complete/incomplete"""
        # Add a task
        task = self.task_manager.add_task("Task to complete")
        
        # Mark it as complete
        result = self.task_manager.mark_complete(task.id)
        assert result is True
        
        # Verify task is marked complete
        updated_task = self.task_manager.get_task_by_id(task.id)
        assert updated_task.completed is True
    
    def test_mark_incomplete_user_story_3(self):
        """Test User Story 3: Mark task as complete/incomplete"""
        # Add a task
        task = self.task_manager.add_task("Task to mark incomplete")
        
        # Mark it as complete first
        self.task_manager.mark_complete(task.id)
        updated_task = self.task_manager.get_task_by_id(task.id)
        assert updated_task.completed is True
        
        # Mark it as incomplete
        result = self.task_manager.mark_incomplete(task.id)
        assert result is True
        
        # Verify task is marked incomplete
        updated_task = self.task_manager.get_task_by_id(task.id)
        assert updated_task.completed is False
    
    def test_update_task_user_story_4(self):
        """Test User Story 4: Update task details"""
        # Add a task
        task = self.task_manager.add_task("Original title", "Original description")
        
        # Update the task
        result = self.task_manager.update_task(task.id, "Updated title", "Updated description")
        assert result is True
        
        # Verify task is updated
        updated_task = self.task_manager.get_task_by_id(task.id)
        assert updated_task.title == "Updated title"
        assert updated_task.description == "Updated description"
    
    def test_delete_task_user_story_5(self):
        """Test User Story 5: Delete a task"""
        # Add a task
        task = self.task_manager.add_task("Task to delete")
        initial_count = len(self.task_manager.get_all_tasks())
        
        # Delete the task
        result = self.task_manager.delete_task(task.id)
        assert result is True
        
        # Verify task is deleted
        final_count = len(self.task_manager.get_all_tasks())
        assert final_count == initial_count - 1
        
        # Verify task no longer exists
        deleted_task = self.task_manager.get_task_by_id(task.id)
        assert deleted_task is None
    
    def test_validation_edge_cases(self):
        """Test edge cases and validation"""
        # Attempt to add a task with empty title
        with pytest.raises(ValueError):
            self.task_manager.add_task("")
        
        # Attempt to add a task with very long title
        with pytest.raises(ValueError):
            self.task_manager.add_task("A" * 256)  # 256 characters exceeds limit
        
        # Attempt to update a non-existent task
        result = self.task_manager.update_task(999, "New title")
        assert result is False
        
        # Attempt to delete a non-existent task
        result = self.task_manager.delete_task(999)
        assert result is False
        
        # Attempt to mark complete a non-existent task
        result = self.task_manager.mark_complete(999)
        assert result is False
        
        # Attempt to mark incomplete a non-existent task
        result = self.task_manager.mark_incomplete(999)
        assert result is False

if __name__ == '__main__':
    pytest.main()
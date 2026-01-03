# Data Model for Todo Console Application

## Task Entity

**Definition**: Represents a to-do item in the application

**Fields**:
- `id` (Integer, Auto-incremented): Unique identifier for each task
- `title` (String, Required): The task title/description
- `description` (String, Optional): Additional details about the task
- `completed` (Boolean): Whether the task has been completed

**Validation Rules**:
- `id` must be a positive integer and unique within the application session
- `title` must be a non-empty string (1-255 characters)
- `description` can be empty or up to 1000 characters
- `completed` can only be true or false

**State Transitions**:
- New task: `completed` defaults to `false`
- Complete task: `completed` transitions from `false` to `true`
- Incomplete task: `completed` transitions from `true` to `false`

## Task List

**Definition**: Collection of Task entities stored in memory during application runtime

**Operations**:
- Add new task to collection
- Retrieve all tasks
- Update existing task details
- Delete task from collection
- Mark task as complete/incomplete

**Constraints**:
- Tasks exist only in memory during application session
- Tasks are not persisted beyond application runtime
- Maximum recommended size is 1000 tasks to prevent memory issues
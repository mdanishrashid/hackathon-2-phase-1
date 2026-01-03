# API Contract for Todo Console Application

## Task Operations

### Add Task
- **Command**: `add`
- **Parameters**: 
  - `title` (required, string): The task title
  - `description` (optional, string): Additional details about the task
- **Output**: 
  - Success: "Task added successfully with ID: {id}"
  - Error: "Error: {error_message}"

### View Tasks
- **Command**: `list` or `view`
- **Parameters**: None
- **Output**:
  - Success: Formatted list of all tasks with ID, title, description, and completion status
  - Error: "No tasks found." (when no tasks exist)

### Update Task
- **Command**: `update`
- **Parameters**:
  - `id` (required, integer): The task ID
  - `title` (optional, string): New title
  - `description` (optional, string): New description
- **Output**:
  - Success: "Task {id} updated successfully"
  - Error: "Error: {error_message}"

### Delete Task
- **Command**: `delete`
- **Parameters**:
  - `id` (required, integer): The task ID
- **Output**:
  - Success: "Task {id} deleted successfully"
  - Error: "Error: {error_message}"

### Mark Complete/Incomplete
- **Command**: `complete` or `incomplete`
- **Parameters**:
  - `id` (required, integer): The task ID
- **Output**:
  - Success: "Task {id} marked as {status}"
  - Error: "Error: {error_message}"
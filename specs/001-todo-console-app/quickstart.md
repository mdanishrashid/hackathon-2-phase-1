# Quickstart Guide for Todo Console Application

## Getting Started

### Prerequisites
- Python 3.13+ installed on your system
- Basic command line knowledge

### Installation
1. Clone or download the repository
2. Navigate to the project directory
3. Ensure Python 3.13+ is available in your environment

## Basic Usage

### Running the Application
Execute the application using Python:
```bash
python -m src.cli.main [command] [arguments]
```

### Adding a Task
```bash
python -m src.cli.main add "Task Title" "Optional description"
```

### Viewing All Tasks
```bash
python -m src.cli.main list
# or
python -m src.cli.main view
```

### Updating a Task
```bash
python -m src.cli.main update 1 "New Title" "New Description"
```

### Marking a Task as Complete
```bash
python -m src.cli.main complete 1
```

### Marking a Task as Incomplete
```bash
python -m src.cli.main incomplete 1
```

### Deleting a Task
```bash
python -m src.cli.main delete 1
```

### Getting Help
```bash
python -m src.cli.main --help
# or for a specific command
python -m src.cli.main add --help
```

## Available Commands
- `add` - Add a new task
- `list` or `view` - View all tasks
- `update` - Update a task's details
- `complete` - Mark a task as complete
- `incomplete` - Mark a task as incomplete
- `delete` - Delete a task
- `--help` - Show help information

## Example Workflow
1. Add a task: `python -m src.cli.main add "Buy groceries" "Get milk, bread, and eggs"`
2. View tasks: `python -m src.cli.main list`
3. Mark task as complete: `python -m src.cli.main complete 1`
4. Update task: `python -m src.cli.main update 1 "Buy groceries" "Get milk, bread, eggs, and fruits"`
5. Delete task: `python -m src.cli.main delete 1`

## Testing the Application
Run the full test suite with:
```bash
python -m pytest
```

Or run specific test types:
```bash
# Unit tests
python -m pytest tests/unit/

# Integration tests
python -m pytest tests/integration/
```

## Implementation Notes
- Tasks are stored in-memory only (no persistence beyond runtime)
- IDs are auto-incremented starting from 1
- Title validation: 1-255 characters
- Description validation: 0-1000 characters
- Task status is either complete (✓) or incomplete (○) when viewing
import argparse
import sys
from src.services.task_manager import TaskManager
from src.lib import utils

def create_parser():
    """
    Create the argument parser with all required commands
    """
    parser = argparse.ArgumentParser(
        description='Todo Console Application - Manage your tasks in memory'
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', help='Task title')
    add_parser.add_argument('description', nargs='?', help='Task description')

    # List command
    list_parser = subparsers.add_parser('list', help='List all tasks')

    # View command (alternative to list)
    view_parser = subparsers.add_parser('view', help='View all tasks')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', type=int, help='Task ID')
    update_parser.add_argument('title', nargs='?', help='New task title')
    update_parser.add_argument('description', nargs='?', help='New task description')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID')

    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
    complete_parser.add_argument('id', type=int, help='Task ID')

    # Incomplete command
    incomplete_parser = subparsers.add_parser('incomplete', help='Mark a task as incomplete')
    incomplete_parser.add_argument('id', type=int, help='Task ID')

    return parser

def main():
    """
    Main entry point for the CLI application
    """
    parser = create_parser()
    args = parser.parse_args()

    # Create a task manager instance
    task_manager = TaskManager()

    # Load tasks from file (or initialize empty list)
    # (For now, tasks are in-memory only)

    # Route to appropriate function based on command
    if args.command == 'add':
        try:
            # Validate arguments
            if not utils.validate_title(args.title):
                print("Error: Title cannot be empty and must be 1-255 characters")
                return
            if args.description and not utils.validate_description(args.description):
                print("Error: Description must be 0-1000 characters")
                return

            task = task_manager.add_task(args.title, args.description)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")
    elif args.command in ['list', 'view']:
        tasks = task_manager.get_all_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            print("\nTask List:")
            for task in tasks:
                status = "✓" if task.completed else "○"
                desc = f" - {task.description}" if task.description else ""
                print(f"[{status}] {task.id}. {task.title}{desc}")
    elif args.command == 'update':
        try:
            # Validate task ID
            if not utils.validate_task_id(args.id):
                print(f"Error: Invalid task ID {args.id}")
                return

            success = task_manager.update_task(args.id, args.title, args.description)
            if success:
                print(f"Task {args.id} updated successfully")
            else:
                print(f"Error: Task with ID {args.id} not found")
        except ValueError as e:
            print(f"Error: {e}")
    elif args.command == 'delete':
        # Validate task ID
        if not utils.validate_task_id(args.id):
            print(f"Error: Invalid task ID {args.id}")
            return

        success = task_manager.delete_task(args.id)
        if success:
            print(f"Task {args.id} deleted successfully")
        else:
            print(f"Error: Task with ID {args.id} not found")
    elif args.command == 'complete':
        # Validate task ID
        if not utils.validate_task_id(args.id):
            print(f"Error: Invalid task ID {args.id}")
            return

        success = task_manager.mark_complete(args.id)
        if success:
            print(f"Task {args.id} marked as complete")
        else:
            print(f"Error: Task with ID {args.id} not found")
    elif args.command == 'incomplete':
        # Validate task ID
        if not utils.validate_task_id(args.id):
            print(f"Error: Invalid task ID {args.id}")
            return

        success = task_manager.mark_incomplete(args.id)
        if success:
            print(f"Task {args.id} marked as incomplete")
        else:
            print(f"Error: Task with ID {args.id} not found")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
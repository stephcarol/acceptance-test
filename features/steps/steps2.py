from behave import *
from main import ToDoListManager
from task import Task
# Step 1: Given the to-do list is empty
@given('the to-do list contains tasks about to be listed')
def step_impl(context):
    # Set the to-do list as an empty list
    context.task1 = Task("1","pepe","2023-12-12",True)
    context.manager = ToDoListManager()
    context.manager.add_task(context.task1)
# Step 2: When the user adds a task "Buy groceries"
@when('the user lists all tasks')
def step_impl(context):
    # Add the task to the to-do list
    context.manager.list_tasks()
# Step 3: Then the to-do list should contain "Buy groceries"
@then('the output should contain')
def step_impl(context):
    # Check if the task is in the to-do list
    assert context.task1 in context.manager.tasks, f'Task not found in the to-do list'
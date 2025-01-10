from behave import *
from main import ToDoListManager
from task import Task
# Step 1: Given the to-do list is empty
@given('the to-do list contains tasks is about to be cleared')
def step_impl(context):
    # Set the to-do list as an empty list
    context.task1 = Task(1,"jose","2024-02-08",False)
    context.manager = ToDoListManager()
    context.manager.add_task(context.task1)
# Step 2: When the user adds a task "Buy groceries"
@when('the user clears the to-do list')
def step_impl(context):
    # Add the task to the to-do list
    context.manager.clear_all_tasks()
# Step 3: Then the to-do list should contain "Buy groceries"
@then('the to-do list should be empty')
def step_impl(context):
    # Check if the task is in the to-do list
    assert len(context.manager.tasks) == 0 , f'Task not found in the to-do list'
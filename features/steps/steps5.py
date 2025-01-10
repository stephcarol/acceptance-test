from datetime import datetime
from behave import *
from main import ToDoListManager
from task import Task
# Step 1: Given the to-do list is empty
@given('the to-do list contains tasks that needs editing')
def step_impl(context):
    # Set the to-do list as an empty list
    context.task1 = Task(1,"pepe","2023-12-12",False)
    context.manager = ToDoListManager()
    context.manager.add_task(context.task1)
# Step 2: When the user adds a task "Buy groceries"
@when('the user edits the task in the to-do list')
def step_impl(context):
    # Add the task to the to-do list
    new_due_date = datetime.strptime("2022-8-8", "%Y-%m-%d")
    context.manager.edit_task(1,"editado",new_due_date)
# Step 3: Then the to-do list should contain "Buy groceries"
@then('the task should be edited')
def step_impl(context):
    # Check if the task is in the to-do list
    assert context.manager.tasks[0].description == "editado", f'Task not found in the to-do list'
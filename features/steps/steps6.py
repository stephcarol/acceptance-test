from behave import *
from main import ToDoListManager
from task import Task
# Step 1: Given the to-do list is empty
@given('the to-do list contains all tasks')
def step_impl(context):
    # Set the to-do list as an empty list
    context.task1 = Task("1","pepe","2023-12-12",False)
    context.task2 = Task("2","pepe","2023-12-12",True)
    context.manager = ToDoListManager()
    context.manager.add_task(context.task1)
    context.manager.add_task(context.task2)
    
# Step 2: When the user adds a task "Buy groceries"
@when('the user chooses to view only uncompleted tasks')
def step_impl(context):
    # Add the task to the to-do list
    context.manager.list_uncompleted_tasks()
# Step 3: Then the to-do list should contain "Buy groceries"
@then('the output shows uncompleted tasks')
def step_impl(context):
    uncompleted_task_ids = [task.task_id for task in context.manager.tasks if not task.completed]
    assert len(uncompleted_task_ids) > 0, "No uncompleted tasks found."
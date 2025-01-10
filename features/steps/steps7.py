from behave import *
from main import ToDoListManager
from task import Task
# Step 1: Given the to-do list is empty
@given('the to-do list contains all tasks with various due dates')
def step_impl(context):
    # Set the to-do list as an empty list
    context.task1 = Task(1,"medio","2023-12-12",False)
    context.task2 = Task(1,"inicial","2022-12-12",False)
    context.task3 = Task(1,"final","2024-12-12",False)
    context.manager = ToDoListManager()
    context.manager.add_task(context.task1)
    context.manager.add_task(context.task2)
    context.manager.add_task(context.task3)

# Step 2: When the user adds a task "Buy groceries"
@when('the user chooses to sort tasks by due date')
def step_impl(context):
    # Add the task to the to-do list
    context.manager.sort_tasks_by_due_date()
# Step 3: Then the to-do list should contain "Buy groceries"
@then('the to-do list should show tasks sorted by due date in ascending order')
def step_impl(context):
    # Check if the task is in the to-do list
    assert context.task2 == context.manager.tasks[0], f'Task not found in the to-do list'
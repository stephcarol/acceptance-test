Feature: To Do list management

    Scenario: Adding a task
        Given the To-Do list is empty
        When the user adds a task "Buy groceries"
        Then the to-do list should contain "Buy groceries"

    Scenario: List all tasks in the to-do list
        Given the to-do list contains tasks about to be listed
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user lists all tasks
        Then the output should contain

    Scenario: Mark a task as completed
        Given the to-do list contains tasks about to be completed
            | Task          | Status  |
            | Buy groceries | Pending |
        When the user marks task 1 as completed
        Then the to-do list should show task 1 as completed

    Scenario: Clear the entire to-do list
        Given the to-do list contains tasks is about to be cleared
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user clears the to-do list
        Then the to-do list should be empty

    Scenario: Edit a task
        Given the to-do list contains tasks that needs editing
        When the user edits the task in the to-do list
        Then the task should be edited

    Scenario: Show only uncompleted tasks
        Given the to-do list contains all tasks
            | Task          | Status    | 
            | Buy groceries | Pending   |
            | Pay bills     | Completed |
        When the user chooses to view only uncompleted tasks
        Then the output shows uncompleted tasks
    
    Scenario: Sort tasks by due date
        Given the to-do list contains all tasks with various due dates
        When the user chooses to sort tasks by due date
        Then the to-do list should show tasks sorted by due date in ascending order


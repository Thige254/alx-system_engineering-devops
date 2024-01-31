#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
from a REST API.
"""

import requests
from sys import argv


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    # Extract employee ID from command-line arguments
    employee_id = int(argv[1])

    # Fetch user data from the API
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list data from the API
    todo_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id))
    todo_data = todo_response.json()

    # Calculate TODO list progress
    total_tasks = len(todo_data)
    completed_tasks = sum(task.get("completed") for task in todo_data)

    # Display the result
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks, total_tasks))

    # Display titles of completed tasks
    for task in todo_data:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))

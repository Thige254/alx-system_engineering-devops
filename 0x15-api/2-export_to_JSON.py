#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
from a REST API and exports it to a JSON file.
"""

import requests
import json
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

    # Create JSON file and write data
    json_filename = "{}.json".format(employee_id)
    with open(json_filename, 'w') as jsonfile:
        json.dump({str(employee_id): [
            {"task": task.get("title"), "completed":
             task.get("completed"), "username": employee_name}
            for task in todo_data
        ]}, jsonfile)

    print("Data exported to {}".format(json_filename))

#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
from a REST API and exports it to a CSV file.
"""

import requests
import csv
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

    # Create CSV file and write header
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write each task to CSV
        for task in todo_data:
            csv_writer.writerow([
                str(employee_id),
                employee_name,
                str(task.get("completed")),
                task.get("title")
            ])

    print("Data exported to {}".format(csv_filename))

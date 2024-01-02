#!/usr/bin/python3
"""
Export data in the CSV format
"""
import csv
from sys import argv
from requests import get


def export_to_csv(user_id, username, tasks):
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write CSV header
        csv_writer.writerow([
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
        ])

        for task in tasks:
            csv_writer.writerow([
                user_id,
                username,
                str(task['completed']),
                task['title']
            ])

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    # Extract employee ID from command-line arguments
    employee_id = int(argv[1])

    # Fetch user data from the API
    user_response =
    get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch TODO list data from the API
    tasks_response =
    get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    tasks_data = tasks_response.json()

    # Call the export_to_csv function
    export_to_csv(employee_id, username, tasks_data)

#!/usr/bin/python3
"""
Export data in the CSV format
"""
import csv
from sys import argv
from requests import get

if __name__ == "__main__":
    user_id = argv[1]

    api_url = 'https://jsonplaceholder.typicode.com/'
    user = get(api_url + 'users/' + str(user_id)).json()

    username = user['username']
    tasks = get(api_url + 'todos', params={'userId': user_id}).json()

    csv_filename = f"{user_id}.csv"

    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write CSV header
        csv_writer.writerow(["USER_ID",
                             "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks:
            csv_writer.writerow([user_id, username,
                                 str(task['completed']), task['title']])

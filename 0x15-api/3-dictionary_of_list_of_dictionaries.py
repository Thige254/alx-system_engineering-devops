#!/usr/bin/python3
"""
Export data in the JSON format
"""
import json
from sys import argv
from requests import get


if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/'
    users = get(api_url + 'users').json()

    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        tasks = get(api_url + 'todos', params={'userId': user_id}).json()

        task_list = []
        for task in tasks:
            task_dict = {
                'username': username,
                'task': task['title'],
                'completed': task['completed']
            }
            task_list.append(task_dict)

        all_tasks[str(user_id)] = task_list

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)

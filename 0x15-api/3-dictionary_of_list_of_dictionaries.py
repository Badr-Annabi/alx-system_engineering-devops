#!/usr/bin/python3
""" This python script exports all data in json file """

import json
import requests
import sys

if __name__ == "__main__":

    users = requests.get(
            "https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()
    alldict = {}

    for user in users:
        tasks = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                Taskdict = {
                        "username": user.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')}
                tasks.append(Taskdict)
        alldict[user.get('id')] = tasks

    with open('todo_all_employees.json', 'w') as jsonfall:
        json.dump(alldict, jsonfall)

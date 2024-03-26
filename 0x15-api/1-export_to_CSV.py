#!/usr/bin/python3
""" This python script exports data in CSV format """

import csv
import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(userId))
    name = user.json().get('username')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    filename = userId + ".csv"
    with open(filename, 'w') as csvf:
        writer = csv.writer(
                csvf, delimiter=',', quotechar='"',
                quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == int(userId):
                writer.writerow(
                        [userId, name, str(task.get("completed")),
                            task.get("title")])

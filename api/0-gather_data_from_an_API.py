#!/usr/bin/python3
"""Script that returns information about an employee's TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(sys.argv[1])

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos?userId={}".format(base_url, employee_id)
    ).json()

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]
    total = len(todos)
    done = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done, total))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))

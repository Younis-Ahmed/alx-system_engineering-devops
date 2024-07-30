#!/usr/bin/python3
"""retrievs information from an API and save as json file"""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    json_file = "{}.json".format(employee_id)

    empl_res = requests.get("{}/users/{}".format(url, employee_id))
    todo_res = requests.get("{}/todos?userId={}".format(url, employee_id))

    employee = empl_res.json()
    todos = todo_res.json()

    username = employee.get("username")
    values = []

    for todo in todos:
        values.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
            })

    json_dict = {employee_id: values}

    with open(json_file, "w") as f:
        json.dump(json_dict, f)

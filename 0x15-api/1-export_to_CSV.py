#!/usr/bin/python3
"""Retrieves information about an employee todo list"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    csv_file = "{}.csv".format(employee_id)

    empl_res = requests.get("{}/users/{}".format(url, employee_id))
    todo_res = requests.get("{}/todos?userId={}".format(url, employee_id))

    employee = empl_res.json()
    todos = todo_res.json()

    username = employee.get("username")

    with open(csv_file, "w") as f:
        for todo in todos:
            csv_data = (
                    f'"{employee_id}",'
                    f'"{username}",'
                    f'"{todo.get("completed")}",'
                    f'"{todo.get("title")}"\n'
                    )
            f.write(csv_data)

#!/usr/bin/python3
""" Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


def fetchdata(user_id):
    """ Write a Python script that, using this REST API,
    for a given employee ID,
    returns information about his/her TODO list progress.
    """
    if user_id is None:
        return
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    tott = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
                ) for t in tott]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(0)
    fetchdata(sys.argv[1])
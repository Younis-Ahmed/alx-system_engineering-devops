#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests
import sys


def fetchdata(user_id):
    """ do json file from aspi"""
    if user_id is None:
        return

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    tott = requests.get(url + "todos", params={"userId": user_id}).json()
    result = {}
    result[str(user_id)] = []
    for task in tott:
        result[str(user_id)].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        })

    # Now, let's save the data to a JSON file
    filename = f'{user_id}.json'

    with open(filename, 'w') as jsonfile:
        json.dump(result, jsonfile)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(0)
    fetchdata(sys.argv[1])

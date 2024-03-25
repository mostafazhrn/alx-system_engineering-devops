#!/usr/bin/python3
"""THis script shall export lst to json format"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(url + "users").json()
    does = requests.get(url + "todos").json()

    info = {}
    for each in usr:
        usr_id = each.get("id")
        usr_name = each.get("username")
        info[usr_id] = [{"task": task.get("title"),
                         "completed": task.get("completed"),
                         "username": usr_name}
                        for task in does if usr_id == task.get("userId")]
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(info, jsonfile)

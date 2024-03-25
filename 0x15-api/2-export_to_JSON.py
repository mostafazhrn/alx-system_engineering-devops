#!/usr/bin/python3
"""THis script shall gather data from API to return from about employees"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(url + "users/{}".format(sys.argv[1])).json()
    usr_id = sys.argv[1]
    does = requests.get(url + "todos", params={"userId": usr_id}).json()
    usr_name = usr.get("username")

    with open("{}.json".format(usr_id), "w") as jsonfile:
        json.dump({usr_id: [{"task": task.get("title"),
                             "completed": task.get("completed"),
                             "username": usr_name} for task in does]},
                  jsonfile)

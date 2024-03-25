#!/usr/bin/python3
"""THis script shall gather data from API to return from about employees"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(url + "users/{}".format(sys.argv[1])).json()
    does = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    done = [task for task in does if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        usr.get("name"), len(done), len(does)))
    [print("\t {}".format(task.get("title"))) for task in done]

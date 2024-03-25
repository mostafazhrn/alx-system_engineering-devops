#!/usr/bin/python3
"""THis script shall gather data from API to return from about employees"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(url + "users/{}".format(sys.argv[1])).json()
    does = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    with open("{}.csv".format(sys.argv[1]), "w") as csvfile:
        write = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [write.writerow([usr.get("id"), usr.get("username"),
                         task.get("completed"),
                         task.get("title")]) for task in does]

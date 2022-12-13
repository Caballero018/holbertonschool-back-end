#!/usr/bin/python3
"""Script that, using a REST API"""
import requests
from sys import argv
import json


def first_line(id):
    id = eval(id)
    if type(id) != int:
        raise TypeError("The data entered is not an integer type")

    users_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos/"

    response2 = requests.get(todos_url)
    response = requests.get(users_url)

    if (response.status_code and response2.status_code) == 200:
        response = requests.get(users_url).json()
        response2 = requests.get(todos_url).json()

        k = 0
        ls = []
        for j in range(len(response2)):
            if response2[j]['userId'] == response[id-1]['id']\
                    and response2[j]['completed'] is True:
                k += 1
                ls.append(response2[j]['title'])

        for i in range(len(response)):
            if response[i]['id'] == id:
                print("Employee {} is done with tasks({}/20):".format(
                    response[i]['name'], k
                    ))
                for done_task in ls:
                    print("\t", done_task)


if __name__ == "__main__":
    first_line(argv[1])

#!/usr/bin/python3
"""Script to export data in the JSON format."""
import json
import requests
from sys import argv


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

        instance = {}
        ins = {}
        for i in range(len(response)):
            if response[i]['id'] == id:
                instance["{}".format(id)] = []
                ins['username'] = response[i]['username']

                for j in range(len(response2)):
                    if response2[j]['userId'] == id:
                        if response2[j]['title'] or response2[j]['completed']:
                            ins = {k: v for k, v in response2[j].items()}

                        instance["{}".format(id)].append(ins)

        with open("{}.json".format(id), 'w+') as f:
            json.dump(instance, f)


if __name__ == "__main__":
    first_line(argv[1])

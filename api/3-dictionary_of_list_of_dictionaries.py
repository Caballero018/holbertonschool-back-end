#!/usr/bin/python3
"""Script to export data in the JSON format."""
import json
import requests
from sys import argv


def all_employees():
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
            instance["{}".format(response[i]['id'])] = []
            for j in range(len(response2)):
                if response2[j]['userId'] == response[i]['id']:
                    ins = {k: v for k, v in response2[j].items()}
                    ins['username'] = response[i]['username']
                    delete(ins)
                    instance["{}".format(response[i]['id'])].append(ins)

        with open("todo_all_employees.json".format(id), 'w+') as f:
            json.dump(instance, f)


def delete(ins):
    if ins['id']:
        del ins['id']
    if ins['userId']:
        del ins['userId']
    if ins['title']:
        ins['task'] = ins['title']
        del ins['title']


if __name__ == "__main__":
    all_employees()

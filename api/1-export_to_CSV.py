#!/usr/bin/python3
"""Script that, using a REST API"""
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

        with open(f"{id}.csv", "w+") as f: 
            for i in range(len(response)):
                for j in range(len(response2)):
                    if response[i]['id'] == id and response2[j]['userId'] == response[i]['id']:
                        f.write('"{}","{}","{}","{}"\n'.format(
                                id, response[i]['name'], response2[j]['completed'],
                                response2[j]['title']
                                ))

if __name__ == "__main__":
    first_line(argv[1])

#!/usr/bin/python3
"""Script to export data in the CSV format."""
import requests
from sys import argv
import csv


def script(id):
    "Doc"
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

        with open(f"{id}.csv", "w", encoding='UTF8') as f:
            for i in range(len(response)):
                for j in range(len(response2)):
                    if response[i]['id'] == id and response2[j]['userId'] \
                            == response[i]['id']:
                        writer = csv.writer(
                            f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL
                                            )
                        writer.writerow((
                            id, response[i]['name'], response2[j]['completed'],
                            response2[j]['title']
                            ))


if __name__ == "__main__":
    script(argv[1])

#!/usr/bin/python3
'''
Extracting info from API
'''
import csv
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]

    URL_name = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    URL_todos = 'https://jsonplaceholder.typicode.com/todos'

    r_name = requests.get(url=URL_name)
    r_todos = requests.get(url=URL_todos)

    dict_name = r_name.json()
    dict_todos = r_todos.json()

    EMPLOYEE_NAME = dict_name.get('name')

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASKS = ''

    for dictio in dict_todos:

        if (dictio.get('userId') is int(user_id)):

            if (dictio.get('completed')):
                NUMBER_OF_DONE_TASKS += 1
                TASKS += '\t' + dictio.get('title') + '\n'

            TOTAL_NUMBER_OF_TASKS += 1

    TASKS = TASKS.rstrip()
    LINE = 'Employee {} is done with tasks({}/{}):\n{}'.format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS, TASKS)

    print(LINE)

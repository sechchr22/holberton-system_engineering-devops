#!/usr/bin/python3
'''
Extracting info from API
'''
import json
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

    USER_NAME = dict_name.get('username')

    dictio_employee = {}
    list_json = []

    for dictio in dict_todos:

        dictio_task = {}
        TASK_TITTLE = ''
        TASK_COMPLETED_STATUS = ''

        if (dictio.get('userId') is int(user_id)):

            dictio_task['username'] = USER_NAME

            TASK_TITTLE = dictio.get('title')
            dictio_task['task'] = TASK_TITTLE

            if (dictio.get('completed')):
                TASK_COMPLETED_STATUS = "True"
            else:
                TASK_COMPLETED_STATUS = "False"

            dictio_task['completed'] = TASK_COMPLETED_STATUS

            list_json.append(dictio_task)

    dictio_employee[str(user_id)] = list_json

    with open('{}.json'.format(user_id), mode='w',
              encoding='utf-8') as json_file:

        json.dump(dictio_employee, json_file)

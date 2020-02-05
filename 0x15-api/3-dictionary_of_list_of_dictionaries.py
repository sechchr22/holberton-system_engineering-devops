#!/usr/bin/python3
'''
Extracting info from API
'''
import json
import requests

if __name__ == "__main__":

    URL_name = 'https://jsonplaceholder.typicode.com/users/'
    URL_todos = 'https://jsonplaceholder.typicode.com/todos'

    r_name = requests.get(url=URL_name)
    r_todos = requests.get(url=URL_todos)

    dict_name = r_name.json()
    dict_todos = r_todos.json()
    id_list = []

    for dictio_1 in dict_name:
        _id = 0
        _id = dictio_1.get('id')
        id_list.append(_id)

    dictio_all = {}
    dictio_employees = {}
    list_json = []

    for dictio in dict_todos:

        for ID in id_list:

            USER_NAME = ''

            for dictio_2 in dict_name:

                if (dictio_2.get('userId') is ID):

                    USER_NAME = dict_2.get('username')

            if (dictio.get('userId') is ID):

                dictio_task = {}
                TASK_TITTLE = ''
                TASK_COMPLETED_STATUS = ''

                dictio_task['username'] = USER_NAME

                TASK_TITTLE = dictio.get('title')
                dictio_task['task'] = TASK_TITTLE

                if (dictio.get('completed')):
                    TASK_COMPLETED_STATUS = "True"
                else:
                    TASK_COMPLETED_STATUS = "False"

                dictio_task['completed'] = TASK_COMPLETED_STATUS

                list_json.append(dictio_task)

                dictio_employees[str(ID)] = list_json

    with open('todo_all_employees.json', mode='w',
              encoding='utf-8') as json_file:

        json.dump(dictio_employees, json_file)

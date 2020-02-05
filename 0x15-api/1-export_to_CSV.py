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

    USER_NAME = dict_name.get('username')

    with open('{}.csv'.format(user_id), mode='w',
              encoding='utf-8') as csv_file:

        csv_file_writer = csv.writer(csv_file)

        for dictio in dict_todos:

            TASK_TITTLE = ''
            TASK_COMPLETED_STATUS = ''

            if (dictio.get('userId') is int(user_id)):

                TASK_TITTLE = dictio.get('title')

                if (dictio.get('completed')):
                    TASK_COMPLETED_STATUS = "True"
                else:
                    TASK_COMPLETED_STATUS = "False"

                csv_file_writer.writerow(
                    [user_id, USER_NAME, TASK_COMPLETED_STATUS, TASK_TITTLE])

#!/usr/bin/python3
'''
Module to Return number of subscribers
from a subreddit
'''
import requests
import sys


def top_ten(subreddit):
    '''
    Queries the Reddit API and returns the number of subscribers
    '''
    user_agent = {'User-Agent': 'reddit'}

    try:
        r = requests.get(
            'https://www.reddit.com/r/{}/top/.json'.format(subreddit),
            headers=user_agent, allow_redirects=False)

        r_json = r.json()
        children = r_json.get('data').get('children')

        for i in range(10):
            print(children[i].get('data').get('title'))

    except BaseException:
        print('None')

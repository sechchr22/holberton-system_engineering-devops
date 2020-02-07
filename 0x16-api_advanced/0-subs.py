#!/usr/bin/python3
'''
Module to Return number of subscribers
from a subreddit
'''
import requests
import sys


def number_of_subscribers(subreddit):
    '''
    Queries the Reddit API and returns the number of subscribers
    '''
    user_agent = {'User-Agent': 'reddit'}

    try:
        r = requests.get(
            'https://www.reddit.com/r/{}/about.json'.format(subreddit),
            allow_redirects=False, headers=user_agent)

        r_json = r.json()
        return (r_json.get('data').get('subscribers'))

    except BaseException:
        return (0)

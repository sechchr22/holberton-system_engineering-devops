#!/usr/bin/python3
'''
Module to Return number of subscribers
from a subreddit
'''
import requests
import sys


def recurse(subreddit, hot_list=[]):
    '''
    Queries the Reddit API and returns the number of subscribers
    '''
    user_agent = {'User-Agent': 'reddit'}

    r = requests.get(
        'https://www.reddit.com/r/{}/hot/.json'.format(subreddit),
        headers=user_agent)

    r_json = r.json()
    children = r_json.get('data').get('children')

    if len(children) == len(hot_list):
        return (hot_list)

    title = children[len(hot_list) + 1].get('data').get('title')

    hot_list.append(title)
    return (recurse(subreddit), hot_list)

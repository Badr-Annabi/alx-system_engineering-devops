#!/usr/bin/python3

"""
This function is quering the Reddit API
and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'CustomClient/1.0'}
    url = f"https://api.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status.code != 200:
        return 0
    if 'data' in response:
        return (response.get('data').get('subscribers'))
    else:
        return 0

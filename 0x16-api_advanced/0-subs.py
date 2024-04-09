#!/usr/bin/python3
"""
THis script shall count the number of subscribers for given subreddit to return
the num of total subs
"""


def number_of_subscribers(subreddit):
    """
    THis shall query the Reddit API and return number of subscribers or to
    give zero if fake sub reddit
    """
    import requests
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit),
                       headers={'User-Agent': 'Python/requests'},
                       allow_redirects=False)
    if url.status_code != 200:
        return 0
    else:
        return url.json().get('data').get('subscribers')

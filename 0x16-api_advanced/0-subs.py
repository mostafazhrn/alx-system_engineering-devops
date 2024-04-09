#!/usr/bin/python3
"""
THis script shall count the number of subscribers for given subreddit to return
the num of total subs
"""
import requests
from requests import get


def number_of_subscribers(subreddit):
    """
    THis shall query the Reddit API and return number of subscribers or to
    give zero if fake sub reddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    hdrs = {'User-Agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers=hdrs, allow_redirects=False)
    if resp.status_code != 200:
        return 0
    compte_subs = resp.json().get('data').get('subscribers')
    return compte_subs

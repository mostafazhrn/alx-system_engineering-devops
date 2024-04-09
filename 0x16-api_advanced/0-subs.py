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
    bz_url = 'https://www.reddit.com'
    url = '{base}/r/{subreddit}/about.json'.format(base=bz_url,
                                                   subreddit=subreddit)
    usr_agt = {'User-Agent': 'Python/requests'}
    respo = requests.get(url, headers=usr_agt, allow_redirects=False)
    if respo.status_code != 200:
        return 0
    return respo.json().get('data').get('subscribers')

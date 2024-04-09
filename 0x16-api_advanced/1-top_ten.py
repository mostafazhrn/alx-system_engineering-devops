#!/usr/bin/python3
"""
THis script shall print the titles of the first 10 posts listed for a given
subreddit
"""
import requests


def top_ten(subreddit):
    """ THis shall query the Reddit API to prnt titles of first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    hdrs = {'User-Agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers=hdrs, allow_redirects=False)
    if resp.status_code != 200:
        print(None)
        return
    posts = resp.json().get('data').get('children')
    for post in posts[:10]:
        print(post.get('data').get('title'))

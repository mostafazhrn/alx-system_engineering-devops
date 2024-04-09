#!/usr/bin/python3
"""
THis script shall return a list containing the titles of all hot articles for
a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], compte=''):
    """
    THis shall query the Reddit API and return a list containing the titles
    of all hot articles
    """
    bz_url = 'https://www.reddit.com'
    url = '{base}/r/{subreddit}/hot.json'.format(base=bz_url,
                                                 subreddit=subreddit)
    usr_agt = {'User-Agent': 'Python/requests'}
    pay = {'after': compte, 'count': '100'}
    respo = requests.get(url, headers=usr_agt, params=pay,
                         allow_redirects=False)
    if respo.status_code == 200:
        respo = respo.json()
        psts = respo.get('data').get('children')
        for pst in psts:
            hot_list.append(pst.get('data').get('title'))
        compte = respo.get('data').get('after')
        if compte is not None:
            return recurse(subreddit, hot_list, compte)
        return hot_list
    return None

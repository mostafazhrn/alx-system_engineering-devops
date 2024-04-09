#!/usr/bin/python3
"""
THis script shall print the titles of the first 10 posts listed for a given
subreddit
"""
import requests


def top_ten(subreddit):
    """ THis shall query the Reddit API to prnt titles of first 10 hot posts"""
    bz_url = 'https://www.reddit.com'
    url = '{base}/r/{subreddit}/hot.json'.format(base=bz_url,
                                                 subreddit=subreddit)
    usr_agt = {'User-Agent': 'Python/requests'}
    respo = requests.get(url, headers=usr_agt, allow_redirects=False)
    if respo.status_code != 200:
        print(None)
        return
    else:
        respo_json = respo.json()
        if respo_json.get('data') and respo_json.get('data').get('children'):
            psts = respo_json.get('data').get('children')
            for pst in psts[:10]:
                if pst.get('data') and pst.get('data').get('title'):
                    print(pst.get('data').get('title'))

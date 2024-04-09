#!/usr/bin/python3
"""
THis script shall get the title of hot art and print sorted count of
given keywords from API
"""
import requests


def count_words(subreddit, word_list, hot_list=[], compte='', nxt={}):
    """
    This instance shall query the API to get title of hot art and
    print the coubnt of given words
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
            return count_words(subreddit, word_list, hot_list, compte, nxt)
        for lett in word_list:
            lett = lett.lower()
            if lett not in nxt:
                nxt[lett] = 0
            for titre in hot_list:
                titre = titre.lower()
                if lett in titre.split():
                    nxt[lett] += titre.split().count(lett)
        for cle in sorted(nxt.keys()):
            if nxt[cle] != 0:
                print('{}: {}'.format(cle, nxt[cle]))
    else:
        print('')

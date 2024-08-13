#!/usr/bin/python3
"""Module for task 2 - count it"""

import requests


def count_words(subreddit, word_list, after=None, dic=None):
    """A recursive function that queries the Reddit API,
        parses the title of all hot articles"""

    if dic is None:
        dic = {word: 0 for word in word_list}

    link = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    resp = requests.get(link, headers={'User-Agent': 'hussien'})

    if resp.status_code != 200:
        return

    hots = resp.json()
    for article in hots['data']['children']:
        for word in word_list:
            key_word = f" {word.lower()} "
            title = article['data']['title'].lower()
            dic[word] += key_word.count(title)

    after = hots['data']['after']
    if not after:
        sorted_dict = dict(sorted(dic.items()))
        for key, value in sorted_dict.items():
            if value:
                print(f"{key}: {value}")
        return

    return (count_words(subreddit, word_list, after, dic))

#!/usr/bin/python3
"""Module for task 2 Recursive function"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """Queries the Reddit API and returns all hot posts
    of the subreddit or Reddit."""

    link = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    heads = {'User-Agent': 'Mozilla/5.0'}

    resp = requests.get(link, headers=heads,
                        params={"limit": 100, "after": after})

    if resp.status_code != 200:
        return None

    posts = resp.json().get("data").get("children")

    if posts:
        for post in posts:
            hot_list.append(post.get("data").get("title"))
            after = resp.json().get("data").get("after")
            if after:
                return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

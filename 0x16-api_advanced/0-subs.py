#!/usr/bin/python3
"""Task 0 how many subs? reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Function to Get number of subscribers from reddit API"""

    resp = requests.get("https://www.reddit.com/r/{subreddit}/about.json"
                        .format(subreddit),
                        headers={'User-Agent': 'Hussien'})

    if resp.status_code != 200:
        return 0

    if resp.json().get("data").get("subscribers"):
        return resp.json().get("data").get("subscribers")
    else:
        return 0

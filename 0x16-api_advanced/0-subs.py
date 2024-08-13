#!/usr/bin/python3
"""TASK-0-GETTING A NUMBER OF SUBCRIBTS"""
import requests


def number_of_subscribers(subreddit):
    """function to Get number of subscribers from reddit API"""
    url = "https://www.reddit.com/r/{subreddit}/about.json".format(subreddit)

    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if resp.status_code != 200:
        return 0

    if resp.json().get("data").get("subscribers"):
        return resp.json().get("data").get("subscribers")
    else:
        return 0
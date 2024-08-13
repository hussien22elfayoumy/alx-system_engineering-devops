"""Task 1 - module to return top ten hot posts"""

import requests

def top_ten(subreddit):
    """function that print the titles and top10"""

    data = requests.get("https://www.reddit.com/r/{subreddit}/top.json"
                        .format(subreddit),
                        headers={'User-Agent': 'Mozilla/5.0'},
                        params={"limit": 10})

    if data.status_code != 200:
        print(None)
        return

    usr_posts = data.json().get("data").get("children")

    if usr_posts:
        for usr_post in usr_posts:
            print(usr_post.get("data").get("title"))
    else:
        print("None")

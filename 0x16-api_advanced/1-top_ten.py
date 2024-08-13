"""Task 1 - module to return top ten hot posts"""

import requests

def top_ten(subreddit):
    """function that print the titles and top10"""

    link = "https://www.reddit.com/r/{subreddit}/top.json".format(subreddit)
    
    heads = {'User-Agent': 'Mozilla/5.0'}

    data = requests.get(link, headers=heads, params={"limit": 10})

    if data.status_code != 200:
        print(None)
        return

    usr_posts = data.json().get("data").get("children")

    if usr_posts:
        for post in usr_posts:
            print(post.get("data").get("title"))
    else:
        print(None)

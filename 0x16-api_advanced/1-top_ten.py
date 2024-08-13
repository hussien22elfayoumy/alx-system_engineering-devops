"""Task 1 - module to return top ten hot posts"""

import requests

def top_ten(subreddit):
    """function that print the titles and top10."""
    link = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/your_username)"
    }

    resp = requests.get(link, headers=headers, allow_redirects=False)

    if resp.status_code == 404:
        print("None")
        return
    elif resp.status_code == 200:
        data = resp.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")

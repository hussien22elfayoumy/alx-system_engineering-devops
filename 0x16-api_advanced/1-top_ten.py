"""Task 1 - module to return top ten hot posts"""

import requests

def top_ten(subreddit):
    """function that print the titles and top10"""

    subs = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if subs.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in subs.json().get("data").get("children")]

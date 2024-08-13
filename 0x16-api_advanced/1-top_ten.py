"""Task 1 - module to return top ten hot posts"""

import requests

def top_ten(subreddit):
    """function that print the titles and top10"""

    sub_info = requests.get("https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in sub_info.json().get("data").get("children")]
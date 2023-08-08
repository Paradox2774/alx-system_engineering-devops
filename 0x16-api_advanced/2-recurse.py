
#!/usr/bin/python3
"""
Using reddit's API
"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    headers = {'User-Agent': 'MyRedditBot/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('data', {}).get('children', [])

        if not articles:
            return None

        for article in articles:
            title = article.get('data',b {}).get('title', '')
            hot_list.append(title)

        after = data.get('data', {}).get('after', None)

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

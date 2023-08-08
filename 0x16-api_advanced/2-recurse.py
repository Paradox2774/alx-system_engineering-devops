#!/usr/bin/python3
"""
Using reddit's API
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Return a list of hot post titles recursively from a subreddit."""
    headers = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}
    
    result = requests.get(url, params=params, headers=headers, allow_redirects=False)
    
    if result.status_code == 200:
        data = result.json().get("data")
        if data is not None:
            after = data.get("after")
            children = data.get("children")
            for child in children:
                title = child.get("data").get("title")
                hot_list.append(title)
            
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None


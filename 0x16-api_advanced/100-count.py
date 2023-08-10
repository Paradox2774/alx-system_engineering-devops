#!/usr/bin/python3
"""Reddit API"""

import requests

def count_words(subreddit, word_list, after=None, count=None):
    if count is None:
        count = {word: 0 for word in word_list}
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'api_advanced-project'}
    
    response = requests.get(url, params=params, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get("data")
        if data is not None:
            children = data.get("children")
            for child in children:
                title_words = child.get("data").get("title").lower().split()
                for word in word_list:
                    for title_word in title_words:
                        if title_word.startswith(word.lower()) and title_word[len(word):].isalpha() == False:
                            count[word] += 1
            
            after = data.get("after")
            if after:
                return count_words(subreddit, word_list, after, count)
            else:
                sorted_words = sorted(word_list, key=lambda w: (-count[w], w.lower()))
                for word in sorted_words:
                    if count[word] > 0:
                        print(f"{word.lower()}: {count[word]}")
        else:
            return
    elif response.status_code == 404:
        return
    else:
        raise Exception(f"Request failed with status code: {response.status_code}")


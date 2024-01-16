#!/usr/bin/python3
"""function that queries Reddit API n prints titles of first 10 hot posts"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, prints None.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'custom-user-agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])
            if data:
                for post in data:
                    print(post.get('data', {}).get('title'))
            else:
                print("No posts found.")
        else:
            print(None)
    except Exception as e:
        print(None)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

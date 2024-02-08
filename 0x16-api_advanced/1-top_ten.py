#!/usr/bin/python3
"""
Module to print titles offirst 10 hot posts listed for a given subreddit
"""

from requests import get
import json


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.

    Args:
        subreddit: A string representing the name of the subreddit.

    Returns:
        None
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    try:
        response = get(url, headers=user_agent, params=params)
        results = response.json()

        if 'error' in results:
            print("None")
            return

        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")


# Test the function with subreddit names
if __name__ == "__main__":
    top_ten("programming")
    top_ten("this_is_a_fake_subreddit")

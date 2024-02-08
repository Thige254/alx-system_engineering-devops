#!/usr/bin/python3
"""
Module to query the Reddit API for the number of subscribers of a subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers of a subreddit.

    Args:
        subreddit: A string representing the name of the subreddit.

    Returns:
        No. of subscribers of the subreddit, or 0 if invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}  # Setting a custom User-Agent
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0


if __name__ == "__main__":
    subreddit_name = input("Enter the name of the subreddit: ")
    print("Number of subscribers:", number_of_subscribers(subreddit_name))

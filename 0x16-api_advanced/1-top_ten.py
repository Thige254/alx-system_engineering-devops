#!/usr/bin/python3
"""
This script retrieves no. of subscribers for a specified Reddit subreddit.
"""

import requests


def get_subreddit_subscribers(subreddit):
    """Retrieve the total number of subscribers for a specified subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent: linux:my_script:v1.0.0 (by /u/myredditusername)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    return data.get("subscribers")

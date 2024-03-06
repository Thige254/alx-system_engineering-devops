#!/usr/bin/python3
"""
Recursive function to query list of all hot posts on a given Reddit subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the post titles.
                                   Default is an empty list.
        after (str, optional): Token used for pagination.
                               Default is None.

    Returns:
        list: A list of post titles from the hot section of the subreddit.
              None if the subreddit is invalid or no results are found.
    """
    # Base case: if subreddit is None or empty, return None
    if not subreddit:
        return None

    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, including pagination and limit
    params = {
        "limit": 100,
        "after": after
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        return None

    # Parse the JSON response and extract relevant data
    data = response.json().get("data")
    after = data.get("after")
    children = data.get("children")

    # Append post titles to the hot_list
    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)

    # If there are more posts to retrieve, recursively call the function
    if after:
        return recurse(subreddit, hot_list, after)

    # Return the final list of hot post titles
    return hot_list


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result:
            print(len(result))
        else:
            print("None")

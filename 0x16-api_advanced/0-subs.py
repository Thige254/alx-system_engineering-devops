#!/usr/bin/python3
"""
0-subs function queries Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If not a valid subreddit, returns 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'custom-user-agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for redirection
        if response.status_code == 302:
            print("0")
            return 0

        # Check for successful response
        if response.status_code == 200:
            data = response.json().get('data')
            if data:
                print("OK")
                return data.get('subscribers', 0)

        print("0")
        return 0
    except Exception as e:
        print("0")
        return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subscribers_count = number_of_subscribers(sys.argv[1])
        print("{:d}".format(subscribers_count))

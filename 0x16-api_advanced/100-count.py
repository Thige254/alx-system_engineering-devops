#!/usr/bin/python3
"""
100-count recursively queries Reddit API, parses titles of all hot articles
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.
    """
    url_base = f'https://www.reddit.com/r/{subreddit}/hot.json'
    url = url_base if after is None else f'{url_base}?after={after}'

    headers = {'User-Agent': 'custom-user-agent'}

    if counts is None:
        counts = {}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            after = data.get('after', None)

            for post in children:
                title = post['data']['title'].lower()
                for word in word_list:
                    word = word.lower()
                    if word in title:
                        counts[word] = counts.get(word, 0) + 1

            if after:
                return count_words(subreddit, word_list, after, counts)
            elif not counts:
                print("No posts matched the given keywords.")
            else:
                print_results(counts)
        elif response.status_code == 404:
            error_message = (
                f"Error: Subreddit '{subreddit}' not found."
            )
            print(error_message)
        else:
            error_message = (
                f"Error: Unable to fetch data from Reddit. "
                f"Status code: {response.status_code}"
            )
            print(error_message)
    except Exception as e:
        print(f"Error: {str(e)}")


def print_results(counts):
    """
    Prints results in descending order by count and alphabetically.
    """
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <keyword list>".format(sys.argv[0]))
        print("Ex: {} programming 'py java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])

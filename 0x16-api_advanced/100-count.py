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
    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

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
            else:
                print_results(counts)
        else:
            print("None")
    except Exception as e:
        print("None")


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

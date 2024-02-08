#!/usr/bin/python3
"""Module to count words in subreddit titles"""

import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """
    Counts occurrences of words from a list in subreddit titles.

    Args:
        subreddit: A string representing the name of the subreddit.
        word_list: A list of strings containing words to count occurrences of.
        after: string representing last post identifier in the pagination.
        count: A list to store the counts of each word.

    Returns:
        None
    """
    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'thige'}  # Adjusted User-Agent
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers=headers)

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[i])):
                        aux = count[i]
                        count[i] = count[j]
                        count[j] = aux
                        aux = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = aux

            for i in range(len(word_list)):
                if (count[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
        else:
            count_words(subreddit, word_list, after, count)

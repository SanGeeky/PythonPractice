# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math
import os
import random
import re
import sys

import requests

url = 'https://jsonmock.hackerrank.com/api/article_users?page='


def getUsernames(threshold):
    usernames = []
    page = 1

    while len(usernames) < threshold:
        response = requests.get(url + str(page))
        data = response.json()

        if threshold > data["total"]:
            return []

        for user in data["data"]:
            usernames.append(user["username"])
            if len(usernames) == threshold:
                return usernames
        page += 1


if __name__ == '__main__':
    result = getUsernames(10)

    print(result)
    print(len(result))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

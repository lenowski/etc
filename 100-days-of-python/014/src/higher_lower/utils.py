"""
Helper functions.
"""


import random

from higher_lower.art import VS


def get_random_option(data):
    """
    Return a randomly selected option from the data list.
    """
    return data.pop(random.choice(range(len(data))))


def compare_options(opt_a, opt_b):
    """
    Compare the number of followers of two options,
    return True if opt_a has more followers, otherwise False.
    """
    return opt_a["follower_count"] >= opt_b["follower_count"]


def print_options(opt_a, opt_b):
    """
    Print the details of two options to compare.
    """
    print(
        f"Compare A: {opt_a['name']}, a {opt_a['description']}, from {opt_a['country']}."
    )
    print(VS)
    print(
        f"Against B: {opt_b['name']}, a {opt_b['description']}, from {opt_b['country']}."
    )

"""
Helper functions.
"""

import random


def deal_card():
    """
    Return a random card from the deck.
    """

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(hand):
    """
    Take a list of cards and return the score calculated from the cards.
    """

    score = sum(hand)
    if score == 21 and len(hand) == 2:
        return 0

    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

    return score


def compare(player_score, dealer_score):
    """
    Compare the scores and return the result of the game.
    """

    if player_score == dealer_score:
        return "Draw."
    if dealer_score == 0:
        return "Lose, opponent has Blackjack."
    if player_score == 0:
        return "Win with a Blackjack."
    if player_score > 21:
        return "You went over. You lose."
    if dealer_score > 21:
        return "You win."
    return "You lose."

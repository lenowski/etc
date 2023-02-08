"""
Entry point to the Blackjack.
"""

from os import system

from blackjack.art import LOGO
from blackjack.utils import calculate_score, compare, deal_card


def main():
    while True:
        system("clear")
        print(LOGO)

        player_cards = [deal_card(), deal_card()]
        dealer_cards = [deal_card(), deal_card()]

        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards[:1])

        print(f"   Your cards: {player_cards}, current score: {player_score}")
        print(f"   Computer's first card: {dealer_cards[0]}")

        while player_score < 21 and input("Another card? [y/n] ").lower() == "y":
            player_cards.append(deal_card())
            player_score = calculate_score(player_cards)

        while dealer_score < 17:
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)

        print(f"   Your final hand: {player_cards}, final score: {player_score}")
        print(f"   Computer's final hand: {dealer_cards}, final score: {dealer_score}")
        print(compare(player_score, dealer_score))

        if input("Do you want to play again? [y/n] ").lower() != "y":
            break

import os
import sys

from blind_auction.art import LOGO
from blind_auction.auctioneer import find_highest_bidder


def main():
    print(LOGO)
    auction_log = {}
    bidding_finished = False
    while not bidding_finished:
        name = input("What is your name? ")
        bid = int(input("What is your bid? $"))

        auction_log[name] = bid
        should_continue = input("Are there any other bidders? [yes/no] ")
        if should_continue == "no":
            bidding_finished = True
            find_highest_bidder(auction_log)
        else:
            os.system("clear")


if __name__ == "__main__":
    sys.exit(main())

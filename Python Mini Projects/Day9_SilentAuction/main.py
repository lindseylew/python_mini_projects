print(art.logo)

bidders = {}

def silent_bid():
    name = input("What is your name? ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    print(bidders)

add_bidder = True
while add_bidder == True:
    silent_bid()

    more_bidders = input("Are there any other bidders. Type 'yes' or 'no'.").lower()

    if more_bidders == "no":
        add_bidder = False

        highest_bid = 0
        winner = ""
        for bidder in bidders:
            if bidders[bidder] > highest_bid:
                highest_bid = bidders[bidder]
                winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}!")
    elif more_bidders == "yes":
        print("\n" * 100)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from logo import logo
from replit import clear

print(logo)
print("Welcome to the secret auction program.")

bidding_finished = False
bids = {}

def find_heighest_bidder(bidding_record):
  heighest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > heighest_bid:
      heighest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${heighest_bid}")

while bidding_finished == False:
  bidder_name = input("What is your name?:\t")
  bidder_bid = int(input("What is your bid?:\t$"))
  other_bidder = input("Are there any other bidders?Type 'yes' or 'no'.\n")
  bids[bidder_name] = bidder_bid
  if other_bidder.lower() == "yes":
    clear()
  elif other_bidder.lower() == "no":
    bidding_finished = True
    clear()
    
find_heighest_bidder(bids)
from replit import clear
from art import logo
print("Welcome to Secret Bidding Auction\n")
print(logo+"\n")
bidding={}
def add_bidder(bidder_dict):
  bidder_name =input("What is your name ?:")
  bid_amount = input("what's your bid ?:\n")
  bidder_dict[bidder_name]=bid_amount
add_bidder(bidding)
while True:
  next_bidder = input("Are there any other bidders? Type 'Yes' or 'No': ").capitalize()
  if next_bidder == 'No':
    clear()
    break
  elif next_bidder=='Yes':
    clear()
    add_bidder(bidding)
    
max_amount = max(bidding.values())
max_bidder = [key for key, value in bidding.items() if value == max_amount]
max_bidder_names=', '.join(max_bidder)
print(f"The winner is {max_bidder_names} and the bid is ${max_amount}")

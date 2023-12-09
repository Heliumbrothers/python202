import os, time
def clear():
  os.system('cts' if os.name == 'nt' else 'clear')
  
clear()
for i in range(0, 6):
  print(".")
  clear()
  time.sleep(0.5)
  print(".")
  clear()
  time.sleep(0.5)  
  print("...")
  clear()
  time.sleep(0.5)

print("loading almost comeplete...")
time.sleep(1.2)
clear()
print("loading complete")
time.sleep(0.4)


from day9_art import logo
clear()
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":

    clear()
  


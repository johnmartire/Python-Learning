bids = {}  # Dictionary to store names and their bids

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))  # Convert bid to an integer

    bids[name] = bid  # Store the name and bid in the dictionary

    after = input("Are there any other bidders? yes or no: ").lower()
    
    if after == 'no':
        break
    elif after != 'yes':
        print("Only say yes or no")

# Find the person with the highest bid
max_key = max(bids, key=bids.get)

print(f"The person with the highest bid is: {max_key} with a bid of ${bids[max_key]}")

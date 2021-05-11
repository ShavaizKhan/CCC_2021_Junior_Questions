N = int(input())

highest_bid = 0

for i in range(N):
  name = input()
  bid = int(input())
  if highest_bid == 0 or bid > highest_bid:
    highest_bid = bid
    winner = name
  elif highest_bid == bid:
    continue

print(winner)    

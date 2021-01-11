# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
    return 2 ** n

print(coin_flips(1)) 
# => ["H", "T"]
print(coin_flips(2)) 
# => ["HH", "HT", "TH", "TT"]
print(coin_flips(3)) 
# => ["HHH", "HHT", "HTH", "HTT", "THH", "THT", "TTH", "TTT"]
# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
    if n == 1:
        return ['H', 'T']
    flipped = coin_flips(n - 1)
    history_plus_heads = map(lambda el: el + 'H', flipped)
    history_plus_tails = map(lambda el: el + 'T', flipped)
    return history_plus_heads + history_plus_tails

print(coin_flips(1)) 
# => ["H", "T"]
print(coin_flips(2)) 
# => ["HH", "HT", "TH", "TT"]
print(coin_flips(3)) 
# => ["HHH", "HHT", "HTH", "HTT", "THH", "THT", "TTH", "TTT"]

# DIFFERENCE BETWEEN PYTHON AND JAVASCRIPT WITH ANONYMOUS FUNCTIONS

# Python:
# map(lambda el: el + 'H', history)

# JavaScript:
# history.map((el) => {
#     return el + 'H'
# })
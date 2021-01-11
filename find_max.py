# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(l, current_max = -float('inf')):
    if len(l) == 0:
        return current_max
    if l[0] > current_max:
        new_current_max = l[0]
    else:
        new_curent_max = current_max
    return find_max(l[1:], new_current_max)

print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45
assert(find_max([1, 4, 45, 6, -50, 10, 2]) == 45)
# => True
print(find_max([198, -487, 68, -5, 321, 11, 226]))
# => 321
assert(find_max([198, -487, 68, -5, 321, 11, 226]) == 321)
# => True
print(find_max([2, 3, 5, 7]))
# => 7
assert(find_max([2, 3, 5, 7]) == 7)
# => True
print(find_max([10000, 5000, 2500, 1250]))
# => 10000
assert(find_max([10000, 5000, 2500, 1250]) == 10000)
# => True
# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(l):
    if len(l) == 1:
        return l[0]
    else:
        if l[1] > l[0]:
            l.remove(l[0])
        else:
            l.remove(l[1])
        find_max(l)

print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45
print(find_max([198, -487, 68, -5, 321, 11, 226]))
# => 321
print(find_max([2, 3, 5, 7]))
# => 7
print(find_max([10000, 5000, 2500, 1250]))
# => 10000
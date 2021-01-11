# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(l):
    maximum = l[0]
    for i in range(len(l)):
        if l[i] > maximum:
            maximum = l[i]
        else:
            find_max(i + 1)
    return maximum

print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45
print(find_max([198, -487, 68, -5, 321, 11, 226]))
# => 321
print(find_max([2, 3, 5, 7]))
# => 7
print(find_max([10000, 5000, 2500, 1250]))
# => 10000
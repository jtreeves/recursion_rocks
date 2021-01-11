# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

print(factorial(0))
# => 1
print(factorial(3))
# => 6
print(factorial(5))
# => 120
print(factorial(7))
# => 5040
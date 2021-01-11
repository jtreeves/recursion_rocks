# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n):
    if type(n) != int:
        raise TypeError('Input needs to be a whole number')
    product = 1
    if n < 0:
        return
    elif n == 0:
        return 1
    else:
        product *= factorial(n - 1)
        return product

print(factorial(0))
# => 1
print(factorial(3))
# => 6
print(factorial(5))
# => 120
print(factorial(7))
# => 5040
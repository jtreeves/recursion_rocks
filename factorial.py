# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n):
    if type(n) != int or n < 0:
        raise TypeError('Input needs to be a whole number')
    if n > 0:
        return n * factorial(n-1)
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
print(factorial('-2'))
# => TypeError: Input needs to be a whole number
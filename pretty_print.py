# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a function that accepts a complex dictionary and prints out all of it's keys and all of its values. 
# The dictionary can have dictionaries nested inside of it
# 'dictionary' is the dictionary that's currently being iterated over.
# 'indent' is a string representing the current level of indentation
# ...
# pretty_print(inner_dictionary, indent + '..');
# ...

def pretty_print(dictionary, indent, level = 1):
    for key in dictionary:
        value = dictionary[key]
        if type(value) is dict:
            print(f'{indent*level}{key}:')
            pretty_print(value, indent, level + 1)
        else:
            print(f'{indent*level}{key}: {value}')

o1 = {"a": 1, "b": 2}
o2 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero"}, "d": 4}
o3 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero", "friends": {"spiderman": {"name": "Peter Parker"}, "superman": {"name": "Clark Kent"}}}, "d": 4}

pretty_print(o1, "-")
# -a: 1
# -b: 2
pretty_print(o2, " ")
#  a: 1
#  b: 2
#  c:
#   name: Bruce Wayne
#   occupation: Hero
#  d: 4
pretty_print(o3, "..")
# ..a: 1
# ..b: 2
# ..c:
# ....name: Bruce Wayne
# ....occupation: Hero
# ....friends: 
# ......spiderman:
# ........name: Peter Parker
# ......superman: 
# ........name: Clark Kent
# ..d: 4
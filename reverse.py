# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(ss):
    original_list = list(ss)
    reversed_list = []
    for letter in original_list:
        reversed_list.insert(0, letter)
    reversed_string = ''.join(reversed_list)
    return reversed_string

print(reverse("")) 
# => ""
print(reverse("a")) 
# => "a"
print(reverse("ab")) 
# => "ba"
print(reverse("computer")) 
# => "retupmoc"
print(reverse(reverse("computer"))) 
# => "computer"
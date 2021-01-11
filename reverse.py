# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(input, output):
    if len(input) == 0:
        return output
    new_output = input[0] + output
    new_input = input[1:]
    return reverse(new_input, new_output)

print(reverse('', '')) 
# => ''
print(reverse('a', '')) 
# => 'a'
print(reverse('ab', '')) 
# => 'ba'
print(reverse('computer', '')) 
# => 'retupmoc'
print(reverse(reverse('computer', ''), '')) 
# => 'computer'
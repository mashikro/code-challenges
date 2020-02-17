# Prompt: Write a function that takes a list of characters and reverses 
# the letters in place.

lst = ['a', 'p', 'p', 'l', 'e']

# print(lst) # ['a', 'p', 'p', 'l', 'e']

def reverse_char_in_place(lst):
    # pos1 = 0
    # pos2 = -1

    i = 0
    
    while i <= len(lst)//2:
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
        i +=1

    #     # pos1 +=1
    #     # pos2 -=1

reverse_char_in_place(lst) # [e, l, p, p, a]

# print(lst)




def reverse_char(lst):
    return lst[::-1] # doesnt reverse in place, creates a new lst
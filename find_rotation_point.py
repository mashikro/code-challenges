# Prompt: Write a function for finding the index of the "rotation point," 
# which is where I started working from the beginning of the dictionary. 
# This list is huge (there are lots of words I don't know) so we want to 
# be efficient here.

# Test Case:
# Input:
words = [
'ptolemaic',
'retrograde',
'supplant',
'undulate',
'xenoepist',
'asymptote',  # <-- rotates here! w index 5
'babka',
'banoffee',
'engender',
'karpatka',
'othellolagkage',
]

# output: 5

def find_rotation_point(words):
    floor_i = -1
    ceiling_i = len(words)

    while floor_i+1 < ceiling_i:

        half_dis = (ceiling_i - floor_i)//2
        gueess_i = floor_i+half_dis
        guess_v = words[gueess_i]

        if guess_v[0] == 'a':
            return gueess_i

        if guess_v[0] > 'a':
            ceiling_i=gueess_i
        else:
            floor_i = gueess_i
    return 'not found'



print(find_rotation_point(words))


# Runtime: Binary Search thus O(n log n)




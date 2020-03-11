# You're given strings J representing the types of stones that are jewels, and S 
# representing the stones you have.  Each character in S is a type of stone you have.  
# You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. 
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Test Case:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3

def find_stones_that_are_also_jewels(jewel, stone):

    jewels = set(jewel)

    count = 0

    for item in stone:
        if item in jewels:
            count+=1

    return count


print(find_stones_that_are_also_jewels("aA",  "aAAbbbb")) #3
print(find_stones_that_are_also_jewels("z", "ZZ")) #0

# Runtime: O(n)
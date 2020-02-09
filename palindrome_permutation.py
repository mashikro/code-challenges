# Prompt: Given a str write a func to check if it's a permutation of a palindrome
# palindrome = word that's spelled the same forward and backwards
# permutation = rearrangement of letters
# Palindorme doesn't need to be limited to dictionary word

# Test case:
# Input: Tact Coa
# output: True 

def make_dict(s):
    counts = {}

    for l in s:
        lowered_l = l.lower()
        if lowered_l not in counts:
            counts[lowered_l] = 1
        else:
            counts[lowered_l] += 1

    if " " in counts:
            del counts[" "]

    return counts

def check_palindorme(s):
    
    counts = make_dict(s)
    list_counts = list(counts.values())
    list_counts.sort()
    
    if list_counts[0] == 1:
        for n in list_counts[1:]:
            if n%2 != 0:
                return False
        return True
    else:
        for n in list_counts:
            if n%2 != 0:
                return False
        return True


print(check_palindorme("Tact Coa")) #TRUE
print(check_palindorme("Tact Coza")) #FALSE
print(check_palindorme("hannah")) #TRUE


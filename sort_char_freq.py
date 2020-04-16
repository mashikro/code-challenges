# Prompt: Given a string, sort it in decreasing order based on the frequency of characters.

# Test Cases:
# Input: "tree"
# Output: "eert"

#or
# Input: "cccaaa"
# Output: "cccaaa"

def sort_char_by_freq(s):

    import collections

    count = collections.Counter(s)

    # print('count', count)

    letters = []

    for k, v in count.items():
        letters.append((v,k))
    
    letters.sort(reverse=True)
    
    # print('letters', letters)

    ret = ""

    for item in letters:
        ret += (item[0]* item[1])
    return ret

print(sort_char_by_freq('eert'))
print(sort_char_by_freq('cccaaa'))
print(sort_char_by_freq("Aabb"))

# Runtime: O(3n) for count, letters and ret loops and O(nlogn) for sorting-> O(n log n) time
# Runtime: count - O(n), letters - O(n), ret- O(1) -> O(n) space
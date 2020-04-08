# Prompt: https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

def two_string_overlap(s1, s2):
    lst_s1 = list(s1)
    s1_set = set(lst_s1)

    for l in s2:
        if l in s1_set:
            return 'YES'
    return 'NO'

print(two_string_overlap('hello', 'world'))

#Runtime: O(n) time and O(n) space
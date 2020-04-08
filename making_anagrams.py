# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings


def making_anagrams(a, b):

    import collections

    a_count = collections.Counter(a)
    b_count = collections.Counter(b)

    for k in a_count.keys():
        if k in b_count:
            temp = a_count[k]
            a_count[k] -= b_count[k]
            b_count[k] -=temp
        

    ret = 0

    for v in a_count.values():
        if v > 0:
            ret+=v
    for v in b_count.values():
        if v > 0:
            ret +=v

    return ret


print(making_anagrams('bacdc', 'dcbac')) #0
print(making_anagrams('bacdc', 'dcbad')) #2
print(making_anagrams('cde', 'abc')) #4

# Runtime: O(n) time and O(n) space
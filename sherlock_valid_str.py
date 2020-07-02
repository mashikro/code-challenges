# prompt:
    # https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings


# test cases:
# input: aabbcd
# output: NO

# input: abcdefghhgfedecba
# output: YES


def is_valid(s):
    import collections
    
    count = collections.Counter(s)
    print('count:', count)
    
    lst = list(count.values())
    sorted_count = sorted(lst) #sorts lst by frequency (how often it appears)
    print('sorted_vals:', sorted_count)

    set_ = set(count.values())
    print('set_:', set_)
    
    if len(set_)<=1:
        return 'YES'
    if len(set_) == 2:
        temp = sorted_count[0]
        sorted_count[0] = temp-1
        print('new sorted_vals', sorted_count)
        if len(set(sorted_count)) == 1 or (len(set(sorted_count))==2 and 0 in sorted_count):
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO' 

print(is_valid('abc')) #Y
print(is_valid('abccc')) #N
print(is_valid('aabbcd')) #N
# print(is_valid('')) #Y
# print(is_valid('aaaa')) #Y
print(is_valid('accddff')) #Y
# print(is_valid('abcdefghhgfedecba')) #Y
print(is_valid('aabbccc')) #Y (4)

# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing 
# second character of the final pair with an underscore ('_').

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def split_str(s):

    ret = []

    beg = 0
    end = 2

    for l in s:
        ret.append(s[beg:end])
        beg += 2
        end += 2
    
    r = []

    for i in range(len(ret)):
        if len(ret[i]) == 2:
            r.append(ret[i])
        if len(ret[i]) == 1:
            r.append(ret[i]+'_')

    return r

# print(split_str('abcdef'))
# print(split_str('abc'))
# print(split_str('a'))

def split_str2(s):

    if len(s) % 2 == 1:
        s+= "_"

    ret = []

    beg = 0
    end = 2

    # >>> range(0,10,2)
    #     [0, 2, 4, 6, 8]
    
    for i in range(0, len(s), 2):
        ret.append(s[i:i+2])

    return ret


print(split_str2('abcdef'))
print(split_str2('abc'))
print(split_str2('a'))

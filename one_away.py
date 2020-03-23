# There are 3 types of edits that can be performed on str:
#     insert a char
#     remove a char
#     replace a char
# Write a func to check if they are one or 0 edits away

# Test Case:
# pale, ple -> True
# pales, pale -> True
# pale, bale -> True
# pale, bake -> False

def check_one_away(s1,s2):
    
    def one_edit_replace(s1, s2):
        edited = False
        for c1, c2 in zip(s1, s2): #zip() takes in iterables and creates a tuple of tuples. ((a,b), (c,d))
            if c1 != c2:
                if edited:
                    return False #only returns when it detects 2nd edit
                edited = True
        return True


    def one_edit_insert(s1, s2):
        edited = False
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                if edited:
                    return False #only returns when it detects 2nd edit
                edited = True
                i += 1 # note to update the longer string
            else:
                i += 1
                j += 1
        return True

    if s1==s2:
        return True
    if len(s1) == len(s2):
        return one_edit_replace(s1,s2)
    if len(s1)+1 == len(s2):
        return one_edit_insert(s1,s2)
    if len(s1)-1 == len(s2):
        return one_edit_insert(s1,s2)

    return False

# True cases
print(check_one_away('pale', 'bale'))
print(check_one_away('pale','pales'))
print(check_one_away('pale', 'ple'))

# False cases
print(check_one_away('pale', 'bake'))
print(check_one_away('pale','pakes'))
print(check_one_away('pale', 'ples'))















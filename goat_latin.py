# Prompt: Given a sentence do the following:

# If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
# For example, the word 'apple' becomes 'applema'.
 
# If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
 
# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.


# Test Case:
# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

def translate_to_goat_latin(s):

    vowels = {'a', 'e', 'i', 'o', 'u'} 

    list_s = s.split() 

    new_s = []

    for i in range(len(list_s)):
        if list_s[i][0].lower() in vowels:
            list_s[i] = list_s[i] + 'ma'
        else:
            removed = list_s[i][0]
            list_s[i] = list_s[i][1:] + removed + 'ma'
        
        list_s[i]+=('a'*(1+i))

        new_s.append(list_s[i])

    return ' '.join(new_s)

print(translate_to_goat_latin("I speak Goat Latin"))
# Prompt: Write a function that, given a sentence like the one above, along with
#  the position of an opening parenthesis, finds the corresponding closing parenthesis.
# Test Case:
# "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

# Example: if the example string above is input with the number 10 (position of the 
# first parenthesis), the output should be 79 (position of the last parenthesis).


def match_paren(index_, s): #where i-index and s-string
    

    opener = '('
    closer = ')'

    opener_count = 0

    for i in range(len(s)):
        if s[i] == opener:
            opener_count+=1
        if s[i] == closer:
            opener_count-=1
            if opener_count < 1:
                return i


print(match_paren(10, "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."))#79
print(match_paren(0, "(()(()))")) #7

#Runtime is O(n)


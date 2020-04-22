# Prompt: https://leetcode.com/problems/verifying-an-alien-dictionary/submissions/

def is_ordered(alien_dict, word_1, word_2):

    i = 0
    w1 = len(word_1)
    w2 = len(word_2)
    min_len = min(w1,w2)

    while i < min_len:

        if word_1[i] == word_2[i]:
            i+=1
        elif word_1[i] != word_2[i]:
            if alien_dict[word_1[i]] < alien_dict[word_2[i]]:
                return True
            else:
                return False
    
    if len(word_1) <= len(word_2):
        return True
    return False

# print(is_ordered("hlabcdefgijkmnopqrstuvwxyz", 'word', 'world')) #false
# print(is_ordered("hlabcdefgijkmnopqrstuvwxyz", 'world', 'word')) #true
# print(is_ordered("hlabcdefgijkmnopqrstuvwxyz", 'word', 'word')) #true
# print(is_ordered("hlabcdefgijkmnopqrstuvwxyz", 'w', 'w')) #true
# print(is_ordered("hlabcdefgijkmnopqrstuvwxyz", 'w', 'z')) #true
# print(is_ordered("hlabcdefgijkmnopqrstuvwxyz", 'z', 'w')) #false
# print(is_ordered("hlabcdefgijkmnopqrstuvwxyz", 'apple', 'app')) #false
# print(is_ordered("hlabcdefgijkmnopqrstuvwxyz", 'app', 'apple')) #false


def verify_order(words, order):
    alien_dict = {}

    for i in range(len(order)):
        alien_dict[order[i]] = i

    for i in range(len(words)-1):

        if not is_ordered(alien_dict, words[i], words[i+1]):
            return False
    return True

print(verify_order(["word","world","row"], "hlabcdefgijkmnopqrstuvwxyz")) #false
print(verify_order(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")) #true
print(verify_order(["",""], "hlabcdefgijkmnopqrstuvwxyz")) #true
print(verify_order([], "hlabcdefgijkmnopqrstuvwxyz")) #true
print(verify_order(['word'], "hlabcdefgijkmnopqrstuvwxyz")) #true





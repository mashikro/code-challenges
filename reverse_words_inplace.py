# Prompt: Write a function reverse_words() that takes a message as a list 
# of characters and reverses the order of the words in place. 

message = [ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ]
# Prints: 'steal pound cake'

def make_word(lst):

    words = []
    start_index = {}

    word_start_i = 0
    word_len = 0

    for i in range(len(lst)):
        if lst[i] != " ":
            word_start_i = i
            print(word_start_i)
            word_len += 1
        else:
            words.append(lst[word_start_i:word_len])

    return words

print(make_word(message))
def reverse_words(message):
    message = make_word(message)
    print('original message', message)

    pos1 = 0
    pos2 = -1
    i = 0

    while i <= len(message)//2: 
        message[pos1], message[pos2] = message[pos2], message[pos1]

        pos1+=1
        pos2-=1
        i +=1

    print(' '.join(message))
    return message

# print(reverse_words(message))


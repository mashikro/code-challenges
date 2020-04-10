# Prompt: Write a function reverse_words() that takes a message as a list 
# of characters and reverses the order of the words in place. 

message = [ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ]
# Prints: 'steal pound cake'


def reverse_words_in_place(lst):
    def swap(lst, pos1, pos2):
        while pos1 < pos2:
            lst[pos1], lst[pos2] = lst[pos2], lst[pos1]

            pos1+=1
            pos2-=1

    swap(lst, 0, len(lst)-1) #reverse entire lst
    
    
    # reversing each word
    beg = 0
    
    for i in range(len(lst)+1): 
        if (i == len(lst)) or (lst[i] == ' '):
            swap(lst, beg, i-1) #-1 because we're either at space or end
            # print('swap happened:', lst)
            beg = i+1 #+1 to skip the " "

    print(' '.join(lst))
            
input1 = ['l', 'o', 'v', 'e', ' ', 'y', 'o', 'u']
print('before', message)
reverse_words_in_place(message)
print('++++++++++')
print('AFTER',message)

# Runtime: O(n) time and O(1) space!
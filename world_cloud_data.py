# Prompt:  Write code that takes a long string and builds its word cloud 
# data in a dictionary ↴ , where the keys are words and the values are the number 
# of times the words occurred. Think about capitalized words.

string1 = "After beating the eggs, Dana read the next step:"

def split_words(s):
    letters = []
    punctuations = []
    
    for l in s:
        if l.isalpha() or l == " ":
            letters.append(l)
        else:
            punctuations.append(l)
   
    ret = ("".join(letters)).split(" ")

    ret.extend(punctuations)

    return ret

# print(split_words(string1))

def check_case(lst):

    ret = []

def prep_word_cloud_data(s):

    words = {}

    list_s = split_words(s)

    for word in list_s:
        word = word.lower()

        if word not in words:
            words[word] = 1
        else:
            words[word] +=1

    # for punc in list_punctuations:
    #     if punc not in words:
    #         words[punc] = 1
    #     else:
    #         words[punc] +=1


    return words

print(prep_word_cloud_data(string1))








# Prompt: Write method to replace all string with '%20'
# input: 'Mr John Smith   ', 13
# output: 'Mr%20John%20Smith'

def url_ify(s):

    new_s = s.rstrip() 

    result = ''

    for l in new_s:
        if l == " ":
            result += '%20'
        else: 
            result += l


    return result

# print(url_ify("Mr John Smith   "))

#runtime: rstrip() - O(n), O(n) --> O(n)


def url_ify2(s):

    return (s.rstrip()).replace(" ", "%20")

print(url_ify2("Mr John Smith   "))



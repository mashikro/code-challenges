# Let us consider this example (array written in general format): https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python

# ls = [0, 1, 3, 6, 10]

# Its following parts:

# ls = [0, 1, 3, 6, 10]
# ls = [1, 3, 6, 10]
# ls = [3, 6, 10]
# ls = [6, 10]
# ls = [10]
# ls = []
# The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

# The function parts_sums will take as parameter a list ls and return a list of 
# the sums of its parts as defined above.

def parts_sums(ls):

    sums = []

    for i in range(len(ls)):
        t = 0
        for j in range(len(ls)-i):
            t+=ls[j+i]
        sums.append(t)
    sums.append(0)

    return sums

#Runtime O(n^2)
# print(parts_sums([0, 1, 3, 6, 10]))

def parts_sums2(ls):
    sums = []

    for i in range(len(ls)):
        sums.append(sum(ls[i:]))
    sums.append(0)

    return sums

# Runtime O(n^2) bc sum() is a hidden loop
# print(parts_sums2([0, 1, 3, 6, 10]))

def parts_sums3(ls):
    result = [sum(ls)] #O(n)
    for item in ls:
        result.append(result[-1]-item)
    return result
#Runtime O(n)
 print(parts_sums3([0, 1, 3, 6, 10])) #[20, 20, 19, 16, 10, 0]
       

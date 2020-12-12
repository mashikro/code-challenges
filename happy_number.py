# https://leetcode.com/problems/happy-number/

def is_happy(n):
    num = str(n)
    mem=set()

    while int(num) != 1:
        s = 0
        for number in num:
            s+=int(number)**2

        num =str(s)
        print('num=', num)

        if num in mem:
            return False
        else:
            mem.add(num)
    return True
        

    # print(num)
    # if int(num) is 1:
    #     return True
    # return False

print(is_happy(19))
print(is_happy(2))

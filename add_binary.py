# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"

# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


# Different built in ways to do this:
# >>> int('11', 2) --> takes binary str and outputs decimal num 3
# >>> "{0:b}".format(37)  -> the str formatting can output a binary num
# '100101'
# 'b' Binary format. Outputs the number in base 2.

#One way to solve this using python built in func:
def add_binary(a,b):
    
    return '{0:b}'.format(int(a, 2) + int(b, 2))

# print(add_binary('11', '1')) #'100'


def add_binary_bit_by_bit(a,b):
    #make sure len of both a and b equal by adding leading 0s using .zfill()
    n = max(len(a), len(b))
    a, b = a.zfill(n), b.zfill(n)
    
    carry = 0
    answer = []
    for i in range(n - 1, -1, -1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1
            
        if carry % 2 == 1:
            answer.append('1')
        else:
            answer.append('0')
        
        carry //= 2
    
    if carry == 1:
        answer.append('1')
    answer.reverse()
    
    return ''.join(answer)


def add_binary_bit_mani(a,b):
    x, y = int(a, 2), int(b, 2) #turn a and b into decimal nums
    print('x:', x)
    print('y:', y)
    while y:
        answer = x ^ y #taking XOR of base2 of x and y
        print('answer:', answer)
        carry = (x & y) << 1
        print('carry', carry)
        x, y = answer, carry
    return bin(x)[2:]


print(add_binary_bit_mani('11', '1'))
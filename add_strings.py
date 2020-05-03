# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
# ord('0') -> 48
# chr(48) -> '0'
# .zfill() -> adds leading zeros to str 




def add_strings(num1, num2):

    if len(num2)<len(num1):
        num1, num2 = num2, num1
    num1 = num1.zfill(len(num2)) #zfill() is a method that fills a str with zero at the front '50'.zfill(4) -> '0050' only adds 0s once param is larger than len of text
    print(num1)
    print(num2)
    num1, num2 = num1[::-1], num2[::-1] #reverse the strings

    ans = ''
    carry_over = 0
    #traverse the str backwards
    for d1, d2 in zip(num1, num2): #zip them into a list of tuples
        d1, d2 = ord(d1)-ord('0'), ord(d2)-ord('0') #turn it into numbers the ascii way
        dsum = d1 + d2 + carry_over
        if dsum < 10:
            carry_over = 0
            ans += str(dsum)
        else:
            carry_over = 1
            ans += str(dsum%10) #mod of 10 leaves anything but 10 ex: 13%10 -> 3
    if carry_over: 
        ans += '1'

    # reverse            
    return ans[::-1]

print(add_strings('123', '1234')) # 1357
# print(add_strings('123', '1239')) #1362
# print(add_strings('0', '0')) #0
# print(add_strings('1', '9')) #10
# print(add_strings('9133', '0')) #9133



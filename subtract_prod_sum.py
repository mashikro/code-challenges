# Given an integer number n, return the difference between the product of its 
# digits and the sum of its digits.

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

def subtract_prod_sum(n):

    def digitize(n):
        s = str(n)
        lst = []

        for num in s:
            lst.append(int(num))

        return lst

    nums = digitize(n)

    prod = 1
    sum_ = 0

    for num in nums:
        prod *= num
        sum_ += num

    return prod-sum_

print(subtract_prod_sum(234)) #15
print(subtract_prod_sum(4421)) #21
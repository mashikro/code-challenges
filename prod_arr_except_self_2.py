def multiply(skip_index, nums):
    res = 1
    for i in range(len(nums)):
        if i != skip_index:
            res *= nums[i]

    return res

# print(multiply(0, [1,2,3,4])) #24
# print(multiply(1, [1,2,3,4])) #12


def find_prod(nums):
    ret = []

    for i in range(len(nums)):
        res = multiply(i, nums)
        ret.append(res)

    return ret

# print(find_prod([1,2,3,4])) #[24,12,8,6]
# this solution is O(n^2) time and it is too slow and times out with really large inputs


#########OPTIMIZED Solutions#########
# Note: Please solve it without division and in O(n).

def find_prod_faster(nums):
    length = len(nums)

    L, R, answer = [0]*length, [0]*length, [0]*length

    L[0] = 1
    for i in range(1, length):
        L[i] = L[i-1] * nums[i-1]
        print(L)
    
    print('----------')

    R[length-1] = 1
    for i in reversed(range(length-1)):
        R[i] = R[i+1] * nums[i+1]
        print(R)

    for i in range(length):
        answer[i] = L[i]*R[i]

    return answer





print(find_prod_faster([1,2,3,4]))
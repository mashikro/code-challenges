# Prompt: Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is equal to the 
# product of all the elements of nums except nums[i].

# Test Case:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# Input:  [1,2,3]
# Output: [24,12,8]

def find_prod_of_arr(nums):

    
    # The length of the input array 
    length = len(nums)
    
    # The left and right arrays as described in the algorithm
    L, R, answer = [0]*length, [0]*length, [0]*length
    
    # L[i] contains the product of all the elements to the left
    # Note: for the element at index '0', there are no elements to the left,
    # so the L[0] would be 1
    L[0] = 1
    for i in range(1, length):
        
        # L[i - 1] already contains the product of elements to the left of 'i - 1'
        # Simply multiplying it with nums[i - 1] would give the product of all 
        # elements to the left of index 'i'
        L[i] = nums[i - 1] * L[i - 1]
        print('l', L)
    
    # R[i] contains the product of all the elements to the right
    # Note: for the element at index 'length - 1', there are no elements to the right,
    # so the R[length - 1] would be 1
    R[length - 1] = 1
    for i in reversed(range(length - 1)):
        
        # R[i + 1] already contains the product of elements to the right of 'i + 1'
        # Simply multiplying it with nums[i + 1] would give the product of all 
        # elements to the right of index 'i'
        R[i] = nums[i + 1] * R[i + 1]
        print('r', R)
    
    # Constructing the answer array
    for i in range(length):
        # For the first element, R[i] would be product except self
        # For the last element of the array, product except self would be L[i]
        # Else, multiple product of all elements to the left and to the right
        print('L[i]', L[i])
        print('R[i]', R[i])
        answer[i] = L[i] * R[i]
        print('a', answer)

    return answer
print(find_prod_of_arr([1,2,3,4]))
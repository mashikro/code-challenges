# Given a 6x6 2D Array find the sum of all hourglass and return the max sum
# We define an hourglass in arr to be a subset of values with indices falling in this 
# pattern in qrr's graphical representation:
# a b c
#   d
# e f g
# Test Case: There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass'
# values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.
# For example, given the 2D array:

# -9 -9 -9  1 1 1 
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0

#  We calculate the following 16 hourglass values:

#  -63, -34, -9, 12, 
# -10, 0, 28, 23,     # return 28           
# -27, -11, -2, 10, 
# 9, 17, 25, 18

# input: 6x6 2d arr
# output is int - max sum
def find_max_sum(arr):
    sum_ = []
 
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            temp=0
            if (j+2 < 6) and (i+2 < 6):                
                temp+= (
                    arr[i][j] + 
                    arr[i][j+1] + 
                    arr[i][j+2] + 
                    arr[i+1][j+1] + 
                    arr[i+2][j] + 
                    arr[i+2][j+1] + 
                    arr[i+2][j+2]
                    )
                sum_.append(temp)
                print('sum_', sum_)         

    return max(sum_)

a = [[1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]]
print(find_max_sum(a)) #19

b = [[-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9,  1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]]
print(find_max_sum(b)) #28


#Runtime: O(n^2) time and O(m) space


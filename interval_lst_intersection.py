# Prompt:
# Given two lists of closed intervals (is an interval which includes all its limit points, and is denoted with square brackets.)
# each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  
# The intersection of two closed intervals is a set of real numbers that is either empty, or can be 
# represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

# Input: 
# A = [[0,2],[5,10],[13,23],[24,25]], 
# B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
    
def interval_intersection(A,B):

    overlapp = []
    i, j = 0,0
    while i<len(A) and j<len(B):
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])
  
        if lo <= hi:
            overlapp.append([lo, hi])

         # Remove the interval with the smallest endpoint
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1


    return overlapp

print(interval_intersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
# [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# [[1, 2], [1, 5], [8, 10], [8, 12], [15, 23], [15, 24], [25, 25]]
# [[1, 2], [0, 2], [1, 5], [8, 10], [5, 10], [8, 12], [15, 23], [13, 23], [15, 24], [25, 25]]

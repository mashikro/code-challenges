# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.


def merge(nums1, m, nums2, n):
    #merging items into nums1 thus made a copy of relevant elements in nums1

    i = 0
    j = 0
    k = 0 #index merge
    nums1_copy = nums1[:m]
    
    while k < m+n:
        if i >= m:
            nums1[k] = nums2[j]
            j+=1
        elif j >= n: 
            nums1[k] = nums1_copy[i]
            i+=1
        elif nums1_copy[i] < nums2[j]:
            nums1[k] = nums1_copy[i]
            i+=1
        else:
            nums1[k] = nums2[j]
            j+=1
           
        k+=1

        # print('i:', i)
        # print('j:', j)
        # print('k:', k)
        # print('nums1:', nums1)

    return nums1

# print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
# print(merge([-1,0,1,2,3,0,0,0], 5, [2,5,6], 3))


def merge2(nums1, m, nums2, n):

    i = m-1
    j = n-1
    k = (m+n)-1

    print('i:', i)
    print('j:', j)
    print('k:', k)
    print('-----------')

    while i >= 0 and j >= 0:
        print('i:', i)
        print('j:', j)
        print('k:', k)
        print('nums1:', nums1)

        if nums2[j] > nums1[i]:
            nums1[k] = nums2[j]
            j-=1
        else:
            nums1[k] = nums1[i]
            i-=1

        k -=1
    print('j', j)
    print(nums1[:j+1])
    print(nums2[:j+1])
    nums1[:j+1] = nums2[:j+1]

    return nums1


# print(merge2([1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge2([0], 0, [1], 1))





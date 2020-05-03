# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:

# Each element in the result must be unique.
# The result can be in any order.

def intersection(nums1, nums2):

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    inter=set()

    for i in range(len(nums1)):

        if nums1[i] in nums2:
            inter.add(nums1[i])


    return inter

print(intersection([1,2,2,1], [2,2]))
print(intersection([4,9,5], [9,4,9,8,4]))

#using the Built-in Set Intersection '&' operation is MUCH faster
def intersection_set(nums1, nums2):

    set1 = set(nums1)
    set2 = set(nums2)
    return list(set2 & set1)


print(intersection_set([1,2,2,1], [2,2]))
print(intersection_set([4,9,5], [9,4,9,8,4]))
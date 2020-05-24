# Find the kth largest element in an unsorted array. Note that it is the kth 
# largest element in the sorted order, not the kth distinct element.

# You may assume k is always valid, 1 ≤ k ≤ array's length.

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5

def find_kth_largest_elem(nums, k):

    nums.sort()

    return nums[-k]

print(find_kth_largest_elem([3,2,1,5,6,4], 2))

#Using a heap to solve this problem
    # here is an article about heaps
    #https://towardsdatascience.com/data-structure-heap-23d4c78a6962
    # documentation: https://docs.python.org/2/library/heapq.html

def find_kth_largest_elem_heap(nums, k):
    import heapq
    print(heapq.nlargest(k, nums)) # --> [6, 5]
    #nlargest is a heapq method -> Return a list with the n largest elements from the dataset defined by iterable.
    return heapq.nlargest(k, nums)[-1] #last item in list is what we want returned

print(find_kth_largest_elem_heap([3,2,1,5,6,4], 2))

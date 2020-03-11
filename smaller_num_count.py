# Given the array nums, for each nums[i] find out how many numbers in the array are 
# smaller than it. That is, for each nums[i] you have to count the number of valid j's 
# such that j != i and nums[j] < nums[i].

# Return the answer in an array.

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]

def smaller_num_count(nums):
   
    ret = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j]<nums[i]:
                count += 1
        ret.append(count)
    return ret

print(smaller_num_count([8,1,2,2,3])) #[4,0,1,1,3]
print(smaller_num_count([6,5,4,8])) # [2,1,0,3]
print(smaller_num_count([7,7,7,7])) #[0,0,0,0]

#Runtime for above : O(n^2) because we have two nested loops, not good. 

def smaller_num_count2(nums):

    counts = {}
    sorted_nums = sorted(nums) #nlogn


    for i in range(len(sorted_nums)): 
        if sorted_nums[i] not in counts:
            counts[sorted_nums[i]] = i # number : index  
    
    ret = []
    
    for n in nums: #using original list
        ret.append(counts[n]) #n is number and counts[n] is index
    

    return ret

print(smaller_num_count2([8,1,2,2,3])) #[4,0,1,1,3]
print(smaller_num_count2([6,5,4,8])) # [2,1,0,3]
print(smaller_num_count2([7,7,7,7])) #[0,0,0,0]

#Runtime: O(n log n) + O(n) + O(n) = O(n log n)



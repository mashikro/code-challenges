# Given an array nums of n integers, are there elements a, b, c in nums such 
# that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]



def three_sum(nums):
    nums = sorted(nums) # O(nlogn)
    print('sorted nums', nums)
    result = set()
    for i in range(len(nums)):
        looking_for = 0-nums[i] 
        print('looking_for', looking_for)
        k,j = i+1, len(nums)-1 #approach from either end of nums
        print('k', k)
        print('j', j)
        while k < j:
            sum_two = nums[k] + nums[j]
            print('sum two', sum_two)
            if sum_two < looking_for:
                k += 1
                print('k', k)
            elif sum_two > looking_for:
                j -= 1
                print('j', j)
            else:
                result.add((nums[i],nums[k],nums[j]))
                k += 1
                j -= 1
                print('k', k)
                print('j', j)
                print('result', result)
    return result


print(three_sum([-1, 0, 1, 2, -1, -4]))
# print(three_sum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))


#######vvvvvvvv Buggy vvvvvvvvv#########

def find_two_sum(nums, target):
    for i in range(len(nums)):
        looking_for = target - nums[i]
        # print('looking_for', looking_for)
        if looking_for in nums:
            return [looking_for, nums[i]]
    return []

# print(find_two_sum([-1, 0, 1, 2, -1, -4], 0))


def find_three_sum(nums):

    if len(nums) <3:
        return []
    if len(nums) == 3:
        if sum(nums) == 0:
            return [nums]
        else:
            return []

    ret = {}

    result = []

    all_possibilities = []
    for i in range(len(nums)):
        temp = [nums[i]]
        # print('temp', temp)
        looking_for = 0-nums[i]
        # print('looking_for', looking_for)

        if looking_for in ret:
            temp.extend(ret[looking_for])

        else:
            ret[looking_for] = find_two_sum((nums[:i]+ nums[i+1:]), looking_for)
            temp.extend(ret[looking_for])
            # print('temp.extend(res)', temp)
        
        # print('ret', ret)
        temp.sort()
        # print('temp', temp)
        all_possibilities.append(temp)
        if sum(temp) == 0 and len(temp) == 3:
            if temp not in result:
                result.append(temp)
            # print('result', result)
    print(all_possibilities)
    return result



# print(find_three_sum([-1, 0, 1, 2, -1, -4]))
# print(find_three_sum([0,0,0]))
# print(find_three_sum([0]))
# print(find_three_sum([0,1,1]))
# print(find_three_sum([3,-2,1,0]))

# print(find_three_sum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
# Expected [[-4,0,4], [-4,-2,6],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
# Mine [[-4,2,2],[-2,0,2],[-4,1,3],[-2,-2,4],[-4,-2,6]]




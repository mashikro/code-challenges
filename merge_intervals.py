# Given a collection of intervals, merge all overlapping intervals.

# Test Case:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.


def is_overlap(lst1, lst2): 
    lst1_r = range(lst1[0], lst1[1]+1)
    lst2_r = range(lst2[0], lst2[1]+1)

    if lst1[0] in lst2_r or lst1[1] in lst2_r:
        return True
    elif lst2[0] in lst1_r or lst2[1] in lst1_r:
        return True
    else:
        return False

# print(is_overlap([1,3],[2,6])) # True
# print(is_overlap([8,10],[15,18])) # False
# print(is_overlap([1,4], [0,0])) #False

def mini_merge(lst1, lst2):
  

    beg = min(min(lst1), min(lst2))
    end = max(max(lst1), max(lst2))
    
    return [beg, end]

# print(mini_merge([1,3],[2,6]))


def merge_intervals2(intervals): #input is list of lists
    if len(intervals) < 2:
        return intervals
    
    ret = []
    i = 0

    intervals.sort()

    while i < len(intervals):
   
        if i < len(intervals)-1:
            if is_overlap(intervals[i], intervals[i+1]):
                merged = (mini_merge(intervals[i], intervals[i+1]))
                
                if ret and is_overlap(ret[-1], merged):
                    temp = ret[-1]
                    ret[-1] = mini_merge(temp, merged)
                else: 
                    ret.append(merged)

                i+=2

            else:
                if not ret:
                    ret.append(intervals[i])
                elif is_overlap(ret[-1], intervals[i]) == False:
                    ret.append(intervals[i])
                else: 
                    temp = ret[-1]
                    ret[-1] = mini_merge(temp, intervals[i])
                i+=1

        if i == len(intervals)-1:
            if is_overlap(ret[-1], intervals[i]) == False:
                ret.append(intervals[i])
            else:
                temp = ret[-1]
                ret[-1] = mini_merge(temp, intervals[i])
            i+=1
    return ret


# print(merge_intervals2([[1,3],[2,6],[8,10],[15,18]]))
# print(merge_intervals2([[1,4],[4,5]]))
# print(merge_intervals2([[1,3]]))
# print(merge_intervals2([[1,4],[5,6]])) #no overlap
# print(merge_intervals2([[1,4],[0,1]])) # [[0,4]]
# print(merge_intervals2([[1,4],[0,0]])) # [[1, 4], [0, 0]]
# print(merge_intervals2([[1,4],[0,2],[3,5]])) # [[0,5]]
# print(merge_intervals2([[2,3],[4,5],[6,7],[8,9],[1,10]])) # [1,10]
# print(merge_intervals2([[2,3],[5,5],[2,2],[3,4],[3,4]])) # [[2,4],[5,5]]
# print(merge_intervals2([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]])) # [[1,3],[4,7]]


# always compares with the interval in merged lst unlike above which compares 
# 2 intervals in lst, merges them and then compares against interval in merged lst
def merge_intervals(intervals):
    intervals.sort()

    merged = []
    for interval in intervals:
        # if the list of merged intervals is empty or if the current
        # interval does not overlap with the previous, simply append it.
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
        # otherwise, there is overlap, so we merge the current and previous
        # intervals.
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged



print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
print(merge_intervals([[1,4],[4,5]]))
print(merge_intervals([[1,3]]))
print(merge_intervals([[1,4],[5,6]])) #no overlap
print(merge_intervals([[1,4],[0,1]])) # [[0,4]]
print(merge_intervals([[1,4],[0,0]])) # [[1, 4], [0, 0]]
print(merge_intervals([[1,4],[0,2],[3,5]])) # [[0,5]]
print(merge_intervals([[2,3],[4,5],[6,7],[8,9],[1,10]])) # [1,10]
print(merge_intervals([[2,3],[5,5],[2,2],[3,4],[3,4]])) # [[2,4],[5,5]]
print(merge_intervals([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]])) # [[1,3],[4,7]]



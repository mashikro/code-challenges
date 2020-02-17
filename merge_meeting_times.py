# Prompt: Your company built an in-house calendar tool called HiCal. 
# You want to add a feature to see the times in a day when everyone is available.

# input = [(1, 3), (2, 4)]
# ret =   [(1, 4)]

# a & b are tuples of (start,end)
# assume a & b are in sorted order.
# output is boolean (whether they overlap)
def is_overlapping(a, b):
    return (a[1] >= b[0])

# a & b are tuples of (start,end)
# assume that they overlap.
# returns a single merged range.
def merge_two_ranges(a, b):
    return (min(a[0], b[0]), max(a[1], b[1]))

# ranges is list of [start,end]
def merge_all_ranges(ranges):
    ret = [] # return value of merged ranges
    ranges = sorted(ranges) #O(nlgn)
    i = 0    # which of the input ranges we are considering
    while i<len(ranges): #O(n)
        if (len(ret)==0):
            ret.append(ranges[i])
        else:
            if (is_overlapping(ret[-1], ranges[i])):
                ret[-1] = merge_two_ranges(ret[-1], ranges[i])
            else:
                ret.append(ranges[i])
        i += 1
    return ret

#Runtime O(nlgn)

print(merge_all_ranges([(1, 3), (2, 4)])) #   [(1, 4)]
print(merge_all_ranges([(1, 5), (2, 3)])) # 1,5
print(merge_all_ranges( [(1, 2), (2, 3)])) #1,3
print(merge_all_ranges([(0,1), (3,5), (4,8), (10,12), (9,10)])) #  [(0, 1), (3, 8), (9, 12)]
print(merge_all_ranges([(1, 10), (2, 6), (3, 5), (7, 9)])) #(1, 10)




def merge_range(meeting_times):

    all_meeting_times = []
    meeting_times = sorted(meeting_times)

    for i in range(len(meeting_times)-1):
        start_time=None
        end_time=None
     
        if meeting_times[i][1] >= meeting_times[i+1][0]:
            start_time=meeting_times[i][0]
            if meeting_times[i][1] < meeting_times[i+1][1]:
                end_time=meeting_times[i+1][1]
            else:
                end_time=meeting_times[i][1]

            all_meeting_times.append((start_time, end_time))
            
        else:
            if all_meeting_times:
                last = all_meeting_times.pop()
                if last[1] >= meeting_times[i][1]:
                    all_meeting_times.append((last[0],last[1]))
            else:
                all_meeting_times.append((meeting_times[i][0],meeting_times[i][1]))

        

    return all_meeting_times




print(merge_range([(1, 3), (2, 4)])) #   [(1, 4)]
print(merge_range([(1, 5), (2, 3)])) # 1,5
print(merge_range( [(1, 2), (2, 3)])) #1,3
print(merge_range([(0,1), (3,5), (4,8), (10,12), (9,10)])) #  [(0, 1), (3, 8), (9, 12)]
print(merge_range([(1, 10), (2, 6), (3, 5), (7, 9)])) #(1, 10)























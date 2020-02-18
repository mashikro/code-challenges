# Prompt: Write a function to merge our lists of orders into one sorted list.
# input:
# my_list= [3, 4, 6, 10, 11, 15]
# alices_list = [1, 5, 8, 12, 14, 19]

# output:
# # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

def merge_sorted_lists(lst1, lst2):
    ret = []

    index_1 = 0
    index_2 = 0
    index_merge = 0

    while index_merge < (len(lst1)+len(lst2)):
        #check if you've exhausted lst1 and add from 2 instead
        if index_1 >= len(lst1):
            ret.append(lst2[index_2])
            index_2 +=1
        #check if you've exhausted lst2 and add from 1 instead
        elif index_2 >= len(lst2):
            ret.append(lst1[index_1])
            index_1 +=1
        elif lst1[index_1] < lst2[index_2]:
            ret.append(lst1[index_1])
            index_1+= 1
        else:
            ret.append(lst2[index_2])
            index_2 += 1

        index_merge +=1

    return ret # O(n) time


# print(merge_sorted_lists([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]))

# print(merge_sorted_lists([3, 4, 6], [1, 2, 5]))



########### more DRY way to write the above ############
def merge_sorted_lists2(lst1, lst2):
    
    ret = []

    index_1 = 0
    index_2 = 0
    index_merge = 0

    while index_merge < (len(lst1)+len(lst2)):
        #check if you've exhausted lst1 and add from 2 instead
        is_lst1_exhausted = (index_1 >= len(lst1))
        #check if you've exhausted lst2 and add from 1 instead
        is_lst2_exhausted = (index_2 >= len(lst2))
        if (not is_lst1_exhausted and (is_lst2_exhausted or lst1[index_1] < lst2[index_2])):
            ret.append(lst1[index_1])
            index_1+= 1
        else:
            ret.append(lst2[index_2])
            index_2 += 1

        index_merge +=1

    return ret # O(n) time


print(merge_sorted_lists2([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]))

print(merge_sorted_lists2([3, 4, 6], [1, 2, 5]))




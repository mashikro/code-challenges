# Prompt: Write a function that takes: a list of unsorted_scores the highest_possible_score
# in the game and returns a sorted list of scores in less than O(nlgn) time.

# Test Case:
# input:
# unsorted_scores = [37, 89, 41, 65, 91, 53]
# HIGHEST_POSSIBLE_SCORE = 100
# Returns [91, 89, 65, 53, 41, 37]

def sort_top_scores(unsorted_scores, highest):
    count = [0] * (highest+1)

    for num in unsorted_scores:
        count[num] += 1 

    # print('count', count)
    sorted_lst = []

    for i in range(len(count)-1, -1, -1):

        if count[i] != 0:
            sorted_lst.extend([i]*count[i])

    return sorted_lst

print(sort_top_scores([37, 89, 41, 65, 91, 1, 4, 4, 53,53], 100))




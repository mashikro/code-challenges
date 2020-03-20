#Medium level qs from Netflix
# Prompt:Find the biggest overlap/rectangle given a lst and return the max int


# Test Cases:
# Input: [5,2,3,1]
# Output: 2*3 = 6
# How?
# x x x x x
# x x
# x x x
# x


def find_max(lst):
    '''Find every possible combination of overlap and return the biggest one'''

    if len(lst) < 1:
        raise Exception('Empty List')

    if len(lst) <2:
        return lst[0]

    possibilites = set()

    for i in range(len(lst)):
        x = []
        for j in range(len(lst)):
            x.append(lst[j])

            prod = len(x) * min(x)

            possibilites.add(prod)

    # print(possibilites)
    return max(possibilites)

print(find_max([5,2,3,1])) #6
print(find_max([0])) #0
print(find_max([3])) #3
print(find_max([5,1,3,2])) #5
print(find_max([])) #exception

#Runtime: Space O(n) Time O(n^3)






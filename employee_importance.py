# Prompt:
# You are given a data structure of employee information, which includes the employee's
# nique id, his importance value and his direct subordinates' id.

# For example, employee 1 is the leader of employee 2, and employee 2 is the leader 
# of employee 3. They have importance value 15, 10 and 5, respectively. 
# Then employee 1 has a data structure like [1, 15, [2]], 
# and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. 
# Note that although employee 3 is also a subordinate of employee 1, 
# the relationship is not direct.

# Now given the employee information of a company, and an employee id, 
# you need to return the total importance value of this employee and all his 
# subordinates.


# Test Case:
# Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# Output: 11


def calculate_importance(employees, id):
    e_dict={}

    for e in employees:
        e_dict[e[0]]=((e[1],e[2])) #0 - id, 1 - importance, 2 - subordinates

    print(e_dict)

    total = 0

    queue = []

    queue.append((id,e_dict[id])) # Using a queue we will do a BFS
    
    while queue: #while there is stuff in the queue
        current_id, importance_subordinates_info =queue.pop(0) #importance_subordinates_info will be a tuple
            
        total += importance_subordinates_info[0] #add importance
        subordinates=importance_subordinates_info[1] #list of subordinates
        for subordinate in subordinates:
            queue.append((subordinate, e_dict[subordinate]))

    return total

print(calculate_importance([[1, 5, [2,3]], [2, 3, []], [3, 3, []]], 1))



















"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Input: (2 -> 4) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 5
Explanation: 42 + 465 = 507

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convert_linked_list_to_int(linked_list):
    val_int = 0
    current = linked_list
    i = 0
    while current:
        # 4 -> 6 -> 2
        # 4 + 10 * 6 + 100 * 2 -> 4 + 60 + 200 -> 264
        # (10**0 * 4) + (10**1 * 6) + (10**2 *2)
        val_int += (10 ** i) * current.val
        current = current.next
        i+=1
    
    return val_int

def create_linked_list_repr(val_int):
    # val_int = 264
    # -> 4 -> 6 -> 2
    val_int_str = str(val_int)
    head = ListNode(0)
    
    prev = ListNode(val_int_str[-1])
    head.next = prev

    for digit in val_int_str[::-1][1:]:
        new_node = ListNode(digit)
        prev.next = new_node
        prev = prev.next
    return head.next
            


def add_numbers(ll1, ll2):
    # convert each linked list into its integer repr
    val1 = convert_linked_list_to_int(ll1)
    val2 = convert_linked_list_to_int(ll2)
    
    #add them 
    sum_val = val1 + val2

    #use a helper func to convert sum into a linked list repr
    return create_linked_list_repr(sum_val)

 

###### A diff approach #######
def add_nums(l1, l2):
    dummy_head = ListNode(0)
    curr = dummy_head
    carry = 0
    p = l1
    q = l2

    while p or q:
        if p:
            x = p.val
        else:
            x = 0

        if q:
            y = q.val
        else:
            y = 0

        sum_ = x+y+carry

        carry = sum_//10

        curr.next = ListNode(sum_%10)

        curr = curr.next
        if p:
            p = p.next
        if q:
            q = q.next

    if carry>0:
        curr.next=ListNode(carry)

    return dummy_head.next
        
two=ListNode(2)
four=ListNode(4)
three=ListNode(3)

two.next=four
four.next=three

five=ListNode(5)
six=ListNode(6)
four=ListNode(4)

five.next=six
six.next=four

# add_numbers(two, five)

# 2 -> 4 -> 3 + 5 -> 6 -> 4
# (6 -> 4 -> 1) + (4 -> 6 -> 2)
#   146 + 264 = 410
    
# six_=ListNode(6)
# four=ListNode(4)
# one=ListNode(1)

# six_.next=four
# four.next=one

# four=ListNode(4)
# six=ListNode(6)
# two=ListNode(2)

# four.next=six
# six.next=two

# add_numbers(six_, four)


# 6->4->8 + 4->6->2->1

six__=ListNode(6)
four=ListNode(4)
eight=ListNode(8)

six__.next=four
four.next=eight

four_=ListNode(4)
six=ListNode(6)
two=ListNode(2)
one=ListNode(1)

four_.next=six
six.next=two
two.next=one

add_numbers(six__, four_)
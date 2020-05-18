# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

def add_two_nums(l1, l2): 
    #initiating the new linkedlist. dummy_head.next will actually be what we return (first node in linked list)
    dummy_head = ListNode(0)
    curr = dummy_head
    current_1 = l1
    current_2 = l2
  
    carry = 0
    while current_1 or current_2: #We are looping through and adding val of nodes as we go
        if current_1 != None: #note checking current_1.val will return NoneType error if current is None
            val_1 = current_1.val
        else:
            val_1 = 0

        if current_2 != None:
            val_2 = current_2.val
        else:
            val_2 = 0

        sum_ = val_1+val_2+carry 

       
        carry = sum_//10 # sum = 11 -> carry will be 1
        #we are creating the new summed nodes as we go (greedy approach)
        curr.next = ListNode(sum_%10) #sum = 11 -> sum%10 = 1 and we would have carry =1
        
        curr = curr.next # if curr==0 and curr.next == 1, we now need to update curr from 0 to 1 so the next, .next is correct

        #moving the loop along
        if current_1 != None:
            current_1 = current_1.next
        if current_2 != None:
            current_2 = current_2.next

    #dont forget about the carry 
    if carry == 1:
        curr.next = ListNode(carry)

    return dummy_head.next #return first item in node


###testing code

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


two = ListNode(2)
four = ListNode(4)
three = ListNode(3)

two.next = four
four.next = three

five = ListNode(5)
six = ListNode(6)
four = ListNode(4)

five.next = six
six.next = four

####### different example
one = ListNode(1)
eight = ListNode(8)
one.next = eight
#calling func
zero = ListNode(0)

print(add_two_nums(two, five))
print('------------------------ df ex ---------------')
print(add_two_nums(one,zero))

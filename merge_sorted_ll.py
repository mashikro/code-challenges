# Merge two sorted linked lists and return it as a new sorted list. The new list 
# should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(l1, l2):
    # we set up a false "prehead" node that allows us to easily return the head of the merged list later.
    prehead=ListNode(-1)
    # maintain a prev pointer, which points to the current node for which we are considering adjusting its next pointer. 
    prev=prehead

    # Then, we do the following until at least one of l1 and l2 points to null: if 
    # the value at l1 is less than or equal to the value at l2, then we connect l1 to 
    # the previous node and increment l1. Otherwise, we do the same, but for l2. 
    # Then, regardless of which list we connected, we increment prev to keep it
    # one step behind one of our list heads.

    while l1 and l2:
        print('prev.val', prev.val)
        print('l1.val:', l1.val)
        print('l2.val:', l2.val)

        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        print('>>>ppp', prev.val)
        prev = prev.next
        print('prev.val', prev.val)
        print('---')

    # After the loop terminates, at most one of l1 and l2 is non-null. 
    # Therefore (because the input lists were in sorted order), if either list is non-null, 
    # it contains only elements greater than all of the previously-merged elements.
    # This means that we can simply connect the non-null list to the merged list and return it.
    prev.next = l1 if l1 is not None else l2 # can also be written as prev.next = l1 or l2

    return prehead.next

#### Testing ###

one=ListNode(1)
two=ListNode(2)
four=ListNode(4)
one.next =two
two.next=four

one_=ListNode(1)
three=ListNode(3)
four_=ListNode(4)
one_.next=three
three.next=four_

merge(one, one_)


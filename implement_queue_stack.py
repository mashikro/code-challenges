# Prompt:
# Implement a queue with 2 stacks. Your queue should have an enqueue and a dequeue method 
# and it should be "first in first out" (FIFO). Optimize for the time cost of
# m calls on your queue. These can be any mix of enqueue and dequeue calls.
# Assume you already have a stack implementation and it gives O(1) time push and pop.


class QueueTwoStacks(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

# Runtime Analysis for dequeue():
# So let's look at the worst case for a single item, which is the case where it is 
# enqueued and then later dequeued. In this case, the item enters in_stack (costing 1 push), 
# then later moves to out_stack (costing 1 pop and 1 push), then later comes off out_stack to 
# get returned (costing 1 pop).

# Each of these 4 pushes and pops is O(1) time. So our total cost per item is O(1). Our m enqueue and 
# dequeue operations put m or fewer items into the system, giving a total runtime of 
# O(m).
    def dequeue(self):
      
        if len(self.out_stack) == 0:
            while self.in_stack:
                x = self.in_stack.pop()
                self.out_stack.append(x)

            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empty queue!")

        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            return None
        return self.out_stack[-1]

    def __repr__(self):
        return '<IN:{}> | <OUT: {}>'.format(self.in_stack, self.out_stack)



#Testing
q = QueueTwoStacks()

print('empty Queue', q)

print('---Enquing----')

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print('queue w 3 items', q)

print('---Dequing----')

q.dequeue() #remove a

print('removed -a- from queue', q)

print('---Enquing----')

q.enqueue('d')

print('added -d- to queue', q)













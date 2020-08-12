# Prompt: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# test case 1:
# input: [2,1,5,3,4]
# output: 3

# test case 2:
# input: [2,3,1,3,4]
# output: 'Too chaotic'
    
# print(is_skipper(3,5))
# print(is_skipper(5, 3))


# pseudocode
# skip_count=0
#off_by_1 = set() #add in
 #loop through list
    #check if val == index+1
    #if not check diff > 2
        #return too chaotic

    # diff = val - (index+1)
        # if diff ==2:
        #     off_by_1.add(index+1)
            # off_by_1.add(index+2)
        # skip_count+=diff


    # val < (index+1)
        # continue


# [2,1,5,4,3]

def min_bribes(lst):
    skip_count = 0
    off_by_1 = set()

    for i in range(len(lst)):
        val = lst[i]
        pos = (i+1)
        print("val:", val)
        print("pos 1:", pos)
        
        if val < pos:
            continue 

        if pos in off_by_1:
            pos += 1
            print("pos 2:::::", pos)

      

        diff = abs(val - pos)

        if diff > 2:
            print("Too chaotic")
            return 

        if diff == 2:
            skip_count+=diff
            off_by_1.add(pos+1)
            off_by_1.add(pos+2)

        else:
            skip_count+=diff

        print("skip_count:", skip_count)
        print("off_by_1:", off_by_1)
    print(skip_count)

# min_bribes([2,5,1,3,4]) #too chaotic - passed
# min_bribes([2,1,5,3,4]) #3
# min_bribes([2,1,5,4,3]) #4
# min_bribes([5 ,1 ,2, 3, 7, 8, 6, 4]) #too chaotic - passed
# min_bribes([1, 2, 5, 3, 7, 8, 6, 4]) #7



def min_bribes2(q):
    moves = 0 
    q = [P-1 for P in q]
    print("q", q)
    
    for i,P in enumerate(q):
        # i is the current position of P, while P is the
        # original position of P.

        if P - i > 2:
            print("Too chaotic")
            return
        print(">>>>>>> i:", i)
        print("max(P-1,0)", max(P-1,0))
        

        for j in range(max(P-1,0),i):
            print('P:', P)
            print("q[j]", q[j])
            if q[j] > P:
                moves += 1
                print("moves:", moves)

    print(moves)


min_bribes2([2,1,5,3,4]) #3
# min_bribes([2,1,5,4,3]) #4


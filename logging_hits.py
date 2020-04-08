import time

# How many visits did my page get in the last 5 minutes

hits = []
FIVE_MINS_SECS = (5*60)

def log_hit():
    '''Whenever a user visits the page the time stamp is appended to hits'''
    global hits
    hits.append(time.time())

def clean_up_hits(start):
    '''Keeps hits updated with the data from the past 5 mins since get_hits is called'''
    global hits 
    hits = hits[start:]


def get_hits(cut_off_window=FIVE_MINS_SECS):
    '''Returns how many users have visited the page since cut_off_window'''
    global hits
    now = time.time() #its in seconds floating point
    cutoff_time = now - cut_off_window 

    ret = 0 
    start = []

    for i  in range(len(hits)):
        if hits[i] > cutoff_time:
            start.append(i)
            # print('start', start)
            ret+=1

    clean_up_hits(start[0])

    return ret

#Testing code

# log_hit()
# log_hit()
# # log_hit()
# time.sleep(1)
# print('*****')
# log_hit()
# log_hit()
# log_hit()

# print(hits)
# wait 6 minutes before calling the next line...
# print(get_hits(1))

# print(time.time())

hits = [1, 2, 3, 4, time.time(), time.time()]
print('HITS', hits)
print(get_hits(1))

print('hits', hits)
# Prompt: https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
import collections 
def check_magazine(magazine, note): #both inputs are an arr of strs
    if len(note) > len(magazine):
        print('No')
        return

    mag_count = collections.Counter(magazine)
    print('mag_count', mag_count)
    note_count = collections.Counter(note)
    print('note_count', note_count)

    for w in note_count:
        if note_count[w] > mag_count[w]:
            print('No')
            return    
    
    print('Yes')


check_magazine(['give', 'me', 'one', 'grand', 'today', 'night'], ['give', 'one', 'grand', 'today'])

# Prompt:  So you're building a feature for choosing two movies whose 
# total runtimes will equal the exact flight length.

# Write a function that takes an integer flight_length (in minutes) 
# and a list of integers movie_lengths (in minutes) and returns a boolean 
# indicating whether there are two numbers in movie_lengths whose sum equals 
# flight_length.

# Test Case:
# input: 140, [30, 40, 60, 60, 80, 200]
# output: True # bc two movies do add up to lenght of movie

def find_two_movies(flight_length, movie_lengths):

    set_movies = set(movie_lengths)

    for movie_length in movie_lengths:
        target = flight_length-movie_length
        if target in set_movies:
            return True
    return False


print(find_two_movies(140, [30, 40, 60, 60, 80, 200]))
print(find_two_movies(104, [30, 40, 60, 60, 80, 200]))

def find_two_movies2(flight_length, movie_lengths):

    set_movies_seen = set()

    for movie_length in movie_lengths:
        target = flight_length-movie_length
        if target in set_movies_seen:
            return True
        else:
            set_movies_seen.add(movie_length)
    return False

print(find_two_movies2(140, [30, 40, 60, 60, 80, 200]))
print(find_two_movies2(104, [30, 40, 60, 60, 80, 200]))



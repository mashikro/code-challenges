# Prompt: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search


def find_flavors(cost, money):

    flavor_id ={}


    for i in range(len(cost)):
        change = money - cost[i]

        if change in flavor_id:
            print(flavor_id[change]+1, i+1)

        flavor_id[cost[i]] = i

print(find_flavors([2,1,3,5,6],5))
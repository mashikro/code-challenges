# Prompt: https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


def sockMerchant(n, ar):
    d = {}
    for sock in ar:
        if sock not in d:
            d[sock] = 1
        else:
            d[sock] += 1
    print(d)

    count = 0
    for v in d.values():
        count+= v//2

    return count
print(sockMerchant(7, [1,2,1,2,1,3,2]))
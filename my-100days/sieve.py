import itertools

def sieve():
    # begin with all natural numbers above 1
    picker = itertools.count(2)
    while True:
        # take the next available number
        v = next(picker)
        yield v
        # filter from the generator its multiples
        picker = filter(lambda x, prime = v: x % prime != 0, picker)

import heapq
# In the proper sieve we will cross multiples as we go,
# For each prime we found we'll keep its largest multiple generated
# that wasn't reached so far in our search.
#
# When our iteration reaches a multiple, it gets popped and the next
# multiple is inserted in the heap.
def proper_sieve():
    yield 2
    crt_number = 3
    multiples = [(4,2)]

    while True:
        next_multiple = multiples[0]
        # if the next smalles multiple is larger than the number we're currently looking at
        # then all the numbers between the two are primes
        # we'll report them as such and add their first multiples to the queue
        if next_multiple[0] > crt_number:
            for n in range(crt_number, next_multiple[0]):
                yield n
                heapq.heappush(multiples, (n * n, n))
            crt_number = next_multiple[0]
        else:
            # otherwise, the current number is not a prime, and we'll pop it
            # from the queue, and add the next multiple to the queue
            while next_multiple[0] == crt_number:
                heapq.heappop(multiples)
                heapq.heappush(multiples, (next_multiple[0] + next_multiple[1], next_multiple[1]))
                next_multiple = multiples[0]
            crt_number += 1

if __name__ == '__main__':
    s = proper_sieve()
    for i in range(0,10):
        print(next(s))

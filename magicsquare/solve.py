from math import factorial
from itertools import permutations
from itertools import islice

dim = 4

skip = factorial(pow(dim,2)) // factorial(dim)

target = [[42,14,46,34],[38,15,52,31]]

proposal_1 = set(range(1,17))

def consume(iterator, n):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        print("we should not get here")
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        print("trying to jump %d steps" % (n))
        next(islice(iterator, n, n), None)
        print("jumped %d steps" % (n))

def try_proposal(prop):
    for y in range(0,dim):
        check = sum(prop[y*dim:(y+1)*dim])
        if check != target[1][y]:
            print("prop=%s ; y = %d ; target = %d ; check = %d" % (prop, y, target[1][y], check))
            print("returning")
            return False, skip

    for x in range(0,dim):
        check = sum( [item[1] for item in enumerate(prop) if (item[0]-x) % dim == 0] )
        if check != target[0][x]:
            print("prop=%s ; x = %d ; target = %d ; check = %d" % (prop, x, target[0][x], check))
            return False, 1
    return True, None

count = 0

propositions = permutations(range(1,17))

while True:
    prop = next(propositions)
    count = count+1

    if count % 1 == 0:
        print("prop %d: %s" % (count, prop))

    result, step = try_proposal(prop)

    if result:
        print(prop)
        break

    print("consuming")
    consume(propositions, step-1)
    print("consumed")

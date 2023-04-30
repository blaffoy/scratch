from math import factorial
from itertools import permutations
from itertools import islice


target = [[42,14,46,34],[38,15,52,31]]
dim = len(target[0])

# skip = factorial(pow(dim,2)) // factorial(dim)
skip = 1


def sum_to_target(target, max_element, set_size):
    """
    Returns a list of lists of integers that sum to the given target value.
    """
    result = []
    def backtrack(start, path, total):

        if total == target:
            result.append(path[:])
            return

        if total > target:
            return

        if len(path) >= set_size:
            return

        for i in range(start, target+1):
            path.append(i)
            backtrack(i, path, total+i)
            path.pop()

    backtrack(1, [], 0)
    return result



def consume(iterator, n):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        prin_("we should not get here")
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

def try_proposal(prop):
    for y in range(0,dim):
        check = sum(prop[y*dim:(y+1)*dim])
        if check != target[1][y]:
            print("prop=%s ; y = %d ; target = %d ; check = %d" % (prop, y, target[1][y], check))
            return False, skip

    for x in range(0,dim):
        check = sum( [item[1] for item in enumerate(prop) if (item[0]-x) % dim == 0] )
        if check != target[0][x]:
            print("prop=%s ; x = %d ; target = %d ; check = %d" % (prop, x, target[0][x], check))
            return False, 1
    return True, None

def generate_proposals():
    t = target[1][0]


    return permutations(range(1,17))


if __name__ == '__main__':
    count = 0

    propositions = generate_proposals()

    while True:
        prop = next(propositions)
        count = count+1

        if count % 100000 == 0:
            print("prop %d: %s" % (count, prop))

        result, step = try_proposal(prop)

        if result:
            print(prop)
            break

        consume(propositions, step-1)

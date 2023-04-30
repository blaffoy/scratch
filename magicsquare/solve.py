from math import factorial
from itertools import permutations
from itertools import islice


target = [[42,14,46,34],[38,15,52,31]]
dim = len(target[0])

skip = 1

def sum_to_target(target, max_element, set_size):
    """
    Returns a list of lists of integers that sum to the given target value.
    """
    result = []
    def backtrack(_target, path, total, length, start):

        if total == target and length == set_size:
            result.append(path[:])
            return

        if total > target or length >= set_size:
            return

        for i in range(start, max_element+1):
            path.append(i)
            backtrack(_target-i, path, total+i, length+1, i+1)
            path.pop()

    backtrack(target, [], 0, 0, 1)
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

def compose_lists(list_of_lists):
    def backtrace(path, items, tail):
        result = []
        if not items:
            print(path)
            return path
        if not tail:
            for item in items:
                result.append(path.append(item))
            print(result)
            return result
        for item in items:
            stub = path + [item]
            backtrace(stub, tail[0], tail[1:])

    backtrace([], list_of_lists[0], list_of_lists[1:])


def generate_proposals():
    sums = []
    for y in range(0,dim):
        t = target[1][y]
        sums.append(sum_to_target(t, pow(dim,2), dim))


    return solns


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

        consume(propositions, step)

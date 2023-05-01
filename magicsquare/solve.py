#!python

from itertools import permutations

target = [[42,14,46,34],[38,15,52,31]]
dim = len(target[0])

flat_map = lambda f, xs: [y for ys in xs for y in f(ys)]

def reorder(list_of_lists):
    result = []

    def backtrace(path, items, tail):
        if not items or not tail:
            for perm in permutations(items):
                stub = path + list(perm)
                result.append(stub)
            return
        for perm in permutations(items):
            stub = path + list(perm)
            backtrace(stub, tail[0], tail[1:])


    backtrace([], list_of_lists[0], list_of_lists[1:])
    return result


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

def try_proposal(prop):
    for y in range(0,dim):
        check = sum(prop[y*dim:(y+1)*dim])
        if check != target[1][y]:
            print("prop=%s ; y = %d ; target = %d ; check = %d" % (prop, y, target[1][y], check))
            return False

    for x in range(0,dim):
        check = sum( [item[1] for item in enumerate(prop) if (item[0]-x) % dim == 0] )
        if check != target[0][x]:
            print("prop=%s ; x = %d ; target = %d ; check = %d" % (prop, x, target[0][x], check))
            return False
    return True

def compose_lists(list_of_lists):
    result = []
    def backtrace(path, items, tail):
        if not items:
            return path
        if not tail:
            for item in items:
                result.append(path + [item])
            return result
        for item in items:
            stub = path + [item]
            backtrace(stub, tail[0], tail[1:])

    backtrace([], list_of_lists[0], list_of_lists[1:])

    return result


def generate_proposals():
    # create a list of quartets that generate the correct sums along the x axis
    sums = []
    for y in range(0,dim):
        t = target[1][y]
        sums.append(sum_to_target(t, pow(dim,2), dim))

    # compose the sums into collections of quartets of quartets
    unfiltered = compose_lists(sums)

    # filter out any quartets that have duplicates
    deduped = [item for item in unfiltered if len(set(flat_map(lambda x:x, item))) == len(flat_map(lambda x:x, item))]

    # generate combinations that allow the inner quartets to be re-arranged
    proposals = flat_map(reorder, deduped)

    return proposals
    #return [flat_map(lambda args:args, item) for item in proposals]


if __name__ == '__main__':
    proposals = generate_proposals()

    for prop in proposals:
        result = try_proposal(prop)

        if result:
            print("SOLUTION: " + prop)
            break

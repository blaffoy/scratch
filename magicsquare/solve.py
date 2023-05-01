#!python

from itertools import permutations

target = [[42,14,46,34],[38,15,52,31]]
dim = len(target[0])

flat_map = lambda f, xs: [y for ys in xs for y in f(ys)]

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

    return flat_map(lambda x: list(permutations(x)), result)

def try_proposal(prop):
    for y in range(0,dim):
        check = sum(prop[y*dim:(y+1)*dim])
        if check != target[1][y]:
            print("prop=%s ; y = %d ; target = %d ; check = %d" % (prop, y, target[1][y], check))
            return False

    for x in range(0,dim):
        check = sum( [item[1] for item in enumerate(prop) if (item[0]-x) % dim == 0] )
        if check != target[0][x]:
            # print("prop=%s ; x = %d ; target = %d ; check = %d" % (prop, x, target[0][x], check))
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

    return [flat_map(lambda args:args, item) for item in result]


def generate_proposals():
    sums = []
    for y in range(0,dim):
        t = target[1][y]
        sums.append(sum_to_target(t, pow(dim,2), dim))

    unfiltered = compose_lists(sums)
    proposals = [item for item in unfiltered if len(set(item)) == len(item)]

    return proposals


if __name__ == '__main__':
    proposals = generate_proposals()

    for prop in proposals:
        result = try_proposal(prop)

        if result:
            print("SOLUTION: " + prop)
            break

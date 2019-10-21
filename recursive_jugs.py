from collections import defaultdict

tried = defaultdict(lambda: False)
steps = []

jugsize1 = 4
jugsize2 = 4
goal = 2


def solve_jugs(contents1, contents2):
    if (contents1 is goal) or (contents2 is goal):
        # Found solution
        steps.append((contents1, contents2))
        print(steps)
        return True

    if tried[contents1, contents2] is False:
        # found new step
        steps.append((contents1, contents2))
        tried[contents1, contents2] = True
        # Try all operations
        return fill_jug1(contents2) or fill_jug2(contents1) or empty_jug1(contents2) or \
               empty_jug2(contents1) or transfer_jug1(contents1, contents2) or transfer_jug2(contents2, contents1)
    else:
        if len(steps) is 0:
            print("No solution.")
        return False


def fill_jug1(contents2):
    return solve_jugs(jugsize1, contents2)


def fill_jug2(contents1):
    return solve_jugs(contents1, jugsize2)


def empty_jug1(contents2):
    return solve_jugs(0, contents2)


def empty_jug2(contents1):
    return solve_jugs(contents1, 0)


def transfer_jug1(contents1, contents2):
    # transfer contents of jug one to jug two
    transferred = min(contents1, jugsize2 - contents2)
    remainder = contents1 - transferred
    return solve_jugs(remainder, transferred + contents2)


def transfer_jug2(contents1, contents2):
    # transfer contents of jug two to jug one
    transferred = min(contents2, jugsize1 - contents1)
    remainder = contents2 - transferred
    return solve_jugs(transferred + contents1, remainder)


solve_jugs(0, 0)

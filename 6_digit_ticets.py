First
20
tamacjp[Follow]


def divide(data):
    # as integer (allow over 10)
    yield int(data)

    # divide 123456: 1 23456, 12 3456, 123 456, ...
    for pos in range(1, len(data)):
        for left in divide(data[:pos]):
            for right in divide(data[pos:]):
                # calculate + - * /
                yield left + right
                yield left - right
                yield left * right
                if right:
                    yield left / right


def checkio(data):
    # enumerate all pattern
    for x in divide(data):
        if x == 100:
            return False
    return True


Clear
solution
for Mathematically Lucky Tickets
BackShow
description
Recursive
Generator
44
flpo[Follow]
import itertools
from operator import add, mul, sub, truediv

operations = add, mul, sub, truediv


def checkio(number):
    def results(n):
        yield int(n)
        for i in range(1, len(n)):
            for x, y in itertools.product(results(n[:i]), results(n[i:])):
                yield from (op(x, y) for op in operations) if y else (x,)

    return 100 not in results(number)


def possible_values(substring: str) -> set:
    """All values obtainable from substring."""
    from operator import add, sub, mul, truediv as div
    entire_number = int(substring)
    results = {entire_number}
    for split_position in range(1, len(substring)):
        # split substring in all possible ways
        left_part = substring[:split_position]
        right_part = substring[split_position:]
        for left_operand in possible_values(left_part):
            for operation in add, sub, mul, div:
                for right_operand in possible_values(right_part):
                    try:
                        current_result = operation(left_operand, right_operand)
                    except ZeroDivisionError:
                        pass
                    else:
                        results.add(current_result)
    return results


from itertools import product


def possible_results(data):
    yield int(data)
    for i in range(1, len(data)):
        for (x, y) in product(
                possible_results(data[:i]), possible_results(data[i:])
        ):
            yield from (x + y, x - y, x * y)
            if y:
                yield x / y


def checkio(data):
    return all(result != 100 for result in possible_results(data))


def combine(x, y):
    return [x + y, x - y, x * y] + ([x / y] if y != 0 else [])


def checkio(data):
    N = len(data)
    gen = {}
    for l in range(1, N + 1):
        for i in range(0, N + 1 - l):
            gen[i, l] = set([int(data[i:i + l])])
            for k in range(1, l):
                gen[i, l] |= set(g for x in gen[i, k] for y in gen[i + k, l - k]
                                 for g in combine(x, y))
    return 100 not in gen[0, N]
def classic_fibonacci(limit):
    """Normal way to create fibonacci"""
    nums = []
    current, nxt = 0, 1

    while True:
        current, nxt = nxt, nxt + current
        if current > limit:
            break
        nums.append(current)

    return nums


def generator_fibonacci(limit):
    current, nxt = 0, 1

    while True:
        current, nxt = nxt, current + nxt
        if current > limit:
            break
        yield current


def even_fib(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n


print "Classic  :", classic_fibonacci(10000)

print "Generator:",
for item in generator_fibonacci(10000):
    print item,

print "\nComposed :",
for item in even_fib(generator_fibonacci(10000)):
    print item,

from multiprocessing import Queue, Process
import re


def square(num, q):
    sq = num ** 2
    q.put(f'Square of {num} is {sq}')


def cube(num, q):
    cb = num ** 3
    q.put(f'Cube of {num} is {cb}')


def factorial(num, q):
    fact = 1
    for multiplier in range(1, num + 1):
        fact *= multiplier
    q.put(f'Factorial of {num} is {fact}')


def print_result(q, fq):
    while not q.empty():
        result = q.get()
        print(result)
        fq.put(result)


def print_factorials(q):
    facts = []
    while not fq.empty():
        item = q.get()
        if 'factorial' in item.lower():
            facts.append(re.findall('\d+$', item)[0])

    print(f'Factorials: {facts}')


if __name__ == '__main__':
    mq = Queue()
    fq = Queue()

    processes = (
        Process(target=square, args=(9, mq)),
        Process(target=factorial, args=(4, mq)),
        Process(target=cube, args=(9, mq)),
        Process(target=factorial, args=(5, mq)),
        Process(target=factorial, args=(6, mq)),
        Process(target=factorial, args=(10, mq)),
        Process(target=print_result, args=(mq, fq)),
        Process(target=print_factorials, args=(fq,)),
    )

    for process in processes:
        process.start()
        process.join()

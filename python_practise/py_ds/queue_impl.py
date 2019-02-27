"""
    Queue implementation using indexing
"""
from collections import deque


class Queue:
    def __init__(self):
        self._list = list()
        self._f_elem = 0
        self._l_elem = 0

    @property
    def size(self):
        return self._l_elem - self._f_elem

    def add(self, e):
        self._list.append(e)
        self._l_elem += 1

    def __str__(self):
        return str(self._list[self._f_elem:self._l_elem])

    def pop(self):
        self._l_elem -= 1


class List:
    def __init__(self):
        self._list = list()

    @property
    def size(self):
        return len(self._list)

    def add(self, e):
        self._list.append(e)

    def __str__(self):
        return str(self._list)

    def pop(self):
        self._list.pop(-1)


if __name__ == '__main__':
    from datetime import datetime
    iter = 100000000

    li = list()
    start = datetime.now()
    for i in range(iter):
        li.append(i)
    print('List Add took: {}'.format((datetime.now() - start)))

    start = datetime.now()
    for i in range(iter):
        li.pop()
    print('List Pop took: {}'.format((datetime.now() - start)))

    # q = Queue()
    # start = datetime.now()
    # for i in range(iter):
    #     q.add(i)
    # print('Size: {}'.format(q.size))
    #
    # for i in range(iter):
    #     q.pop()
    # print('Queue took: {}'.format((datetime.now() - start)))

    dq = deque()
    start = datetime.now()
    for i in range(iter):
        dq.append(i)
    print('Deque add took: {}'.format((datetime.now() - start)))

    start = datetime.now()
    for i in range(iter):
        dq.popleft()
    print('Deque Pop took: {}'.format((datetime.now() - start)))

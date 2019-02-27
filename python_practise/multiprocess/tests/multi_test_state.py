from multiprocess import Value, Array, Process


def f(num, arr):
    num.value = 3.14

    for i in range(len(arr)):
        arr[i] = -arr[i]

if __name__ == '__main__':
    n = Value('d', 0.0)
    a = Array('i', range(10))

    p = Process(target=f, args=(n, a))
    p.start()
    p.join()

    print n.value
    print a[:]
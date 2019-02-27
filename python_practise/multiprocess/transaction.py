from multiprocessing import Process, Lock, Value
from time import sleep


class Account(object):
    """Class that creates an account object for performing transactions"""
    def __init__(self, balance, lock=None):
        self.lock = lock
        self.balance = balance

    def deposit(self):
        sleep(0.01)
        for i in range(100):
            self.lock.acquire()
            print("Depositing 1 rupee...")
            self.balance.value += 1
            self.lock.release()

    def withdraw(self):
        sleep(0.01)
        for i in range(100):
            self.lock.acquire()
            print("Withdrawing 1 rupee...")
            self.balance.value -= 1
            self.lock.release()

if __name__ == '__main__':
    balance = Value('i', 100)
    lock = Lock()

    account = Account(balance=balance, lock=lock)

    d = Process(target=account.deposit)
    w = Process(target=account.withdraw)
    rd = Process(target=account.deposit)

    d.start()
    w.start()
    rd.start()

    d.join()
    w.join()
    rd.join()

    print balance.value

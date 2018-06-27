import multiprocessing
import time


def deposit(balance, lock):
    for n in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value += 1
        lock.release()


def withdraw(balance, lock):
    for n in range(100):
        time.sleep(0.01)
        with lockb:
            balance.value -= 1


if __name__ == "__main__":
    numbers = [2, 3, 5]
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    p = multiprocessing.Process(target=deposit, args=(balance, lock))
    q = multiprocessing.Process(target=withdraw, args=(balance, lock))

    p.start()
    q.start()

    p.join()
    q.join()

    print(balance.value)

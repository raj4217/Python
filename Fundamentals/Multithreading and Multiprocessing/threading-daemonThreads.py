import time
import threading

total = 4


def create_items():
    global total
    for i in range(10):
        time.sleep(2)
        print('added items')
        total += 1
    print('creation is done')


def create_items_2():
    global total
    for i in range(7):
        time.sleep(1)
        print('added items')
        total += 1
    print('creation is done')


def limit_items():
    global total
    while True:
        if total > 5:
            print('overload')
            total -= 3
            print('subtracted 3')
        else:
            time.sleep(1)
            print('waiting')


creator1 = threading.Thread(target=create_items)
creator2 = threading.Thread(target=create_items_2)`
limitor = threading.Thread(target=limit_items, daemon=True)  # daemon ends the infinite loop once the main method is over
print(limitor.isDaemon())


creator1.start()
creator2.start()
limitor .start()

creator1.join()
creator2.join()
# limitor.join()


print('Ultimate total = {}'.format(total))

import time
import threading


class myThread(threading.Thread):
    def __init__(self, number, style, *args, **kwargs):
        super(myThread, self).__init__(*args, **kwargs)
        self.number = number
        self.style = style
        self.start()

    def run(self, *args, **kwargs):
        print('thread started')
        super(myThread, self).run(*args, **kwargs)
        print('thread ended')


def sleeper(num, style):
    print('Sleeping for {} secs as {}'.format(num, style))
    time.sleep(num)


t = myThread(number=3, style='blue', target=sleeper, args=[3, 'blue'])


# _______________________________________________________________


# class myThread(threading.Thread):
#     def __init__(self, number, func, args):
#         threading.Thread.__init__(self)
#         self.number = number
#         self.func = func
#         self.args = args

#     def run(self):
#         print(f'thread {self.number} has started')
#         self.func(*self.args)
#         print(f'thread {self.number} has finished')


# def double(number, cycles):
#     for i in range(cycles):
#         number += number
#     print(number)


# thread_list = []
# for i in range(50):
#     t = myThread(i + 1, double, [i, 3])
#     thread_list.append(t)
#     t.start()

# for t in thread_list:
#     t.join()


# _______________________________________________________________


# class myThread(threading.Thread):
# def run(self):
#     print('{} has started!'.format(self.getName()))
#     try:
#         if self._target:
#             self._target(*self._args, **self._kwargs)
#     finally:
#         del self._target, self._args, self._kwargs
#     print('{} has finished!'.format(self.getName()))


# def sleeper(n, name):
#     print('{} going to sleep for 2 secs \n'.format(name))
#     time.sleep(n)
#     print('{} has woken up \n'.format(name))


# for i in range(4):
#     t = myThread(target=sleeper, name='thread' + str(i + 1), args=(2, 'thread' + str(i + 1)))
#     t.start()

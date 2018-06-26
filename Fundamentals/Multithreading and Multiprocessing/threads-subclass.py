-#------------------test 1-----------------------

# def run(self):
#     """Method representing the thread's activity.
#     You may override this method in a subclass.
#     The standard run() method
#     invokes the callable object passed to
#     the object's constructor as the
#     target argument, if any, with sequential and
#     keyword arguments taken
#     from the args and kwargs arguments, respectively.
#     """
#     try:
#         if self._target:
#             self._target(*self._args, **self._kwargs)
#     finally:
#         # Avoid a refcycle if the thread is running a function with
#         # an argument that has a member that points to the thread.
#         del self._target, self._args, self._kwargs


# import time
# import threading


# class myThread(threading.Thread):
#     def run(self):
#         print('{} has started!'.format(self.getName()))
#         try:
#             if self._target:
#                 self._target(*self._args, **self._kwargs)
#         finally:
#             # Avoid a refcycle if the thread is running a function with
#             # an argument that has a member that points to the thread.
#             del self._target, self._args, self._kwargs
#         print('{} has finished!'.format(self.getName()))


# def sleeper(n, name):
#     print('{} going to sleep for 2 secs \n'.format(name))
#     time.sleep(n)
#     print('{} has woken up \n'.format(name))


# for i in range(4):
#     t = myThread(target=sleeper, name='thread' + str(i + 1), args=(2, 'thread' + str(i + 1)))
#     t.start()


#__________________test 2___________________


# Changing overriding __init__
# def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):

# import time
# import threading


# class myThread(threading.Thread):
#     def __init__(self, number, func, args):
#         threading.Thread.__init__(self)
#         self.number = number
#         self.func = func
#         self.args = args

#     def run(self):
#         print('Thread {} has started'.format(self.number))
#         self.func(*self.args)
#         print('Thread {} has finished!'.format(self.number))


# def double(number, cycles):
#     for _ in range(cycles):
#         number += number
#     print(number)


# threads_list = []
# for i in range(50):
#     t = myThread(number=i + 1, func=double, args=[i, 3])
#     threads_list.append(t)
#     t.start()

# for t in threads_list:
#     t.join()


#----------------------test 3--------------------

import time
import threading


class myThread(threading.Thread):
    def __init__(self, number, style, *args, **kwargs):
        super(myThread, self).__init__(*args, **kwargs)
        self.number = number
        self.style = style
        self.start()

    def run(self, *args, **kwargs):
        print('Thread Starting')
        super(myThread, self).run(*args, **kwargs)
        print('Thread has ended')


def sleeper(num, style):
    print('Sleeping for {} secs as {}'.format(num, style))
    time.sleep(num)


t = myThread(number=3, style='blue', target=sleeper, args=[3, 'yellow'])

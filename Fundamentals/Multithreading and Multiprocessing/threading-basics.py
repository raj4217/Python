'''
global interpreter lock prevents threads from running in parallel
to overcome this python utilises task switching,
which switches between program very rapidly making it seem like working parallely, but its not
'''

import threading
import datetime
import time


def sleeper(n, name):
    print('{} going to sleep for 2 secs \n'.format(name))
    time.sleep(n)
    print('{} has woken up \n'.format(name))

# t = threading.Thread(target = sleeper,name='thread1',args=(2,'thread1'))
#
# t.start()
# t.join()


threads_list = []
start = datetime.datetime.now()
print(start)
for i in range(1, 5):
    t = threading.Thread(target=sleeper, name='thread_' + str(i), args=(2, 'thread' + str(i)))
    t.start()
    threads_list.append(t)
    print('{} has started'.format(t.name))

for t in threads_list:
    t.join()
end = datetime.datetime.now()
print(end)
print('All 5 threads has finished their tasks')
print('time taken: ' + str(end - start))

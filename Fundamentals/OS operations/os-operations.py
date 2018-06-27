import os
from datetime import datetime
# print(os.getcwd())
os.chdir('Z:/')
# os.mkdir('demo2')
# os.makedirs('demo2/demo3/demo4')
# os.rmdir('demo2')
# os.removedirs(('demo2/demo3/demo4'))
# os.rename('printers.txt','print.txt')
print(os.stat('print.txt'))
print(datetime.fromtimestamp((os.stat('print.txt').st_mtime)))
# print(os.listdir())

with open('xyz.txt', 'r') as rf:
    data = rf.readlines()
data.sort(key=len)
for line in data:
    print(line)

with open('abc.txt', 'w') as wf:
    wf.write('\n'.join(data))

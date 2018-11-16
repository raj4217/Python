import re
with open('xyz.txt', 'r') as rf:
    data = rf.read()

print(re.findall(r'\b\w*[aeiouAEIOU]{2}\w*\b', data))

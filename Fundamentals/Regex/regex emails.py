import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
pattern = re.compile(r'[a-zA-Z1-3-.]+@[a-z-]+\.\w+')

matches = pattern.findall(emails)

for match in matches:
    print(match)

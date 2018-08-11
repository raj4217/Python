import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
'''
sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile('\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile('\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*'))
# pattern = re.compile('[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[^a-zA-Z]')
# pattern = re.compile('[^p]at')
# pattern = re.compile(r'sentence')
# pattern = re.compile(r'start', re.I)

matches = re.compile('\d{3}.\d{3}.\d{4}').findall(text_to_search)

# matches = pattern.finditer(text_to_search)
# matches = pattern.findall(text_to_search)
# matches = pattern.match(sentence)
# matches = pattern.search(sentence)

print(matches)
# for match in matches:
#     print(match)

# with open('data.txt','r') as fread:
#     contents = fread.read()
#     matches = pattern.finditer(contents)
#     [print(match) for match in matches]


'''
. - Any Character Except New Line
 \d - Digit (0-9)
 \D - Not a Digit (0-9)
 \w - Word Character (a-z, A-Z, 0-9, _)
 \W - Not a Word Character(-,\n,*,.,' ','(',')')
 \s - Whitespace (space, tab, newline)
 \S - Not Whitespace (space, tab, newline)
 \b - Word Boundary
 \B - Not a Word Boundary
 ^ - Beginning of a String
 $ - End of a String

 [] - Matches Characters in brackets
 [^ ] - Matches Characters NOT in brackets
 | - Either Or
 ( ) - Group

 Quantifiers:
 * - 0 or More
 + - 1 or More
 ? - 0 or One
 {3} - Exact Number
 {3,4} - Range of Numbers (Minimum, Maximum)

'''

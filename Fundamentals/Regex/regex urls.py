import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''


pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

sub_urls = pattern.sub(r'\2\3', urls)

print(sub_urls)


# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(0))

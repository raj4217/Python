import requests
from bs4 import BeautifulSoup
import csv

# source = requests.get('http://coreyms.com').text
# soup = BeautifulSoup(source, 'lxml')

csv_file = open('scrape.csv', 'w', newline='')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Video_link'])

with open('simple.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
# print(soup.prettify())
# article = soup.find('article')
for article in soup.find_all('article'):
    headline = article.h2.a.text
    # print(headline)
    summary = article.find('div', class_='entry-content').p.text
    # print(summary)
    try:
        vid_link = article.find('iframe', class_="youtube-player")['src']
        vid_id = vid_link.split('/')[4].split('?')[0]
        yt_link = f'https://youtu.be/{vid_id}'

    except Exception as e:
        yt_link = None
    # print(yt_link)
    # print()
    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

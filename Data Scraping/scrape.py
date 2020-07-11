# allows us to download the html
import requests
# allows us to use html to grab data
#  will parse through the data and make it an object
from bs4 import BeautifulSoup
# pretty print
import pprint

# url to get the html
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?=2')

# prints html from url above as a string
# print(res.text)

# you have to specify html.parser. Beautiful soup will also parse XML and more
soup=BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup.body)
# print(soup.find_all('div'))
# print(soup.title)

# finds firsts item
# print(find('a'))

# find all using css selectors
# print(soup.select('.score'))


links=soup.select('.storylink')
links2=soup.select('.storylink')

subtext=soup.select('.subtext')
subtext2=soup.select('.subtext')


mega_links = links + links2
mega_subtext = subtext2 + subtext2

# links and votes line up
# print(links[0], subtext[0])

def sort_stories_by_votes(hacker_news_list):
    return sorted(hacker_news_list, key = lambda k: k['votes'], reverse=True)

def create_custom_news_feed(links, subtext):
    hacker_news = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        votes = subtext[index].select('.score')
        if len(votes):
            # .replace() the sting ' points' (space included) with an empty string
            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
                hacker_news.append(
                    {'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hacker_news)

pprint.pprint(create_custom_news_feed(mega_links, mega_subtext))

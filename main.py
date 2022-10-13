import re
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.loteriasdominicanas.com/"

try:
    html = urllib.request.urlopen(url).read()

except:
    print("Error opening the url")
    exit()

soup = BeautifulSoup(html, "html.parser")

lotteries = soup.select('div.game-block div.my-2 a.game-title span')

numbers = soup.select('div.game-block div.game-scores')

date = soup.select('div.game-block div.session-date')

lotteries_names = [
    lottery_name.contents[0].strip() for lottery_name in lotteries
]

dates_list = [dates.contents[0].strip() for dates in date]
numbers_dict = dict()

#print(numbers)
#print(lotteries_names)
#print(numbers_dict)
#print(lotteries_names)

#print(dates_list)

increment = 0

for tag in numbers:
    score_tags = tag.find_all(class_='score')
    numbers_list = list(map(lambda score_tag: score_tag.string, score_tags))
    # print(tag)
    numbers_dict[lotteries_names[increment]] = {
        'numbers': numbers_list,
        'date': dates_list[increment]
    }
    increment = increment + 1

for k, v in numbers_dict.items():
    print(k, "->", v)

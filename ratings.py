import requests
from bs4 import BeautifulSoup

# id = "12408753"

# url = 'https://www.imdb.com/user/ur' + id + '/ratings'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')

# div = soup.find('div', attrs = {'id' : 'ratings-container'})
# deeper = div.find('div', attrs = {'class' : 'lister-item mode-detail'})
# lis = deeper.find_all('a')
# print(deeper)
#main .article .lister #ratings-container .lister-item mode-detail .lister-item-content

page = requests.get('https://www.imdb.com/user/ur12453789/ratings').text
soup = BeautifulSoup(page,"lxml")

lmovies = []
lratings = []
for item in soup.select(".lister-item-header a"):
    lmovies.append(item.text)

user = soup.findAll("div", {"class": "ipl-rating-star--other-user"})

for i in user:
    ratings = i.findAll("span", {"class": "ipl-rating-star__rating"})
    for i in ratings:
        if i.text == "Rate":
            pass
        else:
            lratings.append(i.text)

# print(lmovies)
# print(lratings)

def mergelist(l1, l2):
    final = [0] * len(l1)
    if len(l1) == len(l2):
        for i in range(0, len(l1)):
            final[i] = (l1[i], l2[i])
    return(final)

print(mergelist(lmovies, lratings))


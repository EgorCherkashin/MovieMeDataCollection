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

id = "12659803"
position = "0"
urltemplate = "https://www.imdb.com/user/ur" + id + "/ratings?sort=date_added%2Cdesc&mode=detai&lastPosition=" + position

def nummovies(id):
    url = "https://www.imdb.com/user/ur" + id + "/ratings"
    page = requests.get(url).text
    soup = BeautifulSoup(page,"lxml")
    movienum = soup.findAll("span", {"id": "lister-header-current-size"})
    final = movienum[0].text
    final = final.replace(',', '')
    return(int(final)) 

def pagescan(url, position):
    url = "https://www.imdb.com/user/ur" + id + "/ratings?sort=date_added%2Cdesc&mode=detai&lastPosition=" + position
    page = requests.get(url).text
    print("PAGE: ", url)
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

    def mergelist(l1, l2):
        final = [0] * len(l1)
        if len(l1) == len(l2):
            for i in range(0, len(l1)):
                final[i] = (l1[i], l2[i])
        return(final)

    # print(mergelist(lmovies, lratings))


# number = nummovies(id)
# print(number)
# if number < 100:
#     print("PAGE NUMBER PENIS")
#     pagescan(id, "0")
# else:
#     for i in range(int(number/100)):
#         print("PAGE NUMBER: ", i)
#         pagescan(id, str(100*i))

file = open("usrs.txt", "r") 
usrs = file.readlines()

test = usrs[0].replace("\n", "")

print(pagescan(test, "0"))
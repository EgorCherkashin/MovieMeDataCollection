import requests
from bs4 import BeautifulSoup

class user:
    def __init__(self, id):
        self.id = id
        self.ratings = []
        self.movienum = 0
        
    def nummovies(self):
        url = "https://www.imdb.com/user/ur" + self.id + "/ratings"
        page = requests.get(url).text
        soup = BeautifulSoup(page,"lxml")
        movienum = soup.findAll("span", {"id": "lister-header-current-size"})
        if movienum != []:
            final = movienum[0].text
            final = final.replace(',', '')
            return(int(final)) 
        else: 
            return 0

    def pagescan(self, id):
        # url = "https://www.imdb.com/user/ur" + id + "/ratings?sort=date_added%2Cdesc&mode=detai&lastPosition=" + position
        url = "https://www.imdb.com/user/ur" + id + "/ratings"
        page = requests.get(url).text
        print("PAGE: ", url)
        soup = BeautifulSoup(page,"lxml")

        lmovies = []
        lratings = []
        for item in soup.select(".lister-item-header a"):
            lmovies.append(item.text)
        
        
        def checkfortv(movienum, id, lmovies):
            if movienum >= 100:
                for i in range(0, 99):
                    if lmovies[i][0] == " ":
                        lmovies[i] = lmovies[i][1:]
                        del lmovies[i+1]
                return(lmovies)
            else:
                for i in range(0, len(lmovies)-1):
                    if lmovies[i][0] == " ":
                        lmovies[i] = lmovies[i][1:]
                        del lmovies[i+1]
                return(lmovies)
        movienum = self.nummovies()
        lmovies = checkfortv(movienum, id, lmovies)


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
            print(final)
            return(final)
        
        return(mergelist(lmovies, lratings))

    def shit(self):
        self.ratings = self.pagescan(self.id)
        return(self.ratings)
    
    

file = open("usrs.txt", "r") 
usrs = file.readlines()

test = usrs[0].replace("\n", "")

# person = user(test)
# print(person.shit())
for i in usrs:
    i = i.replace('\n', '')
    person = user(i)
    print(person.shit())
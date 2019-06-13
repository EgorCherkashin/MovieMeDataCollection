import requests
from bs4 import BeautifulSoup
import itertools as it


x=["1","2","3","4","5","6","7","8","9","0"]
allusrs = list(it.permutations(x, 8))


def checkusr(id, i):
    url = 'https://www.imdb.com/user/ur' + id + '/ratings'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    if soup.find_all("div", {"class": "error_code_403"}):
        print("Doesn't' exist ", i)
    elif soup.find_all("div", {"class": "error_code_404"}):
        print("Error 404")
    else:
        headers = soup.find_all('h1')
        f= open("usrs.txt","a")
        f.write(id+"\n")
        print(id, "--> ", headers)
        f.close()


for i in range(50000, len(allusrs)):
    checkusr(''.join(allusrs[i]), i)


#Got to 51897
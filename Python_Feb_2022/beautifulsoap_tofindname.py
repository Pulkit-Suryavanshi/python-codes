import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input('Enter Url: ')
if len(url)<1:
    url="http://py4e-data.dr-chuck.net/known_by_Zaheerah.html"
count = int(input("Enter count: "))
position = int(input("Enter position:"))
for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)

    print(s[position - 1])
    print(t[position - 1])
    url = s[position - 1]
    #the above code is the driver code!!!!!url=
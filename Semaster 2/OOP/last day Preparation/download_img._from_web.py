from urllib import request

def writeImageFile(link, imgName):
    imgConn = request.urlopen(link)
    imgBytes = imgConn.read()
    file = open(f"D:/GitHub/UBIT-Work/Semaster 2/OOP/last day Preparation/images/{imgName}.png", "wb")
    file.write(imgBytes)
    file.close()

URL = "https://www.google.com/"
webConn = request.urlopen(URL)
webBytes = webConn.read()
try:
    html = webBytes.decode("utf-8")
except:
    html = webBytes.decode("cp1252")
links = []
html = html.replace("'",'"')
p = html.find("<img")
counter = 0
while p != -1:
    s = html.find("src=", p) + 4
    e = html.find('"', s+1)
    link = html[s+1:e]
    if link.startswith("/"):
        link = URL + link
    writeImageFile(link, counter)
    counter += 1
    links.append(link)
    print(link)
    p = html.find("<img", e+1)

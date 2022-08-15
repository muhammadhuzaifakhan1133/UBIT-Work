from urllib import request

URL = "https://oxpstopdf.com"
webConn = request.urlopen(URL)
webBytes = webConn.read()
with open("oxpstopdf.html", "wb+") as file:
    file.write(webBytes)
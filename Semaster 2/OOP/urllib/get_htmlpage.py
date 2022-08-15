from urllib import request

URL = "https://oxpstopdf.com"
webConn = request.urlopen(URL)
webBytes = webConn.read()
webString = webBytes.decode("cp1252")
file = open("oxpstopdf", "w")
file.write(webString)
file.close()
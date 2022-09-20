from crawl_links import getWebBytes

webBytes = getWebBytes("https://www.google.com")
try:
    html = webBytes.decode()
except:
    html = webBytes.decode("cp1252")
file = open("google.html", "wb")
file.write(html)
file.close()
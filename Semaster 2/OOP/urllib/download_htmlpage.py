from functions import getWebBytes

webBytes = getWebBytes("https://www.facebook.com/")
file = open("facebook.html", "wb")
file.write(webBytes)
file.close()
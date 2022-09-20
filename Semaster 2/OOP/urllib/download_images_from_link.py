from crawl_links import crawler, getWebBytes

imgLinks = crawler("https://www.google.com", tagToFind="src")
for link in imgLinks:
    ind = link.rfind("/")
    imgname = link[ind+1:]
    file = open(f"images/{imgname}", "wb")
    file.write(getWebBytes(link))
    file.close()
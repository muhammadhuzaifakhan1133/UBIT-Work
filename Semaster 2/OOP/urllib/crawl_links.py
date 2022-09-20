from urllib import request

def getWebBytes(URL):
    webConn = request.urlopen(URL)
    webBytes = webConn.read()
    return webBytes

def isNotVideoAudioImageFile(link):
    VIDEO = ['.m1v', '.mpeg', '.mov', '.qt', '.mpa', '.mpg', '.mpe', '.avi', '.movie', '.mp4']
    AUDIO = ['.ra', '.aif', '.aiff', '.aifc', '.wav', '.au', '.snd', '.mp3', '.mp2']
    IMAGE = ['.ras', '.xwd', '.bmp', '.jpe', '.jpg', '.jpeg', '.xpm', '.ief', '.pbm', '.tif', '.gif', '.ppm', '.xbm', '.tiff', '.rgb', '.pgm', '.png', '.pnm', '.ico']
    lastsubpage = link[link.rfind("/")+1:]
    if "." in lastsubpage:
        ind = lastsubpage.rfind(".")
        ext = lastsubpage[ind:]
        if ext in VIDEO + AUDIO + IMAGE:
            return False
    return True

def crawler(URL: str, tagToFind="href"):
    links = []
    webBytes = getWebBytes(URL)
    try:
        html = webBytes.decode()
    except:
        html = webBytes.decode("cp1252")
    html = html.split()
    for line in html:
        if line.startswith(tagToFind):
            line = line.replace("'", '"')
            s = line.find('"')
            e = line.rfind('"')
            link = line[s+1:e]
            
            if link.startswith("/"):
                link = URL+link

            if (tagToFind=="href"):
                if (link.startswith("https")) and (isNotVideoAudioImageFile(link)):
                    links.append(link)
            else:
                links.append(link)
    return links

if __name__ == "__main__":
    links = crawler("https://www.google.com")
    for link in links:
        print("=====================================================================================")
        print(link)
        print("=====================================================================================")
        sublinks = crawler(link)
        for sublink in sublinks:
            print(sublink)
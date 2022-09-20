from urllib import request

def getWebBytes(URL):
    try:
        webConn = request.urlopen(URL)
    except:
        req = request.Request(
        url=URL,
        headers={'User-Agent': 'Mozilla/5.0'}
        )
        try:
            webConn = request.urlopen(req)
        except Exception as e:
            print(e)
            return None
    webBytes = webConn.read()
    return webBytes

def isNotVideoAudioImageFile(link):
    VIDEO = ['.m1v', '.mpeg', '.mov', '.qt', '.mpa', '.mpg', '.mpe', '.avi', '.movie', '.mp4']
    AUDIO = ['.ra', '.aif', '.aiff', '.aifc', '.wav', '.au', '.snd', '.mp3', '.mp2']
    IMAGE = ['.ras', '.xwd', '.bmp', '.jpe', '.jpg', '.jpeg', '.xpm', '.ief', '.pbm', '.tif', '.gif', '.ppm', '.xbm', '.tiff', '.rgb', '.pgm', '.png', '.pnm', '.ico']
    lastroot = link[link.rfind("/")+1:]
    if "." in lastroot:
        ind = lastroot.rfind(".")
        ext = lastroot[ind:]
        if ext in VIDEO + AUDIO + IMAGE:
            return False
    return True

def crawler(URL: str, attribute):

    if attribute=="src=":
        tag = "<img"
    else:
        tag = "<a"
    links = []
    webBytes = getWebBytes(URL)
    if (webBytes==None):
        return links
    try:
        html = webBytes.decode("cp1252")
    except:
        html = webBytes.decode()
    p = html.find(tag)
    while p != -1:

        s = html.find(attribute, p) + len(attribute) + 1
        e = s
        while True:
            if html[e] in ['"', "'"]:
                break
            e += 1

        link = html[s:e]
        
        p = html.find(tag, e+1)
        
        if ("javascript:void(0)" in link):
            continue
        
        if ((not link.startswith("//")) and (not link.startswith("http"))):
            link = URL + link
        
        elif link.startswith("//"):
            link = "https:" + link
        
        links.append(link)
        
    return links


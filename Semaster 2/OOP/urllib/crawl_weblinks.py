from functions import crawler, isNotVideoAudioImageFile

links = crawler("https://www.w3schools.com/", attribute="href=")
for link in links:
    if isNotVideoAudioImageFile(link):
        print("=====================================================================================")
        print(link)
        print("=====================================================================================")
        sublinks = crawler(link, attribute="href=")
        for sublink in sublinks:
            print(sublink)
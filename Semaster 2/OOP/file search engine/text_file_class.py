from cgitb import text
from distutils.text_file import TextFile
import os, time

class cTextFile:
    
    def __init__(self, path):
        self.path = path
        self.__extractData()

    def __str__(self):
        return self.path

    def __repr__(self):
        return self.path

    def __extractData(self):
        self.ext = self.path[self.path.rfind("."):]
        self.size = os.path.getsize(self.path)
        self.dateCreation = time.ctime(os.path.getctime(self.path))
        self.dateLastAccess = time.ctime(os.path.getatime(self.path))
        self.dateLastModified = time.ctime(os.path.getmtime(self.path))
        file = open(self.path, "r")
        self.text = file.read()

    def getParagraphs(self, number=None):
        paragraphs = self.text.split("\n")
        if (number == None):
            for index, paragraph in enumerate(paragraphs):
                print(index+1)
                print(paragraph, end="\n\n")
        else:
            print(paragraphs[number-1])
    
    def getSentences(self, number=None):
        sentences = self.text.split(".")
        if (number == None):
            for index, sentence in enumerate(sentences):
                print(index+1)
                print(sentence, end="\n\n")
        else:
            print(sentences[number-1])
    
    def getWords(self, number=None):
        words = self.text.split(" ")
        if (number == None):
            for index, word in enumerate(words):
                print(index+1)
                print(word, end="\n\n")
        else:
            print(words[number-1])

txtfile = cTextFile("C://Users//huzai//OneDrive//Documents//GitHub//UBIT-Work//Semaster 2//OOP//file search engine//f1.txt")
print(txtfile.ext)
print(txtfile.size)
print(txtfile.dateCreation)
print(txtfile.dateLastAccess)
print(txtfile.dateLastModified)
txtfile.getParagraphs()
txtfile.getSentences(2)
txtfile.getWords(11)
import os, pickle
from metric_class import cMetrics

class VectorSpaceModel():

    def __init__(self):
        self.M = cMetrics()
        self.UWL = cMetrics()
        self.docNames = cMetrics()
        self.termFreq = cMetrics()
        self.docFreq = cMetrics()
    
    def wordIndex(self, txt:str, filepath):
        self.docNames.append(filepath)
        words = txt.split()
        row = [0 for _ in self.UWL]
        for index, word in enumerate(words):
            if word in words[:index]:
                continue
            if (word == "") or (word == " "):
                continue
            word = word.lower()            
            for sw in list("!@#$%^&*()_+-={}[]\|;:'""',<.>/?"):
                if sw in word:
                    word = word.replace(sw, "")
            if word not in self.UWL:
                self.UWL.append(word)
                row.append(0)
                for ind, prevRow in enumerate(self.M):
                    self.M[ind] = prevRow + [0]
            row[self.UWL.index(word)] = words.count(word)
        self.M.append(row)

    def scan(self, path):
        try:
            for i in os.scandir(path):
                if (i.is_file()):
                    name = i.name
                    if name.endswith(".txt"):
                        file = open(i.path)
                        txt = file.read()
                        file.close()
                        self.wordIndex(txt, filepath=i.path)
                else:
                    self.scan(i)
        except:
            pass

    def createVSM(self, dirPath):
        self.scan(dirPath)
        self.calculateTermAndDocumentFreq()
        self.applyDocumentFrequency()
        self.applyTermFrequency()


    def writeVSM(self):
        self.writeVectorSpaceToFile()
        self.writeUniqueWordListToFile()
        self.writeDocListToFile()
        self.writeDocFreqToFile()
        self.writeTermFreqToFile()

    def readVSM(self):
        self.readDocListFromFile()
        self.readUniqueWordListFromFile()
        self.readVectorSpaceFromFile()
        self.readDocFreqFromFile()
        self.readTermFreqFromFile()


    def calculateTermAndDocumentFreq(self):
        for r in self.M:
            self.termFreq.append(sum(r))
            
        for c in range(self.UWL.NR):
            ans = 0
            for r in range(self.M.NR):
                ans += self.M[r][c]
            self.docFreq.append(ans)

    def applyTermFrequency(self):
        for r in range(self.M.NR):
            for c in range(self.UWL.NR):
                if self.termFreq[r] != 0:
                    self.M[r][c] = self.M[r][c] / self.termFreq[r]
        

    def applyDocumentFrequency(self):
        for c in range(self.UWL.NR):
            for r in range(self.M.NR):
                if self.docFreq[c] != 0:
                    self.M[r][c] = self.M[r][c] / self.docFreq[c]

    def writeVectorSpaceToFile(self, path="vsm.pickle"):
        file = open(path, "wb")
        pickle.dump(self.M, file)
        file.close()
    
    def readVectorSpaceFromFile(self, path="vsm.pickle"):
        file = open(path, "rb")
        self.M = pickle.load(file)
        file.close()

    def readUniqueWordListFromFile(self, path="uwl.pickle"):
        file = open(path, "rb")
        self.UWL = pickle.load(file)
        file.close()
        

    def writeUniqueWordListToFile(self, path="uwl.pickle"):
        file = open(path, "wb")
        pickle.dump(self.UWL, file)
        file.close()

    def writeDocListToFile(self, path="doclist.pickle"):
        file = open(path, "wb")
        pickle.dump(self.docNames, file)
        file.close()
    
    def readDocListFromFile(self, path="doclist.pickle"):
        file = open(path, "rb")
        self.docNames = pickle.load(file)
        file.close()
        
    def writeDocFreqToFile(self, path="docfreq.pickle"):
        file = open(path, "wb")
        pickle.dump(self.docFreq, file)
        file.close()
    
    def readDocFreqFromFile(self, path="docfreq.pickle"):
        file = open(path, "rb")
        self.docFreq = pickle.load(file)
        file.close()
        
    def writeTermFreqToFile(self, path="termfreq.pickle"):
        file = open(path, "wb")
        pickle.dump(self.termFreq, file)
        file.close()
    
    def readTermFreqFromFile(self, path="termfreq.pickle"):
        file = open(path, "rb")
        self.termFreq = pickle.load(file)
        file.close()
        


    def createQueryVector(self, query):
        self.queryVector = [[0] for _ in self.UWL]
        self.queryVector = cMetrics(self.queryVector)
        wordsInQuery = query.lower().split(" ")
        for word in wordsInQuery:
            if word in self.UWL:
                self.queryVector[self.UWL.index(word)][0] = 1

    def calculateResult(self):
        self.Result = self.M.product(self.queryVector)

    def getFileNamesFromResult(self):
        r = zip(*sorted(zip(self.Result, self.docNames), reverse=True))
        self.sortedQueryResult, self.sortedDocNames = r
        for ind, queryDocResult in enumerate(self.sortedQueryResult):
            if queryDocResult[0] == 0.0:
                break
                
        self.sortedDocNames = self.sortedDocNames[:ind]
        self.sortedQueryResult = self.sortedQueryResult[:ind]
        
    def writeResultToHtml(self):
        html = "<!DOCTYPE html><head><title>Result</title></head><body><ol>"
        print(self.sortedDocNames)
        for r in range(len(self.sortedDocNames)):
            print(self.sortedDocNames[r], self.sortedQueryResult[r][0])
            html += "<li>"
            filename = self.sortedDocNames[r].split("\\")[-1]
            html += f"<a href='file:\\{self.sortedDocNames[r]}'>{filename}</a> {self.sortedQueryResult[r][0]}</li>"
        html += "</ol></body></html>"
        file = open("result.html","w")
        file.write(html)
        file.close()
        
    def find(self, query):
        self.createQueryVector(query)
        self.calculateResult()
        self.getFileNamesFromResult()
        print(self.sortedDocNames)

vsm = VectorSpaceModel()
# # only one time
# vsm.createVSM("D:\\")
# vsm.writeVSM()

vsm.readVSM()
vsm.find("INJECTED")

from Category import Category
from ReplicateManager import ReplicateManager

class Image:
    def __init__(self, name, file, *categories: Category, id=None, keyWords='', extension=''):
        self.name = name
        self.file = file
        self.categories = categories
        self.id = id

        self.keyWords = []
        for keyword in keyWords.split(','):
            self.keyWords.append(keyword.strip().lower())
        return 

    def save(self,dbManager):
        iaKeywords = ReplicateManager.askImage(self).split(",")
        print(iaKeywords)

        filteredKeywords = [keyword for keyword in self.getKeyWords() if keyword in iaKeywords]

        if len(filteredKeywords) != 0 or len(filteredKeywords) >= len(self.getKeyWords()):
            self.keyWords = filteredKeywords
            dbManager.insertOneImage(self)

            result = 1
        else:
            result = -1

        return result


        

    def getName(self):
        return self.name
    
    def getFile(self):
        return self.file
    
    def getId(self):
        return self.id

    def getCategories(self):
        return self.categories
    
    def getKeyWords(self):
        return self.keyWords
    
    def getExtension(self):
        return self.extension

    def getKeyWordsAsString(self):
        return ",".join(self.keyWords)

    def writeFile(self):
        path = "./fotos/uploaded/"
        with open( path + self.getName() + ".jpg", 'wb') as f: 
            f.write(self.getFile())



    def getAllImages(dbanager):
        return dbanager.getAllImages()
    
""""
Read
with open('./fotos/Image1.jpeg', 'rb') as f: 
    imageData = f.read() 

"""


""""
Write

with open('image_copy.jpg', 'wb') as f: 
    f.write(data) 
"""





""""
IA prompt

Describe me the image. Just use words, not sentences. Follow the next format: Answer: word1, word2, word3, word4, etc."""
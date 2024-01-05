class Category:
    def __init__(self, name, categoryFather = None, id=None):
        self.name = name
        self.categoryFather = categoryFather
        self.id = id
        return 

    def save(self, dbManager):
        dbManager.insertOneCategory(self)
        
    def getName(self):
        return self.name
    
    def getFather(self): 
        return self.categoryFather
    
    def getAllFathers(self, dbManager):
        return dbManager.getFatherCategories(self)

    def getAllSons(self, dbManager):
        return dbManager.getSonsCategories(self)
    
    def getImages(self, dbManager):
        return dbManager.getImagesByCategory(self)
    
    def getAllImages(self, dbManager):
        images = []
        images.extend(dbManager.getImagesByCategory(self))

        for sonCategory in dbManager.getSonsCategories(self):
            images.extend(dbManager.getImagesByCategory(sonCategory))

        return images


    def getId(self):
        return self.id
    



    def getAllCategories(dbanager):
        return dbanager.getAllCategories()

import psycopg2 
from Category import Category
from Image import Image
from typing import List

class DBManager:

    def __init__ (self):

        url = ""
        user = ""
        password = ""
        db = ""
        
        self.conexion1 = psycopg2.connect(host=url, database=db, user=user,
            password=password)
        self.cursor1=self.conexion1.cursor()
        print("Connection to DB done succesfully :)")




    def insertOneCategory(self, category: Category):
        request = f"insert into public.\"Category\"(name) values ('{category.getName()}')"

        self.cursor1.execute(request)
        self.conexion1.commit()

    def insertOneImage(self, image: Image):
        request = "insert into public.\"Image\"(name, file, KeyWords, extension ) values (%s, %s, %s, %s) returning id;"
        data = (image.getName(), image.getFile(), image.getKeyWordsAsString(), "jpeg")
        self.cursor1.execute(request, data)


        id = self.cursor1.fetchmany(1)[0][0]

        insertRequest = "insert into public.\"img_ctg\"(ctg_id, img_id) values (%s, %s)"
        print(image.getCategories())
        for category in image.getCategories():
            data = [category.getId(), id]
            self.cursor1.execute(insertRequest, data)

        self.conexion1.commit()




    def getAllCategories(self) -> List[Category]: 
        request = "select * from public.\"Category\""
        self.cursor1.execute(request)
        resultSQL = self.cursor1
        
        categories = []
        for row in resultSQL:
            newCategory = Category(row[1], categoryFather=row[2], id=row[0])
            categories.append(newCategory)

        return categories

    def getAllImages(self) -> List[Image]: 
        request = "select * from public.\"Image\""
        self.cursor1.execute(request)
        resultSQL = self.cursor1
        
        images = []
        for row in resultSQL:
            newImage = Image(row[1], row[2], id=row[0], extension = row[4], keyWords=row[3])
            images.append(newImage)

        return images
    
    def getFatherCategories(self, category: Category):
        request = "select * from public.\"Category\" where id = (%s)"
        data = category.getFather()

        # Check it has a father
        if (data == None):
            return []
        
        data = str(data.getId())

        #  Check if the father exists
        countRequest = "select count(*) from public.\"Category\" where id = (%s)"
        self.cursor1.execute(countRequest, data)
        result = self.cursor1.fetchmany(1)
        if result[0] == 0:
            return []


        # Get his fathers and then add it to a list of others fathers
        self.cursor1.execute(request, data)
        resultSQl = self.cursor1
        row = resultSQl.fetchmany(1)
        
        fatherCategory = Category(row[0][1], categoryFather=row[0][2] , id=row[0][0])
        
        
        fatherCategories = self.getFatherCategories(fatherCategory)
        fatherCategories.append(fatherCategory)


        return fatherCategories

    def getSonsCategories(self, category: Category):
        categoryId = category.getId()
        categoryId = str( categoryId )
        
        #  Check if it has a son
        countRequest = "select count(*) from public.\"Category\" where \"Category\".categoryfather = (%s)"
        self.cursor1.execute(countRequest, categoryId)
        result = self.cursor1.fetchmany(1)
        if result[0] == 0:
            return []

        request = "select * from public.\"Category\" where categoryFather = (%s)"

        # Get his fathers and then add it to a list of others fathers
        self.cursor1.execute(request, categoryId)
        resultSQl = self.cursor1
        rows = resultSQl.fetchmany()

        sons = []
        for sonRow in rows:
            sonCategory = Category(sonRow[1], categoryFather=sonRow[2] , id=sonRow[0])
            sons.append(sonCategory)
            sons.extend(self.getSonsCategories(sonCategory))
        
        return sons

    def getImagesByCategory(self, category: Category):
        countRequest = """SELECT count(*)
            FROM public."Category" as category, public."Image" as image, public."img_ctg" as linker
            where category.id = (%s) and category.id = linker.ctg_id and image.id = linker.img_id
            ;"""
        data = category.getId()
        data = str(data)

        self.cursor1.execute(countRequest, data)
        countResult = self.cursor1.fetchmany(1)[0][0]

        request = """SELECT image.*
            FROM public."Category" as category, public."Image" as image, public."img_ctg" as linker
            where category.id = (%s) and category.id = linker.ctg_id and image.id = linker.img_id
            ;"""
        images = []
        data = category.getId()
        data = str(data)

        self.cursor1.execute(request, data)
        resultSQl = self.cursor1
        rows = resultSQl.fetchmany(int(countResult))
        
        for image in rows:
            newImage = Image(image[1], image[2] , id=image[0], extension = image[4], keyWords= image[3])
            images.append(newImage)

        return images

    

    


    def close(self):
        self.cursor1.close()
        self.conexion1.close()
        print("Conexión cerrada")
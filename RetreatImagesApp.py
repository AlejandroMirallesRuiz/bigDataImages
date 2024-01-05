from DBManager import DBManager
from Category import Category
from Image import Image

import gradio as gr

from zipfile import ZipFile

bdManager = DBManager()


allCategories = Category.getAllCategories(bdManager)

categoriesNameList = [category.getName() for category in allCategories]
categoriesNameList.insert(0, "All categories")

def getCategoryByName(name):
    for category in allCategories:
        if category.getName() == name:
            return category
    return None

def createsZip(images):
    archive = "./images.zip"

    with ZipFile(archive, 'w') as zip_archive:
        # Create three files on zip archive

        for image in images:
            with zip_archive.open(image.getName() + ".jpeg", 'w') as file:
                file.write(image.getFile())


    return archive

def getImagesByCategory(choosenCategory):
    if choosenCategory == "All categories" or choosenCategory == [] or choosenCategory == None:
        images = Image.getAllImages(bdManager)
    else: 
        category = getCategoryByName(choosenCategory)
        images = category.getAllImages(bdManager)

    return images

def filterImagesByOptionalKeywords(images, keywords):
    def intersection(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3
    
    filteredImages = []

    for image in images:
        if intersection(image.getKeyWords(), keywords) != []:
            filteredImages.append(image)

    return filteredImages

def filterImagesByAllKeywords(images, keywords):
    filteredImages = []
    keywords.sort()

    for image in images:
        imageKeyWords = image.getKeyWords()
        imageKeyWords.sort()

        if imageKeyWords == keywords:
            filteredImages.append(image)
    
    return filteredImages

def filterImagesByKeywords(keywords, shouldContainAllWords, images):
    if keywords == '' or keywords == None:
        return images #Don't do anything
    
    
    keywords = [keyword.strip().lower() for keyword in keywords.split(",")]
    
    if shouldContainAllWords:
        images = filterImagesByAllKeywords(images, keywords)
    else:
        images = filterImagesByOptionalKeywords(images, keywords)

    return images


def getImagesInZip(choosenCategory, keywords, shouldContainAllWords):
    images = getImagesByCategory(choosenCategory)

    images = filterImagesByKeywords(keywords, shouldContainAllWords, images)
    
    for image in images:
        image.writeFile() 

    return createsZip(images)

demo = gr.Interface(fn=getImagesInZip, 
                    inputs=[gr.Dropdown(categoriesNameList, label="Categorias", info="Escoge una categoría y te doy un zip con una burrada de imágenes"),
                            "text", 
                            "checkbox"],
                    outputs= "file" 
    )

    
if __name__ == "__main__":
    demo.launch(show_api=False) 
    


bdManager.close()


""" 
bdManager = DBManager()

category = Category("Deporte", id=3)

for image in category.getAllImages(bdManager):
    print(image.getName() )


bdManager.close()
 """
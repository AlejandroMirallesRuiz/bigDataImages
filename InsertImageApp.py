from DBManager import DBManager
from Category import Category
from Image import Image

import gradio as gr


bdManager = DBManager()

allCategories = Category.getAllCategories(bdManager)

categoriesNameList = [category.getName() for category in allCategories]


def insertImage(name, categoriesNames, userKeyWords, image):
    # categories -> [Categorias]
    print(categoriesNames)
    categories = [category for category in allCategories if category.getName() in categoriesNames]

    # Get image file
    with open(image, 'rb') as f: 
        file = f.read()

    # Create image
    image = Image(name, file, *categories, keyWords=userKeyWords)

    if image.save(bdManager):
        result="Succesfully inserted"
        filteredKeyWords = image.getKeyWordsAsString()
    else:
        result="Insertion fail"
        filteredKeyWords = "Error 500!!"

    return [result, filteredKeyWords ]


demo = gr.Interface(fn=insertImage, 
                    inputs=[gr.Textbox(label="Nombre"),
                            gr.CheckboxGroup(categoriesNameList, label="Categorias", info="Escoge las categorías a las que perteneece la imagen"),                            
                            gr.Textbox(label="Palabras Clave"),
                            gr.Image(label="Imagen", type="filepath")],
                    outputs=[gr.Textbox(label="Resultado"),
                             gr.Textbox(label="Palabras Claves ya filtradas")
                            ])
    
if __name__ == "__main__":
    demo.load()
    demo.launch(show_api=False) 
    

bdManager.close()
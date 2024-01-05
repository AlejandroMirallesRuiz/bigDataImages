from DBManager import DBManager
from Category import Category
from Image import Image

import gradio as gr

def greet(name):
    return "Hello modificado" + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    
if __name__ == "__main__":
    demo.launch(show_api=False) 
    

""" 
bdManager = DBManager()

category = Category("Deporte", id=3)

for image in category.getAllImages(bdManager):
    print(image.getName() )


bdManager.close()
 """
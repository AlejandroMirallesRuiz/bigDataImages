# bigImagesData
##### Pequeño proyecto tonto no previsto para recibir ni actualizaciones ni mantenimiento. Es una excusa para usar una IA y gradio.

## Qué es bigImagesData

Pequeño proyecto hecho en python y cuyo objetivo es poder insertar imágenes y guardar en una bbdd su nombre, la propia imagen, las categorías a las que pertenece y una lista de palabras claves proporcionadas por el usuario y que tendrán que coincidir con las que proporcione una IA:

![](/assets/images/InsertImages.PNG)

Además se podrán especificar una categorías y unas posibles palabras clave para que se devuelva un archivo zip con todas las imágenes de dicha categoría y palabras clave. 

![](/assets/images/RetreatImages.PNG) 

Como se puede observar, hay dos modos de búsqueda: Opcional y obligatorio. En el primero las imágenes devueltas deben contener al menos una de las palabras clave; mientras que en el segundo debe contener todas las palabras clave

## Instalación

Para poder correr el programa hay que:
- Instalar los siguientes paquetes:
```bash
pip install gradio
pip install psycopg2, psy2copg2-binary
pip install replicate
```

- Configurar DBManager para que modifique la base de datos que tu quieras.

- Crearse una cuenta en [Replicate](https://replicate.com/account/api-tokens) y copiar un token del siguiente enlace: [Replicate](https://replicate.com/account/api-tokens)

- Finalmente ejecuta el siguiente comando:
```bash
export REPLICATE_API_TOKEN=REPLACE_THIS_WITH_YOUR_TOKEN
```
Finalmente ya puedes correr el programa. Si quieres insertar imágenes haz:
```bash
python3 InsertImageApp.py
```
y para recoger imágenes haz:
```bash
python3 RetreatImagesApp.py
```
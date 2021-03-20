# Creando Entornos Virtuales
0.- Entras a CMD.
1.- Entras a tu carpeta con el comando cd.
2.- Ingresa el comando “py -m pip install virtualenv”.
3.- Pones el comando py -m venv nombre_de_tu_espacio_virtual".
4.- Colocas "nombre_de_tu_espacio_virtual\Scripts\activate"
    -tutorial-env\Scripts\activate.bat
5.- Por último, tipeas “pip install nombre_de_librería” en este caso, el nombre de la librería que queremos en “bokeh”.

# importar una libreria externa
from bokeh.plotting import figure , output_file , show
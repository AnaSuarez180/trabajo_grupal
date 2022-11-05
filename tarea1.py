"""Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, 
editorial y autor(es). Considerar que un libro puede tener varios autores.

Se solicita escribir un programa en Python que permita registrar libros. 
Debe utilizar: colecciones (listas, tuplas, etc), funciones y clases de Python.

Dicho programa debe tener un menu (a interactuar en la línea de comando) para:

Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.
Opción 2: Listar libros.
Opción 3: Agregar libro.
Opción 4: Eliminar libro.
Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y 
listar el resultado.
Opción 6: Ordenar libros por título.
Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y 
listar los resultados.
Opción 8: Buscar libros por número de autores. Se debe ingresar un número por 
ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros 
que contengan 2 autores.
Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial 
y autores).
Opción 10: Guardar libros en archivo de disco duro (.txt o csv).
Nota: listar libros involucra: título, género, ISBN, editorial y autor(es)"""


import pandas as pd
from csv import writer
import csv

#data = list(csv.reader(open(input('Escriba la dirección del archivo a leer: '))))

data = pd.read_csv('books2.csv', sep=";") #index_col=0,

def listar_libros():
    print(data)

# listar_libros()

#AGREGAR LIBRO

# datos = [input('Id: '), input('Título: '), input('Género: '), input('ISBN: '), input('Editorial: '), input('Autores: ')]
def append_list_as_row(file_name, raw_content):
    
    with open(file_name,'a+',newline='') as write_obj:
        cvs_writer = writer(write_obj)
        cvs_writer.writerow(raw_content)
        print('¡Listo! Revisa en la ruta que indica la terminal.')

# append_list_as_row('books2.csv', datos)


def eliminar_libro(file_name):
    eliminado = input('Ingresa el libro a eliminar: ')
    with open(file_name, 'r+') as r, open('output.csv', 'w') as f:
        reader = csv.reader(r)
        writer = csv.writer(f)
        for row in reader:
            if eliminado in row:
                print(f'{row} será eliminada')
            else:
                writer.writerow(row)

# eliminar_libro('books2.csv')


def buscar_libro():
    df = pd.DataFrame(data)
    eleccion = input('Título o ISBN: ')
    if eleccion.lower() == 'título':
        libro = input('Ingresa el libro: ')
        df = df[df.apply(lambda r: r.str.contains(libro, na=False).any(), axis=1)]
        print(df)
    elif eleccion.lower() == 'isbn':
        isbn = input('Ingresa el ISBN: ')
        df = df[df.apply(lambda r: r.str.contains(isbn, na=False).any(), axis=1)]
        print(df)
    else:
        print('Opción incorrecta.')

# buscar_libro()

#ORDERNAR LIBROS POR TÍTULO
def ordenar_libros():
    csvData = pd.read_csv('books2.csv')
    csvData.sort_values(csvData.columns[1], axis=0, inplace=True)
    print(csvData)

ordenar_libros() #El primero es Angels and Demons, el último es Twilight




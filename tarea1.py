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
import os

opc = input('Ingresa una opción para continuar: ')

if opc == '1':

#OPCIÓN 1 RUTA

    open_file = input('Escriba el nombre o la dirección del archivo a leer: ')
open_file = 'books2.csv'

data = pd.read_csv(open_file, sep=",") #index_col=0,

if opc == '2':
#OPCIÓN 2 LISTAR LIBROS
    def listar_libros():
        print(data)

    listar_libros()

if opc == '3':
#OPCIÓN 3 AGREGAR LIBRO
    datos = [input('Id: '), input('Título: '), input('Género: '), input('ISBN: '), input('Editorial: '), input('Autores: ')]
    def append_list_as_row(file_name, raw_content):
        
        with open(file_name,'a+',newline='') as write_obj:
            cvs_writer = writer(write_obj)
            cvs_writer.writerow(raw_content)
            print('¡Listo! Revisa en la ruta que indica la terminal.')

    append_list_as_row(open_file, datos)

if opc == '4':
#OPCIÓN 4 ELIMINAR LIBRO
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

    eliminar_libro(open_file)

if opc == '5':
#OPCIÓN 5 BUSCAR LIBRO
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

    buscar_libro()

if opc == '6':
# OPCIÓN 6 ORDERNAR LIBROS POR TÍTULO
    def ordenar_libros():
        csvData = pd.read_csv(open_file)
        csvData.sort_values(csvData.columns[1], axis=0, inplace=True)
        print(csvData)

    ordenar_libros() #El primero es Angels and Demons, el último es Twilight

if opc == '7':
#OPCIÓN 7 Buscar libros por autor, editorial o género
    def buscar_libro_other():
        df = pd.DataFrame(data)
        eleccion = input('¿Buscar por Autor, Editorial o Género?: ')
        if eleccion.lower() == 'autor':
            autor = input('Ingresa el autor: ')
            df = df[df.apply(lambda r: r.str.contains(autor, na=False).any(), axis=1)]
            print(df)
        elif eleccion.lower() == 'editorial':
            editorial = input('Ingresa la editorial: ')
            df = df[df.apply(lambda r: r.str.contains(editorial, na=False).any(), axis=1)]
            print(df)
        elif eleccion.lower() == 'género':
            genero = input('Ingresa el género: ')
            df = df[df.apply(lambda r: r.str.contains(genero, na=False).any(), axis=1)]
            print(df)
        else:
            print('Opción incorrecta.')

    buscar_libro_other()

if opc == 'not intended':

#Not intended: devuelve una lista de autores y cuantas veces se repiten
    def not_intended():
        df = pd.DataFrame(data)
        sixth_column = df.iloc[:, 5]  
        counts = sixth_column.value_counts()
        print(counts) 

    print('Esta es una función secreta.')
    not_intended()

if opc == '8':
#OPCIÓN 8 BUSCAR LIBROS POR No DE AUTORES
    def buscar_num_autores():
        num = int(input('Número de autores: '))
        df = pd.DataFrame(data)
        # df2 = pd.DataFrame(data)
        # df2.sort_values(df2.columns[1], axis=0, inplace=True)
        df_a = df['autores'].str.len().any()
        df = df['autores'].str.len()
        print(df)

    buscar_num_autores()

if opc == '9':
#OPCIÓN 9 EDITAR
    def editar_datos():
        df = pd.read_csv(open_file)
        row = int(input('Número de la fila a modificar: '))
        column = int(input('Nombre de la columna a modificar: '))
        update = input('Información a modificar: ')
        df.at[row, column] = update
        df.to_csv(open_file, index=False)
        print('Listo. Revisa tu archivo')

    editar_datos()

if opc == 10:
#OPCIÓN 10 RUTA OUTPUT
    def definir_ruta():
        df = pd.read_csv(open_file)
        save_path = input('Escriba la carpeta en donde se guardará el archivo: ')
        comp_name = os.path.dirname(os.path.abspath(save_path))
        df.to_csv(os.path.join(comp_name, 'output3.csv'))

    definir_ruta()

else:
    print('Opción incorrecta.')
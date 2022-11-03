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

import csv

#csv

#     data = list(csv.reader(open(input('Escriba la dirección del archivo a leer: '))))
#     #C:\Users\sofia\Desktop\SILABUZ CLASES\SEMANA 2\TRABAJO GRUPAL\books.csv
#     for row in data:
#         print(row) 

class Libro:
    def __init__(self, id, titulo, genero, isbn, editorial, autores, **kwargs) -> None:
        self.__dict__.update(**kwargs)
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autores = autores
    
    def listar_libros(self):
        print(self.id)
        print(self.titulo)
        print(self.genero)
        print(self.isbn)
        print(self.editorial)
        print(self.autores)


# data = list(csv.reader(open(input('Escriba la dirección del archivo a leer: '))))
    #C:\Users\sofia\Desktop\SILABUZ CLASES\SEMANA 2\TRABAJO GRUPAL\books.csv
# print(data)
# for list in data:
#     data.append(book_list)

book_list =[]
with open(r'C:\Users\sofia\Desktop\SILABUZ CLASES\SEMANA 2\TRABAJO GRUPAL\books.csv', 'r') as data:
    #Puede ser solo books.csv o la ruta en la que tengas el archivo
    csv_dict_reader = csv.reader(data)
    for row in csv_dict_reader:
        book_list.append(row)

#Listar libros
book_list.pop(0)
print(book_list)

#Pensé que se necesitarían otras funciones dentro de la clase, pero ya no estoy segura
#Se pueden descartar

def agregar_libros(self):
        pass

def eliminar_libro(self):
        pass



#libro = Libro(data)
#libro.listar_libro .... o algo así?

# libro = Libro(book_list)
# libro.listar_libros()
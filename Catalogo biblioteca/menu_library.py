
import json
import csv
import os

with open("books.json", "r", encoding="utf8") as book:
    read = book.read()
dic_books = json.loads(read)

print("[1] Buscar libro")
print("[2] Añadir libro")
print("[3] Eliminar libro")
print("[4] Salir")
selec = str(input("Ingrese opcion: "))
while True:

    if selec == "1":
        id = str(input("Ingrese id libro: "))
        while True:
            if id not in dic_books.keys():
                os.system("cls")
                print("[1] Buscar libro")
                print("[2] Añadir libro")
                print("[3] Salir")
                print("Libro NO en base de datos")
                break
            if id in dic_books.keys():
                os.system("cls")
                print("[1] Buscar libro")
                print("[2] Añadir libro")
                print("[3] Salir")
                print(id, "=", dic_books[id])
                break
        selec = str(input("Ingrese opcion: "))
    
    if selec == "2":
        id = str(input("Ingrese id: "))
        while True:
            if id in dic_books.keys():
                os.system("cls")
                print("[1] Buscar libro")
                print("[2] Añadir libro")
                print("[3] Salir")
                print("Libro en base de datos (Json)")
                break
            else:
                title = str(input("Ingrese titulo: "))
                author = str(input("Ingrese autor: "))
                year = str(input("Ingrese año: "))
                dic_books[id] = [{"title" : title}, {"author" : author}, {"year" : year}]
                os.system("cls")
                print("[1] Buscar libro")
                print("[2] Añadir libro")
                print("[3] Salir")
                print("Libro ingresado a base de datos (Json)")
                print(id, "=", dic_books[id])
                with open("books.json", "w", encoding="utf8") as book:
                    new_json = json.dumps(dic_books)
                    book.write(new_json)
                break
        selec = str(input("Ingrese opcion: "))

    if selec == "3":
        id = str(input("Ingrese id: "))
        if id in dic_books.keys():
            dic_books.pop(id)
        os.system("cls")
        print("[1] Buscar libro")
        print("[2] Añadir libro")
        print("[3] Salir")
        print("Libro eliminado de base de datos (Json)")
        selec = str(input("Ingrese opcion: "))
        with open("books.json", "w", encoding="utf8") as book:
            new_json = json.dumps(dic_books)
            book.write(new_json)

    if selec == "4":
        print("Haz salido de consola")
        break




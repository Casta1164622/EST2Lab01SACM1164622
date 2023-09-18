import binaryTree as bt
import FileReader as fr
import json
import os

data = fr.readCSVFile()

LT = bt.Node(10000,{'name':'0','dpi':'10000'})

print("Cargando...")
for instruccion in data:

    person = json.loads(instruccion[1])
    if instruccion[0] == "INSERT":
        LT.insert(int(person['dpi']),person)
    if instruccion[0] == "DELETE":
        LT.delete(bt.Node(int(person['dpi']),person))
    if instruccion[0] == "PATCH":

        LT.patch(bt.Node(int(person['dpi']),person),person)

menu_options = {
    1: 'Buscar Por Nombre',
    2: 'Buscar Por DPI',
    3: 'Buscar Por Nombre y DPI',
    4: 'Salir',
}
def print_menu():
    #os.system('cls')
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     os.system('cls')
     print('Buscar Por Nombre')
     print("------------------------")
     print('Ingrese el nombre a buscar')
     nombresearch = input()
     searchNombre = bt.Node.buscarNombres(LT,nombresearch.lower())
     if len(searchNombre)>0:
         print('Resultados:')
         for item in searchNombre:
             print(item)
     else:
         print('No se encontraron resultados con el nombre: ',searchNombre)
     input("Presione enter para regresar al menu principal ")

def option2():
     os.system('cls')
     print('Buscar Por DPI')
     print("------------------------")
     print('Ingrese el DPI a buscar')
     dpisearch = input()
     searchDPI = bt.Node.searchDPI(LT,bt.Node(dpisearch,{'dpi':int(dpisearch)}))
     if searchDPI != None:
         print('Resultados:')
         print(searchDPI.data)
     else:
         print('No se encontraron resultados con el dpi: ',dpisearch)
     input("Presione enter para regresar al menu principal ")

def option3():
     os.system('cls')
     print('Buscar Por Nombre y DPI')
     print("------------------------")
     print('Ingrese el Nombre a buscar')
     nombresearch = input()
     print('Ingrese el DPI a buscar')
     dpisearching = input()
     searchboth = bt.Node.searchDPI(LT,bt.Node({'dpi':int(dpisearching)}))
     if searchboth != None:
         print('Resultados:')
         print(searchboth)
     else:
         print('No se encontraron resultados con el dpi: ',dpisearching,' y el nombre: ',nombresearch)
     input("Presione enter para regresar al menu principal ")

while(True):
    print_menu()
    option = ''
    try:
        option = int(input('Ingresa tu eleccion: '))
    except:
        print('Opcion no valida, ingresa otra...')
    #Check what choice was entered and act accordingly
    if option == 1:
       option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        print('Gracias por utilizar!')
        exit()
    else:
        print('Opcion no valida, ingresa otra...')

import FileReader as fReader
import bplustree as bpt
import json
import os

data = fReader.readCSVFile()

dataTree = bpt.BPlusTree()

print("Cargando...")
for instruction in data:
    person = json.loads(instruction[1])
    personDpi = {key: val for key,
                  val in person.items() if key == 'dpi'}
    personName = {key: val for key,
                  val in person.items() if key == 'name'}
    if instruction[0] == "INSERT":
        dataTree.insert((personDpi,personName),person)
    if instruction[0] == "DELETE":
        dataTree.delete((personDpi,personName))
    if instruction[0] == "PATCH":
        dataTree.change((personDpi,personName),person)

searchambos = dataTree.query((personDpi,personName))
print(searchambos)
print("------------------------")

searchdpi = dataTree.searhDPI((personDpi,personName))
print(searchdpi)
print("------------------------")
personDpi['dpi'] = ""
searchNombre = dataTree.searchNombre((personDpi,personName))
print(searchNombre)
print("------------------------")

menu_options = {
    1: 'Buscar Por Nombre',
    2: 'Buscar Por DPI',
    3: 'Buscar Por Nombre y DPI',
    4: 'Salir',
}
def print_menu():
    os.system('cls')
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     os.system('cls')
     print('Buscar Por Nombre')
     print("------------------------")
     print('Ingrese el nombre a buscar')
     nombresearch = input()
     searchNombre = dataTree.searchNombre(({'dpi':'0'},{'name':nombresearch.lower()}))
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
     searchDPI = dataTree.searhDPI(({'dpi':dpisearch},{'name':''}))
     if searchDPI != None:
         print('Resultados:')
         print(searchDPI)
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
     searchboth = dataTree.query(({'dpi':dpisearching},{'name':nombresearch.lower()}))
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


            





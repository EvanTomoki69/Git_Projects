import time

ordenconst = "Tomando su orden..."
momentoconst = "Un momento..."

def saludo ():
    print("POO CAKES 2023")
    print("¡BIENVENIDO A POO CAKES 2023!, SERÁ UN PLACER ATENDERLE")
    print("Por favor, seleccione el tamaño de su pastel")
    print("Pastel 1: Pequeño, 8 porciones", "Pastel 2: Mediano, 12 porciones", "Pastel 3: Familiar, 18 porciones", "Pastel 4: Gigante, 25 porciones")
    pastel()

def pastel():
    pasteles = ["1", "2", "3", "4"]
    porcion = input("Porfavor selecciona el tamaño de tu pastel ingresando el numero del pastel: ")
    if porcion in pasteles:
        print(porcion, ordenconst)
    else:
        print(momentoconst)
        time.sleep(2)
        print(porcion, "Lo siento, el tamaño del pastel no es válido")
        quit()
    
    print("Bizcocho 1: Vainilla", "Bizcocho 2: Chocolate", "Bizcocho 3: Vainilla con chispas de chocolate", "Bizcocho 4: Choco-vainilla")
    bizcocho()


def bizcocho():
    bizcochosnum = ["1", "2", "3", "4"]
    bizcochoinput = input("Porfavor selecciona el tipo de bizcocho favorito para su pastel: ")
    if bizcochoinput in bizcochosnum:
        print(bizcochoinput, ordenconst)
    else:
        print(momentoconst)
        time.sleep(2)
        print(bizcochoinput, "Lo siento, el biscocho no es válido")
        quit()
    
    print("Relleno 1: Caramelo", "Relleno 2: Crema de coco", "Relleno 3: Crema pastelera", "Relleno 4: Choco-vainilla")
    relleno()

def relleno():
    rellenosnum = ["1", "2", "3", "4"]
    rellenoinput = input("Porfavor selecciona el tipo de relleno favorito para su pastel: ")
    if rellenoinput in rellenosnum:
        print(rellenoinput, ordenconst)
    else:
        print(momentoconst)
        time.sleep(2)
        print(rellenoinput, "Lo siento, el relleno no es válido")
        quit()
    
    print("Remojo 1: Chocolate", "Remojo 2: Fresa", "Remojo 3: Caramelo", "Remojo 4: Vainilla")
    remojo()

def remojo():
    remojosnum = ["1", "2", "3", "4"]
    remojoinput = input("Porfavor selecciona el tipo de remojo favorito para su pastel: ")
    if remojoinput in remojosnum:
        print(remojoinput, ordenconst)
    else:
        print(momentoconst)
        time.sleep(2)
        print(remojoinput, "Lo siento, el remojo no es válido")
        quit()
    
    print("Porfavor selecciona las frutas que llevará tu pastel")
    print("Opción 1: Fresas", "Opción 2: Melocotón y Kiwi", "Opción 3: Mix de Fresas con Melocotón, Kiwi y Uvas" )
    frutas()
    
def frutas():
    frutasopc = ["1", "2", "3"]
    frutasinput = input("Escribe la opción: ")
    if frutasinput in frutasopc:
        print(frutasinput, "Generando precio final" )
    else:
        print(momentoconst)
        time.sleep(2)
        print(frutasinput, "Lo siento, la opción no es válida")
        quit()


#Esto imprime el saludo, no lo borren
saludo()
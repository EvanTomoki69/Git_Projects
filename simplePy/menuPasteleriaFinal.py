import time

print("----------------POO_CAKES-----------------")
print("POO CAKES 2023")
print("¡BIENVENIDO A POO CAKES 2023!, SERÁ UN PLACER ATENDERLE")
print("A continuación te mostraremos nuestro menú con precios actualizados:")
time.sleep(3)
print("Pasteles: ",
    "Pastel 1: Pequeño, 8 porciones",
    "Pastel 2: Mediano, 16 porciones",
    "Pastel 3: Familiar, 24 porciones",
    "Pastel 4: Gigante, 30 porciones")
print("Bizcochos: ",
    "Bizcocho 1: Bizcocho de vainilla",
    "Bizcocho 2: Bizcocho de chocolate",
    "Bizcocho 3: Bizcocho de vainilla con chispas de chocolate",
    "Bizcocho 4: Bizcocho de choco-vainilla")
print("Relleno: ",
    "Relleno 1: Caramelo",
    "Relleno 2: Crema de coco",
    "Relleno 3: Crema pastelera",
    "Relleno 4: Choco-vainilla")
print("Remojo: ",
    "Remojo 1: Chocolate",
    "Remojo 2: Fresa",
    "Remojo 3: Caramelo",
    "Remojo 4: Vainilla")
print("Frutas: ",
    "Frutas 1: Fresas",
    "Frutas 2: Mix de fresas, kiwi, melocotón y uvas")
menu = {"Pastel 1": 9.0,
        "Pastel 2": 15.0,
        "Pastel 3": 23.0,
        "Pastel 4": 29.0,
        "Bizcocho 1": 2.0,
        "Bizcocho 2": 2.0,
        "Bizcocho 3": 4.0,
        "Bizcocho 4": 4.0,
        "Relleno 1": 2.0,
        "Relleno 2": 2.0,
        "Relleno 3": 1.0,
        "Relleno 4": 3.0,
        "Remojo 1": 1.0,
        "Remojo 2": 1.0,
        "Remojo 3": 1.0,
        "Remojo 4": 1.0,
        "Frutas 1": 1.0,
        "Frutas 2": 2.5}
carta = []
total = 0
for key, value in menu.items():
    print(f"{key:30}: ${value:.2f}")
print("-----------------2023---------------------")

while True:
    pastel = input("Selecciona la configuración de tu pastel ingresando el nombre y numero del pastel, bizcocho, relleno, remojo y frutas que llevará (presione Y para confirmar su orden total): ")
    if pastel == "Y":
        break
    elif menu.get(pastel) is not None:
        carta.append(pastel)

print("---------------SU_ORDEN-------------------")
for pastel in carta:
    total += menu.get(pastel)
    print(pastel, end=" ")

print()
print(f"El total de su orden es: ${total:.2f}")
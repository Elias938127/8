#crear un programa que usando diccionarios almacene la informacion de 5
# productos .los campos deben ser codigo,nombre y precio.
#cuando el programa se ejecute debe mediante un bucle solicitar el codigo
# del producto y la cantidad de la, cuando el usuario indique que desea terminar
# el ingreso de datos .el programa debe mostrar: codigo, nombre,precio,cantidad y
# total .y al final el total de toda la compra.




diccionario = {"Codigo": ["e-001", "e-002", "e-003", "e-004", "e-005"],
               "Nombre": ["Leche", "Azucar", "Arroz", "Tomates", "Huevos"],
               "Precio": ["4,40", "4,50", "3,80", "3,60", "6,20"]}
print(diccionario)
for key in diccionario:
    print(key, " : ", diccionario[key])

respuesta = "s"
costo = 0
continuar = True
while respuesta == "s":

    print("-----------------------------------------------------")
    codigo = input("Ingresa el codigo del producto: ")
    cantidad = float(input("Ingresa la cantidad de productos: "))
    continuar = input("¿Quieres añadir mas productos a la lista (si/no)?: ")

    if codigo == "e-001":
        nombre = "Leche"
        precio = 4.40
    elif codigo == "e-002":
        nombre = "Azucar"
        precio = 4.50
    elif codigo == "e-003":
        nombre = "Arroz"
        precio = 3.80
    elif codigo == "e-004":
        nombre = "Tomates"
        precio = 3.60
    elif codigo == "e-005":
        nombre = "Huevos"
        precio = 6.20

    print("-----------------------------------------------------")
    print("Lista de compras:")
    total = precio * cantidad
    print(codigo, '\t', nombre, '\t', precio, '\t', cantidad, '\t', total)
    costo += total
    tupla = [str(codigo),  " ", str(cantidad), " ", str(precio), " ", str(total)]
    cadenavalores = "".join(tupla)
    f = open("demofile.txt", "a")
    f.write("\n" + cadenavalores)
    f.close()

f= open("demofile.txt")
print(f.read())
f.close()
print("El monto total de la venta es :" , total)
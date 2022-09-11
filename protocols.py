condicion = 's'
print("Bienvenid@ al creador de protocolos :)")

protocolo = []

contPasos = 0

while condicion == 's':
    print("¿Qué deseas hacer con tu protocolo?")
    print("1.- Agregar paso")
    print("2.- Borrar el último paso")
    print("3.- Modificar paso")
    print("4.- Imprimir el protocolo")
    print("5.- Guardar protocolo en archivo de texto")
    opcion = int(input("Ingresa el número de opción: "))

    if opcion == 1:
        index = int(input("¿Qué número de paso es?: "))
        cadena = str(input("Escribe el paso que deseas agregar: "))
        i = str(index)
        final =  i + "- " + cadena
        contPasos = contPasos + 1
        protocolo.append(final)
        ultimoPaso = index
        print("Paso añadido")
    elif opcion == 2:
        i = ultimoPaso
        del protocolo[i-1]
        print("Se ha eliminado el último paso")
    elif opcion == 3:
        index = int(input("Ingresa el número de paso que deseas modificar: "))
        cadena = input("Escribe el nuevo paso: ")
        i = str(index)
        final = i + "- " + cadena
        i2 = index - 1
        del protocolo[i2]
        protocolo.insert(i2, final)
        print("Paso modificado")
    elif opcion == 4:
        longitud = len(protocolo)
        for i in range(longitud):
            print(protocolo[i] + "\n")
    elif opcion == 5:
        archivo = open("MiProtocolo.txt", "w")
        archivo.close
        longitud = len(protocolo)
        for i in range(longitud):
            archivo = open("MiProtocolo.txt", "a")
            archivo.write(protocolo[i])
            archivo.write("\n")
        print("Protocolo guardado en archivo: MiProtocolo.txt")
        archivo.close
    else:
        print("Opción no válida")

    condicion = input("Si desea continuar usando el programa, ingrese 's', si no, ingrese cualquier otro caracter: ")

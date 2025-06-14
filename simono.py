#promedio notas
sw = 1
listanotas = []

print("Presione 1 para ingresar sus notas")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opcion "))
if(op == 1):
    while sw==1:
        try:
            print("----------------------------------------------------------")
            nota=float(input("Incorpore su nota, si desea salir, presione 0: "))
            if(nota != 0):
                listanotas.append(nota)
                print(f"Sus notas cargadas son: {listanotas}")
                print(f"Cantidad de notas cargadas: {len(listanotas)}")
                print(f"Su promedio de notas es: {sum(listanotas)/len(listanotas)}")
            else:
                print("Adiós")
                sw=0
        except:
            print("Ingreso Erróneo")
else:
    print("Adios")
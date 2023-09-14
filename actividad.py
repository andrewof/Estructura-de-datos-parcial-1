class Lista:
    def __init__(self):
        self.lista = []

    def verificar_datos(self):
        return len(self.lista) > 0

    def ingresar_dato(self, dato):
        self.lista.append(dato)

    def consultar_dato(self, indice):
        if indice < len(self.lista):
            return self.lista[indice]
        else:
            return None

    def eliminar_dato(self, indice):
        if indice < len(self.lista):
            self.lista.pop(indice)

    def mostrar_lista(self):
        print(self.lista)


def menu():
    lista = Lista()
    while True:
        print("""\n
                 --Menú de opciones--
              1. Verificar si la lista tiene datos
              2. Ingresar un nuevo dato a la lista
              3. Consultar un dato en la lista
              4. Eliminar un dato de la lista
              5. Mostrar por pantalla la lista ingresada
              6. Salir
              """)

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            if lista.verificar_datos():
                print("La lista tiene datos")
            else:
                print("La lista no tiene datos")
        elif opcion == 2:
            dato = input("Ingrese el dato a ingresar: ")
            lista.ingresar_dato(dato)
        elif opcion == 3:
            indice = int(input("Ingrese el índice del dato a consultar: "))
            print(lista.consultar_dato(indice))
        elif opcion == 4:
            indice = int(input("Ingrese el índice del dato a eliminar: "))
            lista.eliminar_dato(indice)
        elif opcion == 5:
            lista.mostrar_lista()
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")


menu()
class Billetera():
    def __init__(self):
        self.consignaciones = []
        
    def billetera_vacia(self):
        if len(self.consignaciones) == 0:
            return True
        else:
            return False
        
    def consignar(self, consignar):
        self.consignaciones.append(consignar)
        
    def pagar(self):
        if self.billetera_vacia():
            print('\nNo hay valores para realizar un pago')
        else:
            self.consignaciones.pop()
            print('\n¡PAGO REALIZADO!')
        
    def consultar_billetera(self):
        if self.billetera_vacia():
            print('\nLa billetera no tiene valores')
        else:
            print('\nVALORES EN LA BILLETERA')
            new_list = list(reversed(self.consignaciones))
            print(new_list)
            
obj = Billetera()

while True:
    print("""\n
          1. Consignar
          2. Pagar
          3. Consultar billetera
          4. Salir
          """)
    opcion = int(input('Digite la opción: '))
    
    if opcion == 1:
        cantidad = int(input('\nDigite la cantidad de valores: '))
        print()
        for i in range(cantidad):
            valor = input(f'Digite el valor {i+1}: ')
            obj.consignar(valor)
    elif opcion == 2:
        obj.pagar()
    elif opcion == 3:
        obj.consultar_billetera()
    elif opcion == 4:
        print('\nPrograma finalizado')
        break
    else:
        print('\nOpción inválida')
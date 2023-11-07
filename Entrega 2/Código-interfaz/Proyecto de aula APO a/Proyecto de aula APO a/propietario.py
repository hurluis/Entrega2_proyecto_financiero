class propietario:
    def __init__(self):
        self.usuario : str = "f834ur834u9843uj"
        self.saldo : int = 0
        
    def curriculum(self,perfiles):
        if input("Desea saber el curriulum de todos sus clientes? s/n\n") == "s":
            for i in perfiles:
                print(i)
    def recarga(self):
        incremento = int(input("Cuanto desea recargar en su saldo"))
        self.saldo += incremento
    def notificacion(self, lista:list,)-> bool:
        if len(lista) > 0:
            print("Tiene nuevos aspitrantes a prestamos")
            for i in lista:
                print(i)
                elecccion = input("Desea conceder el prestamo? s/n\n")
                if elecccion == "s":
                    lista.remove(i)
                    return True                
                else:
                    lista.remove(i)                    
                    return False
    
   
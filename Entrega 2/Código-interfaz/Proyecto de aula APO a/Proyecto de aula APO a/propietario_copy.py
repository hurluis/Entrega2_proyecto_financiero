from Excepciones import ExcepcionNoD
import json

class propietario:
    def __init__(self):
        self.usuario : str = "f834ur834u9843uj"
        self.saldo : int = 10000000000 
        #Tiene un saldo inicial de 10 mil millones, la idea es que vaya mermando conforme se vayan haciendo 
        #prestamos y asi mismo que cuando ya no le quede suficiente saldo para prestar, que no le permita hacre mas prestamos
        #para esto debemos hacer que nunca quede en negativo el saldo y crear mas propietarios, para darle opcion al cliente de 
        #cambiar de prestamista(propietario) y seguir prestando pero con un nuevo propietario.
        
    @staticmethod
    def curriculum ():
        listo = False
        while not listo:
            elecccion = input("Desea saber el curriulum de todos sus clientes? s/n\n")
            if elecccion == "s":
                with open('clientes.json', 'r') as archivo:
                    datos = json.load(archivo)
                    print(json.dumps(datos, indent=4))
                    listo = True
            elif elecccion == "n":            
                listo=True                
            else:
                print("Error: Debe ingresar una de las dos opciones que se muestran en pantalla: s - n")


    def saldo_act(self, cantidad):
        saldo_actual = self.saldo - cantidad
        return saldo_actual

                
    def recarga(self):
        incremento = int(input("Cuanto desea recargar en su saldo"))
        self.saldo += incremento


    def notificacion(self, lista:list)-> bool:
        if len(lista) > 0:
            print("Tiene nuevos aspitrantes a prestamos")
            for i in lista:
                print(i)
                listo = False
                while not listo:
                    elecccion = input("Desea conceder el prestamo? s/n\n")
                    #agregue saldo_actual
                    saldo_actual = self.saldo
                    if elecccion == "s":
                        lista.remove(i)
                        #agregue el if saldo_actual < persona1.monto.......
                        
                        try:
                            if saldo_actual < i.monto or saldo_actual == 0:
                                raise ExcepcionNoD(saldo_actual, i.monto)                                
                                #Lo que esta debajo va si o si
                                listo= True
                                return False
                        except ExcepcionNoD as ERR:
                            print("Usted no tiene suficiente saldo para conceder el prestamo")
                            print(f"Su saldo actual es de {ERR.saldo_actual}")
                            
                        else:
                            print("Usted tiene suficienta saldo para conceder este prestamo")
                            return True               
                    elif elecccion == "n":
                            lista.remove(i)     
                            listo= True               
                            return False
                    else:
                            print("Error: Debe ingresar una de las dos opciones que se muestran en pantalla: s - n")
                            
                        
#PROBAR EL METODO notificacion EN LA PARTE DEL WHILE NOT LISTO, EN EL PRIMER IF Y SUS DEMAS CONDICIONALES

    
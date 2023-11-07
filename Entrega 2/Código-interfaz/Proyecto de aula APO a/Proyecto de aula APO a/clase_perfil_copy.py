import json

class perfil:
    def __init__(self, nombre, profesion, edad):
        self.nombre: str = nombre
        self.profesion: str = profesion
        self.edad: int = edad
        self.cantidad: int = 0
        self.saldo_pagado: int = 0
        self.cuotas: int = 0
        self.cuotainicial: int = 0
        self.mora: int = 0               
    
    def cuota_inicial(self, tipo_prestamo, cant_cuotas):
        self.cuotas += 1
        resultado = self.cantidad * 0.3
        if tipo_prestamo == 1:
            resultado += self.cantidad*0.05
            self.cuotainicial= resultado
            print( "El total de tu cuota inicial es:", resultado)
            capital= float(input("ingrese la cantidad de capital que va a depositar\n"))
            self.saldo_pagado += capital

        else:
            resultado += self.cantidad * 0.03
            self.cuotainicial= resultado
            print( "El total de tu cuota inicial es:", resultado)
            capital= float(input("ingrese la cantidad de capital que va a depositar\n"))
            self.saldo_pagado += capital

    
    def cuota_corriente(self, cant_cuotas, tipo_prestamo, capital: int)-> int:
        self.saldo_pagado += capital
        self.cuotas += 1
        resultado = self.cantidad - self.cuotainicial
        resultado = resultado / cant_cuotas
        if tipo_prestamo == 1:
            resultado += self.cantidad * 0.05 + self.mora
            print( "El total de tu cuota es:", resultado)

            
        else:
            resultado += self.cantidad * 0.03 + self.mora
            print( "El total de tu cuota es:", resultado)
    def __str__(self):        
        return f"nombre: {self.nombre}, profesion:{self.profesion}, edad:{self.edad}, cantidad: {self.cantidad}, su saldo pagado es:{self.saldo_pagado}, el # de cuotas es:{self.cuotas}, su mora acumulada es: {self.mora}, la fecha de su ultima cuota pagada es: {self.fecha_ultimacuota} "

    @staticmethod
    def todict(Perfil:'perfil', usuario)-> dict:
        if isinstance(Perfil, perfil):
            diccionario= {                                  
                    "Nombre": Perfil.nombre,
                    "Profesion": Perfil.profesion,
                    "Edad": Perfil.edad,
                    "Cantidad": Perfil.cantidad,
                    "Saldo pagado": Perfil.saldo_pagado,
                    "Cuotas": Perfil.cuotas,
                    "Cuota inicial": Perfil.cuotainicial,
                    "Mora": Perfil.mora
                    }                        
            return diccionario
        else:
            pass
    @staticmethod
    def guardar_en_json(Perfil: 'perfil', usuario):
        nuevo_datos = Perfil.todict(Perfil, usuario)
        try:
            with open('clientes.json', 'r') as archivo:
                datos_existentes = json.load(archivo)
        except json.decoder.JSONDecodeError:
            datos_existentes = {}
        datos_existentes[usuario] = nuevo_datos        
        with open ('clientes.json', 'w') as archivo:
            json.dump(datos_existentes, archivo)

                     


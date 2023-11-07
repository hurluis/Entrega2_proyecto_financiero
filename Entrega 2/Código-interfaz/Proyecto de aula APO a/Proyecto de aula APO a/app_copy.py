from nuevo_usuario_copy import nuevo_usuario
from clase_perfil_copy import perfil
from propietario_copy import propietario
from Excepciones import mora
import json


def intereses_mora(perfil):    
    perfil.mora += 0.01    
    print("usted ha pagado menos de lo acordado, se han subito los intereses un 0.01% ")  

def prestamo_finalizado(perfil):
    if perfil.cantidad == perfil.saldo_pagado:
        print("usted ya ha pagado el total de su deuda ")
    
              

     
clientes= []
ofreciminetos = []
    
    
    
print("""
██████  ██ ███████ ███    ██ ██    ██ ███████ ███    ██ ██ ██████   ██████       █████      ██ ███    ██ ██    ██ ███████ ██████  ███████ ██  ██████  ███    ██ ███████ ███████     ███████ ██      
██   ██ ██ ██      ████   ██ ██    ██ ██      ████   ██ ██ ██   ██ ██    ██     ██   ██     ██ ████   ██ ██    ██ ██      ██   ██ ██      ██ ██    ██ ████   ██ ██      ██          ██      ██      
██████  ██ █████   ██ ██  ██ ██    ██ █████   ██ ██  ██ ██ ██   ██ ██    ██     ███████     ██ ██ ██  ██ ██    ██ █████   ██████  ███████ ██ ██    ██ ██ ██  ██ █████   ███████     ███████ ██      
██   ██ ██ ██      ██  ██ ██  ██  ██  ██      ██  ██ ██ ██ ██   ██ ██    ██     ██   ██     ██ ██  ██ ██  ██  ██  ██      ██   ██      ██ ██ ██    ██ ██  ██ ██ ██           ██          ██ ██      
██████  ██ ███████ ██   ████   ████   ███████ ██   ████ ██ ██████   ██████      ██   ██     ██ ██   ████   ████   ███████ ██   ██ ███████ ██  ██████  ██   ████ ███████ ███████     ███████ ███████ 
                                                                                                                                                                                                    
                                                                                                                                                                                                   
""")
fin = False
validacion = False
persona1 = nuevo_usuario()

while not fin:
        numeroopcion= int(input ("Ingrese 1 si es propietario, Ingrese 2 si es un cliente\n"))
        if numeroopcion == 1:
            jefe = propietario()
            persona = input("ingrese nombre de usuario\n")
            if persona == "f834ur834u9843ujo":
                validacion =jefe.notificacion(ofreciminetos)
                if validacion:
                    cliente1= perfil(persona1.nombre, persona1.profesion, persona1.edad )
                    cliente1.cantidad = persona1.monto
                    cliente1.todict(cliente1, persona)
                    cliente1.guardar_en_json(cliente1, usuario)                    
                    jefe.saldo_act
                jefe.curriculum()
                #Arreglar el metodo recarga como los demas, con las condicionales(por eso dice que
                #ingrese una opc"ion valida; ingrese 1 si es propietario....")
                if input("Desea recarcar efectivo en su cuenta s/n?") == "s":
                    jefe.recarga()                
            else:
                print("Nombre invalido")

        elif numeroopcion== 2: 
            persona = input("ingrese nombre de usuario\n")             
            opciones= input("presione '1' si desesa un prestamo,presione '2' si desea realizar el pago de una cuota \n")
            if opciones != "1" and opciones != "2":
                print("ingrese numero valido ")
            if opciones == "1":
                try:
                    with open('clientes.json', 'r') as archivo:
                        lectura = json.load(archivo)
                except json.decoder.JSONDecodeError:
                    lectura = {}
                if persona in lectura.keys() and validacion :
                    print("Usted ya tiene un prestamo vigente")
                elif persona in lectura.keys() and not validacion:
                      print("Su prestamo esta en revision")
                else:
                    prestamo_valido = False
                    while not prestamo_valido:
                        cantidad = int(input("cuanta cantidad desea realizar\n"))
                        if cantidad <= 4000000:
                            print("Debe realizar prestamos por encima de 4 millones")
                        else:
                            prestamo_valido = True                    
                    usuario= persona                    
                    persona1 = nuevo_usuario()
                    persona1.monto = cantidad
                    persona1.informacion()                
                    ofreciminetos.append(persona1)
                    print("Su informacion ha sido enviada")                                    
                    persona1.cantidad = cantidad
                    if cantidad >= 4000000 and cantidad <= 55000000:
                        tipo_prestamo = 1                
                    else:
                        tipo_prestamo = 2                
                    
                    print("su prestamo esta en revision")
                            
                                                                    
            elif opciones == "2":
                try:
                    with open('clientes.json', 'r') as archivo:
                        lectura = json.load(archivo)
                except json.decoder.JSONDecodeError:
                    lectura = {}
                    
                if persona not in lectura.keys():
                    print("Usted es un usuario nuevo, no tiene prestamos vijentes")
                    validacion = False
                    prestamo_valido = False
                    while not prestamo_valido:
                        cantidad = int(input("cuanta cantidad desea realizar\n"))
                        if cantidad <= 4000000:
                            print("Debe realizar prestamos por encima de 4 millones")
                        else:
                            prestamo_valido = True
                    clientes.append(persona)                
                    ofreciminetos.append(persona1)
                    persona1.informacion()
                    print("Su informacion ha sido enviada")
                    
                elif validacion:
                    print("su prestamo ha sido validado")
                    try:
                        with open('clientes.json', 'r') as archivo:
                            lectura = json.load(archivo)
                    except json.decoder.JSONDecodeError:
                        lectura = {}
                        cliente1= perfil(lectura[persona]["Nombre"],lectura[persona]["Profesion"],lectura[persona]["Edad"] )
                        cliente1.cantidad= lectura[persona]["Cantidad"]                    
                    if cliente1.cantidad == 0:
                        print("usted no tiene prestamos vijentes")
                    else:
                        if cliente1.cuotas == 0:                        
                            cant_cuotas = int(input("A cuantas cuotas desea pagar su prestamo?\n"))                        
                            print("Debe de realizar el pago de la cuota inicial")
                            print("recuerde que la cuota inicial debe ser el 30% del prestamo mas los intereses")
                            cliente1.cuota_inicial(tipo_prestamo, cant_cuotas)
                            cliente1.todict(cliente1, persona)
                            cliente1.guardar_en_json(cliente1, usuario)                             
                        else:
                            try:
                                capital= float(input("ingrese la cantidad de capital que va a depositar\n"))
                                if cliente1.cuota_corriente(cant_cuotas, tipo_prestamo, capital) > capital:
                                    raise mora(capital, jefe.saldo)
                            except mora:                                                                    
                                intereses_mora(cliente1)
                                cliente1.todict(cliente1, persona)
                                cliente1.guardar_en_json(cliente1, usuario)
                            else:
                                prestamo_finalizado(cliente1)
                                cliente1.todict(cliente1, persona)
                                cliente1.guardar_en_json(cliente1, usuario)                                                    
            
                elif not validacion:
                    print("su prestamo esta en revision")

        else:
            print("Ingrese una opcion valida")
            continue


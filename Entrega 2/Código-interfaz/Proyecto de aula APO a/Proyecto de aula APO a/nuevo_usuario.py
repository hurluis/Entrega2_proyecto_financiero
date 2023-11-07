# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 19:40:16 2023

@author: User

"""
import datetime
from dataclasses import dataclass
class nuevo_usuario:
        nombre: str = ""
        profesion: str = ""
        edad: int = 0
        monto: int = 0
        
        def informacion(self):        
            nombre = input("cual es su nombre completo\n")
            self.nombre = nombre        
            edad = input("Cual es su edad\n")
            self.edad = edad        
            opciones2 = input("presione '1' si es estudiante, presione '2' si ejerce un puesto de trabajo, presione '3' si es independiente, presione '4' si no actualmente esta desempleado\n")
            if opciones2 == "2":
                profesion = input("mencione cual es el puesto de trabajo y el nombre de la empresa\n")
                self.profesion = profesion
            elif opciones2 == "3":
                profesion = "independiente"
                self.profesion = profesion
            elif opciones2 == "4":
                profesion= "desempleado"  
                self.profesion = profesion
            elif opciones2 == "1":
                profesion = input("presione '1' si es estudiante de secundaria, presione '2' si es estudiente de educaion superior\n")
                self.profesion = profesion
                if profesion == "1":
                    profesion = "estudiante de secundaria"
                    self.profesion = profesion
                elif profesion == "2":
                    profesion = "estudiante de educacion superior"
                    self.profesion = profesion
        def __str__(self):
            return f"nombre: {self.nombre}, profesion:{self.profesion}, edad:{self.edad}, monto solicitado: {self.monto}"
                   



    

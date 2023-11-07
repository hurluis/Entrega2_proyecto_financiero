from nuevo_usuario import nuevo_usuario
from clase_perfil_copy import perfil
from propietario import propietario
from dataclasses import dataclass 

#La excepcion sera sobre el dinero del prestamista, cuando no tiene mas dinero no podra prestar mas

class ExcepcionNoD(Exception):
    def __init__(self, parametro1, parametro2):
        self.saldo_actual: int  = parametro1
        self.monto_solicitado: int = parametro2
@dataclass
class mora (Exception):
    cantidad: int
    saldo: int 



        
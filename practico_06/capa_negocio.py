# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass
class LongitudInvalida(Exception):
    pass

class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        return self.datos.buscar(id_socio)
       

    def buscar_dni(self, dni_socio):
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
        return self.datos.todos()
    

    
    def alta(self, socio):
        if self.regla_1(socio):
            if self.regla_2(socio):
                if self.regla_3(socio):
                    self.datos.alta(socio)
                    return True
        return False
       
       #     return True
        #else return False

    def baja(self, id_socio):
        self.datos.baja(id_socio)

    def modificacion(self, socio):
        if self.regla_2(socio):
            return self.datos.modificacion(socio)
        

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        if not self.datos.buscar_dni(socio.dni):
            return True
        else: 
            raise DniRepetido('El dni ya existe')
            return False


    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if len(socio.nombre) <= self.MAX_CARACTERES and len(socio.nombre) >= self.MIN_CARACTERES\
        and len(socio.apellido) <= self.MAX_CARACTERES and len(socio.apellido) >= self.MIN_CARACTERES:
            return True
        else:
            raise LongitudInvalida('Longitud invalida de nombre y/o apellido')
            return False

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if len(self.datos.todos()) >= MAX_SOCIOS:
            raise MaximoAlcanzado('Se ha alcanzado el maximo de socios permitidos')
            return False
        else:
            return True
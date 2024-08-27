# MIT License
#
# Copyright (c) 2024 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#Modulo de la clase Clinica con sus atributos y respectivos metodos.

class Clinica:
    """
    Clase que representa una clínica en el sistema de gestión.

    Atributos:
    ----------
    __razon_social : str
        Razón social de la clínica.
    __lista_pacientes : list
        Lista de pacientes registrados en la clínica.
    __lista_turnos : list
        Lista de turnos programados en la clínica.
    __especialidades : list
        Lista de especialidades médicas disponibles en la clínica.
    __obras_validas : list
        Lista de obras sociales válidas en la clínica.
    __recaudacion : float
        Monto total de la recaudación de la clínica.
    __hay_pacientes_sin_atencion : bool
        Indica si hay pacientes sin atención médica en la clínica.

    Métodos:
    --------
    __init__(self, razon_social, lista_pacientes, lista_turnos,
             especialidades, obras_validas, recaudacion, 
             hay_pacientes_sin_atencion) -> None:
        Inicializa un nuevo objeto de la clase Clinica.

    get_hay_pacientes_sin_atencion(self) -> bool:
        Retorna si hay pacientes sin atención médica en la clínica.

    get_recaudacion(self) -> float:
        Retorna el monto total de la recaudación de la clínica.

    get_razon_social(self) -> str:
        Retorna la razón social de la clínica.

    set_listaturnos(self, lista: list) -> None:
        Actualiza la lista de turnos programados en la clínica.

    set_recaudacion(self, nueva_recaudacion: float) -> None:
        Actualiza el monto total de la recaudación de la clínica.

    set_hay_pacientes_sin_atencion(self, hay_pacientes: bool) -> None:
        Actualiza el estado de si hay pacientes sin atención médica en la clínica.
    """
    
    def __init__(self, razon_social, lista_pacientes, lista_turnos,
                 especialidades, obras_validas, recaudacion, 
                 hay_pacientes_sin_atencion) -> None:
        self.__razon_social = razon_social
        self.__lista_pacientes = lista_pacientes
        self.__lista_turnos = lista_turnos
        self.__especialidades = especialidades
        self.__obras_validas = obras_validas
        self.__recaudacion = recaudacion
        self.__hay_pacientes_sin_atencion = hay_pacientes_sin_atencion

    #Getters
    def get_hay_pacientes_sin_atencion(self):
        return self.__hay_pacientes_sin_atencion
    
    def get_recaudacion(self):
        return self.__recaudacion
    
    def get_razon_social(self):
        return self.__razon_social
    
    #Setters
    def set_listaturnos (self, lista):
        self.__lista_turnos = lista

    def set_recaudacion(self, nueva_recaudacion):
        self.__recaudacion = nueva_recaudacion

    def set_hay_pacientes_sin_atencion (self, hay_pacientes):
        self.__hay_pacientes_sin_atencion = hay_pacientes
    
    def sumar_recaudacion(self):
        '''
        Funcion que se encarga de sumar toda la recaudacion de los turnos ya pagados.
        No recibe nada y retorna un booleano confirmando el exito o no de la suma
        de la recaudacion.
        '''
        retorno = False
        total_recaudado = 0

        if self.__lista_turnos:
            turnos_pagados = list(filter(lambda turno: turno.get_estado_turno() == "Pagado", self.__lista_turnos))

            if turnos_pagados and not self.get_hay_pacientes_sin_atencion():
                for turno in turnos_pagados:
                    total_recaudado += turno.get_monto()
                
                self.set_recaudacion(total_recaudado)
                self.set_hay_pacientes_sin_atencion(False)
                retorno = True
            else:
                print("No hay turnos cobrados o no hay pacientes sin atención")
        else:
            print("La lista de turnos está vacía.")

        return retorno

    def cerrar_caja(self):
        '''
        Funcion que se encarga de cerrar la caja de la Clinica una vez que todos los turnos estén
        pagados y no haya pacientes sin atención.
        No recibe nada y retorna un booleano confirmando el exito o no del cierre de la caja.
        '''
        retorno = False

        if self.__lista_turnos:
            todos_pagados = True
            for turno in self.__lista_turnos:
                if turno.get_estado_turno() != "Pagado":
                    todos_pagados = False
                    break

            if todos_pagados and not self.get_hay_pacientes_sin_atencion():
                print(f"Razon social: {self.get_razon_social()}")
                print(f"La recaudacion total es de: ${self.get_recaudacion()}")
                self.set_recaudacion(0)
                retorno = True
            else:
                if not todos_pagados:
                    print("No se pagaron todos los turnos")
                if self.get_hay_pacientes_sin_atencion():
                    print("Aún hay pacientes por atender")
        else:
            print("La lista de turnos está vacía.")

        return retorno

    
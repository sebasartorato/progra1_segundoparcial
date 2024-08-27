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

#Modulo de la clase Turno con sus atributos y respectivos metodos.

import validaciones as val
import funciones_json as jsonfun
from paciente import Paciente
from collections import Counter


class Turno:
    """
    Clase que representa un turno en el sistema de gestión de la clínica.

    Atributos:
    ----------
    __id : int
        Identificador único del turno.
    __id_paciente : int
        Identificador único del paciente asociado al turno.
    __especialidad : str
        Especialidad médica para la cual se solicita el turno.
    __monto : float
        Monto a pagar por el turno.
    __estado_turno : str
        Estado actual del turno.

    Métodos:
    --------
    __init__(self, id, id_paciente, especialidad, monto, estado_turno) -> None:
        Inicializa un nuevo objeto de la clase Turno.

    get_id_turno(self) -> int:
        Retorna el ID del turno.

    get_id_paciente(self) -> int:
        Retorna el ID del paciente asociado al turno.

    get_especialidad(self) -> str:
        Retorna la especialidad médica del turno.

    get_monto(self) -> float:
        Retorna el monto a pagar por el turno.

    get_estado_turno(self) -> str:
        Retorna el estado actual del turno.

    set_estado_turno(self, estado_turno: str) -> None:
        Actualiza el estado del turno.
    """

    def __init__(self, id, id_paciente, especialidad, monto, estado_turno)-> None:
        self.__id = id
        self.__id_paciente = id_paciente
        self.__especialidad = especialidad
        self.__monto = monto
        self.__estado_turno = estado_turno

    #Getters
    def get_id_turno(self):
        return self.__id

    def get_id_paciente(self):
        return self.__id_paciente
    
    def get_especialidad(self):
        return self.__especialidad
    
    def get_monto(self):
        return self.__monto
    
    def get_estado_turno(self):
        return self.__estado_turno
    
    #Setters
    def set_estado_turno(self, estado_turno):
        self.__estado_turno = estado_turno
    
    def cargar_turno (self,id_turno, lista_pacientes, lista_turnos) -> bool:
        '''
        Funcion que se encarga de cargar un turno solicitando datos al paciente y verificando
        que este dentro de lo solicitado.
        Recibe el ID del turno, la lista de pacientes y la lista de turnos.
        Retorna un booleano en caso de tener exito la funcion siendo este True o False
        si es que no pudo cargarse o se canceló el alta.
        '''

        id_paciente = val.ingresar_entero("Ingrese el ID del paciente: ", "Dato invalido", 1, 10000000)

        if self.verificar_id_paciente(id_paciente, lista_pacientes):
            for paciente in lista_pacientes:
                if paciente.get_id_paciente() == id_paciente:

                    #Especialidad
                    especialidad = val.ingresar_especialidad("Ingrese especialidad:\n- Odontologia\n- Psicologia\n- Medico Clinico\n- Traumatologia:\nSu opcion: ",
                                                            "Error, no es una especialidad valida...")

                    #Extraigo los tipos de especialidades del JSON
                    lista_especialidades = jsonfun.extraer_especialidades()
                    
                    #Defino el monto prestablecido para aplicar el ajuste
                    monto = self.extraer_monto(especialidad, lista_especialidades)
                    
                    estado_turno = "Activo"

                    match (paciente.get_obra_social()):
                        case 'Swiss Medical':
                            if paciente.get_edad() >= 18 and paciente.get_edad() <= 60:
                                monto_nuevo = monto * 0.6 * 0.9
                                monto = monto_nuevo
                            else:
                                monto_nuevo = monto * 0.6
                                monto = monto_nuevo
                        case 'Apres':
                            if paciente.get_edad() >= 26 and paciente.get_edad() <= 59:
                                monto_nuevo = monto * 0.97 * 0.75 
                                monto = monto_nuevo
                            else:
                                monto_nuevo = monto * 0.75
                                monto = monto_nuevo
                        case 'Pami':
                            if paciente.get_edad() >= 80 and paciente.get_edad() <= 90:
                                monto_nuevo = monto * 0.97 * 0.4
                                monto = monto_nuevo
                            else:
                                monto_nuevo = monto * 0.4
                                monto = monto_nuevo
                        case 'Particular':
                            if paciente.get_edad() >= 40 and paciente.get_edad() <= 60:
                                monto_nuevo = monto * 1.15
                                monto = monto_nuevo
                            else:
                                monto_nuevo = monto * 1.05
                                monto = monto_nuevo
                    
                    print(f"Monto final con tarifa nueva: {monto}")
                    
                    turno_nuevo = Turno(id_turno, id_paciente, especialidad, monto, estado_turno)

                    confirma = val.confirmar_accion("¿Desea confirmar el alta (S/N): ","ERROR/Solo se acepta S/N. ¿Desea confirmar el alta (S/N): ")
                    if confirma:
                        lista_turnos.append(turno_nuevo)
                        return True
        else:
            print("No está ese ID del paciente. ")
            return False
        
    
    def extraer_monto (self, especialidad: str, lista_especialidades: list) -> int:
        for dict_especialidad in lista_especialidades:
            if dict_especialidad.get("nombre") == especialidad.lower():
                monto = dict_especialidad.get("monto")

        return monto
    
    def verificar_id_paciente (self, id_paciente: int, lista_pacientes: list):
        for paciente in lista_pacientes:
            if paciente.get_id_paciente() == id_paciente:
                print(f"ID del paciente encontrado.\nNombre: {paciente.get_nombre()} {paciente.get_apellido()}")
                return True
        
        return False

    @staticmethod
    def ordenar_turnos(lista_turnos: list, lista_pacientes: list) -> bool:
        '''
        Funcion que se encarga de ordenar los turnos segun deseado por usuario, por obra social ASC
        o por Monto DESC.
        Recibe la lista de turnos y de pacientes.
        Retorna un booleano True si es que pudo ordenarse la lista o False en caso contrario.
        '''
        # Primero pido opciones de tipo y forma y las valido
        retorno = False
        
        if lista_turnos:
            menu_orden = '''- Seleccione tipo de orden:
                1- Obra Social ASC
                2- Monto DESC
                Su opcion: '''

            opcion_orden = val.ingresar_entero(menu_orden, "Error, ingrese opciones validas", 1, 2)

            # Crear un diccionario de pacientes para acceso rápido
            pacientes_dict = {paciente.get_id_paciente(): paciente for paciente in lista_pacientes}

            # Defino cómo será la llave y el orden
            if opcion_orden == 1:
                llave = "obra_social"
                orden = "ascendente"
            else:
                llave = "monto"
                orden = "descendente"

            
            # Ordeno según orden y tipo
            if orden == "ascendente":
                for i in range(len(lista_turnos) - 1):
                    menor = i
                    for j in range(i + 1, len(lista_turnos)):
                        if llave == "obra_social":
                            obra_social_j = pacientes_dict[lista_turnos[j].get_id_paciente()].get_obra_social()
                            obra_social_menor = pacientes_dict[lista_turnos[menor].get_id_paciente()].get_obra_social()
                            if obra_social_j < obra_social_menor:
                                menor = j
                        elif llave == "monto" and lista_turnos[j].get_monto() < lista_turnos[menor].get_monto():
                            menor = j
                    lista_turnos[i], lista_turnos[menor] = lista_turnos[menor], lista_turnos[i]
            else:
                for i in range(len(lista_turnos) - 1):
                    mayor = i
                    for j in range(i + 1, len(lista_turnos)):
                        if llave == "obra_social":
                            obra_social_j = pacientes_dict[lista_turnos[j].get_id_paciente()].get_obra_social().capitalize()
                            obra_social_mayor = pacientes_dict[lista_turnos[mayor].get_id_paciente()].get_obra_social().capitalize()
                            if obra_social_j > obra_social_mayor:
                                mayor = j
                        elif llave == "monto" and lista_turnos[j].get_monto() > lista_turnos[mayor].get_monto():
                            mayor = j
                    lista_turnos[i], lista_turnos[mayor] = lista_turnos[mayor], lista_turnos[i]

            if Turno.imprimir_orden_turnos (lista_turnos, pacientes_dict ,opcion_orden, orden, llave):
                retorno = True
        else:
            print("Lista de turnos vacia")

        return retorno

    @staticmethod
    def imprimir_orden_turnos (lista_turnos: list, pacientes_dict: dict, opcion_orden: int, orden: str, llave) -> bool:
        '''
        Funcion que se encarga de imprimir los turnos ordenados a elección del usuario.
        Recibe la lista de turnos, el diccionario con los pacientes, la opcion de orden, el tipo de orden y la llave
        (Obra social/Monto).
        Retorna un booleano indicando el exito o no de la impresión de los turnos.
        '''
        retorno = False
        print(f"Lista ordenada en forma {orden} por {llave}: ")

        if lista_turnos:
            for turno in lista_turnos:
                if opcion_orden == 1:
                    print(f"Turno n°: {turno.get_id_turno()} | Obra S: {pacientes_dict[turno.get_id_paciente()].get_obra_social()} | " 
                        f"{pacientes_dict[turno.get_id_paciente()].get_nombre()} {pacientes_dict[turno.get_id_paciente()].get_apellido()} | "
                        f"Especialidad: {turno.get_especialidad()} | Estado: {turno.get_estado_turno()}") 
                    retorno = True
                else:
                    print(f"Turno n°: {turno.get_id_turno()} | "
                          f"{pacientes_dict[turno.get_id_paciente()].get_nombre()} {pacientes_dict[turno.get_id_paciente()].get_apellido()} | "
                          f"Monto: $ {turno.get_monto()} | Estado: {turno.get_estado_turno()}")
                    retorno = True
        else:
            print("Lista de turnos vacia")
        
        return retorno

    @staticmethod
    def mostrar_turnos_activos (lista_turnos: list, lista_pacientes: list)->bool:
        '''
        Funcion que se encarga de mostrar los turnos activos actualmente.
        Recibe la lista de turnos y la lista de pacientes.
        Retorna un booleano indicando si se pudo mostrar la lista de turnos o no.
        '''
        retorno = False

        if lista_turnos:
            turnos_activos = list(filter(lambda turno: turno.get_estado_turno() == "Activo", lista_turnos))

            if turnos_activos:

                pacientes_dict = {paciente.get_id_paciente(): paciente for paciente in lista_pacientes}

                pacientes_activos = map(lambda turno: pacientes_dict.get(turno.get_id_paciente()), turnos_activos)

                #Utilizo zip para iterar en simultaneo ambas variables
                for paciente, turno in zip(pacientes_activos, turnos_activos):
                    if paciente:
                        print(f"ID Paciente: {paciente.get_id_paciente()} - {paciente.get_nombre()} - {paciente.get_apellido()} - {turno.get_especialidad()}")
            
                retorno = True
            else:
                print("No hay pacientes con turno activo.")
        else:
            print("La lista de turnos está vacía.")

        return retorno
    
    @staticmethod
    def atender_pacientes (lista_turnos: list)->bool:
        '''
        Funcion que se encarga de cambiar el estado a Activo seleccionando los primeros dos turnos.
        Recibe la lista de turnos.
        Retorna un booleano indicando si se pudo atender o no a el/los paciente/s.
        '''
        retorno = False

        if lista_turnos:
            turnos_activos = list(filter(lambda turno: turno.get_estado_turno() == "Activo", lista_turnos))

            # Selecciono los primeros dos turnos activos
            turnos_a_atender = turnos_activos[:2]
            
            if turnos_a_atender:
                for turno in turnos_a_atender:
                    for turno_2 in lista_turnos:
                        if turno_2.get_id_turno() == turno.get_id_turno():
                            turno_2.set_estado_turno("Finalizado")
                
                print(f"Se han atendido {len(turnos_a_atender)} pacientes.")
                retorno = True
            else:
                print("No hay pacientes en espera para ser atendidos.")
        else:
            print("La lista de turnos está vacía.")

        return retorno
    
    @staticmethod
    def cobrar_atenciones(lista_turnos: list)->bool:
        '''
        Funcion que se encargará de cobrar las atenciones a los pacientes que tengan el turno en Finalizado.
        Recibe la lista de los turnos.
        Retorna un booleano indicando si se pudo cobrar los turnos correspondientes.
        '''
        
        retorno = False

        if lista_turnos:
            for turno in lista_turnos:
                if turno.get_estado_turno() == "Finalizado" and turno.get_estado_turno() != "Pagado":
                    turno.set_estado_turno("Pagado") 
                    print(f"Turno {turno.get_id_turno()} cobrado por ${turno.get_monto()}")
            
            retorno = True
        else:
            print("La lista de turnos está vacía.")

        return retorno
    
    @staticmethod
    def calcular_max_especialidad (lista_turnos: list)->bool:
        '''
        Funcion que se encarga de calcular la o las maximas especialides pedidas.
        Se utiliza la librería Counter para crear un diccionario y así calcular el número máximo
        de repeticiones primero y luego ver cuales son las que se repiten esa cantidad de veces. 
        Recibe la lista de turnos.
        Retorna un booleano indicando si se pudo calcular e imprimir las esp. más pedidas.
        '''
        retorno = False

        lista_especialidades = []
        lista_mas_pedidas = []
        
        if lista_turnos:
            turnos_pagados = list(filter(lambda turno: turno.get_estado_turno() == "Pagado", lista_turnos))

            if turnos_pagados:
                for turno in turnos_pagados:
                    lista_especialidades.append(turno.get_especialidad())
                
                #Creo un counter a partir de la lista de especialidades
                dict_counter = Counter(lista_especialidades)

                #Busco el conteo maximo de repeticiones
                max_count = max(dict_counter.values())

                #Creo una lista con todas las especialidades (o la especialidad)
                for element, count in dict_counter.items():
                    if count == max_count:
                        lista_mas_pedidas.append(element)

                if lista_mas_pedidas:
                    print("Especialidad mas pedida:\n")
                    for especialidad in lista_mas_pedidas:
                        print(especialidad)
                else:
                    print("No se pudo ver cual era la mas buscada...")

                retorno = True
            else:
                print("Todavia no se pagaron todos los turnos")
        else:
            print("La lista de turnos está vacía.")


        return retorno
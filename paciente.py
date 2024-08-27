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

import validaciones as val

class Paciente:
    """
    Clase que representa un paciente en el sistema de gestión de la clínica.

    Atributos:
    ----------
    __id : int
        Identificador único del paciente.
    __data : dict
        Diccionario que almacena los datos del paciente.

    Métodos:
    --------
    __init__(self, id, diccionario) -> None:
        Inicializa un nuevo objeto de la clase Paciente.

    get_id_paciente(self) -> int:
        Retorna el identificador del paciente.

    get_nombre(self) -> str:
        Retorna el nombre del paciente.

    get_apellido(self) -> str:
        Retorna el apellido del paciente.

    get_dni(self) -> int:
        Retorna el DNI del paciente.

    get_edad(self) -> int:
        Retorna la edad del paciente.

    get_fecha_registro(self) -> str:
        Retorna la fecha de registro del paciente.

    get_obra_social(self) -> str:
        Retorna el nombre de la obra social del paciente, con la primera letra en mayúscula.

    set_id(self, id: int) -> None:
        Actualiza el identificador del paciente.
    """
    def __init__(self, id, diccionario):
        self.__id = id
        self.__data = diccionario  # Almacena los datos como un diccionario

    #Getters
    def get_id_paciente(self):
        return self.__id

    def get_nombre(self):
        return self.__data.get("nombre")

    def get_apellido(self):
        return self.__data.get("apellido")

    def get_dni(self):
        return self.__data.get("dni")

    def get_edad(self):
        return self.__data.get("edad")

    def get_fecha_registro(self):
        return self.__data.get("fecha_registro")

    def get_obra_social(self):
        return self.__data.get("obra_social").title()
    
    #Setters
    def set_id (self, id):
        self.__id = id

    def ingresar_paciente(self, id_auto_incremental_paciente, lista_pacientes):
        '''
        Funcion que se encarga de pedir los datos para instanciar una clase Paciente
        validando que cada dato ingresado esté dentro de lo solicitado.
        Recibe el ID auto incremental del paciente y la lista de pacientes.
        Si el DNI ingresado se repite, devuelve un booleano Falso y si no un True si se confirma
        la adición.
        '''
        
        retorno = False

        # Nombre y apellido
        nombre = val.ingresar_string_nombre("Ingrese un nombre: ", "ERROR/Reingrese un nombre: ")
        apellido = val.ingresar_string_nombre("Ingrese apellido: ", "ERROR/Reingrese apellido: ")

        # DNI
        dni = val.ingresar_entero("Ingrese su DNI: ", "Dato inválido", 7000000, 70000000)

        # Edad
        edad = val.ingresar_entero("Ingrese su Edad: ", "Dato inválido", 18, 90)

        # Fecha de registro
        fecha_registro = val.ingresar_fecha("Error, dato inválido")

        if edad >= 60:
            obra_social = "Pami"
            print(f"Obra social: {obra_social}")
        else:
            obra_social = val.ingresar_obrasocial("Ingrese la obra social (PAMI, Swiss Medical, Apres, Particular): ", 
                                                  "Error, obra social inválida.\n(Recuerde que si es usted menor de "
                                                  "60 NO puede elegir PAMI.. )\nIngrese nuevamente por favor.")
            obra_social = obra_social.capitalize()

        # Creo un diccionario con los datos del paciente nuevo
        datos_paciente = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "edad": edad,
            "fecha_registro": fecha_registro,
            "obra_social": obra_social
        }

        # Creo una instancia de Paciente con el diccionario de datos
        paciente_nuevo = Paciente(id_auto_incremental_paciente, datos_paciente)

        # Verificar si el paciente nuevo es válido (que no se repita el DNI) 
        # y agregarlo a la lista de pacientes
        if self.verificar_nuevo_paciente(paciente_nuevo, lista_pacientes):
            confirma = val.confirmar_accion("¿Desea confirmar el alta (S/N): ", "ERROR/Solo se acepta S/N. ¿Desea confirmar el alta (S/N): ")
            if confirma:
                lista_pacientes.append(paciente_nuevo)
                print("Paciente registrado.")
                print(f"ID al cargar: {paciente_nuevo.get_id_paciente()}")
                retorno = True

        return retorno


    def verificar_nuevo_paciente(self, nuevo_paciente, lista_pacientes):
        '''
        Funcion que se encarga de verificar si el DNI del paciente ingresado ya existe
        dentro del sistema.
        Recibe la lista de pacientes y al nuevo paciente a verificar.
        Retorna un booleano falso si es que el DNI ya está cargado o un True
        en caso contrario.
        '''
        dni_nuevo = nuevo_paciente.get_dni()  # Obtener el DNI del nuevo paciente
        
        for paciente in lista_pacientes:
            if int(paciente.get_dni()) == dni_nuevo:
                print(f"Ya existe un paciente con el DNI: {dni_nuevo}")
                return False
        
        return True
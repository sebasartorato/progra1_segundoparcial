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

def confirmar_accion(mensaje:str,mensaje_error:str)-> bool:
    '''
    Funcion que confirma la accion del usuario mediante un S o N (si o no).
    Recibe un mensaje si desea confirmar la accion y uno de error
    si la respuesta fue incorrecta.
    Retorna un booleano True si el dato es "si" o False si es "no".
    '''
    
    confirmar = input(mensaje)
    
    while confirmar != "S" and confirmar != "N":
        confirmar = input(mensaje_error)
    
    if confirmar == "S":
        retorno = True
    else:
        retorno = False
        
    return retorno

def ingresar_string_nombre(mensaje: str, mensaje_error: str) -> str:
    '''
    Funcion que se encarga de pedir el nombre del paciente validando que 
    no pase de 30 caracteres y que sea alfabético el dato.
    Parametros: un mensaje solicitando el nombre del paciente y un mensaje de error 
    por si es incorrecta la entrada.
    Retorno: devuelve el nombre del proyecto validado.
    '''
    
    while True:
        dato_ingresado = input(mensaje)
        if len(dato_ingresado) <= 30 and dato_ingresado.replace(" ", "").isalpha():
            return dato_ingresado
        
        print(mensaje_error)

def ingresar_entero(mensaje:str,mensaje_error:str,minimo:int,maximo:int)-> int:
    '''
    Funcion que se encarga de pedir un entero y validarlo con un try/except
    si está dentro de los minimo y maximo parametros recibidos.
    Parametros: un mensaje solicitando numeros, un mensaje de error por si es incorrecta la entrada,
    un maximo y un minimo numero.
    Retorno: devuelve el entero validado.
    '''

    while True:
        try: 
            dato_entero = int(input(mensaje))
            if dato_entero <= maximo and dato_entero >= minimo:
                break
            else:
                print(mensaje_error)
        except ValueError:
            print("Formato no válido... ")

    return dato_entero

def ingresar_fecha(mensaje_error)-> str:
    '''
    Funcion que solicita ingresar dia, mes y año de la fecha del turno
    y valida los formatos correctos de cada uno.
    Recibe el mensaje de error por si es incorrecta la entrada de cada uno.
    Retorna la fecha formateada a string.
    '''

    #dia
    while True:
        try: 
            dia = int(input("Ingrese el dia: "))
            if dia <= 31 and dia >= 1:
                break
            else:
                print(mensaje_error)
        except ValueError:
            print("Formato no válido... ")

    #mes
    while True:
        try: 
            mes = int(input("Ingrese el mes: "))
            if mes <= 12 and mes >= 1:
                break
            else:
                print(mensaje_error)
        except ValueError:
            print("Formato no válido... ")

    #año
    while True:
        try: 
            año = int(input("Ingrese el año (mayor o igual a 2023): "))
            if año <= 2100 and año >= 2023:
                break
            else:
                print(mensaje_error)
        except ValueError:
            print("Formato no válido... ")

    #Retorno la fecha (inicio o fin) en forma de string. 
    fecha = f'{dia}-{mes}-{año}'

    return fecha

def ingresar_obrasocial (mensaje: str,  mensaje_error: str) -> str:
    '''
    Funcion que se encarga de solicitar el ingreso de la obra social
    validando que esté dentro de los tipos solicitados.
    Ademas, no deja ingresar PAMI a los paciente ya que previamente al pedir la edad
    definirá si le corresponde o no.
    Recibe un mensaje solicitando el ingreso de la o. social y un mensaje de error
    por si la entrada es incorrecta.
    Retorna el nombre de la obra social verificado y capitalizado.
    '''

    while True:
        obra_social = input(mensaje)
        if (obra_social.lower() == 'swiss medical' or obra_social.lower() == 'apres' 
            or obra_social.lower() == 'particular'):
            return obra_social.capitalize()
        
        print(mensaje_error)

def ingresar_especialidad (mensaje: str,  mensaje_error: str) -> str:
    '''
    Funcion que se encarga de solicitar el ingreso de la especialidad
    validando que esté dentro de los tipos solicitados.
    Recibe un mensaje solicitando el ingreso y un mensaje de error
    por si la entrada es incorrecta.
    Retorna el nombre de la especialidad verificada y capitalizada.
    '''
    
    while True:
        especialidad = input(mensaje)
        if (especialidad.lower() == 'odontologia' or especialidad.lower() == 'medico clinico' 
            or especialidad.lower() == 'psicologia' or especialidad.lower() == 'traumatologia'):
            return especialidad.title()
        
        print(mensaje_error)

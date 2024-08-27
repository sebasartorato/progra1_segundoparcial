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

#Modulo donde se ejecutarán funciones del menú

import re
import library_utn as utn
import funciones_json as jsonfun
from clinica import Clinica
from paciente import Paciente
from turno import Turno


id_auto_incremental_turno = 0

#PACIENTE
def incrementar_id_paciente(id_auto_incremental_paciente):
    '''
    Incrementa el ID en uno cuando se la invoca.
    Recibe el ID auto-incremental del paciente 
    que parte desde el main.
    Retorna el ID aumentado en 1.
    '''
    return id_auto_incremental_paciente + 1
    
def decrementar_id_paciente(id_auto_incremental_paciente):
    '''
    Decrementa Incrementa el ID en uno cuando se la invoca.
    Recibe el ID auto-incremental del paciente 
    que parte desde el main.
    Retorna el ID decrementado en 1.
    '''
    return id_auto_incremental_paciente - 1

#TURNO
def incrementar_id_turno():
    '''
    Incrementa el ID del turno en uno cuando se la invoca.
    No recibe ni retorna nada.
    '''
    global id_auto_incremental_turno
    id_auto_incremental_turno +=1
    
def decrementar_id_turno():
    '''
    Decrementa el ID del turno en uno cuando se la invoca.
    No recibe ni retorna nada.
    '''
    global id_auto_incremental_turno
    id_auto_incremental_turno +=-1

def imprimir_menu ():
    '''
    Función que se encarga de imprimir el menú únicamente.
    No recibe ni retorna nada.
    '''
    print('''Bienvenido al menú:
          1. Alta paciente
          2. Alta turno
          3. Ordenar turnos
          4. Mostrar pacientes en espera
          5. Atender pacientes
          6. Cobrar atenciones
          7. Cerrar caja
          8. Mostrar informe:
           (Informar la especialidad más solicitada por los pacientes)
          9. Salir
          ''')

def main_app(clinica_utn, lista_pacientes, lista_turnos, id_auto_incremental_paciente):
    """
    Aplicacion principal del Segundo Parcial de Laboratorio 1
    Recibe una clase de tipo Clinica, la lista de pacientes y turnos y el id autoincremental
    correspondiente a los pacientes. No retorna nada.
    """
    global id_auto_incremental_turno
    
    while True:
        imprimir_menu()
        selected_option = None
        opcion_str = input(f'Ingrese su opcion: ')
        if re.match('^([1-9])$', opcion_str):
            selected_option = int(opcion_str)
        
        match selected_option:
            case 1: # Alta paciente
                id_auto_incremental_paciente = incrementar_id_paciente(id_auto_incremental_paciente)  # Incrementa el ID de paciente
                paciente_nuevo = Paciente(id_auto_incremental_paciente, {})

                if paciente_nuevo.ingresar_paciente(id_auto_incremental_paciente, lista_pacientes):
                    print("Se agregó el paciente.")
                else:
                    id_auto_incremental_paciente = decrementar_id_paciente(id_auto_incremental_paciente)  # Decrementa el ID si la operación falla
                    print("Operación cancelada")
            case 2:  # Alta turno
                incrementar_id_turno()
                turno_nuevo = Turno(id_auto_incremental_turno, 0, "", 0, "")
                if turno_nuevo.cargar_turno(id_auto_incremental_turno, lista_pacientes, lista_turnos):
                    print("Se agregó el turno.")
                    clinica_utn.set_hay_pacientes_sin_atencion(True)
                else:
                    decrementar_id_turno()
                    print("Operación cancelada")
            case 3: # Ordenar turnos
                if Turno.ordenar_turnos(lista_turnos, lista_pacientes):
                    print("Turnos ordenados.")
                else:
                    print("\nERROR! No pudo ordenarse/imprimirse.")
            case 4: # Mostrar pacientes en espera
                if Turno.mostrar_turnos_activos(lista_turnos, lista_pacientes):
                    print("Ejecutado con exito!")
                else:
                    print("Error. No se pudo ejecutar la muestra.")
            case 5: # Atender pacientes
                if Turno.atender_pacientes(lista_turnos):
                    print("Se pudieron atender.")
                    clinica_utn.set_hay_pacientes_sin_atencion(False)
                else:
                    print("Error. No se pudo atender pacientes...")
            case 6: # Cobrar atenciones
                if Turno.cobrar_atenciones(lista_turnos):
                    clinica_utn.set_listaturnos(lista_turnos)
                    if clinica_utn.sumar_recaudacion():
                        print("Recaudacion hecha.")
                    else:
                        print("No se pudo completar la recaudacion")
                else:
                    print("Error. No se pudo cobrar a los pacientes...")
            case 7: # Cerrar caja
                clinica_utn.set_listaturnos(lista_turnos)
                if clinica_utn.cerrar_caja():
                    print("Caja cerrada")
                    jsonfun.crear_json_turnos (lista_turnos)
                    jsonfun.crear_json_pacientes (lista_pacientes)
                    caja_cerrada = True
                else:
                    print("No se pudo cerrar la caja...")
                    caja_cerrada = False
            case 8: # Mostrar informe
                #Informar la especialidad más solicitada por los pacientes
                if Turno.calcular_max_especialidad(lista_turnos) and caja_cerrada:
                    print("Se pudo ejecutar!")
                else:
                    print("La caja no esta cerrada, por eso no se puede calcular especialidad mas pedida!")
                pass
            case 9: # Salir
                print("¡Fin del menú!")
                break
            case _:
                utn.UTN_messenger('Opción inválida. Por favor, seleccione una opción válida.', 'Error')
        utn.clear_console()
    
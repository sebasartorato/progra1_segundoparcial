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

#Modulo principal del programa.
import app as utn_app
import funciones_json as jsonfun
from clinica import Clinica

if __name__ == '__main__':
    #Arranco cargando pacientes (si hay) y el ID auto incremental.
    lista_pacientes, id_auto_incremental_paciente = jsonfun.cargar_pacientes_json ()
    
    #Arranco la lista de turnos vacía
    lista_turnos = []
    
    #Extraigo especialidades y obras sociales del JSON.
    especialidades = jsonfun.extraer_especialidades()
    obras_sociales = jsonfun.extraer_obras()

    #Instancia clinica_utn como clase Clinica.
    pacientes_sin_atencion = False
    clinica_utn = Clinica("UTN CLINICA S.A.", lista_pacientes, lista_turnos, especialidades, obras_sociales, 0, pacientes_sin_atencion)
    
    # Llamo al menu y ejecuto opciones segun desea el usuario
    utn_app.main_app(clinica_utn, lista_pacientes, lista_turnos, id_auto_incremental_paciente)


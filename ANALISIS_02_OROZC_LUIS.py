# -- coding: utf-8 --
"""
Created on Fri Sep 25 11:40:32 2020

@author: Luis Orozco
"""

import csv
lista_datos =[]

with open("synergy_logistics_database.csv","r") as archivo_csv:
    lector = csv.reader(archivo_csv) #Objeto que ayuda a leer
    
    for linea in lector:
        lista_datos.append(linea) #practicamente lector contiene la data del csv, se hace una copia y se va guardando 
                                  # línea por línea
        

#--------------------------Indagar en rutas-----------------------------------
direction = "Exports"
times = 0
rutas_contadas = [] #rutas que ya estan agregadas
conteo_rutas =[]

for ruta in lista_datos:
    if ruta[1]==direction:
        ruta_actual = [ruta[2],ruta[3]]
        
        if ruta_actual not in rutas_contadas:
            for movimiento in lista_datos:
                if ruta_actual == [movimiento[2], movimiento[3]]:
                    times+= 1
                    
            rutas_contadas.append(ruta_actual)
            #formato=[ruta[2],ruta[3],times]
            conteo_rutas.append([ruta[2],ruta[3],times])
            times = 0
            
conteo_rutas.sort(reverse = True, key = lambda x:x[2])
op1_1 = conteo_rutas #Rutas de exportaciones del mejor al peor

#Indagar rutas Importadas
direction = "Imports"
times = 0
rutas_contadasI = [] #rutas que ya estan agregadas
conteo_rutasI =[]

for ruta in lista_datos:
    if ruta[1]==direction:
        ruta_actual = [ruta[2],ruta[3]]
        
        if ruta_actual not in rutas_contadasI:
            for movimiento in lista_datos:
                if ruta_actual == [movimiento[2], movimiento[3]]:
                    times+= 1
                    
            rutas_contadasI.append(ruta_actual)
            #formato=[ruta[2],ruta[3],times]
            conteo_rutasI.append([ruta[2],ruta[3],times])
            times = 0
            
conteo_rutasI.sort(reverse = True, key = lambda x:x[2])
op1_2 = conteo_rutasI
conteo_rutasI = [] #Rutas Importaciones del mejor al peor

#-----------------Fin de indagar rutas----------------------------------------




#---------------------- Opción 2, rutas más demandadas------------------------
mode = "transport_mode"
times = 0
count_mode = []
counted_mode= []
suma = 0

for route in lista_datos:
    if route[7] != mode:
        actual = [route[7]]
        if actual not in counted_mode:
            for movimiento in lista_datos:
                if actual ==[movimiento[7]]:
                    times +=1
                    suma = suma + int(movimiento[9])
            counted_mode.append(actual)
            count_mode.append([route[7],times,suma])
            times = 0
            suma  = 0
     
count_mode.sort(reverse = True, key = lambda x:x[1])
op2 = count_mode
count_mode = []
#-----------------------------------------------------------------------------

#---------Opción 3 Valor de importaciones y exportaciones---------------------

direction = "Imports"
dir2 = "Exports"
times = 0
rutas_contadasI = [] #rutas que ya estan agregadas
conteo_rutasI =[]
suma = 0
suma_total = 0
op3 = []

for ruta in lista_datos:
    if ruta[1]==direction or ruta[1]==dir2:
        ruta_actual = [ruta[2],ruta[3]]
        
        if ruta_actual not in rutas_contadasI:
            for movimiento in lista_datos:
                if ruta_actual == [movimiento[2], movimiento[3]]:
                    times+= 1
                    suma = suma + int(movimiento[9])
                    exp = str(movimiento[1])
            suma_total = suma_total+suma#Obtener la suma total de valores
            rutas_contadasI.append(ruta_actual)
            conteo_rutasI.append([ruta[2],ruta[3],times,suma,exp])
            exp = ""
            suma = 0
            times = 0

            
conteo_rutasI.sort(reverse = True, key = lambda x:x[2])
op3 = conteo_rutasI

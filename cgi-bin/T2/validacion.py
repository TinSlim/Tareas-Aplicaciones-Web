#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

#var meses_31_dias = ["01","03","05","07","08","10","12"]
#var meses_30_dias = ["02","04","06","09","11"]

from db import DB
from datetime import datetime, date
import os
import filetype
from data_base import *


database = DB('localhost',USER_DB,PASS_DB,DB_DB)

f = open("./proxy.txt","a")

def check_form(formulario):
    # primero se revisa que estén los atributos:
    valores_correctos = []
    #----- Region
    if "region" in formulario.keys():
        resultado_region = valida_region(formulario['region'].value)
    else:
        resultado_region = (False,"El formulario no contiene región")
    
    #----- Comuna
    if "comuna" in formulario.keys():
        resultado_comuna = valida_comuna(formulario['comuna'].value,resultado_region)
    else:
        return (False, "El formulario no contiene comuna")
    #----- Sector
    if "sector" in formulario.keys():
        resultado_sector = valida_sector(formulario['sector'].value)
    else:
        resultado_sector = (True,"")
    #----- Nombre
    if "nombre" in formulario.keys():
        resultado_nombre = valida_nombre(formulario['nombre'].value)
    else:
        resultado_nombre = (False,"El formulario no contiene nombre")
    #----- Email
    if "email" in formulario.keys():
        resultado_email = valida_email(formulario['email'].value)
    else:
        resultado_email = (False,"El formulario no contiene email")
    #----- Celular
    if "celular" in formulario.keys():
        resultado_celular = valida_celular(formulario['celular'].value)
    else:
        resultado_celular = (True,"")
    
    

    #Ver avistamientos
    #------- Fecha
    cantidad_fechas = 0
    fecha_ok = True
    fechas_todas = []
    fecha_error = ""
    
    if "dia-hora-avistamiento" in formulario.keys():
        #f.write("medi2da" + "\n")
        #f.write(str(type(formulario['dia-hora-avistamiento'])) + "\n")
        #f.write(str(formulario['dia-hora-avistamiento']) + "\n")
        
        #f.write("medid2a" + "\n")
        if type(formulario['dia-hora-avistamiento']) is list:
            for fecha in formulario['dia-hora-avistamiento']:
                cantidad_fechas += 1
                fecha_actual = valida_fecha(fecha.value)
                fechas_todas.append(fecha_actual)
                fecha_ok = fecha_ok and fecha_actual[0]
            resultado_fecha = (fecha_ok,fechas_todas)
            if not fecha_ok:
                fecha_error = "Una fecha es inválida"
        else:
            cantidad_fechas = 1
            fecha_actual = valida_fecha(formulario['dia-hora-avistamiento'].value)
            fechas_todas.append(fecha_actual)
            fecha_ok = fecha_ok and fecha_actual[0]
            resultado_fecha = (fecha_ok,fechas_todas)
            if not fecha_ok:
                fecha_error = "Fecha es inválida"
    else:
        resultado_fecha = (False,[])
        fecha_error = "No se ingresaron fechas"
    
    
    #f.write(fechas_todas + "\n")   
    #------- Tipo
    cantidad_tipos = 0
    tipos_ok = True
    tipos_todos = []
    tipo_error = ""

    if 'tipo-avistamiento' in formulario.keys():
        if type(formulario['tipo-avistamiento']) is list:
            for tipo in formulario['tipo-avistamiento']:
                cantidad_tipos += 1
                tipo_actual = valida_tipo(tipo.value)
                tipos_todos.append(tipo_actual)
                tipos_ok = tipos_ok and tipo_actual[0]
            resultado_tipo = (tipos_ok,tipos_todos)
            if not tipos_ok:
                tipo_error = "Una fecha es inválida"
        else:
            cantidad_tipos = 1
            tipo_actual = valida_tipo(formulario['tipo-avistamiento'].value)
            tipos_todos.append(tipo_actual)
            tipos_ok = tipos_ok and tipo_actual[0]
            resultado_tipo = (tipos_ok,tipos_todos)
            if not tipos_ok:
                tipo_error = "Tipo inválida"
    else:
        resultado_tipo = (False,[])
        tipo_error = "El formulario no contiene tipos"
    

    # ----- fotos 
    imgs_ok = True
    images_paths = []
    
    


    #------- Estado

    cantidad_estados = 0
    estados_ok = True
    estados_todos = []
    estado_error = ""

    if 'estado-avistamiento' in formulario.keys():
        if type(formulario['estado-avistamiento']) is list:
            for estado in formulario['estado-avistamiento']:
                cantidad_estados += 1
                estado_actual = valida_estado(estado.value)
                estados_todos.append(estado_actual)
                #f.write("---" + str(estados_ok) + "\n")
                estados_ok = estados_ok and estado_actual[0]
            resultado_estado = (estados_ok,estados_todos)
            if not estados_ok:
                estado_error = "Algún estado es inválido"
        else:
            cantidad_estados = 1
            estado_actual = valida_estado(formulario['estado-avistamiento'].value)
            estados_todos.append(estado_actual)
            estados_ok = estados_ok and estado_actual[0]
            resultado_estado = (estados_ok,estados_todos)
            if not estados_ok:
                estado_error = "El estado es inválido"
    else:
        resultado_estado = (False,[])
        estado_error = "El formulario no contiene estados"

    
    resultados_unicos = [resultado_region, resultado_comuna, resultado_sector, resultado_nombre, resultado_email,resultado_celular]
    resultado_total = True
    errores = ""
    for resultado in resultados_unicos:
        f.write("CalcTotal" + str(resultado[0]) + "\n")
        if not resultado[0]:
            errores += "<li>" + resultado[1] + "</li>"
        resultado_total = resultado_total and resultado[0]
    
    #f.write("Tipo :"+ str(tipo_error)

    id_avistamiento = 0
    id_detalle = 0
    if (cantidad_fechas == cantidad_tipos == cantidad_estados) and (fecha_ok and tipos_ok and estados_ok) and resultado_total:
        # Todas las condiciones anteriores están OK
        fotos_paths_actuales = add_fotos(formulario)
        f.write(str(fotos_paths_actuales))
        if fotos_paths_actuales[0] and len(fotos_paths_actuales[1]) == cantidad_fechas:
            # Todo Ok, queda agregar las cosas
            #----- Avistamiento
            ahora = datetime.now()
            avistamiento_add = (resultado_comuna[1],ahora,resultado_sector[1],resultado_nombre[1],resultado_email[1],resultado_celular[1])
            id_avistamiento = database.save_avistamiento(avistamiento_add)
            i = cantidad_estados - 1
            while i >= 0:
                id_detalle = database.save_detalle_avistamiento((fechas_todas[i][1],tipos_todos[i][1],estados_todos[i][1],id_avistamiento))
                for foto in fotos_paths_actuales[1][i]:
                    database.save_foto((foto[0],foto[1],id_detalle))
                i = i - 1
        else:
            f.write("Final false \n")
            return False
    else:
        f.write("Final false \n")
        return False
    f.write("Final true \n")
    return True


    
        

    
    
        
    
    
    #-------- Fotos
    #contador_fotos = 0
    #if "foto-avistamiento" in formulario.keys():
    #    for foto in formulario['foto-avistamiento']:
    #        if contador_fotos = cantidad_avistamientos:
    #            return "eRROR"
    #        else:
    #            fileitem = foto
    #            if fileitem.filename:
    #                filenames = fileitem.filename
    #                hash_archivo = database.hash_name(filenames)
    #                open('media/'+hash_archivo,'wb').write(fileitem.file.read())
    #                size = os.fstat(fileitem.file.fileno()).st_size
    #                if size <= 50000:
    #                    tipo_real = filetype.guess('media/'+hash_archivo)
    #                    if ("image" or "gif" or "jpg") in str(tipo_real).lower() :
    #                        img_ok = True
    #                    else:
    #                        error = "Tipo de archivo no válido"
    #                        os.remove("media/"+hash_archivo)
    #                else:
    #                    error = "Archivo muy pesado"#

    
    
def valida_region(region):
    #f.write(str(region) + "\n")
    resultado = database.get_region_id(region)
    
    if resultado:
        return (True,resultado[0])
    else:
        return (False, "Región inválida")

def valida_comuna(comuna,region_id):
    resultado = database.get_comuna_info(comuna)
    if region_id[0]:
        if resultado:
            if resultado[1] != region_id[1]:
                return (False,"La comuna no corresponde a la region")
            else:
                return (True, resultado[0])
        else:
            return (False, "Comuna no está en la base de datos")
    else:
        if resultado:
            return (True, resultado[0])
        else:
            return (False, "Comuna no está en la base de datos")

def valida_sector(sector):
    regex = "^[A-zÜÑÁÉÍÓÚáéíóúüñ0-9]+(\s[A-zÜÑÁÉÍÓÚáéíóúüñ0-9]+)*"
    if (sector == ""):
        return (True,"")
    if (len(sector) > 200):
        return (False,"El largo del sector supera los 200 caracteres")
    x = re.search(regex,sector)
    if x.span()[1] == len(sector):
        return (True,sector)
    return (False, "Sector solo puede usar letras y números")

def valida_nombre(nombre):
    regex = "^(([A-ZÜÑÁÉÍÓÚ]+([a-záéíóúüñ]*))(\s[A-ZÜÑÁÉÍÓÚ]+([a-záéíóúüñ]*))*)"
    if (nombre == ""):
        return (False, "Se requiere un nombre")
    if (len(nombre) > 100):
        return (False, "El nombre no puede superar los 100 caracteres")
    x = re.search(regex,nombre)
    if not x:
        return (False, "No se cumple el formato de nombre")
    if x.span()[1] == len(nombre):
        return (True,nombre)
    return (False,"Nombre inválido")

def valida_email(email):
    regex = "^[^@]+@[^@]+\.[a-zA-Z]{2,}$"
    if (email == ""):
        return (False, "Email obligatorio")
    x = re.search(regex,email)
    if not x:
        return (False,"Email no cumple el formato")
    if x.span()[1] == len(email):
        return (True,email)
    return (False,"Email no cumple el formato")

def valida_celular(celular):
    regex = "^\+569\d{8}"
    if (celular == ""):
        return (True,celular)
    x = re.search(regex,celular)
    if not x:
        return (False,"Celular no cumple el formato")
    if x.span()[1] == len(celular):
        return (True,celular)
    return (False,"Celular no cumple el formato")

def valida_fecha(fecha):
    regex = "\d{4}-((0[1-9])|(1[0-2]))-((0[1-9])|([1-2][0-9])|(3[0-1])) (([0-1][0-9])|(2[0-3])):(([0-5][0-9]))"
    if fecha == "":
        return (False,"Se requiere fecha")
    x = re.search(regex,fecha)
    if not x:
        return (False,"Formato de fecha inválido")
    if x.span()[1] - x.span()[0] == len(fecha):
        anho = fecha[0:4]
        mes = fecha[5:7]
        dia = fecha[8:10]
        anho_numero = int(anho)
        if mes == "02":
            if int(dia) > 29:
                return (False,"Fecha inválida")
            if dia == "29":
                if ((anho_numero % 4 == 0) and (anho_numero % 100 != 0)) or (anho_numero % 400 == 0):
                    
                    return (True,datetime.strptime(fecha, '%Y-%m-%d %H:%M'))
                else:
                    return (False,"Fecha inválida")
        elif mes in ["02","04","06","09","11"] and dia == "31":
            return (False,"Fecha inválida")
        else:
            return (True,datetime.strptime(fecha, '%Y-%m-%d %H:%M'))
    else:
        return (False,"Fecha inválida")
    

def valida_tipo(tipo):
    if tipo in ['no sé', 'insecto', 'arácnido', 'miriápodo']:
        return (True,tipo)
    return (False,"Tipo inválido")

def valida_estado(estado):
    if estado in ['no sé', 'vivo', 'muerto']:
        return (True,estado)
    return (False,"Tipo inválido")


def valida_imagen(fileitem):
    if fileitem.filename:
        filenames = fileitem.filename
        hash_archivo = database.hash_name(filenames)
        open('media/'+hash_archivo,'wb').write(fileitem.file.read())
        size = os.fstat(fileitem.file.fileno()).st_size
        if size <= 50000:
            tipo_real = filetype.guess('media/'+hash_archivo)
            if ("image" or "gif" or "jpg") in str(tipo_real).lower() :
                img_ok = True
            else:
                error = "Tipo de archivo no válido"
                os.remove("media/"+hash_archivo)
        else:
            error = "Archivo muy pesado"

test_form = {
    "region": "Región del Ñuble",
    "comuna":"Chillan",
    "sector":"",
    "nombre":"Cristóbal",
    "email":"cris@gmail.com",
    "celular":"",
    "dia-hora-avistamiento" : ["2021-03-29 13:21","2021-03-29 13:22"],
    "tipo-avistamiento" : ["no sé","insecto"],
    "estado-avistamiento" : ["vivo","muerto"]
}

def add_fotos(form):
    cantidad_fotos = 0
    fotos_paths = []
    imgs_ok = True
    offset_foto = -1
    if 'foto-avistamiento' in form.keys():
        if type(form['foto-avistamiento']) is list:
            for foto in form['foto-avistamiento']:
                offset_foto += 1
                cantidad_fotos += 1
                fileitem = foto
                if fileitem.filename:
                    filenames = fileitem.filename
                    hash_archivo = database.hash_name(filenames,offset_foto)
                    path_archivo = 'T2/media/'+hash_archivo
                    open(path_archivo,'wb').write(fileitem.file.read())
                    size = os.fstat(fileitem.file.fileno()).st_size
                    if size <= 12000000:
                        tipo_real = filetype.guess(path_archivo)
                        if ("image" or "gif" or "jpg") in str(tipo_real).lower() :
                            imgs_ok = imgs_ok and True
                            fotos_paths.append([[path_archivo,filenames]])
                        else:
                            imgs_ok = imgs_ok and False
                            error = "El tipo de algún archivo no es válido"
                            os.remove(path_archivo)
                            break
                    else:
                        error = "Algún archivo es muy pesado"
                        imgs_ok = imgs_ok and False
                        break
        else:
            offset_foto += 1
            cantidad_fotos = 1
            fileitem = form['foto-avistamiento']
            if fileitem.filename:
                filenames = fileitem.filename
                hash_archivo = database.hash_name(filenames,offset_foto)
                path_archivo = 'T2/media/'+hash_archivo
                open(path_archivo,'wb').write(fileitem.file.read())
                size = os.fstat(fileitem.file.fileno()).st_size
                f.write("size: "+ str(size) + "\n")
                if size <= 12000000:
                    tipo_real = filetype.guess(path_archivo)
                    if ("image" or "gif" or "jpg") in str(tipo_real).lower() :
                        imgs_ok = imgs_ok and True
                        fotos_paths.append([[path_archivo,filenames]])
                    else:
                        error = "Tipo de archivo no válido"
                        os.remove(path_archivo)
                        imgs_ok = imgs_ok and False
                else:
                    error = "Archivo muy pesado"
                    imgs_ok = imgs_ok and False
    else:
        return (False) #TODO
    
    i = 0
    if imgs_ok:
        while i < cantidad_fotos:
            name_form = 'foto-avistamiento-'+str(i)          
            if name_form in form.keys():
                    if type(form[name_form]) is list:
                        if (len(form[name_form])):
                            return (False,[])
                        for foto in form[name_form]:
                            offset_foto += 1
                            fileitem = foto
                            if fileitem.filename:
                                filenames = fileitem.filename
                                hash_archivo = database.hash_name(filenames,offset_foto)
                                path_archivo = 'T2/media/'+hash_archivo
                                open(path_archivo,'wb').write(fileitem.file.read())
                                size = os.fstat(fileitem.file.fileno()).st_size
                                f.write("size: "+ str(size) + "\n")
                                if size <= 12000000:
                                    tipo_real = filetype.guess(path_archivo)
                                    if ("image" or "gif" or "jpg") in str(tipo_real).lower() :
                                        imgs_ok = imgs_ok and True
                                        fotos_paths[i] += [[path_archivo,filenames]]
                                    else:
                                        imgs_ok = imgs_ok and False
                                        error = "El tipo de algún archivo no es válido"
                                        os.remove(path_archivo)
                                        break
                                else:
                                    error = "Algún archivo es muy pesado"
                                    imgs_ok = imgs_ok and False
                                    break
                    else:
                        offset_foto += 1
                        fileitem = form[name_form]
                        if fileitem.filename:
                            filenames = fileitem.filename
                            hash_archivo = database.hash_name(filenames,offset_foto)
                            path_archivo = 'T2/media/'+hash_archivo
                            open(path_archivo,'wb').write(fileitem.file.read())
                            size = os.fstat(fileitem.file.fileno()).st_size
                            f.write("size: "+ str(size) + "\n")
                            if size <= 12000000:
                                tipo_real = filetype.guess(path_archivo)
                                if ("image" or "gif" or "jpg") in str(tipo_real).lower() :
                                    imgs_ok = imgs_ok and True
                                    fotos_paths[i] += [[path_archivo,filenames]]
                                else:
                                    error = "Tipo de archivo no válido"
                                    os.remove(path_archivo)
                                    imgs_ok = imgs_ok and False
                            else:
                                error = "Archivo muy pesado"
                                imgs_ok = imgs_ok and False
            i += 1
    if not imgs_ok:
        for group in fotos_paths:
            for path_foto in group:
                os.remove(path_foto[0])
        return (False,error)
    return (True,fotos_paths)


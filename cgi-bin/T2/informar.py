#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import html
cgitb.enable()

from db import DB
import validacion
from piezas import *
from data_base import *
database = DB('localhost',USER_DB,PASS_DB,DB_DB)




form = cgi.FieldStorage()



print("Content-type: text/html; charset=UTF-8")
utf8stdout = open(1, 'w', encoding='utf-8',closefd=False)
#f = open("./proxy2.txt","a")

#f.write(str(a)+"\n")
print("")
print("""<!DOCTYPE html><html lang="es">""",file=utf8stdout)

# Sin llaves printea formulario
if form.keys() == []:
  print("""
      <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Vivan los Bichos</title>
      <link rel="stylesheet" href="./../../T2/css/mystyles.css">
      <link rel="stylesheet" href="./../../T2/css/hero_style.css">
      <script src="./../../T2/js/nuevafoto.js"></script>
      <script src="https://kit.fontawesome.com/929bc70b66.js" crossorigin="anonymous"></script>
      <script src="./../../T2/js/new_regiones_comunas.js"></script>
      <script src="./../../T2/js/avistamiento_singular.js"></script>
      <script src="./../../T2/js/validacion.js"></script>
    </head>
    <body>
  """,file=utf8stdout)
  print(navbar,file=utf8stdout)
  print(hero_informar,file=utf8stdout)
  print(formulario_informar1,file=utf8stdout)
  print(formulario_informar2,file=utf8stdout)
  print(footer,file=utf8stdout)
  print("""
    <!-- Make regiones -->
    <script>
    make_regiones();
    actualizarFechaUno();
    </script>
    </body>
  </html>""",file=utf8stdout)

else:
  a = validacion.check_form(form)
  # Si hay success
  if a[0]:
    print("""
    <head>
    <meta http-equiv="refresh" content="0;url='portada.py?state=success'"/> 
    </head>
    </html>""")

# Un error
  else:
    total_errores = ""
    #f.write("e------------ \n")
    #f.write(str(a))
    for error in a[1]:
      #f.write("erorr \n" + str(error) +"\n")
      total_errores += f"<li>{error}</li>"
    print("""
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Vivan los Bichos</title>
        <link rel="stylesheet" href="./../../T2/css/mystyles.css">
        <link rel="stylesheet" href="./../../T2/css/hero_style.css">
        <script src="./../../T2/js/nuevafoto.js"></script>
        <script src="https://kit.fontawesome.com/929bc70b66.js" crossorigin="anonymous"></script>
        <script src="./../../T2/js/new_regiones_comunas.js"></script>
        <script src="./../../T2/js/avistamiento_singular.js"></script>
        <script src="./../../T2/js/validacion.js"></script>
      </head>
      <body>
    """,file=utf8stdout)
    print(navbar,file=utf8stdout)
    print(hero_informar,file=utf8stdout)
    print(f"""<div class="columns is-mobile mt-5 mb-5"><div class="box column is-three-fifths is-offset-one-fifth"><form id="formulario" method="POST" enctype="multipart/form-data" action="informar.py" onsubmit="return validar_todo()"><div class="columns"><div class="mr-3 block column"><h2 class="title">Lugar:</h2><div class="field"> <label class="label">Región<span class="has-text-danger" >*</span>:</label><div class="select"> <select id="region" name="region" onchange="region_change(this)"><option value=""> Seleccione una región</option> </select></div></div><div class="field"> <label class="label">Comuna<span class="has-text-danger" >*</span>:</label><div class="select"> <select id="comuna" name="comuna"><option value=""> Seleccione una comuna</option> </select></div></div><div class="field"> <label class="label">Sector:</label> <input id="sector" class="input" type="text" size="200" name="sector" maxlength="100"></div></div><div class="ml-3 block column"><h2 class="title">Datos de Contacto:</h2><div class="field"> <label class="label">Nombre<span class="has-text-danger" >*</span>:</label> <input id="nombre" class="input" type="text" name="nombre" size="100" maxlength="200"><p class="help">Debe empezar con mayúscula y en caso de ser más de uno separarse con espacios</p></div><div class="field"> <label class="label">Email<span class="has-text-danger" >*</span>:</label> <input id="email" class="input" type="text" name="email" size="100"></div><div class="field"> <label class="label">Número de Celular:</label> <input id="celular" class="input" type="text" name="celular" size="15" placeholder="Ejemplo: +569XXXXXXXX"></div></div></div><div class="avistamientos"><div class="block"><h2 class="title">Información de Avistamiento:</h2><div class="field"> <label class="label">Día hora<span class="has-text-danger" >*</span>:</label> <input id="dia-hora-avistamiento-1" class="input dia-hora-avistamiento" type="text" placeholder="año-mes-diahora:minuto" name="dia-hora-avistamiento" size="20"></div><div class="field"> <label class="label">Tipo<span class="has-text-danger" >*</span>:</label><div class="select"> <select class="tipo-avistamiento" name="tipo-avistamiento"><option value=""> Seleccione un tipo</option><option value="no sé"> No sé</option><option value="insecto"> Insecto</option><option value="arácnido"> Arácnido</option><option value="miriápodo"> Miriápodo</option> </select></div></div><div class="field"> <label class="label">Estado<span class="has-text-danger" >*</span>:</label><div class="select"> <select name="estado-avistamiento" class="estado-avistamiento"><option value=""> Seleccione un estado</option><option value="no sé"> No sé</option><option value="vivo"> Vivo</option><option value="muerto"> Muerto</option> </select></div></div><div class="archivos"><div class="field"> <label class="label">Imagen<span class="has-text-danger" >*</span>:</label><div class="file has-name"> <label class="file-label"> <input class="file-input foto-avistamiento" type="file" name="foto-avistamiento" onchange="filename_change(this)"> <span class="file-cta"> <span class="file-icon"> <i class="fas fa-upload"></i> </span> <span class="file-label"> Choose a file… </span> </span> <span class="file-name"> Nombre del Archivo </span> </label></div></div></div><p class="help">Los formatos compatibles son .jpg .jpeg .png, las imágenes deben pesar menos de 10mb</p> <button class="button mt-4" type="button" onclick="add_photo(this,0)"> Agregar otra foto </button></div></div> <button class="button is-link mt-3" type="button" onclick="add_new_bug(this)"> Informar otro avistamiento en este sector </button><button class="button is-primary mt-3" type="button" onclick=show_modal(this)> Enviar información del avistamiento </button><div class="modal is-active"><div class="modal-background"></div><div class="modal-card"> <header class="modal-card-head"><h2 class="modal-card-title">Advertencia</h2> </header> <section class="modal-card-body"><h2>¿Está seguro que desea enviar esta información?</h2> <figure class="image is-128x128"> <img src="./../../T2/images/cucaMexicana.jpg" alt="Cucaracha con sombrero mexicano"> </figure><div class="notification is-warning" id="notificacion-formulario"> <button type="button" class="delete" onclick="esconder_notificacion()"><span class="icon"> <i class="fas fa-times"></i> </span></button><div id="notificacion-formato">Corrija los siguientes problemas para enviar el formulario {total_errores}</div></div> </section> <footer class="modal-card-foot"><div class="buttons"> <button type="button" class="button is-danger" onclick="hide_modal_form(this)"> No estoy seguro,quiero volver al formulario </button> <button class="button is-success"> Sí,estoy total y absolutamente seguro</button></div> </footer></div></div></form></div></div>""",file=utf8stdout)
    print(footer,file=utf8stdout)
    print("""
      <!-- Make regiones -->
      <script>
      make_regiones();
      actualizarFechaUno();
      </script>
      </body>
    </html>""",file=utf8stdout)
  
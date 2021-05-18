#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import html
cgitb.enable()

from db import DB

from piezas_portada import *
from piezas import *
from data_base import *

# f = open("./proxy.txt","a")
database = DB('localhost',USER_DB,PASS_DB,DB_DB)

print("Content-type: text/html; charset=UTF-8")
utf8stdout = open(1, 'w', encoding='utf-8',closefd=False)

print("")
print("""<!DOCTYPE html><html lang="es">""")

print(avistamiento_head,file=utf8stdout)

print("<body>",file=utf8stdout)

print(navbar,file=utf8stdout)

contador = -1
form = cgi.FieldStorage()
if 'num' in form.keys():
    if type(form['num']) is not list:
        if form['num'].value.isdigit():
            numero = int(form['num'].value)
            resultado = database.get_avistamiento_info(numero)
            print(f"""<!-- Info persona -->
            <div class="column is-10 is-offset-1 mt-5 mb-1">
                <div class="box columns">
                    <div class="column">
                        <h2 class="title">Lugar:</h2>
                        <div class="content mb-3">
                            <p class="subtitle is-5 mb-1"><b>Región:</b></p>
                            <p>{html.escape(resultado[0][0])}</p>
                        </div>
                        <div class="content mb-3">
                            <h3 class="subtitle is-5 mb-1"> <b>Comuna:</b></h3>
                            <p>{html.escape(resultado[0][1])}</p>
                        </div>
                        <div class="content mb-3">
                            <h3 class="subtitle is-5 mb-1"> <b>Sector:</b></h3>
                            <p>{html.escape(resultado[0][2])}</p>
                        </div>
                    </div>
                    <div class="column">
                        <h2 class="title">Datos de Contacto:</h2>
                        <div class="content mb-3">
                            <p class="subtitle is-5 mb-1"><b>Nombre:</b></p>
                            <p>{html.escape(resultado[0][3])}</p>
                        </div>
                        <div class="content mb-3">
                            <h3 class="subtitle is-5 mb-1"> <b>Email:</b></h3>
                            <p>{html.escape(resultado[0][4])}</p>
                        </div>
                        <div class="content mb-3">
                            <h3 class="subtitle is-5 mb-1"> <b>Número de Celular:</b></h3>
                            <p>{html.escape(resultado[0][5])}</p>
                        </div>
                    </div>
                </div>
            </div>""",file=utf8stdout)
            id = -10
            contador = -1
            for foto in resultado[1]:
                if id != foto[0]:
                    if contador == 1 or contador == 2 or contador == 3:
                        print("""</div> 
                            </div>
                        </div>""",file=utf8stdout)
                    print(f"""<!-- Info avistamiento 1 -->
                            <div class="column mt-1 mb-4">
                                <div class="box">
                                    <h2 class="title">Avistamiento</h2>
                                    <div class="content mb-3">
                                        <p class="subtitle is-5 mb-1"><b>Día hora:</b></p>
                                        <p>{foto[1].strftime('%Y-%m-%d %H:%M')}</p>
                                    </div>
                                    <div class="content mb-3">
                                        <p class="subtitle is-5 mb-1"><b>Tipo:</b></p>
                                        <p>{html.escape(foto[2])}</p>
                                    </div>
                                    <div class="content mb-3">
                                        <p class="subtitle is-5 mb-1"><b>Estado:</b></p>
                                        <p>{html.escape(foto[3])}</p>
                                    </div>
                            <! - Fotos! >        
                                    <div class="block">
                                    <p class="subtitle is-5 mb-4"><b>Imágenes:</b></p>""",file=utf8stdout)
                    id = foto[0]
                    contador = 0
                if contador == 0: #primera foto
                    print(f"""<div class="block tile is-ancestor mb-5">
                                    <div class="tile is-3">
                                        <img class="pointer-image" onclick="show_modal(this)" src="../../{html.escape(foto[4])}" alt="{html.escape(foto[5])}" width="320" height="240">
                                        <div class="modal">
                                            <div class="modal-background"></div>
                                            <div class="modal-content">
                                                <img src="../../{html.escape(foto[4])}" alt="{html.escape(foto[5])}"  width="800" height="600">
                                            </div>
                                            <button class="modal-close is-large" aria-label="close" onclick="hide_modal(this)"></button>
                                        </div>
                                    </div>""",file=utf8stdout)
                elif contador == 1 or contador == 2 or contador == 3:
                    print(f"""<div class="tile is-3">
                                <img class="pointer-image" onclick="show_modal(this)" src="../../{html.escape(foto[4])}" alt="{html.escape(foto[5])}" width="320" height="240">
                                <div class="modal">
                                    <div class="modal-background"></div>
                                    <div class="modal-content">
                                        <img src="../../{html.escape(foto[4])}" alt="{html.escape(foto[5])}"  width="800" height="600">
                                    </div>
                                    <button class="modal-close is-large" aria-label="close" onclick="hide_modal(this)"></button>
                                </div>
                            </div>
                            """,file=utf8stdout)
                            # foto 5
                elif contador == 4:
                    print(f"""
                                </div>
                            </div>
                            <div class="block tile is-ancestor">
                                <div class="tile is-3">
                                    <img class="pointer-image" onclick="show_modal(this)" src="../../{html.escape(foto[4])}" alt="{html.escape(foto[5])}" width="320" height="240">
                                    <div class="modal">
                                        <div class="modal-background"></div>
                                        <div class="modal-content">
                                            <img src="../../{html.escape(foto[4])}" alt="{html.escape(foto[5])}"  width="800" height="600">
                                        </div>
                                        <button class="modal-close is-large" aria-label="close" onclick="hide_modal(this)"></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>""",file=utf8stdout)
                contador += 1

if contador == 1 or contador == 2 or contador == 3:
    print("""</div> 
        </div>
    </div>""",file=utf8stdout)


print("""<br>
    <div class="block mt-5 mb-5">
        <a class="button is-primary is-medium is-light ml-5" href="avistamientos.py">
            Volver al listado de avistamientos
            </a>
        <a class="button is-primary is-medium is-light ml-5" href="portada.py">
            Volver a la portada del sistema
        </a>
    </div>""",file=utf8stdout)

print(footer,file=utf8stdout)
print("""
    </body>
</html>
""",file=utf8stdout)
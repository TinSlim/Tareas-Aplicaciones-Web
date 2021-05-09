#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import html
cgitb.enable()

from db import DB

from piezas_portada import *
from piezas import *

f = open("./proxy.txt","a")
database = DB('localhost',"root","","tarea2")

print("Content-type: text/html; charset=UTF-8")
utf8stdout = open(1, 'w', encoding='utf-8',closefd=False)
print("""<!DOCTYPE html><html lang="es">""")

print(avistamiento_head,file=utf8stdout)

print("<body>",file=utf8stdout)

print(navbar,file=utf8stdout)


form = cgi.FieldStorage()
if 'num' in form.keys():
    if type(form['num']) is not list:
        if form['num'].value.isdigit():
            numero = int(form['num'].value)
            resultados = database.get_avistamiento_info(numero)
            print(f"""
            <!-- Info persona -->
            <div class="column is-10 is-offset-1 mt-5 mb-1">
                <div class="box columns">
                    <div class="column">
                        <h2 class="title">Lugar:</h2>
                        <div class="content mb-3">
                            <p class="subtitle is-5 mb-1"><b>Región:</b></p>
                            <p>{resultados[0][0]}</p>
                        </div>
                        <div class="content mb-3">
                            <h3 class="subtitle is-5 mb-1"> <b>Comuna:</b></h3>
                            <p>{resultados[0][1]}</p>
                        </div>
                        <div class="content mb-3">
                            <h3 class="subtitle is-5 mb-1"> <b>Sector:</b></h3>
                            <p>{resultados[0][2]}</p>
                        </div>
                    </div>
                    <div class="column">
                        <h2 class="title">Datos de Contacto:</h2>
                        <div class="content mb-3">
                            <p class="subtitle is-5 mb-1"><b>Nombre:</b></p>
                            <p>{resultados[0][3]}</p>
                        </div>
                        <div class="content mb-3">
                            <h3 class="subtitle is-5 mb-1"> <b>Email:</b></h3>
                            <p>{resultados[0][4]}</p>
                        </div>
                        <div class="content mb-3">
                            <h3 class="subtitle is-5 mb-1"> <b>Número de Celular:</b></h3>
                            <p>{resultados[0][5]}</p>
                        </div>
                    </div>
                </div>
            </div>""",file=utf8stdout)
            id_avis = -10
            count_fotos = 0
            for resultado in resultados[1]:
                if id_avis != resultado[0]:
                    if count_fotos !=4:
                        print("""</div>
                            </div>
                        </div>""",file=utf8stdout)

                    print(f"""
        <div class="column mt-1 mb-4">
                <div class="box">
                    <h2 class="title">Avistamiento</h2>
                    <div class="content mb-3">
                        <p class="subtitle is-5 mb-1"><b>Día hora:</b></p>
                        <p>{resultado[1]}</p>
                    </div>
                    <div class="content mb-3">
                        <p class="subtitle is-5 mb-1"><b>Tipo:</b></p>
                        <p>{resultado[2]}</p>
                    </div>
                    <div class="content mb-3">
                        <p class="subtitle is-5 mb-1"><b>Estado:</b></p>
                        <p>{resultado[3]}</p>
                    </div>""",file=utf8stdout)
                    id_avis = resultado[0]
                    count_fotos = 0
                if count_fotos == 0:
                    print(f"""
                    <div class="block">
                        <p class="subtitle is-5 mb-4"><b>Imágenes:</b></p>
                        <div class="block tile is-ancestor mb-5">
                            <div class="tile is-3">
                                <img class="pointer-image" onclick="show_modal(this)" src="../../{resultado[4]}" alt="{resultado[3]}" width="320" height="240">
                                <div class="modal">
                                    <div class="modal-background"></div>
                                    <div class="modal-content">
                                        <img src="../../{resultado[4]}"  width="800" height="600" alt="../../{resultado[3]}">
                                    </div>
                                    <button class="modal-close is-large" aria-label="close" onclick="hide_modal(this)"></button>
                                </div>
                            </div>""",file=utf8stdout)
                elif count_fotos == 1 or count_fotos == 2 or count_fotos == 3:
                    print(f"""
                    <div class="tile is-3">
                        <img class="pointer-image" onclick="show_modal(this)" src="../../{resultado[4]}" alt="{resultado[3]}" width="320" height="240">
                        <div class="modal">
                            <div class="modal-background"></div>
                            <div class="modal-content">
                                <img src="../../{resultado[4]}"  width="800" height="600" alt="{resultado[3]}">
                            </div>
                            <button class="modal-close is-large" aria-label="close" onclick="hide_modal(this)"></button>
                            </div>
                    </div>""",file=utf8stdout)
                
                elif count_fotos == 4:
                    print(f"""
                </div>
            </div>
            <div class="block tile is-ancestor">
                <div class="tile is-3">
                    <img class="pointer-image" onclick="show_modal(this)" src="../../{resultado[4]}" alt="{resultado[3]}" width="320" height="240">
                    <div class="modal">
                        <div class="modal-background"></div>
                        <div class="modal-content">
                            <img src="../../{resultado[4]}"  width="800" height="600" alt="{resultado[3]}">
                        </div>
                        <button class="modal-close is-large" aria-label="close" onclick="hide_modal(this)"></button>
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
""",file=utf8stdout)
                count_fotos +=1
        


    print("""

</div>
</div>
        <br>
        <div class="block mt-5 mb-5">
            <a class="button is-primary is-medium is-light ml-5" href="../avistamientos.html">
                Volver al listado de avistamientos
                </a>
            <a class="button is-primary is-medium is-light ml-5" href="../portada.html">
                Volver a la portada del sistema
            </a>
        </div></div>""",file=utf8stdout)
    print(footer,file=utf8stdout)
    print("""
    </body>
</html>""",file=utf8stdout)

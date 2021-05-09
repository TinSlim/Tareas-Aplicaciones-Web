#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import html
cgitb.enable()

from db import DB

from piezas_portada import *
from piezas import *

database = DB('localhost',"root","","tarea2")

print("Content-type: text/html; charset=UTF-8")
utf8stdout = open(1, 'w', encoding='utf-8',closefd=False)
print("""<!DOCTYPE html><html lang="es">""")

print(avistamientos_head,file=utf8stdout)
print("<body>")
print(navbar,file=utf8stdout)
print(hero_avistamientos,file=utf8stdout)


print("""
<div class="columns is-mobile mt-5 mb-5">
    <div class="box column is-three-fifths is-offset-one-fifth">
        <table class="table">
        <thead>
            <tr>
            <th>Fecha - hora</th>
            <th>Comuna</th>
            <th>Sector</th>
            <th>Nombre contacto</th>
            <th>total avistamientos</th>
            <th>total fotos</th>
            </tr>
        </thead>""",file=utf8stdout)

test_values = [["2021-03-29 13:24","Chillán","Plaza de Armas","Cristóbal","2","7"]]
query = database.avistamientos_query(0)
for avist in query:
    
    print(f"""<tr class="pointer" onmouseout="deselect_row(this)" onmousemove="select_row(this)" onclick="window.location='avistamiento.py?num={avist[6]}'">""",file=utf8stdout)
    print(f"<th>{avist[0]}</th>",file=utf8stdout)
    print(f"<th>{avist[1]}</th>",file=utf8stdout)
    print(f"<th>{avist[2]}</th>",file=utf8stdout)
    print(f"<th>{avist[3]}</th>",file=utf8stdout)
    print(f"<th>{avist[4]}</th>",file=utf8stdout)
    print(f"<th>{avist[5]}</th>",file=utf8stdout)
    print("</tr>",file=utf8stdout)

    
print("</tbody>",file=utf8stdout)

print("""
        </table>
    </div>
</div>""",file=utf8stdout)
print(footer,file=utf8stdout)
print("",file=utf8stdout)
print("</body>",file=utf8stdout)
print("</html>",file=utf8stdout)
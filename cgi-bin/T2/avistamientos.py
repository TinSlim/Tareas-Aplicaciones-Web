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
form = cgi.FieldStorage()
page_number = 0
if "page" in form.keys():
    if form["page"].value.isdigit():
        page_number = int(form["page"].value)

max_pags = database.get_avist_pages()
if page_number > max_pags:
    page_number = max_pags

query = database.avistamientos_query(page_number)
por_mostrar = len(query)
for avist in query:    
    print(f"""<tr class="pointer" onmouseout="deselect_row(this)" onmousemove="select_row(this)" onclick="window.location='avistamiento.py?num={avist[6]}'">""",file=utf8stdout)
    print(f"<th>{avist[0]}</th>",file=utf8stdout)
    print(f"<th>{avist[1]}</th>",file=utf8stdout)
    print(f"<th>{avist[2]}</th>",file=utf8stdout)
    print(f"<th>{avist[3]}</th>",file=utf8stdout)
    print(f"<th>{avist[4]}</th>",file=utf8stdout)
    print(f"<th>{avist[5]}</th>",file=utf8stdout)
    print("</tr>",file=utf8stdout)

i = 5
while (por_mostrar < i):
    print(f"""<tr>""",file=utf8stdout)
    print(f"<th><br></th>",file=utf8stdout)
    print(f"<th> </th>",file=utf8stdout)
    print(f"<th> </th>",file=utf8stdout)
    print(f"<th> </th>",file=utf8stdout)
    print(f"<th> </th>",file=utf8stdout)
    print(f"<th> </th>",file=utf8stdout)
    print("</tr>",file=utf8stdout)
    i -= 1


print("</tbody>",file=utf8stdout)

print("""
        </table>
    </div>
</div>""",file=utf8stdout)


print("""<nav class="pagination is-centered" role="navigation" aria-label="pagination">""",file=utf8stdout)
if page_number != 0:
    print(f"""<a class="pagination-previous" href="avistamientos.py?page={str(page_number - 1)}">Previous</a>""",file=utf8stdout)
else:
    print(f"""<a class="pagination-previous" disabled>Previous</a>""",file=utf8stdout)
if page_number != max_pags:
    print(f"""<a class="pagination-next" href="avistamientos.py?page={str(page_number + 1)}">Next page</a>""",file=utf8stdout)
else:
    print(f"""<a class="pagination-next" disabled>Next page</a>""",file=utf8stdout)
print("""<ul class="pagination-list">""",file=utf8stdout)

if page_number > 1:
    print("""<li><a class="pagination-link" aria-label="Goto page 0" href="avistamientos.py?page=0" >0</a></li>""",file=utf8stdout)
if page_number > 2:
    print("""<li><span class="pagination-ellipsis">&hellip;</span></li>""",file=utf8stdout)
if page_number > 0:
    print(f"""<li><a class="pagination-link" aria-label="Goto page {str(page_number - 1)}" href="avistamientos.py?page={str(page_number - 1)}">{str(page_number - 1)}</a></li>""",file=utf8stdout)
print(f"""<li><a class="pagination-link is-current" aria-label="Page {str(page_number)}" aria-current="page" href="avistamientos.py?page={str(page_number)}">{str(page_number)}</a></li>""",file=utf8stdout)
if max_pags - page_number > 0:
    print(f"""<li><a class="pagination-link" aria-label="Goto page {str(page_number + 1)}" href="avistamientos.py?page={str(page_number + 1)}">{str(page_number + 1)}</a></li>""",file=utf8stdout)
if max_pags - page_number > 2:
    print("""<li><span class="pagination-ellipsis">&hellip;</span></li>""",file=utf8stdout)
if max_pags - page_number > 1:
    print(f"""<li><a class="pagination-link" aria-label="Goto page {str(max_pags)}" href="avistamientos.py?page={str(max_pags)}">{str(max_pags)}</a></li>""",file=utf8stdout)

print("""</ul></nav>""",file=utf8stdout)

print(footer,file=utf8stdout)
print("",file=utf8stdout)
print("</body>",file=utf8stdout)
print("</html>",file=utf8stdout)
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

database = DB('localhost',USER_DB,PASS_DB,DB_DB)

print("Content-type: text/html; charset=UTF-8")
utf8stdout = open(1, 'w', encoding='utf-8',closefd=False)

print("")
print("""<!DOCTYPE html><html lang="es">""")
print(inicio_head,file=utf8stdout)
print("<body>")
print(navbar,file=utf8stdout)
print(hero_portada,file=utf8stdout)



print("""
<div class="columns is-mobile mt-5 mb-5">
  <div class="column is-three-fifths is-offset-one-fifth">
    <div class="box table-container">
      <p class="subtitle is-4"> Últimos avistamientos: </p>
      <table class="table">
        <thead>
          <tr>
            <th>Fecha - hora</th>
            <th>Comuna</th>
            <th>Sector</th>
            <th>Tipo</th>
            <th>Foto</th>
          </tr>
        </thead>""",file=utf8stdout)



print("<tbody>",file=utf8stdout)
query = database.portada_query()

for resultado in query:
  print("<tr>",file=utf8stdout)
  print(f"<th>{resultado[0]}</th>",file=utf8stdout)
  print(f"<th>{resultado[1]}</th>",file=utf8stdout)
  print(f"<th>{resultado[2]}</th>",file=utf8stdout)
  print(f"<th>{resultado[3]}</th>",file=utf8stdout)
  print(f'<td><img src="../../{resultado[4]}" width="320" height="240" alt="{resultado[5]}"></td>',file=utf8stdout)
  print("</tr>",file=utf8stdout)
print("</tbody>",file=utf8stdout)
print("""     </table>
    </div>
  </div>
</div>
""",file=utf8stdout)


            
            
print(footer,file=utf8stdout)
print("",file=utf8stdout)
print("</body>",file=utf8stdout)
print("</html>",file=utf8stdout)
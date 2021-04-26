#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import html
cgitb.enable()

import db

from piezas_portada import *
from piezas import *

print("Content-type: text/html; charset=UTF-8")
utf8stdout = open(1, 'w', encoding='utf-8',closefd=False)
print("""<!DOCTYPE html><html lang="es">""")
print(inicio_head,file=utf8stdout)
print("<body>")
print(navbar,file=utf8stdout)
print(hero_portada,file=utf8stdout)

"""print(
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
          </thead>
          <tbody>
          </tbody>
        <table>
      </div>
    </div>
</div>
"""#,file=utf8stdout)

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

test_values = [["2021-03-30 13:21","Chillán","Plaza de Armas","insecto","./../../T2/images/avistamientos/01/2-1.jpg"]]
print("<tbody>",file=utf8stdout)
for avist in test_values:
    print("<tr>",file=utf8stdout)
    print(f"<th>{avist[0]}</th>",file=utf8stdout)
    print(f"<td>{avist[1]}</td>",file=utf8stdout)
    print(f"<td>{avist[2]}</td>",file=utf8stdout)
    print(f"<td>{avist[3]}</td>",file=utf8stdout)
    print(f'<td><img src="{avist[4]}" width="320" height="240" alt=""></td>',file=utf8stdout)
    print("</tr>",file=utf8stdout)
print("</tbody>",file=utf8stdout)
print("""     </table>
    </div>
  </div>
</div>
""",file=utf8stdout)
#print("<tbody>")

#for datos:
#    <tr>
#        <th></th>
#        <td></td>
#        <td></td>
#        <td></td>
#        <td>
#            <img src="" width="320" height="240" alt="">
#        </td>
#    </tr>
            
            
print(footer,file=utf8stdout)
print("",file=utf8stdout)
print("</body>",file=utf8stdout)
print("</html>",file=utf8stdout)
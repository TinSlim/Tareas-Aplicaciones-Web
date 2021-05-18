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
form = cgi.FieldStorage()

print("Content-type: text/html; charset=UTF-8")
utf8stdout = open(1, 'w', encoding='utf-8',closefd=False)

print("")
print("""<!DOCTYPE html><html lang="es">""")
print(inicio_head,file=utf8stdout)
print("<body>")
print(navbar,file=utf8stdout)
print(hero_portada,file=utf8stdout)

if "state" in form.keys():
  if form["state"].value == "success":
    print("""<!-- Modal -->
          <div class="modal is-active">
            <div class="modal-background"></div>
            <div class="modal-card">
              <header class="modal-card-head">
                <h2 class="modal-card-title">Se recibió la información correctamente :)</h2>
              </header>
              <section class="modal-card-body">
                <h2> Gracias por registrar su avistamiento </h2>
                <figure class="image is-128x128">
                  <img src="./../../T2/images/cucaMexicana.jpg" alt="Cucaracha con sombrero mexicano">
                </figure>
              </section>
              <footer class="modal-card-foot">
                <div class="buttons">
                  <button type="button" class="button is-success" onclick="hide_modal_form(this)"> Cerrar </button>
                </div>
              </footer>
            </div>
          </div>""",file=utf8stdout)
    

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
  print(f"<th>{resultado[0].strftime('%Y-%m-%d %H:%M')}</th>",file=utf8stdout)
  print(f"<th>{html.escape(resultado[1])}</th>",file=utf8stdout)
  print(f"<th>{html.escape(resultado[2])}</th>",file=utf8stdout)
  print(f"<th>{html.escape(resultado[3])}</th>",file=utf8stdout)
  print(f'<td><img src="../../{html.escape(resultado[4])}" width="320" height="240" alt="{html.escape(resultado[5])}"></td>',file=utf8stdout)
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
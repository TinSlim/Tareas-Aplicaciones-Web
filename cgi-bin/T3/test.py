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
print("""<!DOCTYPE html><html lang="es">""")
print("""
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Vivan los Bichos</title>
    <link rel="stylesheet" href="./../../T2/css/mystyles.css">
    <link rel="stylesheet" href="./../../T2/css/pointer_style.css">
    <script src="./../../T2/js/avistamiento_singular.js"></script>
    <script src="https://kit.fontawesome.com/929bc70b66.js" crossorigin="anonymous"></script>
</head>""")
print("<body>")
print("""<footer class="footer">
    <div class="columns">
      <div class="column content has-text-centered">
        <div>
          <p><strong>CC5002 - Desarrollo de Aplicaciones Web</strong></p>
        </div>
        <a href="#">Cristóbal Torres Gutiérrez</a>
      </div>
      <div class="column">
      </div>
      <div class="column">
        <p>
          <a href="http://jigsaw.w3.org/css-validator/check/referer">
              <img style="border:0;width:88px;height:31px"
                  src="http://jigsaw.w3.org/css-validator/images/vcss"
                  alt="¡CSS Válido!" />
          </a>
      </p>
      </div>
    </div>
  </footer>""",file=utf8stdout)
print(hero_portada,file=utf8stdout)
print("",file=utf8stdout)
print("</body>",file=utf8stdout)
print("</html>",file=utf8stdout)
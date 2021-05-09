import cgi
import cgitb
import html
cgitb.enable()

from db import DB
import validacion
from piezas_portada import *
from piezas import *

database = DB('localhost',"root","","tarea2")

print("Content-type: text/html; charset=UTF-8")
utf8stdout = open(1, 'w', encoding='utf-8',closefd=False)
print("""<!DOCTYPE html><html lang="es">""")
print(success_head,file=utf8stdout)


print("""
<!DOCTYPE html>
<html lang="es">
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
""")
print(navbar,file=utf8stdout)
print(hero_informar,file=utf8stdout)


#def printFunc(forms):
#  for key in forms.keys():
#    print("<h1>")
#    print(forms[key])
#    print("</h1>")
form = cgi.FieldStorage()
validacion.check_form(form)

#form = cgi.FieldStorage()
#if cgi.FieldStorage():
#  print("<h1>" + str(form['region']) + "</h1>")
#  print("<h1>" + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" + "</h1>")
#  f.write(str(form['region']) + "\n")
#  #validacion.check_form(form)
#print("<h1>asdaff</h1>")

print(formulario_informar,file=utf8stdout)
print(footer,file=utf8stdout)
print("""
  <!-- Make regiones -->
  <script>
  make_regiones();
  actualizarFechaUno();
  </script>
  </body>
</html>""",file=utf8stdout)
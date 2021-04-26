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
print(success_head,file=utf8stdout)
print(navbar,file=utf8stdout)

ok_data = True

# Se recibe formulario
arguments = cgi.FieldStorage()

# Revisa inputs obligatorios
if "region" and "comuna" and "nombre" and "email" in arguments.keys:
  if not (check_region(arguments["region"]) and check_comuna(arguments["comuna"]) and check_nombre(arguments["nombre"]) and check_email(arguments["email"])):
    ok_data = False
else:
  ok_data = False


# Inputs no obligatorios
if ok_data:
  if "sector" in arguments.keys:
    ok_data = check_sector(arguments["sector"])

if ok_data:
  if "celular" in arguments.keys:
    ok_data = check_celular(arguments["celular"])



if ok_data:
  if "dia-hora-avistamiento" in arguments.keys:
    for fecha in arguments["dia-hora-avistamiento"]:
      if not ok_data:
        break
      ok_data = check_fecha(fecha)
    total_bichos = len(arguments["dia-hora-avistamiento"])
  else:
    ok_data = False

if ok_data:
  if "celular" in arguments.keys:
    ok_data = check_celular(arguments["celular"])



#if len(arguments) == 5 and ("nombre-medico" and "experiencia-medico" and "especialidad-medico" and "email-medico" and "celular-medico" in arguments.keys()):
#    print("""
#    <div>
#        <h1>Los datos fueron enviados con éxito</h1>
#        <br>
#        <h3>Se han recibido los siguientes datos</h3>
#    """,file=utf8stdout)    
#    to_add = (html.escape(arguments["nombre-medico"].value),html.escape(arguments["experiencia-medico"].value),
#    html.escape(arguments["especialidad-medico"].value),
#    #None,
#    html.escape(arguments["email-medico"].value), html.escape(arguments["celular-medico"].value))#
#
#    database.save_doctor(to_add)
#    for i in arguments.keys():
#        print("<li>", html.escape(arguments[i].name), ": ", html.escape(arguments[i].value),file=utf8stdout)
#else:
#    print("""
#    <div>
#        <h1>No se enviaron los datos</h1>
#        <br>
#        <h3>Debe llenar todas las entradas del formulario</h3>
#    """,file=utf8stdout)  
#print("""
#    </div>
#</body>
#</html>
#""",file=utf8stdout)


if ok_data:
    print("""
    <div class="box mt-3">
    <p class="subtitle is-4">Hemos recibido su información,muchas gracias por colaborar.</p>
    <div class="block mt-5 mb-5">
        <a class="button is-primary is-light is-large is-fullwidth" href="portada.html">
          Volver a la portada del sistema
        </a>
      </div>
    </div>""",file=utf8stdout)

else:
    print("""
    <div class="box mt-3">
    <p class="subtitle is-4">Algunos de los datos ingresados son incorrectos, no se ingresó la información, intentalo de nuevo</p>
    <div class="block mt-5 mb-5">
        <a class="button is-primary is-light is-large is-fullwidth" href="portada.html">
          Volver a la portada del sistema
        </a>
      </div>
    </div>""",file=utf8stdout)

print("<body></body></html>")
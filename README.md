# Tarea3AppsWeb

## Ejecución

- Ejecutar `python -m http.server  --bind localhost --cgi 10000` desde la carpeta que tiene como subcarpetas T2 T3 cgi-bin, desde ahi ir después a portada.py en cgi-bin.


## Consideraciones

- Cuando se trabaja con html identado en los archivos .py, en anakena a veces se llena la salida y lanza
error, esto no pasa en local. Para evitaro se usan .py con el html minimizado en anakena.

- Para subir a anakena, se deben cambiar algunos path comentados con anakena en validacion.py

- Para subir a anakena, cambiar los valores de data_base.py a los de la base de datos.

- En la tabla de la portada cada fila se muestra con la fecha y hora que inserta el usuario. Se muestran los 5 más recientes, que es lo mismo que los 5 últimos en entrar en el sistema.

- En la tabla de listado de avistamientos, cada fila muestra la fecha y hora en la entró en el sistema esa información y se ordena de acuerdo a esta misma.

- Solo se valida el archivo cuando lugar y datos de contacto son válidos, así se ahorra esa escritura.

- Se tienen que cambiar los paths de la api en estadísticas.html para subir a anakena.

## Link Tareas

Las tareas 2 y 3 tienen problemas dado que no conecta con la base de datos.

1. Tarea1: [http://anakena.dcc.uchile.cl/~ctorresg/cgi-bin/T3/portada.py](http://anakena.dcc.uchile.cl/~ctorresg/T1/portada.html)
2. Tarea2: [http://anakena.dcc.uchile.cl/~ctorresg/cgi-bin/T3/portada.py](http://anakena.dcc.uchile.cl/~ctorresg/cgi-bin/T2/portada.py)
3. Tarea3: [http://anakena.dcc.uchile.cl/~ctorresg/cgi-bin/T3/portada.py](http://anakena.dcc.uchile.cl/~ctorresg/cgi-bin/T3/portada.py)


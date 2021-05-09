from db import DB
database = DB('localhost',"root","","tarea2")
resultados = database.get_avistamiento_info(82)
print(resultados)
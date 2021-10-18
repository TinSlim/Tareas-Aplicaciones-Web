from db import DB

database = DB('localhost',"root","","tarea2")
result = database.get_regiones_comunas_dict()
dict_final = {}
for value in result:
    if value[0] in dict_final.keys():
        dict_final[value[0]] = dict_final[value[0]] + [value[1]]
    else:
        dict_final[value[0]] = [value[1]]
print(dict_final)
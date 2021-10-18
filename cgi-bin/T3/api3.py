#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import html
cgitb.enable()
import json
from datetime import datetime

from db import DB
from data_base import *

empty_dict = {
    "meses":["Enero","Febrero","Marzo","Abril","Mayo","Junio",
    "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    "vivo":[0,0,0,0,0,0,0,0,0,0,0,0],
    "muerto":[0,0,0,0,0,0,0,0,0,0,0,0],
    "no sé":[0,0,0,0,0,0,0,0,0,0,0,0]}

month_dict = {
    1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",
    5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",
    9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}

database = DB('localhost',USER_DB,PASS_DB,DB_DB)
query_result = database.get_state_month_count()

for result in query_result:
    mes = result[2] - 1
    empty_dict[result[1]][mes] = result[0]


result_dict = empty_dict

data = json.dumps(result_dict, separators=(',',':'))
print("Content-type: application/json,charset=UTF-8")
print("Access-Control-Allow-Origin: *")

utf8stdout = open(1, 'w', encoding='utf-8',closefd=False)
print("")
print(str(data))
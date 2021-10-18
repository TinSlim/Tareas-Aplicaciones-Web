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

empty_dict = {}


database = DB('localhost',USER_DB,PASS_DB,DB_DB)
query_result = database.get_map_data()

lugar = None
detalle_av = None
contador = 0
for result in query_result:
    if result[7] != lugar:
        lugar = result[7]
        empty_dict[lugar] = {}
    if result[0] != detalle_av:
        detalle_av = result[0]
        empty_dict[lugar][detalle_av] = {}
        empty_dict[lugar][detalle_av]["foto"] = {}
        contador = 0
    empty_dict[lugar][detalle_av]["dia_hora"] = result[1].strftime("%m/%d/%Y %H:%M")
    empty_dict[lugar][detalle_av]["tipo"] = result[2]
    empty_dict[lugar][detalle_av]["estado"] = result[3]
    empty_dict[lugar][detalle_av]["avist_id"] = result[4]
    empty_dict[lugar][detalle_av]["foto"][contador] = {}
    empty_dict[lugar][detalle_av]["foto"][contador]["path"] = result[5]
    empty_dict[lugar][detalle_av]["foto"][contador]["n_archivo"] = result[6]
    contador += 1
    

result_dict = empty_dict

data = json.dumps(result_dict, separators=(',',':'))
print("Content-type: application/json,charset=UTF-8")
print("Access-Control-Allow-Origin: *")

utf8stdout = open(1, 'w', encoding='utf-8',closefd=False)
print("")
print(str(data))
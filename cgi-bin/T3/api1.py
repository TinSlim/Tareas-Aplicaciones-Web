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

database = DB('localhost',USER_DB,PASS_DB,DB_DB)
query_result = database.get_avist_per_day()
fechas = []
conteo = []
for result in query_result:
    fechas += [result[1].strftime("%m/%d/%Y")]
    conteo += [result[0]]

result_dict = {"fechas":fechas,"conteos":conteo}

data = json.dumps(result_dict, separators=(',',':'))
print("Content-type: application/json,charset=UTF-8")
print("Access-Control-Allow-Origin: *")

utf8stdout = open(1, 'w', encoding='utf-8',closefd=False)
print("")
print(str(data))
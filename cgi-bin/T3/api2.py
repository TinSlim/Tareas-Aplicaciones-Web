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
query_result = database.get_type_count()
tipos = []
conteo = []
for result in query_result:
    tipos += [result[0]]
    conteo += [result[1]]

result_dict = {"tipos":tipos,"conteos":conteo}

data = json.dumps(result_dict, separators=(',',':'))
print("Content-type: application/json,charset=UTF-8")
print("Access-Control-Allow-Origin: *")

utf8stdout = open(1, 'w', encoding='utf-8',closefd=False)
print("")
print(str(data))
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import html
cgitb.enable()
import json
from datetime import datetime

now = datetime.now()

month_day = '-05-03'
str_waitdatetime = str(now.year) + month_day
wait_datetime = datetime.strptime(str_waitdatetime, '%Y-%m-%d')

if (wait_datetime - now).days == 0:
    response_new = "https://imagenes.milenio.com/CDybslY6tjqXRVLtr4mx7DhB2-Q=/958x596/smart/https://www.milenio.com/uploads/media/2017/12/25/susto-provocar-aparicion-diabetes-persona.jpeg"
elif (wait_datetime - now).days < 0:
    str_waitdatetime = str(now.year + 1) + month_day
    wait_datetime = datetime.strptime(str_waitdatetime, '%Y-%m-%d')
    response_new = ""
else:
    response_new = ""
dict = {"diference" : (wait_datetime - now).days,
        "response" : response_new}

data = json.dumps(dict, separators=(',',':'))
print("Content-type: application/json,charset=UTF-8")
print("Access-Control-Allow-Origin: *")

utf8stdout = open(1, 'w', encoding='utf-8',closefd=False)
print("")
print(data)
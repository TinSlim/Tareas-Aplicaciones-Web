#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector
import hashlib

class DB:

    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host="localhost",
            user=user,
            password=password,
            database=database,
        )
        self.cursor = self.db.cursor()

    def portada_query(self):
        # Antigua Query
        # sql_query = '''
        #SELECT DA.dia_hora, CO.nombre, AV.sector, DA.tipo , FO.ruta_archivo, FO.nombre_archivo
        #FROM avistamiento AV, detalle_avistamiento DA, comuna CO , (
        #SELECT min(id), ruta_archivo, nombre_archivo, detalle_avistamiento_id
        #FROM foto
        #GROUP BY detalle_avistamiento_id    
        #) FO
        #WHERE DA.avistamiento_id = AV.id AND AV.comuna_id=CO.id AND DA.id = FO.detalle_avistamiento_id ORDER BY DA.dia_hora DESC LIMIT 5
        #'''
        sql_query = '''
        SELECT DA.dia_hora, CO.nombre, AV.sector, DA.tipo , FO.ruta_archivo, FO.nombre_archivo
        FROM avistamiento AV, detalle_avistamiento DA, comuna CO , (
        SELECT min(id), ruta_archivo, nombre_archivo, detalle_avistamiento_id
        FROM foto
        GROUP BY detalle_avistamiento_id    
        ) FO
        WHERE DA.avistamiento_id = AV.id AND AV.comuna_id=CO.id AND DA.id = FO.detalle_avistamiento_id ORDER BY DA.id DESC LIMIT 5
        '''
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()

    def avistamientos_query(self,page):
        if type(page) != int:
            page = 0
        else:
            page = page * 5
        sql_query = f'''
        SELECT AV.dia_hora,CO.nombre, AV.sector, AV.nombre, CA.conteo,TF.conteo, AV.id
        FROM comuna CO, avistamiento AV,
        (SELECT sum(TF.conteo) AS conteo, DA.avistamiento_id
        FROM (SELECT detalle_avistamiento_id AS id,COUNT(detalle_avistamiento_id) AS conteo FROM foto GROUP BY detalle_avistamiento_id) TF,  
            detalle_avistamiento DA
        WHERE DA.id = TF.id
        GROUP BY DA.avistamiento_id) TF,
        (SELECT avistamiento_id AS id ,COUNT(avistamiento_id) AS conteo FROM detalle_avistamiento GROUP BY avistamiento_id) CA
        WHERE AV.comuna_id = CO.id AND TF.avistamiento_id = AV.id AND CA.id = AV.id
        ORDER BY AV.dia_hora DESC
        LIMIT 5
        OFFSET {page} 
        '''
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()

    def save_avistamiento(self,data):
        # data = (comuna_id,dia_hora,sector,nombre,email,celular)
        sql_query = '''
        INSERT INTO avistamiento (comuna_id,dia_hora,sector,nombre,email,celular) VALUES (%s,%s,%s,%s,%s,%s)
        '''
        self.cursor.execute(sql_query,data)
        self.db.commit()
        return self.cursor.getlastrowid()
    
    def save_detalle_avistamiento(self,data):
        # data = (dia_hora,tipo,estado,avisamiento_id)
        sql_query = '''
        INSERT INTO detalle_avistamiento (dia_hora,tipo,estado,avistamiento_id) VALUES (%s,%s,%s,%s)
        '''
        self.cursor.execute(sql_query,data)
        self.db.commit()
        return self.cursor.getlastrowid()

    #def save_image(self,data):


    def get_region_id(self,region):
        sql_query = f"""
        SELECT id FROM region WHERE nombre = '{region}'
        """
        self.cursor.execute(sql_query)
        return self.cursor.fetchone()

    def get_comuna_info(self,comuna):
        sql_query = f"""
        SELECT id,region_id FROM comuna WHERE nombre = '{comuna}'
        """
        self.cursor.execute(sql_query)
        return self.cursor.fetchone()

    def get_regiones_comunas_dict(self):
        sql_query = """SELECT RE.nombre, CO.nombre FROM region RE, comuna CO WHERE RE.id = CO.region_id"""
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()
    
    def hash_name(self, filenames, offset=0):
        sql = "SELECT COUNT(id) FROM foto"
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1 + offset
        hash_archivo = str(total) + hashlib.sha3_256(filenames.encode()).hexdigest()[0:30]
        return hash_archivo

    def save_foto(self,data):
        sql_query = '''
        INSERT INTO foto (ruta_archivo,nombre_archivo,detalle_avistamiento_id) VALUES (%s,%s,%s)
        '''
        self.cursor.execute(sql_query,data)
        self.db.commit()

    def get_avistamiento_info(self,numero):
        #info avistamiento
        sql_query1 = f"""
        SELECT RE.nombre, CO.nombre,AV.sector,AV.nombre,AV.email,AV.celular
        FROM region RE, comuna CO, avistamiento AV
        WHERE CO.region_id = RE.id AND AV.comuna_id = CO.id AND AV.id ='{numero}'"""
        sql_query2 = f"""
        SELECT DA.id, DA.dia_hora, DA.tipo,DA.estado, FT.ruta_archivo,FT.nombre_archivo
        FROM detalle_avistamiento DA, foto FT
        WHERE FT.detalle_avistamiento_id = DA.id AND DA.avistamiento_id = '{numero}'"""

        self.cursor.execute(sql_query1)
        resultado_1 = self.cursor.fetchone()
        self.cursor.execute(sql_query2)
        resultado_2 = self.cursor.fetchall()
        return (resultado_1,resultado_2)

    def get_avist_pages(self):
        sql_query = "SELECT COUNT(*) FROM avistamiento"
        self.cursor.execute(sql_query)
        resultado = int(self.cursor.fetchone()[0])
        if resultado % 5 == 0:
            final = max(0,resultado//5 -1)
        else:
            final = resultado//5
        return final
        
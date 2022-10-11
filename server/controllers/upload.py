
from typing import List

# from config.db import SessionLocal
# from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd    
import json as js
from sqlalchemy import text


# from functools import reduce
# import operator
# import pprint
# import os

engine = create_engine('postgresql+psycopg2://postgres:Manjunath96@localhost:5432/Xvector', echo=False)


class upload_files:

    def dataset(file):
        data = pd.read_csv(file.file)
        df = pd.DataFrame(data)
        df['file_name'] = file.filename
        # df1 = df.to_dict()
        
        df.to_sql('data', con=engine, index=False, if_exists = 'append')
        return {"success": "ok", "message": "Data inserted successfully", "data": file.filename}


    def getdata(filename, columnname, value, columnname2):
        if filename is None and columnname is None and value is None:
            res = pd.read_sql("SHOW COLUMNS FROM data", engine)
            # print(res)
            mydict = res.Field.to_dict()
            # print(mydict)
            return {"success": "ok", "message": "List of columns", "data": mydict}
        elif columnname2 is None:
            if value == "max" or value == "MAX":
                res = pd.read_sql("select max("+columnname+") as max From data WHERE file_name = '%s'" % filename, engine)
                print(res)
                mydict = res.to_dict()
                print(mydict)
                return {"success": "ok", "message": "Max", "data": mydict}
            elif value == "min" or value == "MIN":
                res = pd.read_sql("select min("+columnname+") as max From data WHERE file_name = '%s'" % filename, engine)
                print(res)
                mydict = res.to_dict()
                print(mydict)
                return {"success": "ok", "message": "min", "data": mydict}
            elif value == "sum" or value == "SUM":
                res = pd.read_sql("select sum("+columnname+") as max From data WHERE file_name = '%s'" % filename, engine)
                print(res)
                mydict = res.to_dict()
                print(mydict)
                return {"success": "ok", "message": "sum", "data": mydict}
        else:
            res = pd.read_sql("select "+columnname+" as x, "+columnname2+" as y From data WHERE file_name = '%s'" % filename, engine)
            print(res)
            x = res['x'].to_list()
            y = res['y'].to_list()
            # print(mydict)
            mydict = {
                "x": x,
                "y": y
            }
            return {"success": "ok", "message": "plot data", "data": mydict}


            
        

    



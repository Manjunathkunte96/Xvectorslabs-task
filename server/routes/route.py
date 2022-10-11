from fastapi import APIRouter, Form, UploadFile, File, Depends, Response, status,Request

from typing import List, Union, Optional
from config.db import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from controllers.upload import upload_files
import pprint
route = APIRouter()


@route.post('/dataset')
async def datatest(file: UploadFile = File()):
    return upload_files.dataset(file)

@route.get('/getdata')
def getdata(filename: Optional[str] = None, columnname: Optional[str] = None, value: Optional[str] = None, columnname2: Optional[str] = None):
    return upload_files.getdata(filename, columnname, value, columnname2)



from fastapi import FastAPI, Request, Form, Response, UploadFile, File
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware


from routes.index import route
from fastapi.staticfiles import StaticFiles
import pandas as pd  


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



origins = ["*"]
methods = ["*"]

app.add_middleware(
    CORSMiddleware,
    
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=["*"],
    
)

app.include_router(route)
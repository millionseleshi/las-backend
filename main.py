import json
from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import orjson
from pydantic import BaseModel
from las import *
from fastapi.responses import JSONResponse, ORJSONResponse

app = FastAPI()

class Points(BaseModel):
    pointNumber:int
    

@app.get("/")
def read_root():
    return "welcome"

@app.get("/count")
def read_point_count():
    return {"point_count":read_pointCloud_count()}

@app.get("/format")
def read_point_format():
    return {"point_format":read_pointCloud_format()} 

@app.get("/dime")
def read_point_dimmension():
    return {"dimension_name":read_pointCloud_dimension_names()}

@app.post("/points")
def read_chuncked_points(point: Points):
    if( point.pointNumber >= read_pointCloud_count()):
         return "point number can't excede total point count"
    else:
        point_clollection=read_pointCloud_xyz(point_number=point.pointNumber)
        return ORJSONResponse(point_clollection.tolist(),media_type="application/json")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

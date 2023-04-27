# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：json_compatible.py
@Author  ：Yuqi.W
@Date    ：2023/4/27 10:56 
@DOC     : JSON 兼容编码器
"""
from datetime import datetime

import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str


app = FastAPI()


@app.put("/items/{id}", tags=["JSON 兼容编码器"])
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data


if __name__ == '__main__':
    uvicorn.run("json_compatible:app", reload=True)

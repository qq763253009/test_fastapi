# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：req_body.py
@Author  ：Yuqi.W
@Date    ：2023/4/27 16:23 
@DOC     :
"""

from typing import List, Union

import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Union[str: None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: List[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]



@app.put("/items/{items_id}", response_model=Item)

async def updata_item(item_id: str,item: Item):
    updata_item_encoded = jsonable_encoder(item)
    items[item_id]= updata_item_encoded
    return updata_item_encoded

if __name__ == '__main__':
    uvicorn.run("req_body:app", reload=True)

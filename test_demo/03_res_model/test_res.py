# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：test_res.py
@Author  ：Yuqi.W
@Date    ：2022/12/27 17:10 
@DOC     :
"""
from typing import List, Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.post("/items/{item_id}", response_model=Item, response_model_exclude_unset=True, tags=["响应模型编码参数"])
async def create_item(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/name", response_model=Item, response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]


# UserIn
class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: str
    full_name: Union[str, None] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


if __name__ == '__main__':
    uvicorn.run("test_res:app", reload=True)

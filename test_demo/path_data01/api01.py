# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：api01.py
@Author  ：Yuqi.W
@Date    ：2022/9/9 6:22 PM 
@DOC     : 路径参数

"""

from fastapi import FastAPI
from enum import Enum

app = FastAPI()


# 声明路径"参数"或"变量"：
@app.get("/items/{item_id}", tags=["路径参数"])
async def read_item(item_id: str):
    return {"ieem_id": item_id}


# api顺序
@app.get("/user/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/user/{user_id}")
async def read_user_id(user_id: str):
    return {"user": user_id}


# 枚举 预设值


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

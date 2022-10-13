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
import uvicorn

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


# 声明路径参数
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "传参="+model_name}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "参数="+model_name}
    return {"model_name": model_name, "message": "参数="+model_name}


# 路径转换器

@app.get("/files/{files_path: path}")
async def get_path(files_path: str):
    return {"files_path": files_path}



# 查询参数

test_db = [{"name": "a", "name": "b", "name": "c", "name": "d"}]
@app.get("/get_data/")
async def get_data(skip: int = 0, limit: int = 1):
    return test_db[skip: skip + limit]

# 可选参数
@app.get()













if __name__ == '__main__':
    uvicorn.run("api01:app", reload=True)
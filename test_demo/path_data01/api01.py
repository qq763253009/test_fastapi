# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：api01.py
@Author  ：Yuqi.W
@Date    ：2022/9/9 6:22 PM 
@DOC     : 路径参数

"""

from fastapi import FastAPI, Query, Path
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
# 多个路径和查询参数
from typing import Union


@app.get("/users/{user_id}/items/{item_id}", tags=["可选参数,多个路径和查询参数"])
async def get_item(user_id: str, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "user_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"api中不存在： short"})
    return item




# 必需查询参数
@app.get("/id/{id}")
async def required_id(ids: str, nedey: str, skip: int = 0, limit: Union[int, None] = None):
    item = {"id": ids, "nedey": nedey, "skip": skip, "limit": limit}
    return item


# 请求体 :我们使用 Pydantic 模型来声明请求体，并能够获得它们所具有的所有能力和优点。

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.post("/ps/",tags=["请求体"])
async def ps_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict

# 查询参数和字符串校验
@app.put("/ps/{item_id}",tags=["请求体 + 路径参数 + 查询参数"])
async def get_ps_item(item_id: int, item: Item,
                      q: Union[str, None] = Query(default=None, min_length=3, max_length=50),
                      regex="^fixedquery$"):
    res = {"item_id": item_id, **item.dict()}
    if q:
        res.update({"q": q})

    return res



# 查询参数和字符串校验

@app.get("/data_get/",tags=["查询参数和字符串校验"])
async def data_get(q: Union[str, None] = Query(default=None, min_length=10, max_length=50)):
    results = {"items": [{"ietm_id": "alxe"}, {"item_id": "wyq"}]}
    if q:
        results.update({"q": q})

    return results


# 查询参数列表 / 多个值
from typing import List
@app.get("/list/",tags=["多个参数 "])
async def list_data(q: Union[List[str], None] = Query(default=None,
                                                      alias='sss',
                                                      deprecated=True,
                                                      title="Query string",
                                                      description="Query string for the items to search in the database that have a good match",
                                                      )):
    list_items = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        list_items.update({"q": q})

    return list_items


# 路径参数和数值校验
@app.get("/path_id/{id}")
async def path_id(
        id: int = Path(..., title="id"),
        q: Union[str, None] = Query(default=None, alias="path_id"),):
    res = {"item_id": id}
    if q:
        res.update({"q": q})
    return res


# 请求体 - 多个参数

class ItemEnum(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/item_enum/{id}", tags=["混合使用 Path、Query 和请求体参数"])
async def updata_item(
        *,
        id: int = Path(...,title="The ID of the item to get", ge=0, le=1000),
        q: Union[str, None] = None,
        item: Union[ItemEnum, None] = None,
):
    results = {"item_id": id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})

    return results










if __name__ == '__main__':
    uvicorn.run("api01:app", reload=True)
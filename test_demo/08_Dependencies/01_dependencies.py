# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：01_dependencies.py
@Author  ：Yuqi.W
@Date    ：2023/4/27 17:31 
@DOC     :
"""
import uvicorn
from fastapi import FastAPI,Depends
from typing import Union
from typing import Optional



app = FastAPI()



async def common_parameters(q :Union[str,None]=None, skip: int=0, limit: int=100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/",tags=['依赖注入'])
async def read_item(commons: dict = Depends(common_parameters)):
    return commons

@app.get("/users/",tags=['依赖注入'])
async def read_users(commons: dict = Depends(common_parameters)):
    return commons

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# 我们可以将上面的依赖项 "可依赖对象" common_parameters 更改为类 CommonQueryParams
class UserQueryParams:
    def __init__(self,name:Optional[str] = None, age: int =0, sex: str = None):
        self.name=name
        self.age= age
        self.sex = sex

@app.get("/user")
async def UserParms(user :UserQueryParams = Depends()):
    response = {}
    if user.name:
        response.update({"name":user.name})
    items = fake_items_db[user.age : user.age]
    response.update({"info":items})
    return response



if __name__ == '__main__':
    uvicorn.run("01_dependencies:app", reload=True)
# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：03_Path_operation_decorator.py
@Author  ：Yuqi.W
@Date    ：2023/9/8 14:25 
@DOC     :
"""
import uvicorn
from fastapi import FastAPI,Depends,Header,HTTPException



app = FastAPI()



def verify_token(x_token: str = Header(title="token")):
    if x_token != "user":
        raise HTTPException(status_code=400, detail="Header No token")



def veify_key(x_key: str = Header(title="key")):
    if x_key != "user_key":
        raise HTTPException(status_code=400, detail="Header No key")
    return x_key


#路径操作装饰器支持可选参数 ~ dependencies。
@app.get("/items",deprecated=[Depends(verify_token), Depends(veify_key)])
async def get_user():
    return [{"item": "Foo"}, {"item": "Bar"}]


if __name__ == '__main__':
    uvicorn.run("03_Path_operation_decorator:app", reload=True)
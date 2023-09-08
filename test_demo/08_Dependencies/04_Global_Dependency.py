# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：04_Global_Dependency.py
@Author  ：Yuqi.W
@Date    ：2023/9/8 14:36 
@DOC     :
"""

from fastapi import FastAPI, Depends, Header, HTTPException


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


app = FastAPI(deprecated=[Depends(verify_token),Depends(verify_key)])



@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
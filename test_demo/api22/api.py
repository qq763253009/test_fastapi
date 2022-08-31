# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：api.py
@Author  ：Yuqi.W
@Date    ：2022/8/31 3:10 PM 
@DOC     :练习api
"""
from typing import Optional
from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


# api分组备注

# 22节
def common_parameters(q: Optional[str] = None,
                      skip: int = 0,
                      limit: int = 100
                      ):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/22/", tags=["22"], description="依赖注入")
def read_items_22(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/user/", tags=["22"], description="依赖注入")
def read_user_22(commons: dict = Depends(common_parameters)):
    return commons


# 23
fake_items_db = [{"city": "beijing"}, {"city": "shanghai"}, {"city": "heze"}]


class CommonQueryParams:
    def __init__(self, desc: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.desc = desc
        self.skip = skip
        self.limit = limit


@app.get("/23/", tags=[23])
def read_items_23(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if commons.desc:
        response.update({"desc": commons.desc})
    items = fake_items_db[commons.skip:commons.skip + commons.limit]
    response.update({"items": items})
    return response


# 25
def verify_token(token: str = Header(...)):
    if token != "ceshi":
        raise HTTPException(status_code=400, datail="Token header invalid")
    return token


def verify_key(key: str = Header(...)):
    if key != "key":
        raise HTTPException(status_code=400, datail="Key header invalid")
    return key


# @app.get("/25/", tags=[25],description=[Depends(verify_token(), verify_key())])
# def read_items_25():
#     return fake_items_db

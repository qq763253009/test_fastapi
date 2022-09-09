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
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

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
        raise HTTPException(status_code=400, detail="Token header invalid")
    return token


def verify_key(key: str = Header(...)):
    if key != "key":
        raise HTTPException(status_code=400, detail="Key header invalid")
    return key


@app.get("/25/", tags=[25], dependencies=[Depends(verify_token), Depends(verify_key)])
def read_items_25():
    return fake_items_db


# 26 继续使用 verify_token


app = FastAPI(dependencies=[Depends(verify_token)])


@app.get("/26/")
def read_items_26():
    return fake_items_db


@app.get("/26s/")
def read_item_26(city: str):
    for item in fake_items_db:
        if item['city'] == city:
            return item

    return {"msg": "not exict"}


# 28 获取当前用户

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    status: Optional[bool] = None


def fake_decode_token(token):
    return User(uasrname=token, email="wyq@qq.com", full_name="wyq")


def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@app.get("/28/")
async def read_users_me_27(current_user: User = Depends(get_current_user)):
    return current_user






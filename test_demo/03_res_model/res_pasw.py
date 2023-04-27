# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：res_pasw.py
@Author  ：Yuqi.W
@Date    ：2022/12/27 18:59 
@DOC     :
"""
import uvicorn
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(UserBase):
    password: str


class UserOut(BaseModel):
    pass


class UserInDb(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDb(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int


itemsa = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/itemsa/{item_id}", response_model=Union[CarItem, PlaneItem])
async def read_item(item_id: str):
    return itemsa[item_id]


if __name__ == '__main__':
    uvicorn.run("res_pasw:app", reload=True)

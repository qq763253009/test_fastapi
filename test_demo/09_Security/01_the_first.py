# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：01_the_first.py
@Author  ：Yuqi.W
@Date    ：2023/9/8 15:44 
@DOC     :
"""
import uvicorn
from fastapi import FastAPI, Depends
from typing import Annotated, Union
# OAuth2 身份验证。
from fastapi.security import  OAuth2PasswordBearer
from pydantic import  BaseModel


auth = OAuth2PasswordBearer(tokenUrl="token")


app = FastAPI()

# 创建一个用户模型
class User(BaseModel):
    username: str
    email : str
    full_name : Union[str, None] = None
    disabled: Union[bool, None]= None



def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

def get_current_user(token: str = Depends(auth)):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user



if __name__ == '__main__':
    uvicorn.run("01_the_first:app", reload=True)
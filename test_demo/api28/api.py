# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：api.py
@Author  ：Yuqi.W
@Date    ：2022/9/7 11:49 AM 
@DOC     : FastAPI 学习之路（二十九）使用密码和 Bearer 的简单 OAuth2
"""

from fastapi import FastAPI, Depends,status,HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
fake_user = {
    "wyq": {
        "username": "user",
        "all_name": "username",
        "email": "user@qq.com",
        "password": "123456",
        "disabled": False
    }
}

app = FastAPI()


def fake_hash_password(password: str):
    return password


class User(BaseModel):
    username: str
    all_name: Optional[str] = None
    email: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_dcoe_token(token):
    user = get_user(fake_user, token)
    return user


def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_dcoe_token(token)
    print(user)
    # if not user:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Invalid authentication",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )
    return user


# 校验
# 目前我们已经从数据库中获取了用户数据，但尚未校验密码。

# 让我们首先将这些数据放入 Pydantic UserInDB 模型中。
# 永远不要保存明文密码，因此，我们将使用（伪）哈希密码系统。

# 如果密码不匹配，我们将返回同一个错误。
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_user.get(form_data.username)
    print(user_dict)
    if not user_dict:
        raise HTTPException(status_code=400, detail="用户名错误")

    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="密码错误 ")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/user/me")
async def read_user_me(current_user: User = Depends(get_current_user())):
    print(current_user)
    return current_user






# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：test_cookie.py
@Author  ：Yuqi.W
@Date    ：2022/12/27 16:57 
@DOC     :
"""
# 你可以像定义 Query 参数和 Path 参数一样来定义 Cookie 参数。

from typing import Union

import uvicorn
from fastapi import Cookie, FastAPI, Header

app = FastAPI()


# 声明cookie参数
@app.get("/items/", tags=["声明cookie"])
async def read_items(cookie: Union[str, None] = Cookie(default=None)):
    return {"cookie": cookie}


# 导入 Header:
@app.get("/test_header/", tags=["Header参数"])
async def read_header(header: Union[str, None] = Header(default=None)):
    return {"header": header}


if __name__ == '__main__':
    uvicorn.run("test_cookie:app", reload=True)

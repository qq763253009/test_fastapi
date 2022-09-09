# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：api01.py
@Author  ：Yuqi.W
@Date    ：2022/9/9 6:22 PM 
@DOC     : 路径参数

"""

from fastapi import FastAPI

app = FastAPI()


# 声明路径"参数"或"变量"：
@app.get("/items/{item_id}",tags=["路径参数"] )
async def read_item(item_id):
    return {"ieem_id": item_id}

# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：test_errors.py
@Author  ：Yuqi.W
@Date    ：2023/4/26 15:35 
@DOC     :
"""
import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

err = {"errors": "This is a errors"}


@app.get("/items/{item_id}",tags=["错误处理"])
async def read_item(item_id: str):
    if item_id not in err:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": err[item_id]}


if __name__ == '__main__':
    uvicorn.run("test_errors:app", reload=True)

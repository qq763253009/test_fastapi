# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：demo_from.py
@Author  ：Yuqi.W
@Date    ：2022/12/28 15:41 
@DOC     :
"""
## 表单数据
import uvicorn
from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(default=None), password: str = Form(default=None), ):
    return {"username": username, "password": password}


@app.post("/file/", tags=['文件api'])
async def create_file(file: bytes = File(default=None)):
    return {"file_size": len(file)}


@app.post("/uploadfile/", tags=['上传文件api'])
async def create_upload_file(up_file: UploadFile):
    return {"uploadfile": up_file}


@app.post("/upfileform/", tags=["请求表单与文件"])
async def create_upfile_form(file: bytes = File(default=None), fileb: UploadFile = File(default=None),
                             token: str = Form(default=None)):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }


if __name__ == '__main__':
    uvicorn.run("test_from:app", reload=True)

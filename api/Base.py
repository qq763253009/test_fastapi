#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Date    ：2022/8/3 12:33 上午 
@Author  ：wangyuqi
@Project ：test_fastapi 
@File    ：Base.py
@IDE     ：PyCharm
@Des     : 基本路由
"""
from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/")
async def home(req: Request):
    return "fastapi"

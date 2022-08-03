#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Date    ：2022/8/3 12:39 上午 
@Author  ：wangyuqi
@Project ：test_fastapi 
@File    ：Events.py
@IDE     ：PyCharm 
@Des     ：事件监听
"""
from typing import Callable
from fastapi import FastAPI
from aioredis import Redis


def startup(app: FastAPI) -> Callable:
    """
    FastApi 启动完成事件
    :param app: FastAPI
    :return: start_app
    """
    # async def app_start() -> None:
    #     # APP启动完成后触发
    #     print("fastapi已启动")
    #     # 注册数据库
    #     await register_mysql(app)
    #     # 注入缓存到app state
    #     app.state.cache = await sys_cache()
    #     app.state.code_cache = await code_cache()
    #
    #     pass
    # return app_start


def stopping(app: FastAPI) -> Callable:
    """
    FastApi 停止事件
    :param app: FastAPI
    :return: stop_app
    """
    async def stop_app() -> None:
        # APP停止时触发
        print("fastapi已停止")
        cache: Redis = await app.state.cache
        code: Redis = await app.state.code_cache
        await cache.close()
        await code.close()

    return stop_app

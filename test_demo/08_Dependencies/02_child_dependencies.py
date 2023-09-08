# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：02_child_dependencies.py
@Author  ：Yuqi.W
@Date    ：2023/9/8 14:11 
@DOC     :
"""

from  typing import Union

from fastapi import FastAPI,Cookie,Depends


app = FastAPI()

# 默认空 限制q是一个str 类型
def get_query(q: Union[str, None]= None):
    return q

# 可选查询参数 q 从 get_query 获取  last_query 为str类型,属于Cookie 默认为空
def get_query_or_cookie(q: str=Depends(get_query),last_query: Union[str: None]=Cookie(default=None)):
    if not q :
        return last_query
    else:
        return q

# 在高级使用场景中，如果不想使用「缓存」值，而是为需要在同一请求的每一步操作（多次）中都实际调用依赖项，可以把 Depends 的参数 use_cache 的值设置为 False :
@app.get("/items")
async def read_query(query_or_default: str=Depends(get_query_or_cookie,use_cache=False)):
    return {"info":query_or_default}


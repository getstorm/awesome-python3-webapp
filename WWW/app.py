#!/user/bin/env python3
# -*- coding: utf-8 -*-

__author__='getstorm'

'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO) #设置了logging的等级为INFO
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

#编写响应处理器handler也就是下文的index（request）

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})



async def init(loop):   #async把一个generator标记为coroutine类型，然后，我们可以把这个coroutine扔到EventLoop中执行
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)  #await新语法代替yield from
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

#asyncio的编程模型就是一个消息循环，我们从asyncio模块中直接获取一个Eventloop的引用
#然后把需要执行的协程扔到Eventloop中执行，就实现了异步IO

loop = asyncio.get_event_loop()       #获取eventloop循环，
loop.run_until_complete(init(loop))   #执行coroutine
loop.run_forever()                    #Eventloop永远循环下去等待响应
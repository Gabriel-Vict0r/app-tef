import os
from aiohttp import web
import socketio
from card_transaction import transaction
import webbrowser
from threading import Timer

sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
print(BASE_DIR)
STATIC_DIR = os.path.join(BASE_DIR, 'static')

@sio.event
def connect(sid, environ, auth):
    print('connect', sid)

@sio.event
async def do_transaction(sid, data):
    result = transaction(data)
    #print(result)
    await sio.emit('result_transaction', result, room=sid)

@sio.event
def disconnect(sid):
    print('Sessão encerrada...')

async def index(req):
    with open(os.path.join(BASE_DIR, 'index.html'), encoding='UTF-8') as f:
        return web.Response(text =f.read(), content_type = 'text/html', charset='UTF-8')
    
def open_browser():
    webbrowser.open('http://localhost:5050')
app.router.add_get('/', index)
app.router.add_static('/static/', path=STATIC_DIR)

if __name__ == '__main__':
    Timer(1, open_browser).start()
    web.run_app(app, port=5050)
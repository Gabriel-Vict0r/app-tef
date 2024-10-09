from aiohttp import web
import socketio
from card_transaction import transaction
import json
sio = socketio.AsyncServer()

app = web.Application()
sio.attach(app)
@sio.event
def connect(sid, environ, auth):
    print('connect', sid)

@sio.event
async def do_transaction(sid, data):
    result = transaction(data)
    #print(result)
    await sio.emit('result_transaction', json.dumps(result), room=sid)

@sio.event
def disconnect(sid):
    print('encerrando a sessao...')

async def index(req):
    with open('index.html') as f:
        return web.Response(text = f.read(), content_type = 'text/html', charset='UTF-8')
#app.router.add_static('/static', 'static')
app.router.add_get('/', index)


if __name__ == '__main__':
    web.run_app(app, port=5050)
from aiohttp import web
import socketio
from card_transaction import transaction
sio = socketio.AsyncServer()

app = web.Application()
sio.attach(app)
@sio.event
def connect(sid, environ, auth):
    print('connect', sid)

@sio.event
def proccess_data(sid, data):
    print('Iniciando DPOS')
    return transaction(data)

@sio.event
def disconnect(sid):
    print('encerrando a sessao...')

async def index(req):
    with open('index.html') as f:
        return web.Response(text = f.read(), content_type = 'text/html')

#app.router.add_static('/static', 'static')
app.router.add_get('/', index)


if __name__ == '__main__':
    web.run_app(app, port=5050)
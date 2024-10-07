from aiohttp import web
import socketio


sio = socketio.AsyncServer()

app = web.Application()
sio.attach(app)


@sio.event

def connect(sid):
    print('connect', sid)

async def index(req):
    with open('src/index.html') as f:
        return web.Response(text = f.read(), content_type = 'text/html')

app.router.add_static('/static', 'static')
app.router.add_get('/', index)


if __name__ == '__main__':
    web.run_app(app, port=5050)
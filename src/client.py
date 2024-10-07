import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('established')

sio.connect('http://localhost:5050')
sio.wait()
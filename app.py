from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from morse.translate import traduzir
from constants.constantes import CONECTAR

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zl4hyafu=ky(m@r&0pbg7qfsro*@r=2r%-js7y3#pj0g8onwvi'
socketio = SocketIO(app, async_mode=None)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@socketio.on('event_morse', namespace='/morse')
def receive_message(message):
    if message['data'] == CONECTAR:
        emit('event_morse_response', {'data': 'Conectado!'})
    else:
        emit('event_morse_response', {'data': traduzir(message['data'])})


if __name__ == '__main__':
    socketio.run(app, debug=True)

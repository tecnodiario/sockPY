from flask import Flask, render_template
from flask_socketio import SocketIO, emit
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('client request')
def test_message(message):
    print('Server has received a request.')
    print('Request recived: {}'.format(message))
    emit('server response', {'data_of_server': 'This is a certificate!'})
    print('Server has send a certification to client.')

if __name__ == '__main__':
    socketio.run(app)
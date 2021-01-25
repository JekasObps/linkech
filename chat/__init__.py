from flask import Flask, render_template, request

from flask_socketio import SocketIO

def create_socketio_app():
    """ Initialize application """

    app = Flask('__name__')
    app.config.from_pyfile('chat.cfg')

    @app.route('/chat')
    def chat():
        return render_template('chat.html')
    
    socket = SocketIO(app)
    
    @socket.on('connect', namespace='/char')
    def connect():
        print('connected!')



    return app, socket
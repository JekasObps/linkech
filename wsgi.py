from chat import create_socketio_app

app, socket = create_socketio_app()

if __name__ == '__main__':
    socket.run(app)

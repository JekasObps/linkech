

(function main(){
    'use strict';
    const socket = io('/chat');
    socket.emit('notification', 'message');
})();

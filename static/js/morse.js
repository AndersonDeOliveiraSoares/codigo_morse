let ws = io('/morse');

$( document ).ready(function() {
     ws.on('connect', function() {
        ws.emit('event_morse', {data: "Conectar"});
    });

    ws.on('event_morse_response', function(msg, callBack) {
        renderResponse(msg.data);
        if (callBack) callBack();
    });
});

function enviar() {
    let codigo = $('#message_input').val();
    $('#chat-body').append('<tr><td><div style="float: right;" align="right" class="box1 sb1">' + codigo + '</div></td></tr>');
    scrollEnd();
    ws.emit('event_morse', {data: codigo});
}

function renderResponse(msg) {
    $('#chat-body').append('<tr><td><div class="box2 sb2">' + msg + '</div></td></tr>');
    scrollEnd();
}

function scrollEnd() {
    let elem = $('#area-msg');
    elem.scrollTop(elem.prop("scrollHeight"));
}

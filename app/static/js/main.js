function inputBorderLogin(e) {
    let value = $(e).attr('id')
    if (value == 'username') {
        $('#user').css({
            'border-left': '3px solid #2e3192'
        })
    } else if (value == 'password') {
        $('#senha').css({
            'border-left': '3px solid #2e3192'
        })
    }
}

function resetUnputBorderLogin(e) {
        let value = $(e).attr('id')
    if (value == 'username') {
        $('#user').css({
            'border-left': '1px solid #dee2e6'
        })
    } else if (value == 'password') {
        $('#senha').css({
           'border-left': '1px solid #dee2e6'
        })
    }
}

function dropMenuMB(e) {
    $('#menuLat').addClass('drop');
}

function dropMenuOff(e) {
    $('#menuLat').removeClass('drop');
}
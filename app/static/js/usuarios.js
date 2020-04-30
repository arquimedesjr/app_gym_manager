
function filterUser(e) {
    var texto = $(e).val();
    $("[data-id='listAlunosItem']").each(function () {
        var resultado = $(this).text().toUpperCase().indexOf(' ' + texto.toUpperCase());

        if (resultado < 0) {
            $(this).fadeOut();
        } else {
            $(this).fadeIn();
        }
        debugger;
    });
}

function deleteAvaliacao(e) {
    let action = $(e).find('#actionUser').val();
    Swal.fire({
        html: `<h3 class="mb-3 h4"> Tem certeza que deseja excluir?</h3>
                <p class="mb-0"> Você não poderá voltar atrás dessa alteração.</p>`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#f0b413',
        confirmButtonText: `Excluir`,
        cancelButtonText: 'Cancelar',
        showClass: {
            popup: 'animated fadeInDown faster'
        },
        hideClass: {
            popup: 'animated fadeOutUp faster'
        },
    })
    .then((result) => {
        if (result.value) {
            $('#pkavaliacao').val(action);
            Swal.fire({
                icon: 'success',
                title: 'Avaliação Excluída com sucesso',
                showConfirmButton: false,
                timer: 1500
            })
            .then((result) => {
                 $('form').submit();
            });
        }
    });
}

function deleteUser(e) {
    let user = $(e).find('input').val();
    let action = $(e).find('#actionUser').val();
    Swal.fire({
        html: `<h3 class="mb-3 h4"> Tem certeza que deseja excluir o aluno ${user}?</h3>
                <p class="mb-0"> Você não poderá voltar atrás dessa alteração.</p>`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#f0b413',
        confirmButtonText: `Excluir`,
        cancelButtonText: 'Cancelar',
        showClass: {
            popup: 'animated fadeInDown faster'
        },
        hideClass: {
            popup: 'animated fadeOutUp faster'
        },
    })
    .then((result) => {
        if (result.value) {
            $('#pkAluno').val(action);
            Swal.fire({
                icon: 'success',
                title: 'Aluno excluído com sucesso',
                showConfirmButton: false,
                timer: 1500
            })
            .then((result) => {
                 $('form').submit();
            });
        }
    });
}
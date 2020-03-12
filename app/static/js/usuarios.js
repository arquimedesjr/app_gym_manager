function deleteUser(e) {
    Swal.fire({
        title: 'Tem certeza que deseja excluir o usuário "{{ usuario.username }}"?',
        text: "Você não poderá voltar atrás depois disso",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: `
            <form method="post">
                {% csrf_token %}
                <button type="submit" class="btn btn-primary">Remover</button>
            </form>`,
        cancelButtonText: 'Cancelar',
        showClass: {
            popup: 'animated fadeInDown faster'
        },
        hideClass: {
            popup: 'animated fadeOutUp faster'
        },
        }).then((result) => {
        if (result.value) {
            Swal.fire(
            'Ecluído!',
            'success'
            )
        }
    })
}
$(document).ready( () => {
  const container = $('.container-fluid');
  if(container.hasClass("pageDashboard") ) {
    $("nav ul li#dashboard").addClass("active");
  }
  if(container.hasClass("pageListarAlunos") ) {
    $("nav ul li#listar-alunos").addClass("active");
  }
  if(container.hasClass("pageCadastrarAlunos") ) {
    $("nav ul li#cadastrar-alunos").addClass("active");
  }
  if(container.hasClass("pageCadastrarAvaliacaoFisica") ) {
    $("nav ul li#cadastrar-avaliacao-fisica").addClass("active");
  }
  if(container.hasClass("pageDadosPessoais") ) {
    $("nav ul li#dados-pessoais").addClass("active");
  }

});
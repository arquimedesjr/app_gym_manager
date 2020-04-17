new Chart(document.getElementById("chartAvaliacao"), {
    type: 'line',
    data: {
      labels: [300,400, 500, 600, 700],
      datasets: [{ 
          data: [310,350, 340, 450, 530],
          label: "Avaliações Cadastradas",
          borderColor: "rgba(46, 49, 146, .6)",
        },
      ]
    }
});

new Chart(document.getElementById("chartAvaliacaoSemAluno"), {
    type: 'line',
    data: {
      labels: ['Jan','Mar', 'Mai', 'Jul', 'Set', 'Nov'],
      datasets: [{ 
          data: [310,350, 340, 450, 530, 300],
          label: "Alunos sem avalição",
          borderColor: "rgba(46, 49, 146, .6)",
        },
      ]
    }
});

new Chart(document.getElementById("chartAluno"), {
    type: 'line',
    data: {
      labels: ['Jan','Mar', 'Mai', 'Jul', 'Set', 'Nov'],
      datasets: [{ 
          data: [310,350, 340, 450, 530, 300],
          label: "Cadastro de aluno",
          borderColor: "rgba(46, 49, 146, .6)",
        },
      ]
    }
});
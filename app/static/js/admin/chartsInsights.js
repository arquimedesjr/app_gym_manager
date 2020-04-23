

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


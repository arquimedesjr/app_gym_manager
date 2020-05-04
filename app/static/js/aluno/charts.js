$(document).ready(() => {      

  // Funções
  chartPeso();
  chartPercentualGordura();

  let medida_direita = [{% for i in entrys %} {{i.medida_biceps_direito|stringformat:'f'}}, {% endfor %}]
  let medida_esquerda = [{% for i in entrys %} {{i.medida_biceps_esquerdo|stringformat:'f'}}, {% endfor %}]
  new Chart(document.getElementById("chartsMedidas"), {
      type: 'bar',
      data: {
          labels: [{% for item in entrys  %} '{{item.created_at|filter_date}}', {% endfor %}],
          datasets: [
              {
                  label: "Direito",
                  backgroundColor: "#2e3192",
                  data: medida_direita
              }, 
              {
                  label: "Esquerdo",
                  backgroundColor: "#F0B413",
                  data: medida_esquerda
              }
          ]
      },
      options: {
          legend: {
              display: false
          },
          responsive: true,
              scaleStartValue: 0,
              scales: {
                  xAxes: [{
                      gridLines: {
                          color: "rgba(65, 104, 136, 0.4)",
                          borderDash: [5, 5],
                      }
                  }],
                  yAxes: [{
                  gridLines: {
                      color: "rgba(65, 104, 136, 0.2)",
                      drawBorder: false,
                  },
                  ticks: {
                      stepSize: 2,
                      fontColor: "rgba(65, 104, 136, 1)",
                      fontSize: "12", 
                      },
                  }]
              }
      }
  });
});


function FiltrarMedidas(e) {
  let selector = document.getElementById('id_filtros');
  let value = selector[selector.selectedIndex].value;
  let id = $('#idAlunoFiltro').val();
  if( value == 'medida_antebraco' || value == 'medida_triceps' || value == 'medida_biceps' || value == 'medida_panturrilha' || value == 'medida_coxa') {
      chartsMedidas(id, value);
  } else if (value == 'medida_costas' || value == 'medida_abdomen' || value == 'medida_peito') {
      chartsMedidasUnica(id, value);
  }

  console.log(value);
}

function chartPeso() {
  new Chart(document.getElementById("chartPeso"), {
      type: 'line',
      data: {
      labels: [{% for item in peso %} '{{item.get_created}}', {% endfor %}],
      datasets: [{ 
          data: [{%for item in peso %}{{item.medida_peso|stringformat:'f'}},{% endfor %}],
          borderColor: "rgba(46, 49, 146, .6)",
          backgroundColor: 'rgba(46, 49, 146, .1)',
          pointBackgroundColor: 'rgba(240, 180, 19, 1)',
          pointBorderColor: 'rgba(240, 180, 19, 1)',
          },
      ]},
      options: {
          legend: {
              display: false
          },
          responsive: true,
              scaleStartValue: 0,
              scales: {
                  xAxes: [{
                      gridLines: {
                          color: "rgba(65, 104, 136, 0.4)",
                          borderDash: [5, 5],
                      }
                  }],
                  yAxes: [{
                  gridLines: {
                      color: "rgba(65, 104, 136, 0.2)",
                      drawBorder: false,
                  },
                  ticks: {
                      fontColor: "rgba(65, 104, 136, 1)",
                      fontSize: "12", 
                      },
                  }]
              }
      }
  });
}

function chartPercentualGordura() {
  new Chart(document.getElementById("chartPercentualDeGordura"), {
      type: 'line',
      data: {
      labels: [{% for item in percentual_de_gordura %} '{{item.get_created}}', {% endfor %}],
      datasets: [{ 
          data: [{%for item in percentual_de_gordura %} {{item.percentual_gordura|stringformat:'f'}},{% endfor %}],
          borderColor: "rgba(46, 49, 146, .6)",
          backgroundColor: 'rgba(46, 49, 146, .1)',
          pointBackgroundColor: 'rgba(240, 180, 19, 1)',
          pointBorderColor: 'rgba(240, 180, 19, 1)',
          },
      ]},
      options: {
          legend: {
              display: false
          },
          responsive: true,
              scaleStartValue: 0,
              scales: {
                  xAxes: [{
                      gridLines: {
                          color: "rgba(65, 104, 136, 0.4)",
                          borderDash: [5, 5],
                      }
                  }],
                  yAxes: [{
                  gridLines: {
                      color: "rgba(65, 104, 136, 0.2)",
                      drawBorder: false,
                  },
                  ticks: {
                      fontColor: "rgba(65, 104, 136, 1)",
                      fontSize: "12", 
                      },
                  }]
              }
      }
  });
}

function chartsMedidas(pk, params) {
  fetch(`/api/${pk}/${params}/`, {
      method: 'get',
      data: 'json',
      dataType: "json",
  })
  .then((response) => {
      response.json()
  .then((data) => {
      $('#chartsMedidas').remove()
      let novoChartsMedida = '<canvas id="chartsMedidas"></canvas>';
      let result = data;
      let medida_direita = []
      let medida_esquerda = []
      let dado = [];
      if(params == 'medida_coxa' || params == 'medida_panturrilha' ) {
          $.each(result, (i, chave, value) => {
              medida_direita.push(`${chave[`${params}_direita`]}`);
              medida_esquerda.push(`${chave[`${params}_esquerda`]}`);
              dado.push(`${chave['created_at']}`);
          });
      } else {
          $.each(result, (i, chave, value) => {
              medida_direita.push(`${chave[`${params}_direito`]}`);
              medida_esquerda.push(`${chave[`${params}_esquerdo`]}`);
              dado.push(`${chave['created_at']}`);
          });
      }
      $('#evolucaoMedidas').append(novoChartsMedida);
      new Chart(document.getElementById("chartsMedidas"), {
          type: 'bar',
          data: {
              labels: dado,
              datasets: [
                  {
                      label: "Direito",
                      backgroundColor: "#2e3192",
                      data: medida_direita
                  }, 
                  {
                      label: "Esquerdo",
                      backgroundColor: "#F0B413",
                      data: medida_esquerda
                  }
              ]
          },
          options: {
              legend: {
                  display: false
              },
              responsive: true,
                  scaleStartValue: 0,
                  scales: {
                      xAxes: [{
                          gridLines: {
                              color: "rgba(65, 104, 136, 0.4)",
                              borderDash: [5, 5],
                          }
                      }],
                      yAxes: [{
                      gridLines: {
                          color: "rgba(65, 104, 136, 0.2)",
                          drawBorder: false,
                      },
                      ticks: {
                          fontColor: "rgba(65, 104, 136, 1)",
                          fontSize: "12", 
                          },
                      }]
                  }
          }
      });
  });
  })
  .catch(function(error) {
      console.log('Operação deu erro: ' + error.message);
  });
}

function chartsMedidasUnica(pk, params) {
  fetch(`/api/${pk}/${params}/`, {
      method: 'get',
      data: 'json',
      dataType: "json",
  })
  .then((response) => {
      response.json()
  .then((data) => {   
      $('#chartsMedidas').remove()
      let novoChartsMedida = '<canvas id="chartsMedidas"></canvas>';
      let result = data;
      let resultado_medidas = []
      let dado = [];
      $.each(result, (i, chave, value) => {
          resultado_medidas.push(`${chave[`${params}`]}`);
          dado.push(`${chave['created_at']}`);
      });
      $('#evolucaoMedidas').append(novoChartsMedida);
      new Chart(document.getElementById("chartsMedidas"), {
          type: 'bar',
          data: {
              labels: dado,
              datasets: [
                  {
                      label: "Direito",
                      backgroundColor: "#F0B413",
                      data: resultado_medidas
                  }
              ]
          },
          options: {
              legend: {
                  display: false
              },
              responsive: true,
                  scaleStartValue: 0,
                  scales: {
                      xAxes: [{
                          gridLines: {
                              color: "rgba(65, 104, 136, 0.4)",
                              borderDash: [5, 5],
                          }
                      }],
                      yAxes: [{
                      gridLines: {
                          color: "rgba(65, 104, 136, 0.2)",
                          drawBorder: false,
                      },
                      ticks: {
                          fontColor: "rgba(65, 104, 136, 1)",
                          fontSize: "12", 
                          },
                      }]
                  }
          }
      });
  });
  })
  .catch(function(error) {
      console.log('Operação deu erro: ' + error.message);
  });
}
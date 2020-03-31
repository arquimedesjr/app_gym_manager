var ctx = document.getElementsByClassName("line-chart");
    const colorGreen = 'rgba(240, 180, 19, 1)';
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Mar', 'Mai', 'Jul', 'Ago'],
            datasets: [{
                label: "IMC do Aluno",
                data: [ 0, 5 , 15, 5, 20],
                colorGreen,
                borderWidth: 3,
        lineTension: 0,
                borderColor: 'rgba(46, 49, 146, 1)',
                pointBackgroundColor: 'rgba(240, 180, 19, 1)',
                pointBorderColor: 'rgba(240, 180, 19, 1)',
                backgroundColor: 'transparent',
                pointHoverRadius: 10,
                fill: false,
            }]
        },
        options: {
        responsive: true,
                scaleStartValue: 0,
                    scales: {
                        xAxes: [{

                            gridLines: {
                                color: "rgba(46, 49, 146, 1)",
                                borderDash: [10, 10],
                            }
                        }],
                        yAxes: [{
            scaleLabel: {
            //   labelString: "Lorem ipsum dolor sit",
            //  display: true,
            },
                            gridLines: {
                                color: "rgba(46, 49, 146, 1)",
                drawBorder: false,
                            },
                            ticks: {
                                callback: function(value, index, values) {
                                        return value ;
                                },
                                min: 0,
                                stepSize: 5,
                fontColor: "rgba(46, 49, 146, 1)",
                fontSize: "22",
                                },
                        }]
                    }
                }
    })


new Chart(document.getElementById("pie-chart"), {
    type: 'pie',
    data: {
        labels: ["Peso", "Massa de gordura"],
        datasets: [{
        backgroundColor: ["#2e3192", "#F0B413"],
        data: [2478,5267]
        }]
    }
});

new Chart(document.getElementById("bar-chart-horizontal"), {
    type: 'horizontalBar',
    data: {
        labels: ["Peso", "Massa de gordura"],
        datasets: [
            {
                label: "Population (millions)",
                backgroundColor: ["#2e3192", "#F0B413"],
                data: [2478,5267]
            }
        ]
    },
    options: {
      legend: { display: false },
    }
});

new Chart(document.getElementById("line-chart"), {
  type: 'line',
  data: {
    labels: [300,400, 500, 600, 700],
    datasets: [{ 
        data: [310,350, 340, 450, 530],
        label: "Peso",
        borderColor: "#2e3192",
        fill: false
      }, { 
        data: [340, 355, 386, 420, 480],
        label: "Massa Magra",
        borderColor: "#F0B413",
        fill: false
      },
    ]
  }
});

new Chart(document.getElementById("bar-chart-grouped"), {
    type: 'bar',
    data: {
      labels: ["1900", "1950", "1999", "2050"],
      datasets: [
        {
          label: "Peso",
          backgroundColor: "#2e3192",
          data: [133,221,783,2478]
        }, {
          label: "Altura",
          backgroundColor: "#F0B413",
          data: [408,547,675,734]
        }
      ]
    }
});
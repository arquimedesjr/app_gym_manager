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
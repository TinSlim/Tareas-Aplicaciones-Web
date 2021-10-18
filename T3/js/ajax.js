function graph_1(url) {

    let xhr = new XMLHttpRequest();
    xhr.open('GET',url);
    xhr.timeout = 800;
    xhr.responseType = 'json';
    let n_response = {fechas : [],conteos : []};
    xhr.onload = function () {
        n_response = xhr.response;
        const data = {
            labels: n_response["fechas"],
            datasets: [{
                label: 'Avistamientos por día',
                backgroundColor: '#8bc700',
                borderColor: '#8bc700',
                data: n_response["conteos"],
            }]
        };
        const config = {
        type: 'line',
        data,
        options: {}
        };
          
        var myChart = new Chart(
            document.getElementById('myChart1'),
            config
        );
    }
    xhr.onerror = function () {
        alert("Error")
    }
    xhr.send();
}

function graph_2(url) {

    let xhr = new XMLHttpRequest();
    xhr.open('GET',url);
    xhr.timeout = 800;
    xhr.responseType = 'json';
    let n_response = {fechas : [],conteos : []};
    xhr.onload = function () {
        n_response = xhr.response;
        const data = {
            labels: n_response["tipos"],
            datasets: [
              {
                label: 'Dataset 1',
                data: n_response["conteos"],
                backgroundColor: ['rgb(1, 132,99)','rgb(99, 132,1)','#8bc700'],
              }
            ]
          };
        const config = {
            type: 'pie',
            data: data,
            options: {
              responsive: true,
              plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: ''
                }
              }
            },
          };
          
        var myChart = new Chart(
            document.getElementById('myChart2'),
            config
        );
    }
    xhr.onerror = function () {
        alert("Error")
    }
    xhr.send();
}

function graph_3(url) {

    let xhr = new XMLHttpRequest();
    xhr.open('GET',url);
    xhr.timeout = 800;
    xhr.responseType = 'json';
    let n_response = {fechas : [],conteos : []};
    xhr.onload = function () {
        n_response = xhr.response;
        

    const data = {
        labels: n_response["meses"],
        datasets: [
            {
            label: 'Vivo',
            data: n_response["vivo"],
            borderColor: 'rgb(1, 132,99)',
            backgroundColor: 'rgb(1, 132,99)',
            },
            {
            label: 'Muerto',
            data: n_response["muerto"],
            borderColor: 'rgb(99, 132,1)',
            backgroundColor: 'rgb(99, 132,1)',
            },
            {
            label: 'No sé',
            data: n_response["no sé"],
            borderColor: '#8bc700',
            backgroundColor: '#8bc700',
            }
        ]
    };


    const config = {
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Chart.js Bar Chart'
            }
            }
        },
        };
          
        var myChart = new Chart(
            document.getElementById('myChart3'),
            config
        );
    }
    xhr.onerror = function () {
        alert("Error")
    }
    xhr.send();
}

function draw_graphs () {
    graph_1("../../cgi-bin/T3/api1.py"); //TODO cambiar por anakena
    graph_2("../../cgi-bin/T3/api2.py");
    graph_3("../../cgi-bin/T3/api3.py");
}
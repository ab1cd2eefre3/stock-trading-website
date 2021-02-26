document.addEventListener('DOMContentLoaded', function() {
    const stockSymbol = window.location.pathname.split('/')[2];

    document.getElementById("1m").addEventListener('click', () => getStock(stockSymbol, "1m"));
    document.getElementById("3m").addEventListener('click', () => getStock(stockSymbol, "3m"));
    document.getElementById("6m").addEventListener('click', () => getStock(stockSymbol, "6m"));
    document.getElementById("ytd").addEventListener('click', () => getStock(stockSymbol, "ytd"));
    document.getElementById("1y").addEventListener('click', () => getStock(stockSymbol, "1y"));
    document.getElementById("2y").addEventListener('click', () => getStock(stockSymbol, "2y"));
    document.getElementById("5y").addEventListener('click', () => getStock(stockSymbol, "5y"));
})


function getStock(symbol, range) {

    document.getElementById('myChart').innerHTML = '';
    var label = [];
    var chart_data = [];
    

    fetch(`https://sandbox.iexapis.com/stable/stock/${symbol}/chart/${range}?token=Tpk_e5aea29c0d474106b4ecef9d449d122e`)
    .then((response) => {
        return response.json();
    })

    .then((data) => {
        data.forEach((element) => {
            label.push(String(element.date));
            chart_data.push(Number(element.close));
        })

        var ctx = document.getElementById('myChart').getContext('2d');
        var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'line',

            // The data for our dataset
            data: {
                labels: label,
                datasets: [{
                    label: 'Close price in USD',
                    backgroundColor: 'rgb(255, 255, 255)',
                    borderColor: 'rgb(0, 0, 0)',
                    data: chart_data
                }]
            },

            // Configuration options go here
            options: {
                responsive: false
            }
        });
    })
}
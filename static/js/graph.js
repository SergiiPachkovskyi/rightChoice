$(document).ready(function(){
    var data = JSON.parse(document.getElementById("charts_data").value);

    Highcharts.chart('container', {
        chart: {
            type: 'column'
        },

        title: {
            text: 'Діаграма порівняння альтернатив'
        },

        yAxis: {
            title: {
                text: 'Глобальний пріоритет'
            }
        },

        xAxis: {
                categories: ['Альтернативи', '', '']
        },

        series: data.charts_alternatives.priorities_list
    });
});
google.load('visualization', '1.0', {'packages':['corechart']});
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'titulo' );
        data.addColumn('number', 'valor' );

        data.addRows([
          ['Abap', null ],
          ['Portal', null ],
          ['Java Engine', null ],
          ['Opentext', null ],
          ]);

        var options = {'title':'',
                       'width': '435',
                       'height': '131',
                       'backgroundColor':'transparent',
                       //'colors': ['#e0440e', '#e6693e', '#ec8f6e', '#f3b49f', '#f6c7b6'],
                       'chartArea':{left:60,top:0,width:'90%',height:'90%'},
                       //'pieHole': 0.1,
                       };

        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
        chart.draw(data, options);

        var timing = 5000;
        setInterval(function() {
          var abap = $('#instancias_abap_count').html();
          data.setValue(0, 1, abap);
          $( '#btn-loading' ).remove();
          chart.draw(data, options);
        }, timing);

        setInterval(function() {
          var portal = $('#instancias_portal_count').html();
          data.setValue(1, 1, portal);
          chart.draw(data, options);
        }, timing);

        setInterval(function() {
          var javaengine = $('#instancias_javaengine_count').html();
          data.setValue(2, 1, javaengine);
          chart.draw(data, options);
        }, timing);

        setInterval(function() {
          var opentext = $('#instancias_opentext_count').html();
          data.setValue(3, 1, opentext);
          chart.draw(data, options);
        }, timing);

      }
google.setOnLoadCallback(drawChart);


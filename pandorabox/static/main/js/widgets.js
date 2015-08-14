//var danger_count = document.getElementById("danger_count");
//var warning_count = document.getElementById("warning_count");
//var instancias_count = document.getElementById("instancias_count");
var instancias_abap_count = document.getElementById("instancias_abap_count");
var instancias_portal_count = document.getElementById("instancias_portal_count");
var instancias_javaengine_count = document.getElementById("instancias_javaengine_count");
var instancias_opentext_count = document.getElementById("instancias_opentext_count");

swampdragon.onChannelMessage(function (channels, message) {
    danger_count.textContent = message.data.danger_count;
    warning_count.textContent = message.data.warning_count;
    instancias_count.textContent = message.data.instancias_count;
    instancias_abap_count.textContent = message.data.instancias_abap_count;
    instancias_portal_count.textContent = message.data.instancias_portal_count;
    instancias_javaengine_count.textContent = message.data.instancias_javaengine_count;
    instancias_opentext_count.textContent = message.data.instancias_opentext_count;
});

$(function () {
    var options = {
        cell_height: 80,
        vertical_margin: 10
    };
    $('.grid-stack').gridstack(options);
});


google.load('visualization', '1.0', {'packages':['corechart']});
google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'titulo' );
        data.addColumn('number', 'valor' );

        data.addRows([
          ['Abap', 1 ],
          ['Portal', 1 ],
          ['Java Engine', 1 ],
          ['Opentext', 1 ],
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
       
        setInterval(function() {
          data.setValue(0, 1, 20 + Math.round(60 * Math.random()));
          chart.draw(data, options);
        }, 4000);

        setInterval(function() {
          data.setValue(1, 1, 20 + Math.round(60 * Math.random()));
          chart.draw(data, options);
        }, 4000);

        setInterval(function() {
          data.setValue(2, 1, 20 + Math.round(60 * Math.random()));
          chart.draw(data, options);
        }, 4000);

        setInterval(function() {
          data.setValue(3, 1, 20 + Math.round(60 * Math.random()));
          chart.draw(data, options);
        }, 4000);


      }

//----------------------------------------------------------------------
//----------------------------------------------------------------------

/***************************************
// Widget - System Counter
*///////////////////////////////////////
var max_widget = 2; // maximo numero de widgets
var x = 1; // numero inicial de widgets

// if cookie exist
var CookieSet = Cookies.get('widget_counter_node_x');
if (CookieSet == null) {
var widget_counter_node_x = 0;
}
if (CookieSet != null) {
var test = Cookies.get('widget_counter_node_x');
var widget_counter_node_x = test;
//$('#tests').append("test");
}

function do_widget_counter() {
    // main el
    var el = $.parseHTML("<div id='widget_counter'><div class=\"grid-stack-item-content\"/>\
      <div class='btn-group btn-group-xs pull-right btn-group-box'>\
        <button type='button' class='btn btn-default dropdown-toggle' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false'>\
          <span class='glyphicon glyphicon-cog'></span>\
          </button>\
        <button id='del_widget_counter' type='button' class='btn btn-default' aria-haspopup='true' aria-expanded='false'>\
          <span class='glyphicon glyphicon-remove'></span>\
          </button>\
        <ul class='dropdown-menu'>\
          <li id='opt01'><a href='#'>chart</a></li>\
          <li id='opt02'><a href='#'>opcion2</a></li>\
          </ul>\
      </div>\
    <h4>System Counter</h4>\
    <div/>");
    var grid = $('.grid-stack').data('gridstack');
    if(x < max_widget){ // Si x es menor que
    grid.add_widget(el, widget_counter_node_x, 0, 4, 2, false);
    grid.resizable('.grid-stack-item', false );
    x++; //add al contador
    //grid.move(el, widget_counter_node_x, 0); // Mover el objecto grid

    // Cookies
    el = $('#widget_counter');   // definimos el al objecto
    var node = $(el).data('_gridstack_node');   // recuperamos posicion del objecto
    $('#tests').append(node.x, node.y, node.height, node.width );
    Cookies.set('widget_counter_node_x', node.x, { expires: 10 });
    Cookies.set('widget_counter_node_y', node.y, { expires: 10 });

    // On drag stop - Cookies
    $('.grid-stack').on('dragstop', function (event, ui) {
      var grid = this;
      var element = event.target;
      el = $('#widget_counter')   // definimos el al objecto
      var node = $(el).data('_gridstack_node');   // recuperamos posicion del objecto
      $('#tests').append(node.x, node.y, node.height, node.width );
      Cookies.set('widget_counter_node_x', node.x, { expires: 10 });
      Cookies.set('widget_counter_node_y', node.y, { expires: 10 });
      });
   }
// BOTON 01
function do_opt01_01() {
//$( '#widget_counter' ).append( '<li><b>TOTAL SAP instances:</b> <b id=ainstancias_count></b></li>' );
}
$('#opt01').on('click', function() { do_opt01_01() });
$('<div style="position:relative; left:10px;"></div>').attr('id','chart_div').appendTo('#widget_counter');

// BOTON 02
$(document).on('click','#opt02', function () {
  var grid = $('.grid-stack').data('gridstack');
  var e_instancias_count = $('<b></b>');
  e_instancias_count.attr('id', 'instancias_count');
  $('#widget_counter').append(e_instancias_count);
  el = $('#widget_counter')   // definimos el al objecto
    //grid.move(el, 3, 0);   // se puede mover el objecto
  var node = $(el).data('_gridstack_node');   // recuperamos posicion del objecto
    //$('#tests').append(node.x, node.y, node.height, node.width );
    //Cookies.set('position', {node.x:node.x}, { expires: 14 });
}); // Fin - OPT2

// Close button
$(document).on('click','#del_widget_counter', function () {
    ele01 = $('#widget_counter');
    var grid = $('.grid-stack').data('gridstack');

    el = $('#widget_counter')   // definimos el al objecto
    var node = $(el).data('_gridstack_node');   // recuperamos posicion del objecto
    $('#tests').append(node.x, node.y, node.height, node.width );
    Cookies.remove('widget_counter_node_x');
    Cookies.remove('widget_counter_node_y');

    grid.remove_widget(ele01);
    x--; // eliminamos del contador
}); // Fin - Close button

} // fin - do_widget_counter


/***************************************
// Widget - Last Alerts
*///////////////////////////////////////
var max_widget = 2; // maximo numero de widgets
var x01 = 1; // numero inicial de widgets

var CookieSet = Cookies.get('widget_Alerts_node_x');
if (CookieSet == null) {
var widget_Alerts_node_x = 0;
}
if (CookieSet != null) {
var test = Cookies.get('widget_Alerts_node_x');
var widget_Alerts_node_x = test;
}

function do_widget_Alerts() {
    var el = $.parseHTML("<div id='widget_Alerts'><div class=\"grid-stack-item-content\"/>\
      <div class='btn-group btn-group-xs pull-right btn-group-box'>\
        <button type='button' class='btn btn-default dropdown-toggle' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false'>\
          <span class='glyphicon glyphicon-cog'></span>\
          </button>\
        <button id='del_widget_Alerts' type='button' class='btn btn-default' aria-haspopup='true' aria-expanded='false'>\
          <span class='glyphicon glyphicon-remove'></span>\
          </button>\
          </ul>\
      </div>\
    <h4>Alerts</h4>\
    <div/>");
    var grid = $('.grid-stack').data('gridstack');
    if(x01 < max_widget){ 
    grid.add_widget(el, widget_Alerts_node_x, 0, 4, 2, false);
    grid.resizable('.grid-stack-item', false );
    x01++; //add al contador

    el = $('#widget_Alerts'); 
    var node = $(el).data('_gridstack_node');
    Cookies.set('widget_Alerts_node_x', node.x, { expires: 10 });
    Cookies.set('widget_Alerts_node_y', node.y, { expires: 10 });

    $('.grid-stack').on('dragstop', function (event, ui) {
      var grid = this;
      var element = event.target;
      el = $('#widget_Alerts')
      var node = $(el).data('_gridstack_node');
      Cookies.set('widget_Alerts_node_x', node.x, { expires: 10 });
      Cookies.set('widget_Alerts_node_y', node.y, { expires: 10 });
      });
   }

// Close button
$(document).on('click','#del_widget_Alerts', function () {
    ele01 = $('#widget_Alerts');
    var grid = $('.grid-stack').data('gridstack');

    el = $('#widget_Alerts')
    var node = $(el).data('_gridstack_node'); 
    Cookies.remove('widget_Alerts_node_x');
    Cookies.remove('widget_Alerts_node_y');

    grid.remove_widget(ele01);
    x01--; // eliminamos del contador
}); // Fin - Close button

var e_warning_count = $('<b></b>');
e_warning_count.attr('id', 'warning_count');
$('#widget_Alerts').append(e_warning_count);

var e_danger_count = $('<b></b>');
e_danger_count.attr('id', 'danger_count');
$('#widget_Alerts').append(e_danger_count);

}

//----------------------------------------------------------------------
//----------------------------------------------------------------------


//swampdragon ready
swampdragon.ready(function() {
    swampdragon.subscribe('sys', 'sysinfo', null);
});

// Inicio de funciones
$( document ).ready(function() {
var CookieSet = Cookies.get('widget_counter_node_x');
var CookieSet_Alerts = Cookies.get('widget_Alerts_node_x');

if (CookieSet == null) {
  var widget_counter_node_x = 0;
  $('#tests').append("Cookie NO existe, no se recrean los objetos");
}if (CookieSet != null) {
  $('#tests').append("Cookie SI existe, se recrean los objetos");
  $(document).ready(function() { do_widget_counter() });
}

if (CookieSet_Alerts == null) {
  var widget_Alerts_node_x = 0;
}if (CookieSet_Alerts != null) {
  $(document).ready(function() { do_widget_Alerts() });
}

});

$('#add_widget_counter').on('click', function() { do_widget_counter() });
$('#add_widget_Alerts').on('click', function() { do_widget_Alerts() });



$(function () {
    var options = {
        cell_height: 80,
        vertical_margin: 10
    };
    $('.grid-stack').gridstack(options);
});


////////////////////////////
// WIDGET Contador
////////////////////////////
var max_widget = 1; // maximo numero de widgets
var x = 0; // numero inicial de widgets

$(document.body).on('click','#add_widget_counter', function () {
    var el = $.parseHTML("<div><div class=\"grid-stack-item-content\"/>\
<li><b></b></li>\
<div/>");
    var grid = $('.grid-stack').data('gridstack');
    if(x < max_widget){ // Si x es menor que
    grid.add_widget(el, 0, 0, 4, 2, true);
    grid.resizable('.grid-stack-item', false );
    x++; //add al contador

   }
});

$('#del_widget_counter').click(function(){
    ele01 = $('#widget_counter');
    var grid = $('.grid-stack').data('gridstack');
    grid.remove_widget(ele01);
    x--; // eliminamos del contador
});

////////////////////////////
// WIDGET last 5 alerts
////////////////////////////
var max_widget01 = 1; // maximo numero de widgets
var x01 = 0; // numero inicial de widgets
$('#add_widget_last5alerts').click(function(){
    var el = $.parseHTML("<div id=widget_last5alerts><div class=\"grid-stack-item-content\"/>\
    segundowidget\
    <div/>");
    var grid = $('.grid-stack').data('gridstack');
    if(x01 < max_widget01){ // Si x es menor que
    grid.add_widget(el, 1, 1, 4, 2, true);
    grid.resizable('.grid-stack-item', false );
    x01++; //add al contador

   }
});

$('#del_widget_last5alerts').click(function(){
    ele01 = $('#widget_last5alerts');
    var grid = $('.grid-stack').data('gridstack');
    grid.remove_widget(ele01);
    x01--; // eliminamos del contador
});



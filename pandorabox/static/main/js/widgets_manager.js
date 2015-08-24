var e_danger_count = $('<b></b>');
e_danger_count.attr('id', 'danger_count');
$('#tests').append(e_danger_count);

var e_warning_count = $('<b></b>');
e_warning_count.attr('id', 'warning_count');
$('#tests').append(e_warning_count);

var e_instancias_count = $('<b></b>');
e_instancias_count.attr('id', 'instancias_count');
$('#tests').append(e_instancias_count);

var e_instancias_abap_count = $('<b></b>');
e_instancias_abap_count.attr('id', 'instancias_abap_count');
$('#tests').append(e_instancias_abap_count);

var e_instancias_portal_count = $('<b></b>');
e_instancias_portal_count.attr('id', 'instancias_portal_count');
$('#tests').append(e_instancias_portal_count);

var e_instancias_javaengine_count = $('<b></b>');
e_instancias_javaengine_count.attr('id', 'instancias_javaengine_count');
$('#tests').append(e_instancias_javaengine_count);

var e_instancias_opentext_count = $('<b></b>');
e_instancias_opentext_count.attr('id', 'instancias_opentext_count');
$('#tests').append(e_instancias_opentext_count);

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
          <li id='opt01'><a href='#'>Chart Options</a></li>\
          </ul>\
      </div>\
    <h4>System Counter</h4>\
    <button id='btn-loading' class='btn btn-lg btn-success' disabled><span class='glyphicon glyphicon-refresh glyphicon-refresh-animate'></span></button>\
    <div/>");
    var grid = $('.grid-stack').data('gridstack');
    if(x < max_widget){ // Si x es menor que
    grid.add_widget(el, widget_counter_node_x, 0, 4, 2, false);
    grid.resizable('.grid-stack-item', false );
    x++; //add al contador
    $('#add_widget_counter').addClass('hidden');
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
//$('<div style="position:relative; left:10px;"></div>').attr('id','chart_div').appendTo('#widget_counter');
$('#myModal').modal('show')
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
    $('#add_widget_counter').removeClass('hidden');
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
    $('#add_widget_Alerts').addClass('hidden');

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

} //fin do_widget_alerts

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
    $('#add_widget_Alerts').removeClass('hidden');
}); // Fin - Close button

}

/***************************************
// Widget - Manager
*///////////////////////////////////////
var max_widget = 2;
var x02 = 1;

var CookieSet = Cookies.get('widget_manager_node_x');
if (CookieSet == null) {
var widget_manager_node_x = 0;
}
if (CookieSet != null) {
var test = Cookies.get('widget_manager_node_x');
var widget_manager_node_x = test;
}

function do_widget_manager() {
    var el = $.parseHTML("<div id='widget_manager'><div class=\"grid-stack-item-content\"/>\
      <div class='btn-group btn-group-xs pull-right btn-group-box'>\
        <button type='button' class='btn btn-default dropdown-toggle' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false'>\
          <span class='glyphicon glyphicon-cog'></span>\
          </button>\
        <button id='del_widget_manager' type='button' class='btn btn-default' aria-haspopup='true' aria-expanded='false'>\
          <span class='glyphicon glyphicon-remove'></span>\
          </button>\
        <ul class='dropdown-menu'>\
          <li id='opt01'><a href='#'>Locker Manager</a></li>\
          <li id='opt02'><a href='#'>System's Manager</a></li>\
          </ul>\
      </div>\
    <h4>System Manager</h4>\
<form id='manager-form-01' method='POST'>\
  <div class='form-group' id='manager-form-group'>\
  </div>\
  <button type='submit' class='btn btn-default input-sm' id='manager-form-submit'>Submit</button>\
</form>\
<div/>\
    <div/>");
    var grid = $('.grid-stack').data('gridstack');
    if(x02 < max_widget){ 
    grid.add_widget(el, widget_manager_node_x, 0, 4, 2, false);
    grid.resizable('.grid-stack-item', false );
    x02++;
    $('#add_widget_manager').addClass('hidden');
    el = $('#widget_manager'); 
    var node = $(el).data('_gridstack_node');
    $('#tests').append(node.x, node.y, node.height, node.width );
    Cookies.set('widget_manager_node_x', node.x, { expires: 10 });
    Cookies.set('widget_manager_node_y', node.y, { expires: 10 });
    $('.grid-stack').on('dragstop', function (event, ui) {
      var grid = this;
      var element = event.target;
      el = $('#widget_manager')
      var node = $(el).data('_gridstack_node');
      $('#tests').append(node.x, node.y, node.height, node.width );
      Cookies.set('widget_manager_node_x', node.x, { expires: 10 });
      Cookies.set('widget_manager_node_y', node.y, { expires: 10 });
      });
var title = "{{title}}"
var username = "{{username}}"
var password = "{{password}}"
var url = "{{url}}"
var notes = "{{notes}}"
input_title = jQuery('<input type="text" class="form-control input-sm" id="manager-form-title" name="title" value="" placeholder="Title">');
input_username = jQuery('<input type="text" class="form-control input-sm" id="manager-form-username" name="username" value="" placeholder="username">');
input_password = jQuery('<input type="text" class="form-control input-sm" id="manager-form-password" name="password" value="" placeholder="password">');
input_url = jQuery('<input type="text" class="form-control input-sm" id="manager-form-url" name="url" value="" placeholder="url">');
input_notes = jQuery('<input type="text" class="form-control input-sm" id="manager-form-notes" name="notes" value="" placeholder="notes">');
jQuery('#manager-form-group').append(input_title, input_username, input_password, input_url, input_notes);
   }
// BOTON 01
function do_opt01_01() {
}
$('#opt01').on('click', function() { do_opt01_01() });
// BOTON 02
$(document).on('click','#opt02', function () {
}); // Fin - OPT2

// Close button
$(document).on('click','#del_widget_manager', function () {
    ele01 = $('#widget_manager');
    var grid = $('.grid-stack').data('gridstack');

    el = $('#widget_manager')
    var node = $(el).data('_gridstack_node');
    $('#tests').append(node.x, node.y, node.height, node.width );
    Cookies.remove('widget_manager_node_x');
    Cookies.remove('widget_manager_node_y');

    grid.remove_widget(ele01);
    x02--; // eliminamos del contador
    $('#add_widget_manager').removeClass('hidden');
}); // Fin - Close button

} // fin - do_widget_manager

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
var CookieSet_manager = Cookies.get('widget_manager_node_x');

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

if (CookieSet_manager == null) {
  var widget_manager_node_x = 0;
}if (CookieSet_manager != null) {
  $(document).ready(function() { do_widget_manager() });
}

});

$('#add_widget_counter').on('click', function() { do_widget_counter() });
$('#add_widget_Alerts').on('click', function() { do_widget_Alerts() });
$('#add_widget_manager').on('click', function() { do_widget_manager() });


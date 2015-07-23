var danger_count = document.getElementById("danger_count");
var warning_count = document.getElementById("warning_count");
var instancias_count = document.getElementById("instancias_count");
var instancias_abap_count = document.getElementById("instancias_abap_count");
var instancias_portal_count = document.getElementById("instancias_portal_count");
var instancias_javaengine_count = document.getElementById("instancias_javaengine_count");
var instancias_opentext_count = document.getElementById("instancias_opentext_count");


swampdragon.onChannelMessage(function (channels, message) {
    danger_count.innerText = message.data.danger_count;
    warning_count.innerText = message.data.warning_count;
    instancias_count.innerText = message.data.instancias_count;
    instancias_abap_count.innerText = message.data.instancias_abap_count;
    instancias_portal_count.innerText = message.data.instancias_portal_count;
    instancias_javaengine_count.innerText = message.data.instancias_javaengine_count;
    instancias_opentext_count.innerText = message.data.instancias_opentext_count;

});


swampdragon.ready(function() {
    swampdragon.subscribe('sys', 'sysinfo', null);
});


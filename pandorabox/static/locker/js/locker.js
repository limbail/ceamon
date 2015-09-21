/**
## Ocultar pass en tabla 
**/
jQuery(function() {
    jQuery('table td[id=password]').hover(function() {
        jQuery(this).find("div.hidepass").show();
        jQuery(this).find("div.showpass").hide();

    }, function() {
        jQuery(this).find("div.hidepass").hide();
        jQuery(this).find("div.showpass").show();
    });

    $('#table').on('all.bs.table', function (e, name, args) {
        jQuery('table td[id=password]').hover(function() {
        jQuery(this).find("div.hidepass").show();
        jQuery(this).find("div.showpass").hide();

    }, function() {
        jQuery(this).find("div.hidepass").hide();
        jQuery(this).find("div.showpass").show();
    });
    });
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


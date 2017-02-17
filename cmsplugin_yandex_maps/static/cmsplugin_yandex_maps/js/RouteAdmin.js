function getParameterByName(name, url) {
    if (!url) {
      url = window.location.href;
    }
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function results(){
	var val = parseInt($('#id_results').val());
	console.log(val);
	if (val > 1){
		$('div.field-box.field-additional_routes_collor').show();
	} else {
		$('div.field-box.field-additional_routes_collor').hide();
	}
}

$(document).ready(function(){
	var popup = getParameterByName('_popup');
	if (popup == "1"){
		var referrer = document.referrer;
		if (referrer.indexOf('placemark') != -1){
			$('#route_placemarks_set-group').hide();
		} else if (referrer.indexOf('edit-plugin') != -1){
			$('#yandexmaps_routes_set-group').hide();
		} else if (referrer.indexOf('add-plugin') != -1){
			$('#yandexmaps_routes_set-group').hide();
		}
	}
	results();
	$('#id_results').on('keyup' , results);
	$('#id_results').on('mouseleave' , results);
});
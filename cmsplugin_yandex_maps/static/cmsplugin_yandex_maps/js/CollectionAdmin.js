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

$(document).ready(function(){
	var popup = getParameterByName('_popup');
	if (popup == "1"){
		var referrer = document.referrer;
		if (referrer.indexOf('placemark') != -1){
			$('#collection_placemarks_set-group').hide();
		} else if (referrer.indexOf('edit-plugin') != -1){
			$('#yandexmaps_collections_set-group').hide();
		} else if (referrer.indexOf('add-plugin') != -1){
			$('#yandexmaps_collections_set-group').hide();
		}
	}
});
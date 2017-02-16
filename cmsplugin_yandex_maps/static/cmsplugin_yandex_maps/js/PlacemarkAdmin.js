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

function auto_coordinates(){
	if ($('#id_auto_coordinates').prop("checked")){
		$("div.form-row.field-place").show();
		$("div.form-row.field-place label").addClass('required');
		$("div.form-row.field-place_lt.field-place_lg").hide();
		$("div.form-row.field-place_lt.field-place_lg label").removeClass('required');
	} else {
		$("div.form-row.field-place").hide();
		$("div.form-row.field-place label").removeClass('required');
		$("div.form-row.field-place_lt.field-place_lg").show();
		$("div.form-row.field-place_lt.field-place_lg label").addClass('required');
	}
}

$(document).ready(function(){
	var popup = getParameterByName('_popup');
	if (popup == "1"){
		$('div.inline-group').hide();
	}
	auto_coordinates();
	$('#id_auto_coordinates').on('change', auto_coordinates);
});
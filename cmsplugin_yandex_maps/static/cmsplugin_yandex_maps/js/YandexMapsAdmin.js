function route(){
	if ($('#id_route').prop("checked")){
		$('#id_auto_placement').prop("checked", false);
		$('div.form-row.field-auto_placement').hide();
	} else {
		$('div.form-row.field-auto_placement').show();
	}
}

function clusterisation(){
	if ($('#id_clusterisation').prop("checked")){
		$('#id_cluster_disable_click_zoom').parent().show();
		$('div.form-row.field-cluster_icon.field-cluster_color').show();
	} else {
		$('#id_cluster_disable_click_zoom').parent().hide();
		$('div.form-row.field-cluster_icon.field-cluster_color').hide();
	}
}

function auto_placement(){
	if ($('#id_auto_placement').prop("checked")){
		$('div.form-row.field-center_lt.field-center_lg').hide();
	} else {
		$('div.form-row.field-min_zoom.field-max_zoom').hide();
		$('div.form-row.field-center_lt.field-center_lg').show();
	}
}

function sizing(){
	switch ($('#id_sizing').val()){
		case "aspect":
		case "static":
			$('div.form-row.field-width.field-height').show();
			$('div.form-row.field-width.field-height label').addClass('required');
			break;
		case "auto":
			$('div.form-row.field-width.field-height').hide();
			$('div.form-row.field-width.field-height label').removeClass('required');
			break;
	}
}

function size_update_method(){
	switch ($('#id_size_update_method').val()){
		case "":
			$('div.form-row.field-jq_selector.field-jq_event').hide();
			$('div.form-row.field-jq_selector.field-jq_event label').removeClass('required');
			break;
		case "observer":
			$('div.field-box.field-jq_event').hide();
			$('div.form-row.field-jq_selector.field-jq_event').show();
			$('div.form-row.field-jq_selector.field-jq_event label').addClass('required');
			break;
		case "jq_event":
			$('div.field-box.field-jq_event').show();
			$('div.form-row.field-jq_selector.field-jq_event').show();
			$('div.form-row.field-jq_selector.field-jq_event label').addClass('required');
			break;
	}
}

$(document).ready(function(){
	route();
	$('#id_route').on('change', route);
	
	clusterisation();
	$('#id_clusterisation').on('change', clusterisation);
	
	auto_placement();
	$('#id_auto_placement').on('change', auto_placement);
	
	sizing();
	$('#id_sizing').on('change', sizing);
	
	size_update_method();
	$('#id_size_update_method').on('change', size_update_method);
});
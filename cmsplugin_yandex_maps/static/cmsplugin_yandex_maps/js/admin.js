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

function auto_coordinates(elem){
	if ($(elem).prop("checked")){
		$(elem).closest('fieldset').find("div.form-row.field-place").show();
		$(elem).closest('fieldset').find("div.form-row.field-place label").addClass('required');
		$(elem).closest('fieldset').find("div.form-row.field-place_lt.field-place_lg").hide();
		$(elem).closest('fieldset').find("div.form-row.field-place_lt.field-place_lg label").removeClass('required');
	} else {
		$(elem).closest('fieldset').find("div.form-row.field-place").hide();
		$(elem).closest('fieldset').find("div.form-row.field-place label").removeClass('required');
		$(elem).closest('fieldset').find("div.form-row.field-place_lt.field-place_lg").show();
		$(elem).closest('fieldset').find("div.form-row.field-place_lt.field-place_lg label").addClass('required');
	}
}

function icon_style(elem){
	switch ($(elem).val()){
		case "default":
			$(elem).closest('fieldset').find("div.field-box.field-icon_color").show();
			$(elem).closest('fieldset').find("div.field-box.field-icon_glif").hide();
			$(elem).closest('fieldset').find("div.field-box.field-icon_image").hide();
			$(elem).closest('fieldset').find("div.field-box.field-icon_image label").removeClass('required');
			$(elem).closest('fieldset').find("div.field-box.field-icon_caption").hide();
			$(elem).closest('fieldset').find("div.field-box.field-icon_circle").show();
			$(elem).closest('fieldset').find("div.form-row.field-icon_width.field-icon_height").hide();
			$(elem).closest('fieldset').find("div.form-row.field-icon_offset_horizontal.field-icon_offset_vertical").hide();
			$(elem).closest('fieldset').find("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").hide();
			break;
		case "stretchy":
			$(elem).closest('fieldset').find("div.field-box.field-icon_color").show();
			$(elem).closest('fieldset').find("div.field-box.field-icon_glif").hide();
			$(elem).closest('fieldset').find("div.field-box.field-icon_image").hide();
			$(elem).closest('fieldset').find("div.field-box.field-icon_image label").removeClass('required');
			$(elem).closest('fieldset').find("div.field-box.field-icon_caption").hide();
			$(elem).closest('fieldset').find("div.field-box.field-icon_circle").hide();
			$(elem).closest('fieldset').find("div.form-row.field-icon_width.field-icon_height").hide();
			$(elem).closest('fieldset').find("div.form-row.field-icon_offset_horizontal.field-icon_offset_vertical").hide();
			$(elem).closest('fieldset').find("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").hide();
			break;
		case "doted":
			$(elem).closest('fieldset').find("div.field-box.field-icon_color").show();
			$(elem).closest('fieldset').find("div.field-box.field-icon_glif").hide();
			$(elem).closest('fieldset').find("div.field-box.field-icon_image").hide();
			$(elem).closest('fieldset').find("div.field-box.field-icon_image label").removeClass('required');
			$(elem).closest('fieldset').find("div.field-box.field-icon_caption").show();
			$(elem).closest('fieldset').find("div.field-box.field-icon_circle").show();
			$(elem).closest('fieldset').find("div.form-row.field-icon_width.field-icon_height").hide();
			$(elem).closest('fieldset').find("div.form-row.field-icon_offset_horizontal.field-icon_offset_vertical").hide();
			$(elem).closest('fieldset').find("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").hide();
			break;
		case "glif":
			$(elem).closest('fieldset').find("div.field-box.field-icon_color").show();
			$(elem).closest('fieldset').find("div.field-box.field-icon_glif").show();
			$(elem).closest('fieldset').find("div.field-box.field-icon_image").hide();
			$(elem).closest('fieldset').find("div.field-box.field-icon_image label").removeClass('required');
			$(elem).closest('fieldset').find("div.field-box.field-icon_caption").hide();
			$(elem).closest('fieldset').find("div.field-box.field-icon_circle").show();
			$(elem).closest('fieldset').find("div.form-row.field-icon_width.field-icon_height").hide();
			$(elem).closest('fieldset').find("div.form-row.field-icon_offset_horizontal.field-icon_offset_vertical").hide();
			$(elem).closest('fieldset').find("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").hide();
			break;
		case "image":
			$(elem).closest('fieldset').find("div.field-box.field-icon_color").hide();
			$(elem).closest('fieldset').find("div.field-box.field-icon_glif").hide();
			$(elem).closest('fieldset').find("div.field-box.field-icon_image").show();
			$(elem).closest('fieldset').find("div.field-box.field-icon_image label").addClass('required');
			$(elem).closest('fieldset').find("div.field-box.field-icon_caption").show();
			$(elem).closest('fieldset').find("div.field-box.field-icon_circle").hide();
			$(elem).closest('fieldset').find("div.form-row.field-icon_width.field-icon_height").show();
			$(elem).closest('fieldset').find("div.form-row.field-icon_offset_horizontal.field-icon_offset_vertical").show();
			if ($(elem).closest('fieldset').find("input[name*='icon_caption']").prop("checked")){
				$(elem).closest('fieldset').find("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").show();
			} else {
				$(elem).closest('fieldset').find("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").hide();
			}
			break;
	}
}

function icon_caption(elem){
	if ($(elem).closest('fieldset').find('select[name*="icon_style"]').val() == 'image'){
		if ($(elem).prop("checked")){
			$(elem).closest('fieldset').find("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").show();
		} else {
			$(elem).closest('fieldset').find("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").hide();
		}
	}
}

function placemarks(event){
	if (event == 'init'){
		$('#placemark_set-group').find('input[name*="auto_coordinates"]').each(function(){
			auto_coordinates(this);
		});
		$('#placemark_set-group').on('change', 'input[name*="auto_coordinates"]', function(){
			auto_coordinates(this);
		});
		
		$('#placemark_set-group').find('select[name*="icon_style"]').each(function(){
			icon_style(this);
		});
		$('#placemark_set-group').on('change', 'select[name*="icon_style"]', function(){
			icon_style(this);
		});
		
		$('#placemark_set-group').find("input[name*='icon_caption']").each(function(){
			icon_caption(this);
		});
		$('#placemark_set-group').on('change', "input[name*='icon_caption']", function(){
			icon_caption(this);
		});
	} else {
		$('#placemark_set-group').last('input[name*="auto_coordinates"]').each(function(){
			auto_coordinates(this);
			$('#placemark_set-group').on('change', this, function(){
				auto_coordinates(this);
			});
		});
		
		$('#placemark_set-group').last('select[name*="icon_style"]').each(function(){
			icon_style(this);
			$('#placemark_set-group').on('change', this, function(){
				icon_style(this);
			});
		});
		
		$('#placemark_set-group').last("input[name*='icon_caption']").each(function(){
			icon_caption(this);
			$('#placemark_set-group').on('change', this, function(){
				icon_caption(this);
			});
		});
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
	
	placemarks("init");
	$('div.add-row').on("click", function(){
		placemarks("add_placemark");
	});
});


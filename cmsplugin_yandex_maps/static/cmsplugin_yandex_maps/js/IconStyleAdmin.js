function icon_style(){
	switch ($('#id_icon_style').val()){
		case "":
			$("div.field-box.field-icon_color").hide();
			$("div.field-box.field-icon_glif").hide();
			$("div.field-box.field-icon_image").hide();
			$("div.field-box.field-icon_image label").removeClass('required');
			$("div.field-box.field-icon_caption").hide();
			$('#id_icon_caption').prop("checked", false);
			$("div.field-box.field-icon_circle").hide();
			$("div.form-row.field-icon_width.field-icon_height").hide();
			$("div.form-row.field-icon_offset_horizontal.field-icon_offset_vertical").hide();
			$("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").hide();
			break;
		case "default":
			$("div.field-box.field-icon_color").show();
			$("div.field-box.field-icon_glif").hide();
			$("div.field-box.field-icon_image").hide();
			$("div.field-box.field-icon_image label").removeClass('required');
			$("div.field-box.field-icon_caption").hide();
			$('#id_icon_caption').prop("checked", false);
			$("div.field-box.field-icon_circle").show();
			$("div.form-row.field-icon_width.field-icon_height").hide();
			$("div.form-row.field-icon_offset_horizontal.field-icon_offset_vertical").hide();
			$("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").hide();
			break;
		case "stretchy":
			$("div.field-box.field-icon_color").show();
			$("div.field-box.field-icon_glif").hide();
			$("div.field-box.field-icon_image").hide();
			$("div.field-box.field-icon_image label").removeClass('required');
			$("div.field-box.field-icon_caption").hide();
			$('#id_icon_caption').prop("checked", true);
			$("div.field-box.field-icon_circle").hide();
			$("div.form-row.field-icon_width.field-icon_height").hide();
			$("div.form-row.field-icon_offset_horizontal.field-icon_offset_vertical").hide();
			$("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").hide();
			break;
		case "doted":
			$("div.field-box.field-icon_color").show();
			$("div.field-box.field-icon_glif").hide();
			$("div.field-box.field-icon_image").hide();
			$("div.field-box.field-icon_image label").removeClass('required');
			$("div.field-box.field-icon_caption").show();
			$("div.field-box.field-icon_circle").show();
			$("div.form-row.field-icon_width.field-icon_height").hide();
			$("div.form-row.field-icon_offset_horizontal.field-icon_offset_vertical").hide();
			$("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").hide();
			break;
		case "glif":
			$("div.field-box.field-icon_color").show();
			$("div.field-box.field-icon_glif").show();
			$("div.field-box.field-icon_image").hide();
			$("div.field-box.field-icon_image label").removeClass('required');
			$("div.field-box.field-icon_caption").hide();
			$('#id_icon_caption').prop("checked", false);
			$("div.field-box.field-icon_circle").show();
			$("div.form-row.field-icon_width.field-icon_height").hide();
			$("div.form-row.field-icon_offset_horizontal.field-icon_offset_vertical").hide();
			$("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").hide();
			break;
		case "image":
			$("div.field-box.field-icon_color").hide();
			$("div.field-box.field-icon_glif").hide();
			$("div.field-box.field-icon_image").show();
			$("div.field-box.field-icon_image label").addClass('required');
			$("div.field-box.field-icon_caption").show();
			$("div.field-box.field-icon_circle").hide();
			$("div.form-row.field-icon_width.field-icon_height").show();
			$("div.form-row.field-icon_offset_horizontal.field-icon_offset_vertical").show();
			if ($('#id_icon_caption').prop("checked")){
				$("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").show();
			} else {
				$("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").hide();
			}
			break;
	}
}

function icon_caption(){
	if ($('#id_icon_style').val() == 'image'){
		if ($('#id_icon_caption').prop("checked")){
			$("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").show();
		} else {
			$("div.form-row.field-icon_content_offset_horizontal.field-icon_content_offset_vertical").hide();
		}
	}
}

$(document).ready(function(){icon_style();
	$('#id_icon_style').on('change', icon_style);
	
	icon_caption();
	$('#id_icon_caption').on('change', icon_caption);
});
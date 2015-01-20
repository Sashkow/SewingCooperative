$(document).ready(function(){
	$('#dice_value').html("click the button");
	$('#rolldice_button').click(function(){
		
		$.get('/rolldice/ajax/', function(data){
			var dice_value = data.substr(0,data.indexOf("|"));
			console.log(dice_value);
			var location_url = data.substr(data.indexOf("|")+1,data.length);
			console.log(location_url);
	       $('#dice_value').html(dice_value);
	       $('#location_img').attr("src", location_url);
   		});
	});

});


			// $(".img_table_cell a img").each(function(i){
			// 	// refresh all images
			// 	d = new Date();
			// 	var imgsrc = $(this).attr("src");
			// 	console.log(imgsrc);
			// 	if (imgsrc.indexOf("?")!=-1)
			// 		imgsrc=imgsrc.substr(0,imgsrc.indexOf("?"));
			// 	console.log(imgsrc);
		 //        $(this).attr("src", imgsrc+"?"+d.getTime());

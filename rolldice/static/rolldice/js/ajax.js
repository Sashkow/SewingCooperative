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

$('#form').submit(function(e){
    $.post('/rolldice/advert', $(this).serialize(), function(data){
    	
       $('.message').html(data.message);
       $('id_dice1').dice_value(data+1)
    });
    e.preventDefault();
});


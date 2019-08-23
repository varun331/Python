$(document).ready(function() {
	//$('form').on('submit', function(event) {
	$('#button_1').click(function(e) {
		$.ajax({
			data : {
				id: $(this).val()
				//name : $('#nameInput').val(),
				//email : $('#emailInput').val()
			},
			type : 'POST',
			url : '/process',
			cache:false,
			//sucess:function(response) {
			//	$('#output').text(response).show();
			//},
			//error:function(x){
			//	var c =x;
			//}
		//});
		})
		.done(function(data) {
			//$('#output').text(data.output).show();
			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#output').text(data.name);
				$('#errorAlert').hide();
			}
	});
		event.preventDefault();
	});


	$('#button_2').click(function(j) {
		

		$.ajax({
			data : {
				
				output : $('#output').text(),
				//email : $('#emailInput').val()
			},
	
			type : 'POST',
			url : '/email',
			cache:false,
			
		})
		.done(function(data) {
			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}
	});
		event.preventDefault();

});
});

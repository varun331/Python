$(document).ready(function() {

	//$('form').on('submit', function(event) {
	$("button").click(function(e) {

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
				$('#errorAlert').hide();
			}

	});

		event.preventDefault();

});

});
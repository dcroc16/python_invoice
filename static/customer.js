window.addEventListener('load', function(){

	var customerNumber = document.getElementById('customer_number');
	var customerTable = document.getElementById('customer_table');

	customerNumber.addEventListener('click', function(e){
		this.value = (customerTable.rows[customerTable.rows.length-1].cells[0].innerHTML)*1 + 1;
	});

	customerTable.addEventListener('click', function(e){
		var msg = document.getElementById('message_box');
		msg.innerHTML = "<form action='/deleteCustomer/" + e.target.innerHTML + "' method='POST'> \
						Would you like to delete customer: " + e.target.innerHTML + "? \
						<br><input class='bttn' type='submit' value='yes' /></form> \
						<form action='/customers' method='GET'> \
						<input class='bttn' type='submit' value='no' /></form><br><br>";
	});



},false);


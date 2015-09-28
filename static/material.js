window.addEventListener('load', function(){

	var materialNumber = document.getElementById('material_number');
	var materialTable = document.getElementById('material_table');

	materialNumber.addEventListener('click', function(e){
		this.value = (materialTable.rows[1].cells[0].innerHTML)*1 + 1;
	});

	materialTable.addEventListener('click', function(e){
		var msg = document.getElementById('message_box');
		msg.innerHTML = "<form action='/deleteMaterial/" + e.target.innerHTML + "' method='POST'> \
						Would you like to delete material: " + e.target.innerHTML + "? \
						<br><input class='bttn' type='submit' value='yes' /></form> \
						<form action='/materials' method='GET'> \
						<input class='bttn' type='submit' value='no' /></form><br><br>";
	});



},false);


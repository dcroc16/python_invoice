


var addRow = function(){

		var desc = document.getElementsByClassName('desc_options');

		var table = document.getElementById('invoice_table');

		line_count = table.rows.length;

		var row = table.insertRow(line_count -1);


		
		row.innerHTML = "<tr> \
								<td><input class='inputBox' name='material' type='textbox'/></td> \
								<td> \
									<select value=' ' name='desc' id='options_" + (line_count - 1) + "'> \
									</select> \
								</td> \
							    <td><input class='inputBox' name='qty' type='textbox'/></td> \
							    <td><input class='inputBox' name='uom' type='textbox'/></td> \
							    <td><input class='inputBox' name='price' type='textbox'/></td> \
							    <td><input class='inputBox' name='amount' type='textbox'/></td> \
						</tr>";

		var newSelect = document.getElementById('options_' + (line_count -1).toString());
		console.log(newSelect)
		
		for(var i = 0; i < desc.length; i++){
			if(i===0){
				var nextOption = document.createElement("option");

				nextOption.value = 'blank';
				newSelect.appendChild(nextOption);

				var nextOption2 = document.createElement("option");

				nextOption2.value = desc[i].value;
				nextOption2.innerHTML = desc[i].innerHTML;
				newSelect.appendChild(nextOption);
			} else {

				var nextOption = document.createElement("option");

				nextOption.value = desc[i].value;
				nextOption.innerHTML = desc[i].innerHTML;
				newSelect.appendChild(nextOption);

			}

		}




	};

window.addEventListener('load', function(){

	var tbl = document.getElementById('invoice_table');
	
	tbl.addEventListener('change', function(){
		console.log('change');
		for( var i = 0; i < tbl.rows.length; i++){
			for(var j = 0; j < tbl.rows[i].length; j++){
				console.log('row: ' + tbl.rows[i][j].innerHTML);
			}
		}

	});


},false);


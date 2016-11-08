function deleteRow(r) { // When user clicks "Remove" button, removes the row in the table.
	var i = r.parentNode.parentNode.rowIndex;
	document.getElementById("trips").deleteRow(i);
}
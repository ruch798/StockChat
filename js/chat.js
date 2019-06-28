function newchat() {
	if(confirm("Are you sure")){
		window.location.reload();
	}else{
		alert("hi");
	}
}
function chat(val) {
	var answer=val; 
	var txt1 = "<p class='user'>"+val+"</p>";        // Create text with HTML
	$("#homecard").append(txt1);   // Append new elements
	var div='<div class="card question"><img class="card-img-top" src="images/1.jpg" style="width:380px;height:200px;border-radius: 20px;"><div class="card-body"><h4>John Doe</h4><p class="card-text">Some example text some example text. John Doe is an architect and engineer</p></div></div>'
	var question = div;        // Create text with HTML
	$("#homecard").append(question);   // Append new elements
  var elem = document.getElementById('homecard');
  elem.scrollTop = elem.scrollHeight;
}
window.setInterval(function() {

}, 1000);

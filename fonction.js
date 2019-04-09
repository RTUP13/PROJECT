function verifie(){
	var nom = document.getElementById("nom");

	if (nom.value == "") {
		alert("veuillez renseigner un nom");
		return false;
	}

	var str = document.getElementById("email").value;
	var a = str.indexOf("@");
	var p = str.indexOf(".");
	if ( a == -1 || a == 0) {
		alert("veuillez renseigner une adresse mail valide");
		return false;
	}
	else if ( p == -1 || p==0 || p<=(a+1) ) {
	    alert("veuillez renseigner une adresse mail valide");
	    return false;
	}

	var ip=document.getElementById("ip").value;
	var ip= ip.length;

	if ( lon < 10 ) {
	    alert("veuillez renseigner une adresse ip valide");
		return false;
	}
	return true;
}


function Affiche_form() {
  var x = document.getElementById("form");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function closeForm() {
  document.getElementById("form").style.display = "none";
}

function timedRefresh(timeoutPeriod) {
   setTimeout("location.reload(true);",timeoutPeriod);
 }

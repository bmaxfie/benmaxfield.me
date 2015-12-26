//@author: Ben Maxfield
//
//	This script animates the console pieces not able to be handled by the CSS3 animations.
//		Specifically, this handles:
//			* initial hiding of bottom lines 
//				(for sizing of container)
//			* progress bar animation
//			* timed hiding of top lines and showing of bottom lines
//				(to keep console container same size; mimic a Windows' window)
//

$(document).ready(function(){ 
	
	setTimeout(cutBottom, 1);	// Cuts whole bottom 15 lines.
	setTimeout(progressBar, 10900);	// Starts progress bar animation.
	//setTimeout(toggle1, 18000);	// Toggles the hiding of the top lines and the showing of the bottom ones.
	//setTimeout(toggle2, 18100);
	setTimeout(toggle3, 18500);
	setTimeout(toggle4, 19000);
	setTimeout(toggle5, 19500);
	setTimeout(toggle6, 19700);
	setTimeout(toggle7, 20000);
	setTimeout(toggle8, 20200);
	setTimeout(toggle9, 20600);
	setTimeout(toggle10, 21000);
	setTimeout(toggle11, 21000);
	setTimeout(toggle12, 21200);
	setTimeout(toggle13, 21200);
	setTimeout(toggle14, 21200);
	setTimeout(toggle15, 21200);
	
	// Called at 1ms.
	// Sets css visibility variable to 'hidden'
	function cutBottom(){
		//$("#script20").hide();
		$("#script21").hide();
		$("#script22").hide();
		$("#script23").hide();
		$("#script24").hide();
		$("#script25").hide();
		$("#script26").hide();
		$("#script27").hide();
		$("#script28").hide();
		$("#space3").hide();
		$("#script29").hide();
		$("#script30").hide();
		$("#space4").hide();
		$("#script31").hide();
	}
	
	// Called at 10.9s.
	// Timer for setTimeout has restarted and the delay parameter is respective to when this function was called,
	//	aka. progress5 is called at 11s. globally.
	//
	// Note: Couldn't get .delay() animation timer to work so I relied on setTimeout() again.
	//			Also couldn't figure out how to pass data into setTimeout's function parameters 
	//			so I had to hard code it (hence 150 lines of code :( ... )
	function progressBar(){
		progress0();
		setTimeout(progress5, 100);
		setTimeout(progress10, 200);
		setTimeout(progress15, 300);
		setTimeout(progress20, 400);
		setTimeout(progress25, 500);
		setTimeout(progress30, 600);
		setTimeout(progress35, 700);
		setTimeout(progress40, 800);
		setTimeout(progress45, 900);
		setTimeout(progress50, 1000);
		setTimeout(progress55, 1100);
		setTimeout(progress60, 1200);
		setTimeout(progress65, 1300);
		setTimeout(progress70, 1400);
		setTimeout(progress75, 1500);
		setTimeout(progress80, 1600);
		setTimeout(progress85, 1700);
		setTimeout(progress90, 1800);
		setTimeout(progress95, 1900);
		setTimeout(progress100, 2000);
	}
	
	// Hard Coded Animations:
	function progress0(){
		$("#script4").empty().text("  0%|                    |").append("</br>");
	}
	function progress5(){
		$("#script4").empty().append("  5%|=                   |</br>");
	}
	function progress10(){
		$("#script4").empty().append(" 10%|==                  |</br>");
	}
	function progress15(){
		$("#script4").empty().append(" 15%|===                 |</br>");
	}
	function progress20(){
		$("#script4").empty().append(" 20%|====                |</br>");
	}
	function progress25(){
		$("#script4").empty().append(" 25%|=====               |</br>");
	}
	function progress30(){
		$("#script4").empty().append(" 30%|======              |</br>");
	}
	function progress35(){
		$("#script4").empty().append(" 35%|=======             |</br>");
	}
	function progress40(){
		$("#script4").empty().append(" 40%|========            |</br>");
	}
	function progress45(){
		$("#script4").empty().append(" 45%|=========           |</br>");
	}
	function progress50(){
		$("#script4").empty().append(" 50%|==========          |</br>");
	}
	function progress55(){
		$("#script4").empty().append(" 55%|===========         |</br>");
	}
	function progress60(){
		$("#script4").empty().append(" 60%|============        |</br>");
	}
	function progress65(){
		$("#script4").empty().append(" 65%|=============       |</br>");
	}
	function progress70(){
		$("#script4").empty().append(" 70%|==============      |</br>");
	}
	function progress75(){
		$("#script4").empty().append(" 75%|===============     |</br>");
	}
	function progress80(){
		$("#script4").empty().append(" 80%|================    |</br>");
	}
	function progress85(){
		$("#script4").empty().append(" 85%|=================   |</br>");
	}
	function progress90(){
		$("#script4").empty().append(" 90%|==================  |</br>");
	}
	function progress95(){
		$("#script4").empty().append(" 95%|=================== |</br>");
	}
	function progress100(){
		$("#script4").empty().append("100%|====================|</br>");
	}
	
	
	/*function toggle1(){
		$("#script20").show();
		$("#script1").hide();
	}
	function toggle2(){
		$("#script21").show();
		$("#script2").hide();
	}*/
	function toggle3(){
		$("#script21").show();
		$("#script1").hide();
	}
	function toggle4(){
		$("#script22").show();
		$("#script2").hide();
	}
	function toggle5(){
		$("#script23").show();
		$("#script3").hide();
	}
	function toggle6(){
		$("#script24").show();
		$("#space1").hide();
	}
	function toggle7(){
		$("#script25").show();
		$("#script4").hide();
	}
	function toggle8(){
		$("#script26").show();
		$("#script5").hide();
	}
	function toggle9(){
		$("#script27").show();
		$("#script6").hide();
	}
	function toggle10(){
		$("#script28").show();
		$("#script7").hide();
	}
	function toggle11(){
		$("#space3").show();
		$("#script8").hide();
	}
	function toggle12(){
		$("#script29").show();
		$("#script9").hide();
	}
	function toggle13(){
		$("#script30").show();
		$("#script10").hide();
	}
	function toggle14(){
		$("#space4").show();
		$("#script11").hide();
	}
	function toggle15(){
		$("#script31").show();
		$("#script12").hide();
	}
});

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
	
	setTimeout(cutBottom, 1);	// Cuts whole bottom 8 lines.
	setTimeout(progressBar, 10900);	// Starts progress bar animation.
	setTimeout(toggle1, 20200);	// Toggles the hiding of the top lines and the showing of the bottom ones.
	setTimeout(toggle2, 20600);
	setTimeout(toggle3, 21000);
	setTimeout(toggle4, 21000);
	setTimeout(toggle5, 21200);
	setTimeout(toggle6, 21200);
	setTimeout(toggle7, 21200);
	setTimeout(toggle8, 21200);
	
	// Called at 1ms.
	// Sets css visibility variable to 'hidden'
	function cutBottom(){
		$("#script27").hide();
		$("#script28").hide();
		$("#script29").hide();
		$("#space3").hide();
		$("#script30").hide();
		$("#script31").hide();
		$("#space4").hide();
		$("#script32").hide();
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
	
	
	function toggle1(){
		$("#script27").show();
		$("#script1").hide();
	}
	function toggle2(){
		$("#script28").show();
		$("#script2").hide();
	}
	function toggle3(){
		$("#script29").show();
		$("#script3").hide();
	}
	function toggle4(){
		$("#space3").show();
		$("#script4").hide();
	}
	function toggle5(){
		$("#script30").show();
		$("#script5").hide();
	}
	function toggle6(){
		$("#script31").show();
		$("#space1").hide();
	}
	function toggle7(){
		$("#space4").show();
		$("#script6").hide();
	}
	function toggle8(){
		$("#script32").show();
		$("#script7").hide();
	}
});

function changeInfo(idname,obj){
		var divInfo=$(document.getElementById(idname));
		if(divInfo.css('display')=='none'){
			divInfo.css('display','block');
			$(obj).removeClass("tipdown");
			$(obj).addClass("tipright"); 
		}else{
			divInfo.css('display','none');
			$(obj).removeClass("tipright");
			$(obj).addClass("tipdown"); 
		}
}
console.log("Welcome")
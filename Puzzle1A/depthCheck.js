const fs = require('fs')



fs.readFile("subInput.txt","utf8",(err,data)=>{
	if(err){
		console.error(err)
		return;
	}
	//console.log(data);
	var arr = data.toString().replace(/\r\n/g,'\n').split('\n');
	//console.log(arr);
	
	var totalDepthChanges = 0;
	var lastNum = parseInt(arr[0]);
	for(var ctr = 1; ctr < arr.length; ctr++)
	{
			
		var temp = parseInt(arr[ctr]);
		if(temp > lastNum) totalDepthChanges++;
		lastNum = temp;
			
		
	}
	
	console.log(totalDepthChanges);
	//console.log(arr.length);
	
	
	
	
	
	
	
});
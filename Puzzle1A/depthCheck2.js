const { SSL_OP_NO_SSLv2 } = require('constants');
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
	var leadNum = parseInt(arr[0]);
	var nextNum = parseInt(arr[0]) + parseInt(arr[1]);
	var lastNum = parseInt(arr[0]) + parseInt(arr[1]) + parseInt(arr[2]);
	
	


	
	
	for(var ctr = 3; ctr < arr.length; ctr++)
	{
			
		var temp = parseInt(arr[ctr]);
		
		leadNum +=temp;
		nextNum += temp;
		if(nextNum>lastNum)
		{
			totalDepthChanges++;
		}

		lastNum = nextNum;
		nextNum = leadNum;
		
		leadNum = temp;

		
	}
	
	
	
	console.log(totalDepthChanges);
	

	console.log("we passed whew!");
	
});
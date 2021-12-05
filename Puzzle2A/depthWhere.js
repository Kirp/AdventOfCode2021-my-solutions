const fs = require('fs')



fs.readFile("inp.txt","utf8",(err,data)=>{
	if(err){
		console.error(err)
		return;
	}
	var arr = data.toString().replace(/\r\n/g,'\n').split('\n');
	var depth = 0;
	var hori = 0;
	
	
	for(var ctr = 0; ctr < arr.length; ctr++)
	{
		var comm = arr[ctr].split(" ");
		switch(comm[0])
		{
			case "forward":
				
				hori += parseInt(comm[1]);
				break;
			case "up":
				
				depth -= parseInt(comm[1]);
				
				break;
			case "down":
				
				depth += parseInt(comm[1]);
				
				break;
			default:
				console.log("error");
				
		}
	}
	
	console.log("Horizontal Position: "+hori);
	console.log("Depth: "+depth);
	console.log(depth*hori);
	
	
});
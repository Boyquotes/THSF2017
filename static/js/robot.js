
		$(document).ready(function(){

		var c=document.getElementById("myCanvas");
		var ctx=c.getContext("2d");

  		var image = new Image();
  		image.src = '../static/images/background.png';  		

		$(image).load(function() {
		
    	ctx.drawImage(image, 0, 0);
    	
    	console.log(image);

		//ROBOT
		//Width and height for our canvas
			var canvasWidth = 900;
			var canvasHeight = 350;
			
			//the with and height of our spritesheet
			var spriteWidth = 1143; 
			var spriteHeight = 117; 
			
			//we are having two rows and 8 cols in the current sprite sheet
			var rows = 1; 
			var cols2 = 12; 
			
			//To get the width of a single sprite we divided the width of sprite with the number of cols
			//because all the sprites are of equal width and height 
			var width = spriteWidth/cols2; 
			
			//Same for the height we divided the height with number of rows 
			var height = spriteHeight/rows; 
			
			//Each row contains 8 frame and at start we will display the first frame (assuming the index from 0)
			var curFrame = 0; 
			
			//The total frame is 8 
			var frameCount = 12; 
			
			//x and y coordinates to render the sprite 
			var xR=400;
			var yR=362; 
			
			//x and y coordinates of the canvas to get the single frame 
			var srcX=0; 
			var srcY=0; 
				
			//Speed of the movement 
			var speed = 10; 
			
			//Creating an Image object for our character 
			var character = new Image(); 
			
			//Setting the source to the image file 
			character.src = "../static/images/IdleSprite.png";

			function updateFrame(){
			//Updating the frame index 
			curFrame = ++curFrame % frameCount;
			//Calculating the x coordinate for spritesheet 
			srcX = curFrame * width; 
			// Clear the canvas
			//ctx.clearRect(xR,yR,width,height);
			}

			function draw(){
 				//Updating the frame
 				updateFrame();
 				
 				//Dessiner le ROBOT
 				ctx.drawImage(character,srcX,srcY,width,height,xR,yR,width,height);
				}

			setInterval(draw,100);

		});

});
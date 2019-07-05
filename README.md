# Graduation-design

## CBIR with python OpenCV and tkinter

------

## Usage

#### Environment

- python3		->	 tkinter, OpenCV (the IDE is pycharm)
- MongoDB

#### Prepare

- dataset folder : [INRIA Holidays Dataset](http://lear.inrialpes.fr/people/jegou/data.php) is dataset of our images. 
- queries folder: storage query images, like some photos in dataset

#### use

- python root.py



-----



## The problem is following:

#### First: the features need to add:

-  import file path
- add scroll slip to slide pictures
-  we can search more than 6 pictures
- the photos we find more than 17? 
-  add shape and texture rather than only HSV
-  csv -> GUI
-  read the graduation material from the group of QQ
-  strength the skill of circuit of CBIR
-  make the tk GUI to class
- add success rate 

------

#### Second: BUG already fixed:

-  destroy  ->  destory   (this fucking mistake cost me one afternoon time)
- GC garbage collection  : Image doesn't show up
-  global variable and local variable
-  command doesn't work in Button wiget : command = ... 

			and I wanna deliver parameters of imagepath so Ghlin use lambda p : lambda : callback(imgpath) 
		-> use bind widget can bind Button-1 to the function (but the trouble is every function can use that)

-  list of button and append that 
- for a in list_button so we could forget the flag   and list = [] to clear that list

------

#### Third: the tkinter's function which I didn't use yet:

+ Frame
+ timer -> stop 
+ canvas
+  scroller

------

#### Fourth: Ghlin's advise and my own summary:

  Guo:  (He has the strength to see the function's name and conjecture its feature)

- delete the useless commit
- think the principle of things : there are three ways to go and first two ways can't go (In "destory" problem)
- the power to search knowledge U don't know (use English in search engine)

------

  Me:
	1. have a bad memory : (1). kick the board in ground and sabotage the ashcan
						   (2). "destory" write wrong twice and becomes a meme
						   (3). the "death bike" park at south and forget to ride twice
						   (4). return RAM twice

------

Teacher:

- make GUI more easy to operate 
- add input and output text label on it
- add path gui for text to find query and dataset file
- make labels for images
- "之字形" dpd?? d what?
- has the classify for every pictures
- get the camera to got the picture and find it

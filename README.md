# Graduation-design
##CBIR with python opencv and tkinter

First: the features need to add:
	1.  import file path
	2. add scroll slip to slide pictures
	3. we can search more than 6 pictures
	4. the photos we find more than 17? 
	5. add shape and texture rather than only HSV
	6. csv -> GUI
	7. read the graduation material from the group of QQ
	8. strength the skill of circuit of CBIR
	9. make the tk GUI to class

	10. add success rate 

---

Second: BUG already fixed:
	1. destroy  ->  destory   (this fucking mistake cost me one afternoon time)
	2. GC garbage collection  : Image doesn't show up
	2'. global variable and local variable
	3. command doesn't work in Button wiget : command = ... 
		and I wanna deliver parameters of imagepath so Ghlin use lambda p : lambda : callback(imgpath) 
		-> use bind widget can bind Button-1 to the function (but the trouble is every function can use that)
	4. list of button and append that 

	5. for a in list_button so we could forget the flag   and list = [] to clear that list

---

Third: the tkinter's function which I didn't use yet:
	1. Frame
	2. timer -> stop 
	3. canvas

	4. scroller

---

Fourth: Ghlin's advise and my own summary:
  Guo:  (He has the strength to see the function's name and conjecture its feature)
	1. delete the useless commit
	2. think the principle of things : there are three ways to go and first two ways can't go (In "destory" problem)

	3. the power to search knowledge U don't know (use English in search engine)

---

  Me:
	1. have a bad memory : (1). kick the board in ground and sabotage the ashcan
						   (2). "destory" write wrong twice and becomes a meme
						   (3). the "death bike" park at south and forget to ride twice
						   (4). return RAM twice

---

Teacher:

- make GUI more easy to operate 
- add input and output text label on it
- add path gui for text to find query and dataset file
- make labels for images
- "之字形" dpd?? d what?
- has the classify for every pictures
- get the camera to got the picture and find it

 


---------------------------README---------------------------------

We use python code and standard matlab codes(2) in this project.

All the necessary files are attached in this folder.


Before running the code, make sure

1. The code is written in python 3.6 language. Make sure you install the python 3.6 version only.(matlab codes do not work for above versions)

2.PACKAGES:
	This project requires some packages need to be installed for proper functioning.
	They are:
		1.tkinter
		2.PIL
		3.numpy
		4.opencv
		5.scipy
		6.matlab.engine
		7.array
		8.math 



2.PATHS:
    There are several paths involved in the code either directly(in the main code) or indirectly(in matlab code). So make sure you change the paths according to your convenience.
    In the main code, all the paths involved are moved to the beginning of the code at one place for clear understanding.

    Paths involved in the main code:

    PATH1="C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Cat1_1_3.jpg" 
	This is the path of the image named "Cat1_1_3.jpg". When you run the code, this is the default image on which operation begins.
        The image is saved in this folder. Save the image wherever you want and change the PATH1 accordingly.
	

    PATH2="C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\wallimage_withnodoors.jpg"
	This is the path of the image named "wallimage_withnodoors.jpg". This is the image of the "Cat1_1_3.jpg" EXCLUDING THE OBJECTS AND DOORS BEING CLOSED.
	The image is saved in this folder. Save the image wherever you want and change the PATH2 accordingly.

    PATH3="C:\\Users\\User\\Desktop\\ans2.mat"
	This is a resultant matlab file which contains object coordinates.

    PATH4="C:\\Users\\User\\Desktop\\cfile.mat"
	This is a resultant matlab file which contains room coordinates.	

    PATH5="C:\\Users\\User\\Desktop\\tkinter_codes\\roomsymbols\\symbol"
	'roomsymbols' is a folder which contains the images of the objects being used in this project. 'symbol' is the name of the object(no need to change this).

    PATH6="C:\\Users\\User\\Desktop\\wallimage_withnodoor.jpg"
	This is the path of the image obtained after removing the objects and closing doors.

    PATH7="C:\\Users\\User\\Desktop\\wallforflip.jpg"
	This is also the path of the wall image but it modifies itself when flip operation is performed(i.e, for example when flipped vertically wall image gets flipped and saved here)

    PATH8="C:\\Users\\User\\Desktop\\tkinter_codes\\object"
	Objects in the floor plan are saved individually, this is the path of those objects.This appears in the code as "PATH8 + objectnumber + .jpg". 
	So don't try to change the name 'object'

    PATH9="C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Dataset_3rooms"
	This is the path of the folder containing the 3 room floor plan images. This folder is attached in this folder.	

    PATH10="C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Dataset_4rooms"
	This is the path of the folder containing the 3 room floor plan images. This folder is attached in this folder.	

    PATH11="C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Dataset_5rooms"
	This is the path of the folder containing the 3 room floor plan images. This folder is attached in this folder.	

    PATH12="C:\\Users\\User\\Desktop\\dfile.mat"  
	This is the path of a resultant matlab file.

	
    Paths involved in matlab file:
	
	path1 = 'C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\fl_0sym1.tif'
	path2 = 'C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\blb_0_1.jpg' 
 		These two are the intermediate files produced when the matlab code runs. Change these paths accordingly.



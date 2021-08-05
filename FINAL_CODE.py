import tkinter as tk     
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile 
from PIL import Image,ImageTk,ImageGrab,ImageOps
import numpy as np
from scipy.io import loadmat,savemat
import math
from array import *
from tkinter import messagebox
import cv2
import os
import matlab.engine
from scipy import ndimage
#import pyautogui


#PATHS
PATH1="C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Cat1_1_3.jpg"
PATH2="C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\wallimage_withnodoors.jpg"
PATH3="C:\\Users\\User\\Desktop\\ans2.mat"
PATH4="C:\\Users\\User\\Desktop\\cfile.mat"
PATH5="C:\\Users\\User\\Desktop\\tkinter_codes\\roomsymbols\\symbol"
PATH6="C:\\Users\\User\\Desktop\\wallimage_withnodoor.jpg"
PATH7="C:\\Users\\User\\Desktop\\wallforflip.jpg"
PATH8="C:\\Users\\User\\Desktop\\tkinter_codes\\object"
PATH9="C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Dataset_3rooms"
PATH10="C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Dataset_4rooms"
PATH11="C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Dataset_5rooms"
PATH12="C:\\Users\\User\\Desktop\\dfile.mat"








eng = matlab.engine.start_matlab()
#xys="C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Cat1_1_3.jpg"
eng.classify_objects_test1(PATH1,nargout=0)
#pys="C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\wallimage_withnodoors.jpg"
eng.final_room_segmentation(PATH2,nargout=0)
eng.quit()
#matlab.io.saveVariablesToScript('C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\ans.mat',ans)
#eng.boundingbox_Aroundrooms(xys,nargout=0)


root = tk.Tk()
#savemat('Rooms.mat',appendmat=True, format='5', long_field_names=False, do_compression=False)

#canvas = tk.Canvas(width=800, height=800)
#canvas.grid(row=0,column=0,sticky=(N,W,E,S))
#canvas.config(width=100,height=100)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

#I=Image.open("C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\wall_image.jpg")
#I2=I.rotate(-2.783020753856615,fillcolor='white',expand=True)
#I2.save("C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\wall_image100.jpg")

#iux=iux.rotate(-xio-self.angar[x5],fillcolor='white',expand=True)
            


mfile=loadmat(PATH3)
print(mfile)
dfile=loadmat(PATH12)
#cfile=loadmat('C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\room identification\\roomcoordinates.mat')
cfile=loadmat(PATH4)
print(cfile)
#print(cfile['bbox_loc'][0][3])
#print(dfile['dfile'][0])
#print((mfile['bbox_loc'][0][1][0]))
#print(len(mfile['bbox_loc'][0]))
#print(len(cfile['bbox_loc']))
#print(cfile['bbox_loc'][0][1][0][1])
#print(math.degrees(math.tan(0)))
#x=math.radians(45)
#print(math.cos(x))
BORDER_SIZE=10
#PATH_1 = ".\ROBIN\Dataset_3rooms"
#PATH_1 = "C:/Users/User/Desktop/tkinter_codes/floorplans/ROBIN/Dataset/"
#PATH_1= "ROBIN_3rooms"
#MIN_HULL_AREA = 12000#700
#MAX_HULL_AREA = 15000#2900
MIN_HULL_AREA = 12000#700
MAX_HULL_AREA = 15500#2900
BOUNDARY_STORAGE_LOC = "outer_boundary"
CLOSE_DOOR_STORAGE_LOC = "closed doors"

MIN_PROXIMITY = 1.5*2
#list_of_imgs = [os.path.join(PATH_1,i) for i in os.listdir(PATH_1)]
kernel_dilate = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
kernel_erode = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
kernel_erode_2 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

kernel_dilate_1 = np.ones((1,25), np.uint8)
kernel_dilate_2 = np.ones((25,1), np.uint8)

kernel_dilate_1_1 = np.ones((2,5), np.uint8)
kernel_dilate_2_2 = np.ones((5,2), np.uint8)










xorg=IntVar()
yorg=IntVar()




class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y

class Example(tk.Frame):

    def __init__(self, parent):

        self.parent =parent
        tk.Frame.__init__(self, parent)

        self.canvas = tk.Canvas(width=1600,height=1500, bg='white')
        self.canvas.grid(row=0,column=0,sticky=(N,W,E,S))

        

        self.delbut=0
        self.excep_fbox=0
        self.new_obj=0
        self.move_door_perm=0
        self.blink_stop=0
        self.blink=None
        self.excep=0
        self.main_doors=0

        rows=3
        cols=1000

        self.num_new1=[0]*1000
        self.num_new2=[0]*1000
        self.num_new3=[0]*1000
        self.room_doors=[0]*1000
        self.room_doors2=[0]*1000
        self.del_from_plan=[0]*1000
        self.main_doors_check=[0]*1000

        self.numindex=0
        self.blink_stop2=0
        self.first=0
        self.sec=0

        
        self.mylist=[]



        
        w = tk.Label(root, text="FURNITURE BOX",padx=20,bg='black',fg='white',font = "Helectika 12 bold",relief="solid")
        w.place(x=1325,y=5)
        #object1
        I=Image.open(PATH5+"1.tif")
        I1=I.resize((68,42),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        
        mybutton=Button(root,text="TUB",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(1,"TUB"))
        mybutton.place(x=1285,y=35)
        #object2
        I=Image.open(PATH5+"2.tif")
        I1=I.resize((50,63),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="BED",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(2,"BED"))
        mybutton.place(x=1376,y=35)
        #object3
        I=Image.open(PATH5+"13.tif")
        I1=I.resize((60,40),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="SINK",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(13,"SINK"))
        mybutton.place(x=1452,y=35)
        #object4
        I=Image.open(PATH5+"4.tif")
        I1=I.resize((68,50),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="SINK",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(4,"SINK"))
        mybutton.place(x=1285,y=120)
        #object5
        I=Image.open(PATH5+"10.tif")
        I1=I.resize((65,40),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="TWIN SINK",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(10,"TWIN SINK"))
        mybutton.place(x=1367,y=130)
        #object6
        I=Image.open(PATH5+"17.tif")
        I1=I.resize((65,50),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="SMALL SINK",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(17,"SMALL SINK"))
        mybutton.place(x=1450,y=120)
        #object7
        I=Image.open(PATH5+"11.tif")
        I1=I.resize((60,50),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="SMALL SOFA",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(11,"SMALL SOFA"))
        mybutton.place(x=1285,y=210)
        #object8
        I=Image.open(PATH5+"12.tif")
        I1=I.resize((65,50),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="ROUND"+'\n'+"TABLE",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(12,"ROUND TABLE"))
        mybutton.place(x=1370,y=210)
        #object9
        I=Image.open(PATH5+"3.tif")
        I1=I.resize((58,53),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="DOOR",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(3,"DOOR"))
        mybutton.place(x=1453,y=210)
        #object10
        I=Image.open(PATH5+"5.tif")
        I1=I.resize((65,55),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="COFFEE"+'\n'+"TABLE",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(5,"COFFEE TABLE"))
        mybutton.place(x=1285,y=297)
        #object11
        I=Image.open(PATH5+"7.tif")
        I1=I.resize((65,50),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="DINING"+'\n'+"TABLE",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(7,"DINING TABLE"))
        mybutton.place(x=1368,y=308)
        #object12
        I=Image.open(PATH5+"6.tif")
        I1=I.resize((65,55),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="ARMCHAIR",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(6,"ARMCHAIR"))
        mybutton.place(x=1450,y=300)
        #object13
       # I=Image.open(PATH58.tif")
       # I1=I.resize((65,50),Image.ANTIALIAS)
       # self.canvas.photo=ImageTk.PhotoImage(I1)
       # self.mylist.append(self.canvas.photo)
       # mybutton=Button(root,text="SINK",image=self.canvas.photo,compound=TOP,bg="white")
       # mybutton.place(x=1285,y=403)
        #object14
        I=Image.open(PATH5+"19.tif")
        I1=I.resize((65,35),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="LARGE SOFA",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(19,"LARGE SOFA"))
        mybutton.place(x=1365,y=407)
        #object15
       # I=Image.open(PATH515.tif")
       # I1=I.resize((65,50),Image.ANTIALIAS)
       # self.canvas.photo=ImageTk.PhotoImage(I1)
       # self.mylist.append(self.canvas.photo)
       # mybutton=Button(root,text="MIRROR",image=self.canvas.photo,compound=TOP,bg="white")
       # mybutton.place(x=1450,y=407)
        #object16
       # I=Image.open(PATH516.tif")
       # I1=I.resize((65,55),Image.ANTIALIAS)
       # self.canvas.photo=ImageTk.PhotoImage(I1)
       # self.mylist.append(self.canvas.photo)
       # mybutton=Button(root,text="COFFEE TABLE",image=self.canvas.photo,compound=TOP,bg="white")
       # mybutton.place(x=1285,y=506)
        #object17
       # I=Image.open(PATH518.tif")
       # I1=I.resize((65,55),Image.ANTIALIAS)
       # self.canvas.photo=ImageTk.PhotoImage(I1)
       # self.mylist.append(self.canvas.photo)
       # mybutton=Button(root,text="ARMCHAIR",image=self.canvas.photo,compound=TOP,bg="white")
       # mybutton.place(x=1365,y=506)
        #object18
        #I=Image.open(PATH59.tif")
        #I1=I.resize((65,55),Image.ANTIALIAS)
        #self.canvas.photo=ImageTk.PhotoImage(I1)
        #self.mylist.append(self.canvas.photo)
        #mybutton=Button(root,text="WINDOW",image=self.canvas.photo,compound=TOP,bg="white")
        #mybutton.place(x=1450,y=506)
        #object19
        #I=Image.open(PATH514.tif")
        #I1=I.resize((65,35),Image.ANTIALIAS)
        #self.canvas.photo=ImageTk.PhotoImage(I1)
       # self.mylist.append(self.canvas.photo)
       # mybutton=Button(root,text="LARGE SOFA",image=self.canvas.photo,compound=TOP,bg="white")
       # mybutton.place(x=1285,y=609)


        
        




        #toolbar=Frame(root,bg="blue")

        #toolbar.grid(row=1400,column=10)





        my_menu=Menu(root)
        root.config(menu=my_menu)
        file_menu=Menu(my_menu,tearoff=False)
        my_menu.add_cascade(label="File",menu=file_menu)
        #file_menu.add_command(label="Open",command=our_command)
        submenu=Menu(file_menu,tearoff=False)
        submenu.add_command(label="3-Room Floorplan",command=lambda: self.openimage("3-Room Flooplan"))
        #submenu.add_separator()
        submenu.add_command(label="4-Room Floorplan",command=lambda: self.openimage("4-Room Flooplan"))
        #submenu.add_separator()
        submenu.add_command(label="5-Room Floorplan",command=lambda: self.openimage("5-Room Flooplan"))
        file_menu.add_cascade(label="Open", menu=submenu, underline=0)
        #file_menu.add_separator()
        file_menu.add_command(label="Save",command=self.saveimage)
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=root.quit)



        edit_menu=Menu(my_menu,tearoff=False)
        my_menu.add_cascade(label="Edit",menu=edit_menu)
        edit_menu.add_command(label="Flip Vertical",command=self.flipdef)
        #edit_menu.add_separator()
        edit_menu.add_command(label="Flip Horizontal",command=self.fliphordef)






        self.delcom=0
        self.delcom2=0

        self.a1=0
        self.a2=0
        self.a3=0
        self.a4=0
        self.ent2=0
        #self.canvasScale     = 1.0
        #self.canvasScale *= 2.0
        #canvas.pack (expand =1, fill =tk.BOTH)
        self.canvas.tag_bind("DnD","<Button-1>")




        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.iid = None
           
        #self.msd=self.canvas.find_closest(self.event.x, self.event.y)[0]
        self.canvas.bind("<ButtonPress-1>", self.on_button_1)
         
        self.canvas.tag_bind( "token","<ButtonPress-1>", self.drag_start)
        self.canvas.tag_bind("token","<ButtonRelease-1>", self.drag_stop)
        self.canvas.tag_bind("token","<B1-Motion>", self.drag)


        #self.floorplan="C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Dataset_3roomsmall\\Cat1_1.jpg"
        self.floorplan=PATH1





        #self.iimg=Image.open("C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Dataset_3roomsmall\\Cat1_1.jpg")
        self.iimg=Image.open(self.floorplan)


        #iimg=iimg.resize((1000, 800), Image.ANTIALIAS)
        self.canvas.img=ImageTk.PhotoImage(self.iimg)
        #self.mylist.append(self.canvas.img)
        #self.canvas.img = self.canvas.img.resize((1750, 950), Image.ANTIALIAS)
        self.canvas_img=self.canvas.create_image(0,0,image=self.canvas.img,anchor="nw")
        #self.mylist.append(self.iimg)
        
        #for x in range(len(mfile['bbox_loc'][0])):
         #   self.iddi=self.canvas.create_rectangle(mfile['bbox_loc'][0][x][0][0],mfile['bbox_loc'][0][x][0][1],mfile['bbox_loc'][0][x][0][0]+mfile['bbox_loc'][0][x][0][2],mfile['bbox_loc'][0][x][0][1]+mfile['bbox_loc'][0][x][0][3],fill='white',outline='white',tags="whi")
            #  self.mylist.append("whi")
            #emo=ImageGrab.grab(bbox=None)
            #emo.show()

            # self.canvas.img.save("C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Dataset_3roomsmall\\white1_1.jpg")
     

        self.canvas.delete("all")
        #self.iimg=Image.open("C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Dataset_3roomsmall\\Cat1_1.jpg")
        self.iimg=Image.open(PATH1)
        name=self.floorplan
        image = cv2.imread(self.floorplan)
        image = cv2.copyMakeBorder(image,top=BORDER_SIZE,bottom=BORDER_SIZE,left=BORDER_SIZE,right=BORDER_SIZE,borderType=cv2.BORDER_CONSTANT, value=[255,255,255])
        self.get_contours(image,name)



        #iimg=iimg.resize((1000, 800), Image.ANTIALIAS)
        self.canvas.img=ImageTk.PhotoImage(self.iimg)
        #self.mylist.append(self.canvas.img)
        #canvas.img = canvas.img.resize((250, 250), Image.ANTIALIAS)
        self.canvas_img=self.canvas.create_image(0,0,image=self.canvas.img,anchor="nw")


        self.iimg2=Image.open( PATH6 )
        strr=PATH6

        self.iimg2.save(PATH7)
        self.width,self.height=self.iimg2.size
        #self.iimg2 = self.iimg2.resize((self.canvas.winfo_width(),self.canvas.winfo_height()), Image.ANTIALIAS)
        self.iimg2 = self.iimg2.resize((1270,700), Image.ANTIALIAS)
        
        #self.iimg=iimg.resize((1000, 800), Image.ANTIALIAS)
        
        #print(self.width,self.height)
        #print((1350*700)/(self.width*self.height))
        self.canvas.img2=ImageTk.PhotoImage(self.iimg2)
        #self.mylist.append(self.canvas.img)
        #canvas.img = canvas.img.resize((250, 250), Image.ANTIALIAS)
        self.canvas_img2=self.canvas.create_image(0,0,image=self.canvas.img2,anchor="nw")


        #to find the angle of rotation
        #img_before = cv2.imread('C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\wall_image.jpg')
        img_before = cv2.imread(strr)
        cv2.imshow("Before", img_before)    
        key = cv2.waitKey(0)

        img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
        img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
        lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)

        angles = []

        for x1, y1, x2, y2 in lines[0]:
            cv2.line(img_before, (x1, y1), (x2, y2), (255, 0, 0), 3)
            angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
            angles.append(angle)

        median_angle = np.median(angles)
        img_rotated = ndimage.rotate(img_before, median_angle)
        print(median_angle)

        self.theta=median_angle





        self.hor_ver=[None]*1000
        self.up_down=[None]*1000
        self.roomcoord=[[0 for y in range(8)]for x in range(len(cfile['bbox_loc'])) ]
        self.roomcoord2=[[0 for y in range(8)]for x in range(len(cfile['bbox_loc'])) ]
        self.roomcoord3=[[0 for y in range(8)]for x in range(len(cfile['bbox_loc'])) ]
        self.array=[0]*4

        for x in range(len(cfile['bbox_loc'])):
            self.canvas.create_line(cfile['bbox_loc'][x][4]*(1270/self.width),cfile['bbox_loc'][x][0]*(700/self.height),cfile['bbox_loc'][x][5]*(1270/self.width),cfile['bbox_loc'][x][1]*(700/self.height))
            self.canvas.create_line(cfile['bbox_loc'][x][5]*(1270/self.width),cfile['bbox_loc'][x][1]*(700/self.height),cfile['bbox_loc'][x][6]*(1270/self.width),cfile['bbox_loc'][x][2]*(700/self.height))
            self.canvas.create_line(cfile['bbox_loc'][x][6]*(1270/self.width),cfile['bbox_loc'][x][2]*(700/self.height),cfile['bbox_loc'][x][7]*(1270/self.width),cfile['bbox_loc'][x][3]*(700/self.height))
            self.canvas.create_line(cfile['bbox_loc'][x][7]*(1270/self.width),cfile['bbox_loc'][x][3]*(700/self.height),cfile['bbox_loc'][x][4]*(1270/self.width),cfile['bbox_loc'][x][0]*(700/self.height))
                #self.canvas.create_rectangle((cfile['bbox_loc'][x][7]*(1270/self.width)+cfile['bbox_loc'][x][4]*(1270/self.width))/2,(cfile['bbox_loc'][x][2]*(700/self.height)+cfile['bbox_loc'][x][3]*(700/self.height))/2,(cfile['bbox_loc'][x][6]*(1270/self.width)+cfile['bbox_loc'][x][5]*(1270/self.width))/2,(cfile['bbox_loc'][x][0]*(700/self.height)+cfile['bbox_loc'][x][1]*(700/self.height))/2,outline='red')

        for x in range(len(cfile['bbox_loc'])):


            self.roomcoord[x][0]=cfile['bbox_loc'][x][7]*(700/self.height)
            self.roomcoord[x][1]=cfile['bbox_loc'][x][3]*(700/self.height)
            self.roomcoord[x][2]=cfile['bbox_loc'][x][4]*(700/self.height)
            self.roomcoord[x][3]=(cfile['bbox_loc'][x][0])*(700/self.height)
            self.roomcoord[x][4]=cfile['bbox_loc'][x][6]*(700/self.height)
            self.roomcoord[x][5]=(cfile['bbox_loc'][x][2])*(700/self.height)
            self.roomcoord[x][6]=cfile['bbox_loc'][x][5]*(700/self.height)
            self.roomcoord[x][7]=(cfile['bbox_loc'][x][1])*(700/self.height)



            self.roomcoord3[x][0]=self.roomcoord[x][0]
            self.roomcoord3[x][1]=self.roomcoord[x][1]
            self.roomcoord3[x][2]=self.roomcoord[x][2]
            self.roomcoord3[x][3]=self.roomcoord[x][3]
            self.roomcoord3[x][4]=self.roomcoord[x][4]
            self.roomcoord3[x][5]=self.roomcoord[x][5]
            self.roomcoord3[x][6]=self.roomcoord[x][6]
            self.roomcoord3[x][7]=self.roomcoord[x][7]





            #self.canvas.create_rectangle(self.roomcoord[x][0],self.roomcoord[x][1],self.roomcoord[x][2],self.roomcoord[x][3],outline='green')

        #for x in range(len(cfile['bbox_loc'])):
            #print(self.roomcoord[x][0],
            #self.roomcoord[x][1],
            #self.roomcoord[x][2],
            #self.roomcoord[x][3])
        #print(self.roomcoord[2][3])

        self.ro=len(mfile['bbox_loc'][0])
        col=5;
        self.arr1 = [ [0 for y in range(col)] for x in range(1000) ]
        self.arr2 = [ [0 for y in range(col)] for x in range(1000) ] 
        self.arr3=[0]*1000
        self.angar=[0]*1000
        self.flipcheck=[0]*1000

       
        for x in range(self.ro):
            #canvas.create_rectangle((mfile['bbox_loc'][0][x][0][0],mfile['bbox_loc'][0][x][0][1],mfile['bbox_loc'][0][x][0][0]+mfile['bbox_loc'][0][x][0][2],mfile['bbox_loc'][0][x][0][1]+mfile['bbox_loc'][0][x][0][3]),outline='red',tags=("token","DnD"))
            self.im_crop = self.iimg.crop((mfile['bbox_loc'][0][x][0][0],mfile['bbox_loc'][0][x][0][1],mfile['bbox_loc'][0][x][0][0]+mfile['bbox_loc'][0][x][0][2],mfile['bbox_loc'][0][x][0][1]+mfile['bbox_loc'][0][x][0][3]))
            
            self.iwidth,self.iheight=self.im_crop.size

            self.im_crop=self.im_crop.resize((round(self.iwidth*(1270/self.width)),round(self.iheight*(700/self.height))),Image.ANTIALIAS)
            
            self.im_crop.save(PATH8+str(x)+".jpg")                     
      
            self.canvas.im_crop2=ImageTk.PhotoImage(self.im_crop)

 

            #self.xcrop=self.canvas.create_image((((mfile['bbox_loc'][0][x][0][0]+mfile['bbox_loc'][0][x][0][2]+mfile['bbox_loc'][0][x][0][0])*(1270/self.width))/2,((mfile['bbox_loc'][0][x][0][1]+mfile['bbox_loc'][0][x][0][3]+mfile['bbox_loc'][0][x][0][1])*(700/self.height))/2), image=self.canvas.im_crop2)
            self.xcrop=self.canvas.create_image((((mfile['bbox_loc'][0][x][0][0])*(1270/self.width)),((mfile['bbox_loc'][0][x][0][1])*(700/self.height))), image=self.canvas.im_crop2,anchor="nw")
            
            #if(x==13):
             #   self.canvas.tag_lower(self.xcrop)
            #self.images[x]=self.xcrop
            #canvas.create_image(1000,1000,image=im_crop2)
            self.arr1[x][0]=mfile['bbox_loc'][0][x][0][0]*(1270/self.width)
            self.arr1[x][1]=mfile['bbox_loc'][0][x][0][1]*(700/self.height)
            self.arr1[x][2]=(mfile['bbox_loc'][0][x][0][0]+mfile['bbox_loc'][0][x][0][2])*(1270/self.width)
            self.arr1[x][3]=(mfile['bbox_loc'][0][x][0][1]+mfile['bbox_loc'][0][x][0][3])*(700/self.height)

            #print(arr1[x][0])

            self.arr2[x][0]=self.arr1[x][0]
            self.arr2[x][1]=self.arr1[x][1]
            self.arr2[x][2]=self.arr1[x][2]
            self.arr2[x][3]=self.arr1[x][3]


            self.arr3[x]=1
            chck=0
            chck2=0
            y111=0
            y112=0
            x111=Point(0,0)
            x112=Point(0,0)
            ui3=0

            for y in range(len(cfile['bbox_loc'])):

                ui3=0

                for y111 in range(4):

                    chck=0

                    if(y111==0):
                        l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                        d1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                    if(y111==1):
                        l1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                        d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                    if(y111==2):
                        l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                        d1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                    if(y111==3):
                        l1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                        d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                    for y112 in range(4):
                        if(y112==0):
                            l2=Point(self.arr2[x][0],self.arr2[x][1])
                            d2=Point(self.arr2[x][0],self.arr2[x][3])
                        if(y112==1):
                            l2=Point(self.arr2[x][0],self.arr2[x][3])
                            d2=Point(self.arr2[x][2]+3,self.arr2[x][3])
                        if(y112==2):
                            l2=Point(self.arr2[x][0],self.arr2[x][1])
                            d2=Point(self.arr2[x][2]+3,self.arr2[x][1])
                        if(y112==3):
                            l2=Point(self.arr2[x][2]+3,self.arr2[x][1])
                            d2=Point(self.arr2[x][2]+3,self.arr2[x][3])
  
                        #if(self.doIntersect(l1,d1,l2,d2) and (l2.x!=0) and (l2.y!=0) ):
                        if(dfile['dfile'][0][x]==1 and self.doIntersect(l1,d1,l2,d2) and (l2.x!=0) and (l2.y!=0)) :
                            chck=1
                            if(ui3==0):
                                chck2=chck2+1
                                ui3=1

                            print(chck2,x,1000)
                            self.room_doors[y]=self.room_doors[y]+1
                            self.room_doors2[y]=self.room_doors[y]
                            zz=0
                            for z in range(4):
                                if(z==0):
                                    l3=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                    d3=Point(self.roomcoord3[y][2],self.roomcoord3[y][3]) 
                                if(z==1):
                                    l3=Point(self.roomcoord3[y][2],self.roomcoord3[y][3])
                                    d3=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                if(z==2):
                                    l3=Point(self.roomcoord3[y][4],self.roomcoord3[y][5])
                                    d3=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                if(z==3):
                                    l3=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                    d3=Point(self.roomcoord3[y][4],self.roomcoord3[y][5]) 
            
                                l4=Point(self.arr2[x][0],self.arr2[x][1])
                                d4=Point(self.arr2[x][2],self.arr2[x][3])

                                if(l4.x<=l3.x and l3.x<=d4.x):
                                    self.arr2[x][4]=1
                                    self.arr1[x][4]=1
                                    self.hor_ver[x]='V'
                                    if(abs(l4.x-l3.x)>abs(l3.x-d4.x)):
                                        self.up_down[x]='L'
                                    else:
                                        self.up_down[x]='R'
                                if(l4.y<=l3.y and l3.y<=d4.y ):
                                    self.arr2[x][4]=1
                                    self.arr1[x][4]=1
                                    self.hor_ver[x]='H'
                                    if(abs(l4.y-l3.y)>abs(l3.y-d4.y)):
                                        self.up_down[x]='U'
                                    else:
                                        self.up_down[x]='D'

                            break

                    if(chck==1):
                        break



            if(chck2==1):
                self.main_doors=self.main_doors+1
                self.main_doors_check[x]=1


            self.mylist.append(self.canvas.im_crop2)



        self.canvas.delete(self.canvas_img)
        self.popup = tk.Menu(self.canvas, tearoff=0)
        #self.popup.add_command(label="delete",command=lambda: self.dele(id))

        #root.bind("<Button-3>", self.do_popup)
        self.canvas.bind("<Button-3>", self.do_popup)
        
        self.cup=self.canvas.create_rectangle(1275,16,1527,476,fill='grey81')
        self.mylist.append(self.cup)

        self.ent=0



    def our_command(self,event):
        print(1)
    
    def openimage(self,txt):
        if(txt=="3-Room Flooplan"):
            root.filename=filedialog.askopenfilename(initialdir=PATH9,title="Select a file",filetypes=(("jpg files",".jpg"),("all files",".")))
        if(txt=="4-Room Flooplan"):
            root.filename=filedialog.askopenfilename(initialdir=PATH10,title="Select a file",filetypes=(("jpg files",".jpg"),("all files",".")))
        if(txt=="5-Room Flooplan"):
            root.filename=filedialog.askopenfilename(initialdir=PATH11,title="Select a file",filetypes=(("jpg files",".jpg"),("all files",".")))

        self.canvas.delete("all")
        self.floorplan=root.filename    
        #imjj=Image.open(str(root.filename))
        #self.iimg=imjj
        #imjj=imjj.resize((1225,685),Image.ANTIALIAS)
        #self.canvas_img2=ImageTk.PhotoImage(imjj)
        #self.canvas_imjj=self.canvas.create_image(0,0,image=self.canvas_img2,anchor="nw")

        name=str(root.filename)
        image = cv2.imread(str(root.filename))
        image = cv2.copyMakeBorder(image,top=BORDER_SIZE,bottom=BORDER_SIZE,left=BORDER_SIZE,right=BORDER_SIZE,borderType=cv2.BORDER_CONSTANT, value=[255,255,255])
        self.get_contours(image,name)

        eng = matlab.engine.start_matlab()
        xys=str(root.filename)
        eng.classify_objects_test1(xys,nargout=0)
        
        eng.final_room_segmentation(PATH6,nargout=0)
        eng.quit()


        mfile=loadmat(PATH3)
        dfile=loadmat(PATH12)
        #cfile=loadmat('C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\room identification\\roomcoordinates.mat')
        cfile=loadmat(PATH4)


        self.delbut=0
        self.excep_fbox=0
        self.new_obj=0
        self.move_door_perm=0
        self.blink_stop=0
        self.blink=None
        self.excep=0
        self.main_doors=0

        rows=3
        cols=1000

        self.num_new1=[0]*1000
        self.num_new2=[0]*1000
        self.num_new3=[0]*1000
        self.room_doors=[0]*1000
        self.room_doors2=[0]*1000
        self.del_from_plan=[0]*1000
        self.main_doors_check=[0]*1000

        self.numindex=0
        self.blink_stop2=0
        self.first=0
        self.sec=0

        
        self.mylist=[]



        
        w = tk.Label(root, text="FURNITURE BOX",padx=20,bg='black',fg='white',font = "Helectika 12 bold",relief="solid")
        w.place(x=1325,y=5)
        #object1
        I=Image.open(PATH5+"1.tif")
        I1=I.resize((68,42),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        
        mybutton=Button(root,text="TUB",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(1,"TUB"))
        mybutton.place(x=1285,y=35)
        #object2
        I=Image.open(PATH5+"2.tif")
        I1=I.resize((50,63),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="BED",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(2,"BED"))
        mybutton.place(x=1376,y=35)
        #object3
        I=Image.open(PATH5+"13.tif")
        I1=I.resize((60,40),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="SINK",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(13,"SINK"))
        mybutton.place(x=1452,y=35)
        #object4
        I=Image.open(PATH5+"4.tif")
        I1=I.resize((68,50),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="SINK",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(4,"SINK"))
        mybutton.place(x=1285,y=120)
        #object5
        I=Image.open(PATH5+"10.tif")
        I1=I.resize((65,40),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="TWIN SINK",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(10,"TWIN SINK"))
        mybutton.place(x=1367,y=130)
        #object6
        I=Image.open(PATH5+"17.tif")
        I1=I.resize((65,50),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="SMALL SINK",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(17,"SMALL SINK"))
        mybutton.place(x=1450,y=120)
        #object7
        I=Image.open(PATH5+"11.tif")
        I1=I.resize((60,50),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="SMALL SOFA",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(11,"SMALL SOFA"))
        mybutton.place(x=1285,y=210)
        #object8
        I=Image.open(PATH5+"12.tif")
        I1=I.resize((65,50),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="ROUND"+'\n'+"TABLE",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(12,"ROUND TABLE"))
        mybutton.place(x=1370,y=210)
        #object9
        I=Image.open(PATH5+"3.tif")
        I1=I.resize((58,53),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="DOOR",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(3,"DOOR"))
        mybutton.place(x=1453,y=210)
        #object10
        I=Image.open(PATH5+"5.tif")
        I1=I.resize((65,55),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="COFFEE"+'\n'+"TABLE",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(5,"COFFEE TABLE"))
        mybutton.place(x=1285,y=297)
        #object11
        I=Image.open(PATH5+"7.tif")
        I1=I.resize((65,50),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="DINING"+'\n'+"TABLE",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(7,"DINING TABLE"))
        mybutton.place(x=1368,y=308)
        #object12
        I=Image.open(PATH5+"6.tif")
        I1=I.resize((65,55),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="ARMCHAIR",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(6,"ARMCHAIR"))
        mybutton.place(x=1450,y=300)

        I=Image.open(PATH5+"19.tif")
        I1=I.resize((65,35),Image.ANTIALIAS)
        self.canvas.photo=ImageTk.PhotoImage(I1)
        self.mylist.append(self.canvas.photo)
        mybutton=Button(root,text="LARGE SOFA",image=self.canvas.photo,compound=TOP,bg="white",command=lambda: self.adding(19,"LARGE SOFA"))
        mybutton.place(x=1365,y=407)



        my_menu=Menu(root)
        root.config(menu=my_menu)
        file_menu=Menu(my_menu,tearoff=False)
        my_menu.add_cascade(label="File",menu=file_menu)
        #file_menu.add_command(label="Open",command=our_command)
        submenu=Menu(file_menu,tearoff=False)
        submenu.add_command(label="3-Room Floorplan",command=lambda: self.openimage("3-Room Flooplan"))
        #submenu.add_separator()
        submenu.add_command(label="4-Room Floorplan",command=lambda: self.openimage("4-Room Flooplan"))
        #submenu.add_separator()
        submenu.add_command(label="5-Room Floorplan",command=lambda: self.openimage("5-Room Flooplan"))
        file_menu.add_cascade(label="Open", menu=submenu, underline=0)
        #file_menu.add_separator()
        file_menu.add_command(label="Save",command=self.saveimage)
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=root.quit)



        edit_menu=Menu(my_menu,tearoff=False)
        my_menu.add_cascade(label="Edit",menu=edit_menu)
        edit_menu.add_command(label="Flip Vertical",command=self.flipdef)
        #edit_menu.add_separator()
        edit_menu.add_command(label="Flip Horizontal",command=self.fliphordef)






        self.delcom=0
        self.delcom2=0

        self.a1=0
        self.a2=0
        self.a3=0
        self.a4=0
        self.ent2=0
        #self.canvasScale     = 1.0
        #self.canvasScale *= 2.0
        #canvas.pack (expand =1, fill =tk.BOTH)
        self.canvas.tag_bind("DnD","<Button-1>")




        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.iid = None
           
        #self.msd=self.canvas.find_closest(self.event.x, self.event.y)[0]
        self.canvas.bind("<ButtonPress-1>", self.on_button_1)
         
        self.canvas.tag_bind( "token","<ButtonPress-1>", self.drag_start)
        self.canvas.tag_bind("token","<ButtonRelease-1>", self.drag_stop)
        self.canvas.tag_bind("token","<B1-Motion>", self.drag)













        self.floorplan=str(root.filename)
        #self.iimg=Image.open("C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Dataset_3roomsmall\\Cat1_1.jpg")




        self.iimg2=Image.open( PATH6)
        strr=PATH6

        self.iimg2.save(PATH7)
        self.width,self.height=self.iimg2.size
        #self.iimg2 = self.iimg2.resize((self.canvas.winfo_width(),self.canvas.winfo_height()), Image.ANTIALIAS)
        self.iimg2 = self.iimg2.resize((1270,700), Image.ANTIALIAS)
        
        #self.iimg=iimg.resize((1000, 800), Image.ANTIALIAS)
        
        #print(self.width,self.height)
        #print((1350*700)/(self.width*self.height))
        self.canvas.img2=ImageTk.PhotoImage(self.iimg2)
        #self.mylist.append(self.canvas.img)
        #canvas.img = canvas.img.resize((250, 250), Image.ANTIALIAS)
        self.canvas_img2=self.canvas.create_image(0,0,image=self.canvas.img2,anchor="nw")


        #to find the angle of rotation
        #img_before = cv2.imread('C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\wall_image.jpg')
        img_before = cv2.imread(strr)
        cv2.imshow("Before", img_before)    
        key = cv2.waitKey(0)

        img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
        img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
        lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)

        angles = []

        for x1, y1, x2, y2 in lines[0]:
            cv2.line(img_before, (x1, y1), (x2, y2), (255, 0, 0), 3)
            angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
            angles.append(angle)

        median_angle = np.median(angles)
        img_rotated = ndimage.rotate(img_before, median_angle)
        print(median_angle)

        self.theta=median_angle





        self.hor_ver=[None]*1000
        self.up_down=[None]*1000
        self.roomcoord=[[0 for y in range(8)]for x in range(len(cfile['bbox_loc'])) ]
        self.roomcoord2=[[0 for y in range(8)]for x in range(len(cfile['bbox_loc'])) ]
        self.roomcoord3=[[0 for y in range(8)]for x in range(len(cfile['bbox_loc'])) ]
        self.array=[0]*4

        #for x in range(len(cfile['bbox_loc'])):
            
            #self.canvas.create_line(cfile['bbox_loc'][x][4]*(1270/self.width),cfile['bbox_loc'][x][0]*(700/self.height),cfile['bbox_loc'][x][5]*(1270/self.width),cfile['bbox_loc'][x][1]*(700/self.height))
            #self.canvas.create_line(cfile['bbox_loc'][x][5]*(1270/self.width),cfile['bbox_loc'][x][1]*(700/self.height),cfile['bbox_loc'][x][6]*(1270/self.width),cfile['bbox_loc'][x][2]*(700/self.height))
            #self.canvas.create_line(cfile['bbox_loc'][x][6]*(1270/self.width),cfile['bbox_loc'][x][2]*(700/self.height),cfile['bbox_loc'][x][7]*(1270/self.width),cfile['bbox_loc'][x][3]*(700/self.height))
            #self.canvas.create_line(cfile['bbox_loc'][x][7]*(1270/self.width),cfile['bbox_loc'][x][3]*(700/self.height),cfile['bbox_loc'][x][4]*(1270/self.width),cfile['bbox_loc'][x][0]*(700/self.height))
                #self.canvas.create_rectangle((cfile['bbox_loc'][x][7]*(1270/self.width)+cfile['bbox_loc'][x][4]*(1270/self.width))/2,(cfile['bbox_loc'][x][2]*(700/self.height)+cfile['bbox_loc'][x][3]*(700/self.height))/2,(cfile['bbox_loc'][x][6]*(1270/self.width)+cfile['bbox_loc'][x][5]*(1270/self.width))/2,(cfile['bbox_loc'][x][0]*(700/self.height)+cfile['bbox_loc'][x][1]*(700/self.height))/2,outline='red')

        for x in range(len(cfile['bbox_loc'])):


            self.roomcoord[x][0]=cfile['bbox_loc'][x][7]*(700/self.height)
            self.roomcoord[x][1]=cfile['bbox_loc'][x][3]*(700/self.height)
            self.roomcoord[x][2]=cfile['bbox_loc'][x][4]*(700/self.height)
            self.roomcoord[x][3]=(cfile['bbox_loc'][x][0])*(700/self.height)
            self.roomcoord[x][4]=cfile['bbox_loc'][x][6]*(700/self.height)
            self.roomcoord[x][5]=(cfile['bbox_loc'][x][2])*(700/self.height)
            self.roomcoord[x][6]=cfile['bbox_loc'][x][5]*(700/self.height)
            self.roomcoord[x][7]=(cfile['bbox_loc'][x][1])*(700/self.height)



            self.roomcoord3[x][0]=self.roomcoord[x][0]
            self.roomcoord3[x][1]=self.roomcoord[x][1]
            self.roomcoord3[x][2]=self.roomcoord[x][2]
            self.roomcoord3[x][3]=self.roomcoord[x][3]
            self.roomcoord3[x][4]=self.roomcoord[x][4]
            self.roomcoord3[x][5]=self.roomcoord[x][5]
            self.roomcoord3[x][6]=self.roomcoord[x][6]
            self.roomcoord3[x][7]=self.roomcoord[x][7]





            #self.canvas.create_rectangle(self.roomcoord[x][0],self.roomcoord[x][1],self.roomcoord[x][2],self.roomcoord[x][3],outline='green')

        #for x in range(len(cfile['bbox_loc'])):
            #print(self.roomcoord[x][0],
            #self.roomcoord[x][1],
            #self.roomcoord[x][2],
            #self.roomcoord[x][3])
        #print(self.roomcoord[2][3])

        self.ro=len(mfile['bbox_loc'][0])
        col=5;
        self.arr1 = [ [0 for y in range(col)] for x in range(1000) ]
        self.arr2 = [ [0 for y in range(col)] for x in range(1000) ] 
        self.arr3=[0]*1000
        self.angar=[0]*1000
        self.flipcheck=[0]*1000

       
        for x in range(self.ro):
            #canvas.create_rectangle((mfile['bbox_loc'][0][x][0][0],mfile['bbox_loc'][0][x][0][1],mfile['bbox_loc'][0][x][0][0]+mfile['bbox_loc'][0][x][0][2],mfile['bbox_loc'][0][x][0][1]+mfile['bbox_loc'][0][x][0][3]),outline='red',tags=("token","DnD"))
            self.im_crop = self.iimg.crop((mfile['bbox_loc'][0][x][0][0],mfile['bbox_loc'][0][x][0][1],mfile['bbox_loc'][0][x][0][0]+mfile['bbox_loc'][0][x][0][2],mfile['bbox_loc'][0][x][0][1]+mfile['bbox_loc'][0][x][0][3]))
            
            self.iwidth,self.iheight=self.im_crop.size

            self.im_crop=self.im_crop.resize((round(self.iwidth*(1270/self.width)),round(self.iheight*(700/self.height))),Image.ANTIALIAS)
            
            self.im_crop.save(PATH8+str(x)+".jpg")                     
      
            self.canvas.im_crop2=ImageTk.PhotoImage(self.im_crop)

 

            #self.xcrop=self.canvas.create_image((((mfile['bbox_loc'][0][x][0][0]+mfile['bbox_loc'][0][x][0][2]+mfile['bbox_loc'][0][x][0][0])*(1270/self.width))/2,((mfile['bbox_loc'][0][x][0][1]+mfile['bbox_loc'][0][x][0][3]+mfile['bbox_loc'][0][x][0][1])*(700/self.height))/2), image=self.canvas.im_crop2)
            self.xcrop=self.canvas.create_image((((mfile['bbox_loc'][0][x][0][0])*(1270/self.width)),((mfile['bbox_loc'][0][x][0][1])*(700/self.height))), image=self.canvas.im_crop2,anchor="nw")
            
            #if(x==13):
             #   self.canvas.tag_lower(self.xcrop)
            #self.images[x]=self.xcrop
            #canvas.create_image(1000,1000,image=im_crop2)
            self.arr1[x][0]=mfile['bbox_loc'][0][x][0][0]*(1270/self.width)
            self.arr1[x][1]=mfile['bbox_loc'][0][x][0][1]*(700/self.height)
            self.arr1[x][2]=(mfile['bbox_loc'][0][x][0][0]+mfile['bbox_loc'][0][x][0][2])*(1270/self.width)
            self.arr1[x][3]=(mfile['bbox_loc'][0][x][0][1]+mfile['bbox_loc'][0][x][0][3])*(700/self.height)

            #print(arr1[x][0])

            self.arr2[x][0]=self.arr1[x][0]
            self.arr2[x][1]=self.arr1[x][1]
            self.arr2[x][2]=self.arr1[x][2]
            self.arr2[x][3]=self.arr1[x][3]


            self.arr3[x]=1
            chck=0
            chck2=0
            y111=0
            y112=0
            x111=Point(0,0)
            x112=Point(0,0)
            ui3=0

            for y in range(len(cfile['bbox_loc'])):

                ui3=0

                for y111 in range(4):

                    chck=0

                    if(y111==0):
                        l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                        d1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                    if(y111==1):
                        l1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                        d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                    if(y111==2):
                        l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                        d1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                    if(y111==3):
                        l1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                        d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                    for y112 in range(4):
                        if(y112==0):
                            l2=Point(self.arr2[x][0],self.arr2[x][1])
                            d2=Point(self.arr2[x][0],self.arr2[x][3])
                        if(y112==1):
                            l2=Point(self.arr2[x][0],self.arr2[x][3])
                            d2=Point(self.arr2[x][2]+3,self.arr2[x][3])
                        if(y112==2):
                            l2=Point(self.arr2[x][0],self.arr2[x][1])
                            d2=Point(self.arr2[x][2]+3,self.arr2[x][1])
                        if(y112==3):
                            l2=Point(self.arr2[x][2]+3,self.arr2[x][1])
                            d2=Point(self.arr2[x][2]+3,self.arr2[x][3])
  
                        #if(self.doIntersect(l1,d1,l2,d2) and (l2.x!=0) and (l2.y!=0) ):
                        if(dfile['dfile'][0][x]==1 and self.doIntersect(l1,d1,l2,d2) and (l2.x!=0) and (l2.y!=0)) :
                            chck=1
                            if(ui3==0):
                                chck2=chck2+1
                                ui3=1

                            print(chck2,x,1000)
                            self.room_doors[y]=self.room_doors[y]+1
                            self.room_doors2[y]=self.room_doors[y]
                            zz=0
                            for z in range(4):
                                if(z==0):
                                    l3=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                    d3=Point(self.roomcoord3[y][2],self.roomcoord3[y][3]) 
                                if(z==1):
                                    l3=Point(self.roomcoord3[y][2],self.roomcoord3[y][3])
                                    d3=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                if(z==2):
                                    l3=Point(self.roomcoord3[y][4],self.roomcoord3[y][5])
                                    d3=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                if(z==3):
                                    l3=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                    d3=Point(self.roomcoord3[y][4],self.roomcoord3[y][5]) 
            
                                l4=Point(self.arr2[x][0],self.arr2[x][1])
                                d4=Point(self.arr2[x][2],self.arr2[x][3])

                                if(l4.x<=l3.x and l3.x<=d4.x):
                                    self.arr2[x][4]=1
                                    self.arr1[x][4]=1
                                    self.hor_ver[x]='V'
                                    if(abs(l4.x-l3.x)>abs(l3.x-d4.x)):
                                        self.up_down[x]='L'
                                    else:
                                        self.up_down[x]='R'
                                if(l4.y<=l3.y and l3.y<=d4.y ):
                                    self.arr2[x][4]=1
                                    self.arr1[x][4]=1
                                    self.hor_ver[x]='H'
                                    if(abs(l4.y-l3.y)>abs(l3.y-d4.y)):
                                        self.up_down[x]='U'
                                    else:
                                        self.up_down[x]='D'

                            break

                    if(chck==1):
                        break



            if(chck2==1):
                self.main_doors=self.main_doors+1
                self.main_doors_check[x]=1

            self.mylist.append(self.canvas.im_crop2)

        self.canvas.delete(self.canvas_img)
        self.popup = tk.Menu(self.canvas, tearoff=0)
        self.canvas.bind("<Button-3>", self.do_popup)
        
        self.cup=self.canvas.create_rectangle(1275,16,1527,476,fill='grey81')
        self.mylist.append(self.cup)

        self.ent=0





    def bounding_rect(self,contours,image):
        contours_poly = [None]*len(contours)
        boundRect = [None]*len(contours)
        for i, c in enumerate(contours):
            contours_poly[i] = cv2.approxPolyDP(c, 3, True)
            boundRect[i] = cv2.boundingRect(contours_poly[i])
            #cv2.drawContours(image, contours_poly, i, (255,0,0))
            cv2.rectangle(image, (int(boundRect[i][0]), int(boundRect[i][1])),(int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), (255,0,0), 1)

    def bounding_circle(self,contours,image):
        contours_poly = [None]*len(contours)
        centers = [None]*len(contours)
        radius = [None]*len(contours)
        for i, c in enumerate(contours):
            contours_poly[i] = cv2.approxPolyDP(c, 3, True)
            centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])
            cv2.circle(image, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), (0,255,0), -1)
        return centers

    def convex_hull(self,contours,image,drawing):
        temp = drawing.copy()
        hull_list = []
        for i in range(len(contours)):
            hull = cv2.convexHull(contours[i])
            cv2.drawContours(image, contours[i], -1, (150,200,0),1)
            area = cv2.contourArea(hull)
            peri = cv2.arcLength(hull, closed=True)
            approx = cv2.approxPolyDP(hull, 0.16 * peri, True)
            
            '''
            print(cv2.contourArea(hull),peri,len(approx))
            cv2.imshow("con",image)
            cv2.waitKey()
            '''
            if(area>MIN_HULL_AREA and area<MAX_HULL_AREA and len(approx)==3):
                hull_list.append(hull)
        #cv2.drawContours(image, hull_list, -1, (150,200,0),1)
        cv2.drawContours(drawing, hull_list, -1, (255,255,255),1)
        
        return hull_list

    def close_doors(self,hull_list,centers,gray_1):
        partner_points = {"point":[],"hull":[]}
        for i,center in enumerate(centers):
            for j,hull in enumerate(hull_list):
                dist = cv2.pointPolygonTest(hull,(int(center[0]),int(center[1])),True)
                #print(dist)
                if(abs(dist)<=MIN_PROXIMITY):
                    if j in partner_points["hull"]:
                        partner_index = partner_points["hull"].index(j)
                        partner_point = partner_points["point"][partner_index]
                        #print("yo yo : ",partner_index,partner_point)
                        cv2.line(gray_1, (int(centers[partner_point][0]), int(centers[partner_point][1])), (int(centers[i][0]), int(centers[i][1])), (255,255,255), 15,cv2.LINE_AA)
                        #cv2.line(gray_1, (int(centers[partner_point][0]), int(centers[partner_point][1])), (int(centers[i][0]), int(centers[i][1])), (255,255,255), 15,10)
                    
                    partner_points["hull"].append(j)
                    partner_points["point"].append(i)
        
    def get_binary(self,image,_type):
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        if(_type==1):
            gray = cv2.dilate(gray, kernel_dilate, iterations=1)
            gray = cv2.erode(gray, kernel_erode, iterations=1)
            _,gray = cv2.threshold(gray,10,255,cv2.THRESH_BINARY_INV)
            gray = cv2.dilate(gray, kernel_dilate, iterations=3)
            gray = cv2.erode(gray, kernel_erode, iterations=2)
            #gray = cv2.dilate(gray, kernel_dilate, iterations=1)
        else:
            gray = cv2.bitwise_not(gray)
            _,gray = cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
            #gray = cv2.dilate(gray, kernel_dilate, iterations=1)
        return gray

    def get_boundary(self,gray_1):
        temp = gray_1.copy()
        drawing_1 = np.zeros((temp.shape[0], temp.shape[1], 1), dtype=np.uint8)
        contours,_= cv2.findContours(gray_1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(drawing_1,contours,-1,(255,255,255),4)
        #cv2.drawContours(drawing_1,contours,-1,(0,0,0),10,8,4)
        return drawing_1

    def get_contours(self,image,name):

        gray_0 = self.get_binary(image,0)
        gray_1 = self.get_binary(image,1)
        gray_1 = cv2.bitwise_not(gray_1)
        drawing = np.zeros((image.shape[0], image.shape[1], 1), dtype=np.uint8)
        objects = cv2.bitwise_and(gray_0,gray_1)
        objects = cv2.dilate(objects,kernel_dilate,iterations=1)
        gray_1 = cv2.bitwise_not(gray_1)
        contours,_= cv2.findContours(objects,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(image,contours,-1,(0,0,255),1)
        hull_list = self.convex_hull(contours,image,drawing)
        
        door_points = cv2.bitwise_and(gray_1,drawing)
        door_points = cv2.dilate(door_points,kernel_dilate,iterations=1)
        door_point_contours,_= cv2.findContours(door_points,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        centers = self.bounding_circle(door_point_contours,image)
        self.close_doors(hull_list,centers,gray_1)
        
        boundary = self.get_boundary(gray_1)
        #cv2.imshow("gray_1",gray_1)
        #cv2.imshow("boundary",boundary)
        name=name.split('/')
        print("name",len(name))
        #cv2.imwrite("C:\\Users\\User\\Desktop\\outer_boundary",~boundary)
        cv2.imwrite(PATH6,~gray_1)


        print("image saved")







    def saveimage(self):

        files = [('Image','*.jpg'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt'),('All Files', '*.*')] 
        file = asksaveasfile(mode='w',filetypes = files, defaultextension = files)
        if file:
            x2=root.winfo_rootx()+self.canvas.winfo_x()
            y2=root.winfo_rooty()+self.canvas.winfo_y()
            ImageGrab.grab().crop((x2+2,y2+14,x2+1594,y2+900)).save(file)

            #4 10 17 11 12 3 5 7 6 19
    def adding(self,intt,word):

        if(self.ent2==1):
            self.mybutton.unbind('<Button-1>')
            self.canbut.unbind('<Button-1>')
            root.unbind('<Button-1>')
            self.ent=0
                
            self.my_entry.destroy()
            self.mybutton.destroy()
            self.canbut.destroy()
            self.ent2=0




        self.numindex=intt
        self.canvas.delete("colour")
        #self.canvas.delete("delete")
        #self.canvas.delete("Rotate")
        self.obj_name=word

        I=Image.open(PATH5+str(intt)+".tif")
        I=I.convert('RGB')
        I1=I
        if(intt==1):
            I1=I.resize((135,73),Image.ANTIALIAS)
        if(intt==2):
            I1=I.resize((114,180),Image.ANTIALIAS)
        if(intt==13):
            I1=I.resize((115,58),Image.ANTIALIAS)
        if(intt==4):
            I1=I.resize((115,115),Image.ANTIALIAS)
        if(intt==10):
            I1=I.resize((153,62),Image.ANTIALIAS)
        if(intt==11):
            I1=I.resize((86,95),Image.ANTIALIAS)
        if(intt==3):
            I1=I.resize((108,120),Image.ANTIALIAS)
        if(intt==5):
            I1=I.resize((79,86),Image.ANTIALIAS)
        if(intt==6):
            I1=I.resize((92,95),Image.ANTIALIAS)
        if(intt==19):
            I1=I.resize((173,85),Image.ANTIALIAS)

        self.I2=I1

        self.na,self.ha=I1.size
        self.canvas.aimg=ImageTk.PhotoImage(I1)
        self.canvas.create_image(1350,490,image=self.canvas.aimg,anchor="nw")

        if(self.delbut!=0):
            self.adddel.destroy()
        self.delbut=1
        self.adddel=Button(root,text="Delete",bg="red",fg='white',padx=10,pady=3,font="Times 11 bold",command=self.del_new)
        self.adddel.place(x=1360,y=self.ha+510)


    def del_new(self):
        bid=self.canvas.find_closest(1360,510)[0]
        self.canvas.delete("colour")
        self.canvas.delete(bid)
        self.adddel.destroy()
        self.num_new=0








    def do_popup(self,event):
      # display the popup menu
        try:
            
            self.cid=self.canvas.find_closest(event.x, event.y)[0]
            if(event.x<=1270 and event.y<=750):
                recto=self.canvas.bbox(self.cid)
                for x in range(self.ro):
                    self.edty=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                    edty2=self.canvas.bbox(self.edty)
                    #print(x)
                    if(recto[0]!=0 and recto[1]!=0 and self.a1==recto[0] and self.a2==recto[1] and self.a3==recto[2] and self.a4==recto[3] and recto[0]==edty2[0] and recto[1]==edty2[1] and recto[2]==edty2[2] and recto[3]==edty2[3] and self.del_from_plan[x]==0):
                        self.popup.tk_popup(event.x_root, event.y_root, 0)
                        
                    if(recto[0]==0 and recto[1]==0):
                        self.canvas.delete("colour")
                        
                    else:
                        self.canvas.delete("colour")
                        
            else:
                self.canvas.delete("colour")
        finally:
          # make sure to release the grab (Tk 8.0a1 only)
            self.popup.grab_release() 


    def on_button_1(self, event):
        #print(event.x)

       # print(self.main_doors)
      #  for x in range(3):
       #     print(self.room_doors2[x],self.room_doors[x])
        
       # print('\n')


        if(self.ent2==1):
            self.mybutton.unbind('<Button-1>')
            self.canbut.unbind('<Button-1>')
            root.unbind('<Button-1>')
            self.ent=0
            
            self.my_entry.destroy()
            self.mybutton.destroy()
            self.canbut.destroy()
            self.ent2=0



        if(self.ent2==0):
            self.canvas.delete(self.blink)
            self.blink_stop=0
            self.canvas.delete("colour")
            self.iid=self.canvas.find_closest(event.x, event.y)[0]
            
            #self.canvas.tag_lower(self.iid)

            #self.canvas.im_crop2=ImageTk.PhotoImage(self.im_crop)
            #self.canvas.create_image((((mfile['bbox_loc'][0][2][0][0]+mfile['bbox_loc'][0][2][0][2]+mfile['bbox_loc'][0][2][0][0])*(1350/self.width))/2,((mfile['bbox_loc'][0][2][0][1]+mfile['bbox_loc'][0][2][0][3]+mfile['bbox_loc'][0][2][0][1])*(700/self.height))/2), image=self.canvas.im_crop2)
                

                
            #self.canvas.delete(self.iid)

            rect=self.canvas.bbox(self.iid)


            if(rect[0]>1270 and self.ent==0 and not(event.x>=1275 and event.x<=1527 and event.y>=16 and event.y<=476)):
                #self.delcom=1

                self.canvas.delete("colour")
                if(rect[0]!=0 and rect[1]!=0 and event.x>=1350 and event.x<=1350+self.na and event.y>=490 and event.y<=490+self.ha):
                    self.canvas.create_rectangle(*rect,outline='red',tags="colour",width=3)

                #if(self.delcom==1):

                self.r1=1350
                self.r2=490
                self.r3=1350+self.na
                self.r4=490+self.ha


                #self.canvas.create_rectangle(self.r1,self.r2,self.r3,self.r4,outline='green')

                self.a1=rect[0]
                self.a2=rect[1]
                self.a3=rect[2]
                self.a4=rect[3]

                self.canvas.itemconfigure("DEL")
                self.canvas.dtag("all","DEL")
                self.canvas.itemconfigure(self.iid, tags=("DEL","DnD","token","drag"))

                if(self.obj_name=="DOOR"):
                    self.excep_fbox=1

                self.new_obj=1

                if(self.excep==1):
                    self.excep=0







            if(rect[0]!=0 and rect[1]!=0 and self.ent==0 and rect[0]<=1270 and rect[1]<=700):
                #print(rect[0],rect[1],rect[2],rect[3])
                #self.ent=1
            #print(rect[0])
            #print(rect[1])




                ab=rect[0]
                cd=rect[2]
                ef=rect[1]
                gh=rect[3]



                self.a1=ab
                self.a2=ef
                self.a3=cd
                self.a4=gh

                self.new_obj=0
                if(self.excep_fbox==1):
                    self.excep_fbox=0
                




                self.imp=0
                self.excep=0
                for x in range(self.ro):
                    #print(self.arr2[x][0],ab,self.arr2[x][2],cd,self.arr2[x][1],ef,self.arr2[x][3],gh)
                    tiid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                    tiid2=self.canvas.bbox(tiid)

                 
                    if((ab==tiid2[0]) and (cd==tiid2[2]) and (ef==tiid2[1]) and (gh==tiid2[3]) and self.del_from_plan[x]==0):

                        self.imp=x
                        self.excep=self.arr2[x][4]

                        self.r1=self.arr2[x][0]
                        self.r2=self.arr2[x][1]
                        self.r3=self.arr2[x][2]
                        self.r4=self.arr2[x][3]

                        #print(self.up_down[x],self.hor_ver[x])

                        if(self.excep==0):
                            if(self.delcom==1):
                                self.popup.delete("Delete")
                                #self.popup.delete(self.sep_id1)
                                #self.sep_id1.destroy()
                                self.popup.delete("Rotate")
                            if(self.delcom2==1):
                                self.popup.delete("Move the Door")
                                self.popup.delete("Ignore")
                                #self.popup.delete(self.sep_id2)
                                #self.sep_id2.destroy()
                                self.popup.delete("Delete")
                                #self.popup.delete(self.sep_id3)
                                #self.sep_id3.destroy()
                                self.popup.delete("Horizontal Flip")
                                self.popup.delete("Vertical Flip")

                            #self.canvas.unbind('<Button-1>')

                            self.popup.add_command(label="Delete",command=lambda: self.dele(x))
                          #  self.sep_id1=self.popup.add_separator()
                            #self.popup.add_command(label="Rotate",command= lambda: root.bind("<Button-1>",self.rotate))
                            self.popup.add_command(label="Rotate")
                            self.popup.entryconfig("Rotate",command= lambda: self.rotate(event))


                            self.delcom=1
                            self.delcom2=0
                        else:
                            if(self.delcom2==1):
                                self.popup.delete("Move the Door")
                                self.popup.delete("Ignore")
                                #self.popup.delete(self.sep_id2)
                               # self.sep_id2.destroy()
                                self.popup.delete("Delete")
                                #self.popup.delete(self.sep_id3)
                                #self.sep_id3.destroy()
                                self.popup.delete("Horizontal Flip")
                                self.popup.delete("Vertical Flip")
                            if(self.delcom==1):
                                self.popup.delete("Delete")
                                #self.popup.delete(self.sep_id1)
                                #self.sep_id1.destroy()
                                self.popup.delete("Rotate")


                            #self.canvas.unbind('<Button-1>')

                                                     

                            self.popup.add_command(label="Move the Door")
                            self.popup.entryconfig("Move the Door",command= lambda: self.move_door(event))

                            self.popup.add_command(label="Ignore")
                          #  self.sep_id2=self.popup.add_separator()
                            self.popup.add_command(label="Delete",command=lambda: self.dele(x))
                           # self.sep_id3=self.popup.add_separator()

                            self.popup.add_command(label="Horizontal Flip")
                            self.popup.entryconfig("Horizontal Flip",command= lambda: self.flip_door(event,'H'))

                            self.popup.add_command(label="Vertical Flip")
                            self.popup.entryconfig("Vertical Flip",command= lambda: self.flip_door(event,'V'))


                            #self.popup.add_command(label="Rotate",command= lambda: root.bind("<Button-1>",self.rotate))


                                        




                            self.delcom=0                            
                            self.delcom2=1

                        #print(self.imp)
                        break


                self.canvas.delete("colour")
                if(rect[0]!=0 and rect[1]!=0):
                    self.canvas.create_rectangle(*rect,outline='red',tags="colour",width=3)
                    #print(rect[0],rect[1],rect[2],rect[3])


                    #xorg.set(rect[0])
                    #yorg.set(rect[1])
                #xorg=rect[0]
                #yorg=rect[1]
                #iid = self.canvas.find_enclosed(event.x-150, event.y-150, event.x + 150, event.y + 100)
                #iid=canvas.find_closest(event.x, event.y)[0]
                self.canvas.itemconfigure("DEL")
                self.canvas.dtag("all","DEL")
                self.canvas.itemconfigure(self.iid, tags=("DEL","DnD","token","drag")) 

                #self.canvas.unbind("<ButtonPress-1>")
            if(rect[0]==0 and rect[1]==0):
                if(self.delcom==1):
                    self.popup.delete("Delete")
                    self.popup.delete("Rotate")
                    self.delcom=0
                if(self.delcom2==1):
                    self.popup.delete("Move the Door")
                    self.popup.delete("Ignore")
                    self.popup.delete("Delete")
                    self.popup.delete("Horizontal Flip")
                    self.popup.delete("Vertical Flip")
                    self.delcom2=0

            #canvas.unbind("<Button-1>")

    def move_door(self,event):
        self.move_door_perm=1
        if(self.delcom2==1):
            self.popup.delete("Move the Door")
            self.popup.delete("Ignore")
            self.popup.delete("Delete")
            self.popup.delete("Horizontal Flip")
            self.popup.delete("Vertical Flip")
            self.delcom2=0
        self.blink_stop2=0
        self.start_blink()

    def start_blink(self):
        self.blink=self.canvas.create_rectangle(self.a1,self.a2,self.a3,self.a4,outline='maroon1',width=2)
        self.blink_stop=1
        if(self.blink_stop2==-1):
            self.canvas.delete(self.blink)
            self.blink_stop=0
        self.canvas.after(500,self.stop_blink)

    def stop_blink(self):
        self.canvas.delete(self.blink)
        if(self.blink_stop==1):
            self.canvas.after(500,self.start_blink)


    def drag_start(self, event):
        """Begining drag of an object"""
        # record the item and its location
        #x = self.canvas.canvasx(event.x)
        #y = self.canvas.canvasy(event.y)
        if(self.excep==0 or (self.excep==1 and self.move_door_perm==1) or self.new_obj==1  ):
            #print(self.ent)
            #ex1.set(event.x)
            #ey1.set(event.y)
            self.blink_stop=0
            self.blink_stop2=-1
            self.canvas.delete("colour")


                #print(ey1.get())

            self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
                #self.xyz=self.canvas.find_closest(event.x, event.y)[0]
                #self._drag_data["item"] = self.canvas.find_enclosed(event.x-150, event.y-150, event.x + 150, event.y + 100)
            rect=self.canvas.bbox(self._drag_data["item"])

            for xloo in range(self.ro):
                self.edty3=self.canvas.find_closest((self.arr2[xloo][0]+self.arr2[xloo][2])/2,(self.arr2[xloo][1]+self.arr2[xloo][3])/2)[0]
                edty4=self.canvas.bbox(self.edty3)


            
                if(rect[0]!=0 and rect[1]!=0 and not(event.x>=1275 and event.x<=1527 and event.y>=16 and event.y<=476) and rect[0]==edty4[0] and rect[1]==edty4[1] and rect[2]==edty4[2] and rect[3]==edty4[3] and self.del_from_plan[xloo]==0):
                    self.canvas.addtag_enclosed("drag",*rect)
                
                #print(rect)
            self._drag_data["x"] = event.x
            self._drag_data["y"] = event.y
    


    def drag(self, event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved

        if(self.excep==0 or (self.excep==1 and self.move_door_perm==1) or self.new_obj==1):


            self.canvas.delete("colour")
            self.canvas.dtag("colour","colour")
            recti=self.canvas.bbox(self.iid)

            cvt=999
            if(self.new_obj==0):
                cvt=self.imp

            if(recti[0]!=0 and recti[1]!=0 and not(event.x>=1275 and event.x<=1527 and event.y>=16 and event.y<=476) and self.del_from_plan[cvt]==0):
                self.delta_x = event.x - self._drag_data["x"]
                self.delta_y = event.y - self._drag_data["y"]
            # move the object the appropriate amount
            
                self.canvas.move("drag", self.delta_x, self.delta_y)
            # record the new  
                self._drag_data["x"] = event.x
                self._drag_data["y"] = event.y

            
                a0=recti[0]
                a1=recti[1]
                a2=recti[2]
                a3=recti[3]

                rs=0
                #self.move_door_perm=0
                for x in range(self.ro):
                    l1=Point(self.arr2[x][0],self.arr2[x][1])
                    d1=Point(self.arr2[x][2],self.arr2[x][3])
                    l2=Point(recti[0],recti[1])
                    d2=Point(recti[2],recti[3])

                    #p=self.imp
                
                    if(self.doOverlap(l1, d1, l2, d2) and (l2.x!=0) and (l2.y!=0) and self.r1!=l2.x and self.r2!=l2.y and self.del_from_plan[x]==0): 
                        #print(x,p)
                        if(self.new_obj==0):
                            p=self.imp
                            if(x!=p):
                                self.canvas.delete("blucol")
                                rs=1
                                self.canvas.create_rectangle(self.arr2[x][0],self.arr2[x][1],self.arr2[x][2],self.arr2[x][3],outline='purple',tags="blucol",width=3)
                                self.canvas.create_rectangle(recti[0],recti[1],recti[2],recti[3],outline='OrangeRed2',tags="blucol",width=3)
                        else:
                            self.canvas.delete("blucol")
                            rs=1
                            self.canvas.create_rectangle(self.arr2[x][0],self.arr2[x][1],self.arr2[x][2],self.arr2[x][3],outline='purple',tags="blucol",width=3)
                            self.canvas.create_rectangle(recti[0],recti[1],recti[2],recti[3],outline='OrangeRed2',tags="blucol",width=3)

                    #print(x)
                    #print(p)
                    #self.canvas.move(self.iid,xorg.get()-recti[0],yorg.get()-recti[1])
                    #q=1
                    #messagebox.showerror("","Objects cannot be overlapped")
                    #print("Rectangles Overlap")

                if(rs==0):
                    self.canvas.delete("blucol")


                


    def drag_stop(self, event):
        """End drag of an object"""
        
        #print(p)





        q=0
        #ex2.set(event.x)
        #ey2.set(event.y)
        self.move_door_perm=0

        #if(ex2.get()!=ex1.get()):
            #slope.set((ey2.get()-ey1.get())//(ex2.get()-ex1.get()))
            #self.idid = self.canvas.find_closest(event.x, event.y)[0]
        #self.xyz=self.canvas.find_closest(event.x, event.y)[0]
        #self._drag_data["item"] = self.canvas.find_enclosed(event.x-150, event.y-150, event.x + 150, event.y + 100)
        recti=self.canvas.bbox(self.iid)
        c0=recti[0]
        c1=recti[1]
        c2=recti[2]
        c3=recti[3]


        if(not(event.x>=1275 and event.x<=1527 and event.y>=16 and event.y<=476) ):


            if(not(recti[0]==self.a1 and recti[1]==self.a2) and not(self.a1==0 and self.a2==0) and self.excep==1):

                y111=0
                y112=0
                x111=Point(0,0)
                x112=Point(0,0)
                chck=0
                for y in range(len(cfile['bbox_loc'])):
                    for y111 in range(4):

                        chck=0
                        
                        if(y111==0):
                            l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                            d1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                        if(y111==1):
                            l1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                            d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                        if(y111==2):
                            l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                            d1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                        if(y111==3):
                            l1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                            d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                        for y112 in range(4):
                            if(y112==0):
                                l2=Point(self.a1,self.a2)
                                d2=Point(self.a3,self.a2)
                            if(y112==1):
                                l2=Point(self.a3,self.a2)
                                d2=Point(self.a3,self.a4)
                            if(y112==2):
                                l2=Point(self.a3,self.a4)
                                d2=Point(self.a1,self.a4)
                            if(y112==3):
                                l2=Point(self.a1,self.a2)
                                d2=Point(self.a1,self.a4)
      
                            if(self.doIntersect(l1,d1,l2,d2) and (l2.x!=0) and (l2.y!=0) ):
                                chck=1
                                self.room_doors2[y]=self.room_doors2[y]-1
                                break
                    if(chck==1):
                        break


            chck=0
            chck2=0

            

            qrch=0
            for y in range(len(cfile['bbox_loc'])):

                if(1):
                    for y111 in range(4):

                        chck=0
                        
                        if(y111==0):
                            l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                            d1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                        if(y111==1):
                            l1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                            d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                        if(y111==2):
                            l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                            d1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                        if(y111==3):
                            l1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                            d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                        for y112 in range(4):
                            if(y112==0):
                                l2=Point(recti[0],recti[1])
                                d2=Point(recti[0],recti[3])
                            if(y112==1):
                                l2=Point(recti[0],recti[3])
                                d2=Point(recti[2],recti[3])
                            if(y112==2):
                                l2=Point(recti[2],recti[3])
                                d2=Point(recti[2],recti[1])
                            if(y112==3):
                                l2=Point(recti[2],recti[1])
                                d2=Point(recti[0],recti[1])
      
                            if(self.doIntersect(l1,d1,l2,d2) and (l2.x!=0) and (l2.y!=0) ):
                                qrch=1
                                break



            if((qrch == 0 ) and (self.excep==1 or self.excep_fbox==1) and self.new_obj==0 ):
                self.canvas.move(self.iid,(self.a1)-recti[0],(self.a2)-recti[1])
                self.canvas.delete("blucol")
                q=1
                messagebox.showerror("Error occured","Door is not connected with any wall")
                for z2 in range(len(cfile['bbox_loc'])):
                    self.room_doors2[z2]=self.room_doors[z2]
                    #l1=Point(self.roomcoord[z2][0],self.roomcoord[z2][1])
                    #d1=Point(self.roomcoord[z2][2],self.roomcoord[z2][3])
                    #l2=Point(self.a1,self.a2)
                    #d2=Point(self.a3,self.a4)

                    #if(self.doOverlap(l1,d1,l2,d2) and not(l2.x==0 and l2.y==0)):
                    #    self.room_doors2[z2]=self.room_doors2[z2]+1
                   #     self.room_doors[z2]=self.room_doors2[z2]

            if(self.new_obj==1 and self.obj_name=="DOOR" and (qrch == 0) and recti[0]!=1350):
                self.canvas.move(self.iid,(self.a1)-recti[0],(self.a2)-recti[1])
                self.canvas.delete("blucol")
                q=1
                messagebox.showerror("Error occured","Door is not connected with any wall")


                #print("Rectangles Overlap")
            





            for x in range(self.ro):
                l1=Point(self.arr2[x][0],self.arr2[x][1])
                d1=Point(self.arr2[x][2],self.arr2[x][3])
                l2=Point(recti[0],recti[1])
                d2=Point(recti[2],recti[3])


                if(self.doOverlap(l1, d1, l2, d2) and (l2.x!=0) and (l2.y!=0) and self.r1!=l2.x and self.r2!=l2.y and self.del_from_plan[x]==0): 
                    #print(x)
                    #print(p)
                    #print(l1.x,l1.y,r1.x,r1.y,l2.x,l2.y,r2.x,r2.y)
                    if(self.new_obj==0):
                        p=self.imp
                        if(x!=p and self.excep==0):
                            self.canvas.move(self.iid,(self.a1)-recti[0],(self.a2)-recti[1])
                            self.canvas.delete("blucol")
                            q=1
                            messagebox.showerror("Error occured","Objects are overlapping")
                            #print("Rectangles Overlap")
                            break


                    else:
                        if(self.excep_fbox==0):
                            self.canvas.move(self.iid,(self.a1)-recti[0],(self.a2)-recti[1])
                            self.canvas.delete("blucol")
                            q=1
                            messagebox.showerror("Error occured","Objects are overlapping")
                                #print("Rectangles Overlap")
                            break


            #print(len(self.skelarr))

            if(q==0):

                for y in range(len(cfile['bbox_loc'])):
                    qrch=0

                    if(1):
                        for y111 in range(4):

                            chck=0
                            
                            if(y111==0):
                                l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                d1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                            if(y111==1):
                                l1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                            if(y111==2):
                                l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                d1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                            if(y111==3):
                                l1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                            for y112 in range(4):
                                if(y112==0):
                                    l2=Point(recti[0],recti[1])
                                    d2=Point(recti[0],recti[3])
                                if(y112==1):
                                    l2=Point(recti[0],recti[3])
                                    d2=Point(recti[2],recti[3])
                                if(y112==2):
                                    l2=Point(recti[2],recti[3])
                                    d2=Point(recti[2],recti[1])
                                if(y112==3):
                                    l2=Point(recti[2],recti[1])
                                    d2=Point(recti[0],recti[1])
          
                                if(self.doIntersect(l1,d1,l2,d2) and (l2.x!=0) and (l2.y!=0) ):
                                    if((self.excep==0 and self.new_obj==0) or (self.new_obj==1 and self.excep_fbox==0)):
                                        self.canvas.move(self.iid,self.r1-recti[0],self.r2-recti[1])
                                        q=1
                                        messagebox.showerror("Error Occured","Object is overlapping with wall")                                    
                                        break

                            if(q==1):
                                break

                                    
                        



            #    for x in range(len(self.skelarr)):
             #       l1=Point(self.skelarr[x][0],self.skelarr[x][1])
              #      r1=Point(self.skelarr[x][2],self.skelarr[x][3])
               #     l2=Point(recti[0],recti[1])
                #    r2=Point(recti[2],recti[3])

                 #   if(self.walloverlap(l1,r1,l2,r2) and (self.excep==0) and (l2.x!=0) and (l2.y!=0)):
                  #      self.canvas.move(self.iid,self.r1-recti[0],self.r2-recti[1])
                   #     q=1
                    #    messagebox.showerror("Error Occured","Object is overlapping with wall")
                    #print("Rectangles Overlap")
                     #   break 

            check=0
            chck=0
            arch=0

            if(q==0):

                for y in range(len(cfile['bbox_loc'])):
                    chck=0

                    if(1):
                        for y111 in range(4):

                            
                            
                            if(y111==0):
                                l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                d1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                            if(y111==1):
                                l1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                            if(y111==2):
                                l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                d1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                            if(y111==3):
                                l1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                            for y112 in range(4):
                                if(y112==0):
                                    l2=Point(recti[0],recti[1])
                                    d2=Point(recti[0],recti[3])
                                if(y112==1):
                                    l2=Point(recti[0],recti[3])
                                    d2=Point(recti[2],recti[3])
                                if(y112==2):
                                    l2=Point(recti[2],recti[3])
                                    d2=Point(recti[2],recti[1])
                                if(y112==3):
                                    l2=Point(recti[2],recti[1])
                                    d2=Point(recti[0],recti[1])
          
                                if((self.doIntersect(l1,d1,l2,d2)) and (l2.x!=0) and (l2.y!=0) ):
                                    chck=1

                        if(chck==0):

                            xyyz1=min(self.roomcoord[y][0],self.roomcoord[y][2],self.roomcoord[y][4],self.roomcoord[y][6])
                            xyyz2=min(self.roomcoord[y][1],self.roomcoord[y][3],self.roomcoord[y][5],self.roomcoord[y][7])
                            l1=Point(xyyz1,xyyz2)
                            d1=Point(max(self.roomcoord[y][0],self.roomcoord[y][2],self.roomcoord[y][4],self.roomcoord[y][6]),max(self.roomcoord[y][1],self.roomcoord[y][3],self.roomcoord[y][5],self.roomcoord[y][7]))
                    
                            l2=Point(recti[0],recti[1])
                            d2=Point(recti[2],recti[3])
                            if(not(self.doInside(l1,d1,l2,d2))):
                                arch=arch+1

                if(arch==len(cfile['bbox_loc']) and self.a1!=recti[0] and self.a2!=recti[1]):
                    self.canvas.move(self.iid,self.a1-recti[0],self.a2-recti[1])
                    messagebox.showerror("Error occured","Object is not within the boundary")
                    check=0
                    q=1


                    for z2 in range(len(cfile['bbox_loc'])):
                        self.room_doors2[z2]=self.room_doors[z2]










                        #messagebox.showerror("Error occured","Object is not within the boundary")
                        #print("Rectangles Overlap")
                

                    #l1=Point(self.roomcoord[z2][0],self.roomcoord[z2][1])
                    #d1=Point(self.roomcoord[z2][2],self.roomcoord[z2][3])
                    #l2=Point(self.a1,self.a2)
                    #d2=Point(self.a3,self.a4)

                    #if(self.doOverlap(l1,d1,l2,d2) and not(l2.x==0 and l2.y==0)):
                     #   self.room_doors2[z2]=self.room_doors2[z2]+1
                     #   self.room_doors[z2]=self.room_doors2[z2]

                #for y in range(3):
                    #print(self.room_doors[y],self.room_doors2[y])



            p=999
            if(self.new_obj==0):
                p=self.imp



            if(q==0 ):
                if(self.new_obj==0 and self.del_from_plan[p]==0):
                    p=self.imp
                    self.arr2[p][0]=(c0-self.a1)+self.r1
                    self.arr2[p][1]=(c1-self.a2)+self.r2
                    self.arr2[p][2]=(c2-self.a3)+self.r3
                    self.arr2[p][3]=(c3-self.a4)+self.r4

                    #print(self.main_doors,10000)
                    ui=0
                    ui2=0
                    chck53=0
                    #print(self.arr2[p][4])
                    if(self.arr2[p][4]==1):

                        for z3 in range(len(cfile['bbox_loc'])):
                            chck=0
                            ui2=0

                            if(1):
                                for y111 in range(4):

                                    
                                    
                                    if(y111==0):
                                        l1=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                        d1=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                    if(y111==1):
                                        l1=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                        d1=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                    if(y111==2):
                                        l1=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                        d1=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                    if(y111==3):
                                        l1=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                        d1=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                    for y112 in range(4):
                                        if(y112==0):
                                            l2=Point(c0,c1)
                                            d2=Point(c0,c3)
                                        if(y112==1):
                                            l2=Point(c0,c3)
                                            d2=Point(c2,c3)
                                        if(y112==2):
                                            l2=Point(c2,c3)
                                            d2=Point(c2,c1)
                                        if(y112==3):
                                            l2=Point(c2,c1)
                                            d2=Point(c0,c1)
                  
                                        if((self.doIntersect(l1,d1,l2,d2)) and (l2.x!=0) and (l2.y!=0) ):
                                            chck53=chck53+1
                                            ui2=1
                                            break

                                    if(ui2==1):
                                        break





                        if(chck53>1 and self.main_doors_check[p]==1):
                            if(self.main_doors==1):
                                messagebox.showerror("Error Occured","There is no entry door to the house plan")
                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                #                messagebox.showerror("Error occured","Door cannot be connected at the corners")
                                                
                                self.arr2[p][0]=self.r1


                                self.arr2[p][1]=self.r2
                                self.arr2[p][2]=self.r3
                                self.arr2[p][3]=self.r4
                                self.arr2[p][4]=1
                                ui=1

                                for z6 in range(len(cfile['bbox_loc'])):
                                    self.room_doors2[z6]=self.room_doors[z6]

                    if(self.arr2[p][4]==1 and ui==0):
                        self.first=0
                        self.sec=0
                        self.firstv=0
                        self.secv=0
                        ccc=0
                        cccx=0
                        gap1=0
                        gap2=0
                        gap3=0
                        gap4=0
                        self.yy1=0
                        self.yy2=0
                        self.yy3=0

                        self.xx1=0
                        self.xx2=0
                        self.xx3=0
                        self.h1=0
                        self.h2=0
                        self.h3=0

                        self.v1=0
                        self.v2=0

                        cchck=0
                        for y in range(len(cfile['bbox_loc'])):
                            ccc=0
                            cchck=0

                            if(1):
                                for y111 in range(4):

                                    
                                    cchck=0
                                    l2=Point(0,0)
                                    d2=Point(0,0)                                    
                                    if(y111==0):
                                        l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                        d1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                    if(y111==1):
                                        l1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                        d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                                    if(y111==2):
                                        l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                        d1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                    if(y111==3):
                                        l1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                        d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                                    for y112 in range(4):
                                        if(y112==0):
                                            l2=Point(c0,c1)
                                            d2=Point(c0,c3)
                                        if(y112==1):
                                            l2=Point(c0,c3)
                                            d2=Point(c2,c3)
                                        if(y112==2):
                                            l2=Point(c2,c3)
                                            d2=Point(c2,c1)
                                        if(y112==3):
                                            l2=Point(c2,c1)
                                            d2=Point(c0,c1)
                  
                                        if((self.doIntersect(l1,d1,l2,d2)) and (l2.x!=0) and (l2.y!=0) ):
                                            cchck=1


                                            if((self.first==1 and self.sec==1) or (self.firstv==1 and self.secv==1) ):
                                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                self.arr2[p][0]=self.r1
                                                self.arr2[p][1]=self.r2
                                                self.arr2[p][2]=self.r3
                                                self.arr2[p][3]=self.r4
                                                self.arr2[p][4]=1

                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    self.room_doors2[z1]=self.room_doors[z1]
                                                    #l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                    #d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                    #l6=Point(self.a1,self.a2)
                                                    #d6=Point(self.a3,self.a4)
                                                    #chck33=0
                                                    #if((self.doOverlap(l5,d5,l6,d6)) and not(l6.x==0 and l6.y==0)):
                                                        #self.room_doors2[z1]=self.room_doors2[z1]+1
                                                        #self.room_doors[z2]=self.room_doors2[z2]

                                                messagebox.showerror("Error occured","Door cannot be connected at the corners")
                                                print(self.first,self.firstv,self.sec,self.secv)
                                                ccc=1
                                                break




                                            chck2=0
                                            zz=0
                                            #print(111)
                                            for z in range(4):
                                                l3=Point(0,0)
                                                d3=Point(0,0)
                                                if(z==0):
                                                    l3=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                                    d3=Point(self.roomcoord3[y][2],self.roomcoord3[y][3]) 
                                                if(z==1):
                                                    l3=Point(self.roomcoord3[y][2],self.roomcoord3[y][3])
                                                    d3=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                                if(z==2):
                                                    l3=Point(self.roomcoord3[y][4],self.roomcoord3[y][5])
                                                    d3=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                                if(z==3):
                                                    l3=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                                    d3=Point(self.roomcoord3[y][4],self.roomcoord3[y][5]) 
                            
                                                l4=Point(c0,c1)
                                                d4=Point(c2,c3)
                                                if(z==0):
                                                    self.v1=l3.x
                                                if(z==2):
                                                    self.v2=l3.x
                                                if(z==3):
                                                    self.h2=l3.y
                                                if(z==1):
                                                    self.h1=l3.y
                                                #print(l4.x,l3.x,d4.x,d3.x)
                                                if(l4.x<=l3.x and l3.x<=d4.x and (z==0 or z==2)):
                                                    #print(1)
                                                    chck2=chck2+1
                                                    if(self.firstv==1):
                                                        self.secv=1
                                                    else:
                                                        if(self.firstv==0):
                                                            self.firstv=1

                                                    if(self.xx1!=0):
                                                        self.xx2=l3.x
                                                    else:
                                                        self.xx1=l3.x
                                                        self.xx3=self.xx1
                                                    gap3=abs(l4.x-l3.x)
                                                    gap4=abs(l3.x-d4.x)

                                                    #print(chck2)
                                                    if(chck2==2):
                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                        messagebox.showerror("Error occured","Door cannot be connected at the corners")
                                                        print(self.first,self.firstv,self.sec,self.secv)
                                                        #print(chck2)
                                                        
                                                        self.arr2[p][0]=self.r1

                                                        self.arr2[p][1]=self.r2
                                                        self.arr2[p][2]=self.r3
                                                        self.arr2[p][3]=self.r4
                                                        self.arr2[p][4]=1
                                                        for z in range(len(cfile['bbox_loc'])):
                                                            self.room_doors2[z]=self.room_doors[z]
                                                            #l5=Point(self.roomcoord[z][0],self.roomcoord[z][1])
                                                            #d5=Point(self.roomcoord[z][2],self.roomcoord[z][3])
                                                            #l6=Point(self.a1,self.a2)
                                                            #d6=Point(self.a3,self.a4)
                                                            #chck33=0
                                                            #if((self.doOverlap(l5,d5,l6,d6)) and not(l6.x==0 and l6.y==0)):
                                                                
                                                        ccc=1
                                                        break




                                                        

                                                if(l4.y<=l3.y and l3.y<=d4.y and (z==1 or z==3)):
                                                    #print(11)
                                                    chck2=chck2+1
                                                    if(self.first==1):
                                                        self.sec=1
                                                    else:
                                                        if(self.first==0):
                                                            self.first=1


                                                    self.h3=l3.y
                                                    if(self.yy1!=0):
                                                        self.yy2=l3.y
                                                    else:
                                                        self.yy1=l3.y
                                                        self.yy3=self.yy1
                                                    gap1=abs(l4.y-l3.y)
                                                    gap2=abs(l3.y-d4.y)
                                                    #print(chck2)
                                                    if(chck2==2):
                                                        messagebox.showerror("Error occured","Door cannot be connected at the corners")
                                                        print(self.first,self.firstv,self.sec,self.secv)
                                                        #print(1000)
                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                        self.arr2[p][0]=self.r1
                                                        self.arr2[p][1]=self.r2
                                                        self.arr2[p][2]=self.r3
                                                        self.arr2[p][3]=self.r4
                                                        self.arr2[p][4]=1
                                                        for z in range(len(cfile['bbox_loc'])):
                                                            self.room_doors2[z]=self.room_doors[z]
                                       


                                                        ccc=1
                                                        break
                                            break

                                        if(cchck==1):
                                            break

                                    if(cchck==1):
                                        break





                                    if(ccc==1):
                                        break

                                if(ccc==1):
                                    break

                            if(ccc==1):
                                break




                        #print(self.first,self.sec)

                        

                        if(self.firstv==1 and self.first==0):
                            if(self.secv==0 and self.firstv==1):
                                #print(1)
                                self.firstv=0
                                self.secv=0
                                self.xx1=0
                                self.xx2=0
                                #self.yy3=0

                                if(1):

                                    for y in range(len(cfile['bbox_loc'])):
                                        chck=0
                                        ui2=0

                                        if(1):
                                            for y111 in range(4):

                                                l2=Point(0,0)
                                                d2=Point(0,0)                                            
                                                if(y111==0):
                                                    l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                                    d1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                                if(y111==1):
                                                    l1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                                    d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                                                if(y111==2):
                                                    l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                                    d1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                                if(y111==3):
                                                    l1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                                    d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                                                for y112 in range(4):
                                                    if(y112==0):
                                                        if(gap3>gap4):
                                                            l2=Point(c0+20,c1)
                                                            d2=Point(c0+20,c3)
                                                        else:
                                                            l2=Point(c0-20,c1)
                                                            d2=Point(c0-20,c3)
                                                    if(y112==1):
                                                        if(gap3>gap4):
                                                            l2=Point(c0+20,c3)
                                                            d2=Point(c2+20,c3)
                                                        else:
                                                            l2=Point(c0-20,c3)
                                                            d2=Point(c2-20,c3)
                                                    if(y112==2):
                                                        if(gap3>gap4):
                                                            l2=Point(c2+20,c3)
                                                            d2=Point(c2+20,c1)
                                                        else:
                                                            l2=Point(c2-20,c3)
                                                            d2=Point(c2-20,c1)
                                                    if(y112==3):
                                                        if(gap3>gap4):
                                                            l2=Point(c2+20,c1)
                                                            d2=Point(c0+20,c1)
                                                        else:
                                                            l2=Point(c2-20,c1)
                                                            d2=Point(c0-20,c1)
                              
                                                    if((self.doIntersect(l1,d1,l2,d2)) and (l2.x!=0) and (l2.y!=0) ):
                                                        ui2=1

                                                        if((self.firstv==1 and self.secv==1) or (self.first==1 and self.sec==1)):
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            self.arr2[p][4]=1
                                                            for z in range(len(cfile['bbox_loc'])):
                                                                self.room_doors2[z]=self.room_doors[z]

                                                            messagebox.showerror("Error occured","Door cannot be connected at the corners")
                                                            print(self.first,self.firstv,self.sec,self.secv)
                                                            ccc=1
                                                            break
                                                        if(self.firstv==1):
                                                            self.secv=1
                                                        else:
                                                            if(self.firstv==0):
                                                                self.firstv=1


                                                        chck2=0
                                                        zz=0
                                                        #print(111)
                                                        for z in range(4):
                                                            l3=(0,0)
                                                            d3=(0,0)
                                                            if(z==0):
                                                                l3=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                                                d3=Point(self.roomcoord3[y][2],self.roomcoord3[y][3]) 
                                                            if(z==1):
                                                                l3=Point(self.roomcoord3[y][2],self.roomcoord3[y][3])
                                                                d3=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                                            if(z==2):
                                                                l3=Point(self.roomcoord3[y][4],self.roomcoord3[y][5])
                                                                d3=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                                            if(z==3):
                                                                l3=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                                                d3=Point(self.roomcoord3[y][4],self.roomcoord3[y][5]) 

                                                            l4=Point(0,0)
                                                            d4=Point(0,0)
                                        
                                                            if(gap3>gap4):
                                                                l4=Point(c0+20,c1)
                                                                d4=Point(c2+20,c3)
                                                            else:
                                                                l4=Point(c0-20,c1)
                                                                d4=Point(c2-20,c3)
                                                            
                                                            #print(l4.x,l3.x,d4.x,d3.x)
                                                            if(l4.x<=l3.x and l3.x<=d4.x and (z==0 or z==2)):
                                                                #print(1)
                                                                chck2=chck2+1
                                                                #print(z,100)
                                                                if(self.xx1!=0):
                                                                    self.xx2=l3.x
                                                                else:
                                                                    self.xx1=l3.x
                                                                

                                                                #print(chck2)
                                                                if(chck2==2):
                                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                    messagebox.showerror("Error occured","Door cannot be connected at the corners")
                                                                    #print(self.first,self.firstv,self.sec,self.secv)
                                                                    
                                                                    self.arr2[p][0]=self.r1
                                                                    self.arr2[p][1]=self.r2
                                                                    self.arr2[p][2]=self.r3
                                                                    self.arr2[p][3]=self.r4
                                                                    self.arr2[p][4]=1
                                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                                        self.room_doors2[z1]=self.room_doors[z1]

                                                                    ccc=1
                                                                    break


                                                                    

                                                            if(l4.y<=l3.y and l3.y<=d4.y and (z==1 or z==3)):
                                                                #print(11)
                                                                chck2=chck2+1
                                                                #print(z,100)
                                                                if(self.yy1!=0):
                                                                    self.yy2=l3.y
                                                                else:
                                                                    self.yy1=l3.y
                                                                #gap1=abs(l4.y-l3.y)
                                                                #gap2=abs(l3.y-d4.y)
                                                                #print(chck2)
                                                                if(chck2==2):
                                                                    messagebox.showerror("Error occured","Door cannot be connected at the corners")
                                                                    #print(self.first,self.firstv,self.sec,self.secv)
                                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                    self.arr2[p][0]=self.r1
                                                                    self.arr2[p][1]=self.r2
                                                                    self.arr2[p][2]=self.r3
                                                                    self.arr2[p][3]=self.r4
                                                                    self.arr2[p][4]=1
                                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                                        self.room_doors2[z1]=self.room_doors[z1]
                                                                    ccc=1
                                                                    break
                                                        break

                                                    if(ui2==1):
                                                        break

                                                if(ui2==1):
                                                    break

                                        if(ccc==1):
                                            break

                            #print(self.xx1,self.xx2,self.v1,self.v2,self.h1,self.h2,100)

                            if(self.firstv==0 and self.xx3!=0):
                                self.xx1=self.xx3
                                self.firstv=1

                            if(self.secv==1 and ccc==0 and not(c0==self.a1 and c1==self.a2)):
                                #print(1)
                                if(self.xx2>self.xx1):
                                    #print(self.yy2,self.arr2[p][3])]
                                    #print(111)
                                    zq=0
                                    if(self.up_down[p]=='U' or self.up_down[p]=='L'):

                                        for y in range(self.ro):
                                            l1=Point(self.arr2[y][0],self.arr2[y][1])
                                            d1=Point(self.arr2[y][2],self.arr2[y][3])
                                            l2=Point(self.arr2[p][0]+self.xx2-self.arr2[p][2]+6,self.arr2[p][1])
                                            d2=Point(self.xx2+6,self.arr2[p][3])


                                            if(self.doOverlap(l1, d1, l2, d2) and not((l2.x==0) and (l2.y==0)) and self.r1!=l2.x and self.r2!=l2.y and self.del_from_plan[y]==0): 
                                                #print(x)
                                                #print(p)
                                                #print(l1.x,l1.y,r1.x,r1.y,l2.x,l2.y,r2.x,r2.y)
                                                if(self.new_obj==0):
                                                    if(y!=p):
                                                        zq=0
                                                        for z in range(self.ro):
                                                            l3=Point(self.arr2[z][0],self.arr2[z][1])
                                                            d3=Point(self.arr2[z][2],self.arr2[z][3])
                                                            l4=Point(self.xx1-6,self.arr2[p][1])
                                                            d4=Point(self.arr2[p][2]+self.xx1-6-self.arr2[p][0],self.arr2[p][3])

                                                            if(self.doOverlap(l3,d3,l4,d4) and not(l4.x==0 and l4.y==0) and z!=p and self.del_from_plan[z]==0):
                                                                zq=1
                                                                messagebox.showerror("Error occured","Door may overlap with objects")
                                                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                self.arr2[p][0]=self.r1
                                                                self.arr2[p][1]=self.r2
                                                                self.arr2[p][2]=self.r3
                                                                self.arr2[p][3]=self.r4
                                                                self.arr2[p][4]=1

                                                                for z1 in range(len(cfile['bbox_loc'])):
                                                                    self.room_doors2[z1]=self.room_doors[z1]

                                                                self.canvas.delete("blucol")
                                                                break


                                                        if(zq==0):


                                                            p0=self.xx1-6
                                                            p1=self.arr2[p][1]
                                                            p2=self.xx1-6+self.arr2[p][2]-self.arr2[p][0]
                                                            p3=self.arr2[p][3]
                                                            ccc=0
                                                            for z1 in range(len(cfile['bbox_loc'])):
                                                                
                                                                cchck=0

                                                                if(1):
                                                                    for y111 in range(4):

                                                                        
                                                                        
                                                                        if(y111==0):
                                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                            d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                        if(y111==1):
                                                                            l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                        if(y111==2):
                                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                            d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                        if(y111==3):
                                                                            l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                        for y112 in range(4):
                                                                            if(y112==0):
                                                                                l6=Point(p0,p1)
                                                                                d6=Point(p0,p3)
                                                                            if(y112==1):
                                                                                l6=Point(p0,p3)
                                                                                d6=Point(p2,p3)
                                                                            if(y112==2):
                                                                                l6=Point(p2,p3)
                                                                                d6=Point(p2,p1)
                                                                            if(y112==3):
                                                                                l6=Point(p2,p1)
                                                                                d6=Point(p0,p1)
                                                      
                                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                                self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                                ccc=1
                                                                                break

                                                                        if(ccc==1):
                                                                            break



                                                            xlxl=0
                                                            for z1 in range(len(cfile['bbox_loc'])):
                                                                if(self.room_doors2[z1]==0):
                                                                    messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                                    xlxl=1
                                                                    for z2 in range(1000):
                                                                        self.room_doors2[z2]=self.room_doors[z2]

                                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                    self.arr2[p][0]=self.r1
                                                                    self.arr2[p][1]=self.r2
                                                                    self.arr2[p][2]=self.r3
                                                                    self.arr2[p][3]=self.r4
                                                                    break

                                                            if(xlxl==0):
                                                            
                                                                if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                                    messagebox.showerror("Error Occured","There is no entry into the house plan")
                                                                    xlxl=1
                                                                    for z2 in range(1000):
                                                                        self.room_doors2[z2]=self.room_doors[z2]

                                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                    self.arr2[p][0]=self.r1
                                                                    self.arr2[p][1]=self.r2
                                                                    self.arr2[p][2]=self.r3
                                                                    self.arr2[p][3]=self.r4
                                                                    break


                                                            if(xlxl==0):
                                                                for z2 in range(1000):
                                                                    self.room_doors[z2]=self.room_doors2[z2]

                                                                juk=Image.open(PATH8+str(p)+".jpg")
                                                                jux=juk.convert('RGB')
                                                                iiux=ImageOps.mirror(jux)

                                                                if(self.main_doors_check[p]==1):
                                                                    self.main_doors=self.main_doors-1
                                                                    self.main_doors_check[p]=0


                                                                if(self.up_down[p]=='U'):
                                                                    iiux=iiux.rotate(-90,expand=True,fillcolor='white')
                                                                
                                                                iiux=iiux.rotate(-(2*self.theta),expand=True,fillcolor='white')


                                                                x66=iiux.width
                                                                y66=iiux.height
                                                                iiux.save(PATH8+str(p)+".jpg")
                                                                self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                print(2229)
                                                                self.canvas.create_image(self.xx1-6,self.arr2[p][1],image=self.canvas.iip,anchor="nw")
                                                                self.mylist.append(self.canvas.iip)
                                                                self.canvas.delete(self.iid)


                                                                xlxl=0



                                                                xe=self.arr2[p][2]-self.arr2[p][0]
                                                                self.arr2[p][0]=self.xx1-6
                                                                self.arr2[p][3]=self.arr2[p][1]+y66
                                                                self.arr2[p][2]=self.xx1-6+x66
                                                                self.arr2[p][4]=1
                                                                


                                                                if(self.up_down[p]=='U'):
                                                                    self.up_down[p]='R'
                                                                else:
                                                                    if(self.up_down[p]=='L'):
                                                                        self.up_down[p]='R'

                                                                self.hor_ver[p]='V'

                                                                self.canvas.delete("blucol")
                                                                zq=1
                                                                break


                                        if(zq==0):
                                            p0=self.xx2+6-self.arr2[p][2]+self.arr2[p][0]
                                            p1=self.arr2[p][1]
                                            p2=self.xx2+6
                                            p3=self.arr2[p][3]
                                            ccc=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                
                                                cchck=0

                                                if(1):
                                                    for y111 in range(4):

                                                        
                                                        
                                                        if(y111==0):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                        if(y111==1):
                                                            l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        if(y111==2):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                        if(y111==3):
                                                            l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        for y112 in range(4):
                                                            if(y112==0):
                                                                l6=Point(p0,p1)
                                                                d6=Point(p0,p3)
                                                            if(y112==1):
                                                                l6=Point(p0,p3)
                                                                d6=Point(p2,p3)
                                                            if(y112==2):
                                                                l6=Point(p2,p3)
                                                                d6=Point(p2,p1)
                                                            if(y112==3):
                                                                l6=Point(p2,p1)
                                                                d6=Point(p0,p1)
                                      
                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                ccc=1
                                                                break

                                                        if(ccc==1):
                                                            break



                                            xlxl=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                if(1):
                                                    if(self.room_doors2[z1]==0):
                                                        messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                        xlxl=1
                                                        for z2 in range(1000):
                                                            self.room_doors2[z2]=self.room_doors[z2]
                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                        self.arr2[p][0]=self.r1
                                                        self.arr2[p][1]=self.r2
                                                        self.arr2[p][2]=self.r3
                                                        self.arr2[p][3]=self.r4
                                                        break

                                            if(xlxl==0):
                                                
                                                if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                    messagebox.showerror("Error Occured","There is no entry into the houseplan")
                                                    xlxl=1
                                                    for z2 in range(1000):
                                                        self.room_doors2[z2]=self.room_doors[z2]
                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                    self.arr2[p][0]=self.r1
                                                    self.arr2[p][1]=self.r2
                                                    self.arr2[p][2]=self.r3
                                                    self.arr2[p][3]=self.r4
                                                    


                                            if(xlxl==0):
                                                for z2 in range(1000):
                                                    self.room_doors[z2]=self.room_doors2[z2]

                                                if(self.main_doors_check[p]==1):
                                                    self.main_doors_check[p]=0
                                                    self.main_doors=self.main_doors-1
                                                if(self.up_down[p]=='U'):
                                                    juk=Image.open(PATH8+str(p)+".jpg")
                                                    #juk.show()
                                                    jux=juk.convert('RGB')
                                                    #iiux=ImageOps.flip(jux)
                                                   
                                                    iiux=jux.rotate(90,expand=True,fillcolor='white')
                                                    #iiux.show()
                                                    x66=iiux.width
                                                    y66=iiux.height
                                                    
                                                    iiux.save(PATH8+str(p)+".jpg")
                                                    self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                
                                                    self.canvas.create_image(self.xx2+6-x66,self.arr2[p][1],image=self.canvas.iip,anchor="nw")
                                                    self.mylist.append(self.canvas.iip)
                                                    self.canvas.delete(self.iid)

                                                if(self.up_down[p]=='L'):
                                                    self.canvas.move(self.iid,(self.xx2-self.arr2[p][2]+6),0)
                                                    self.arr2[p][0]=self.arr2[p][0]+self.xx2-self.arr2[p][2]+6
                                                    self.arr2[p][2]=self.xx2+6
                                                    self.arr2[p][4]=1
                                                    self.canvas.delete("blucol")
                                                else:
                                                    self.up_down[p]='L'
                                                    self.hor_ver[p]='V'
                                                    self.arr2[p][0]=self.xx2+6-x66
                                                    self.arr2[p][2]=self.xx2+6
                                                    self.arr2[p][3]=self.arr2[p][1]+y66
                                                    self.arr2[p][4]=1
                                                    self.canvas.delete("blucol")


                                    if(self.up_down[p]=='D' or self.up_down[p]=='R'):
                                        zq=0

                                        for y in range(self.ro):
                                            l1=Point(self.arr2[y][0],self.arr2[y][1])
                                            d1=Point(self.arr2[y][2],self.arr2[y][3])
                                            l2=Point(self.xx1-6,self.arr2[p][1])
                                            d2=Point(self.arr2[p][2]+self.xx1-6-self.arr2[p][0],self.arr2[p][3])


                                            if(self.doOverlap(l1, d1, l2, d2) and not((l2.x==0) and (l2.y==0)) and self.r1!=l2.x and self.r2!=l2.y and self.del_from_plan[y]==0): 
                                                #print(x)
                                                #print(p)
                                                #print(l1.x,l1.y,r1.x,r1.y,l2.x,l2.y,r2.x,r2.y)
                                                if(self.new_obj==0):
                                                    if(y!=p):
                                                        zq=0
                                                        for z in range(self.ro):
                                                            l3=Point(self.arr2[z][0],self.arr2[z][1])
                                                            d3=Point(self.arr2[z][2],self.arr2[z][3])
                                                            l4=Point(self.arr2[p][0]+self.xx2-self.arr2[p][2]+6,self.arr2[p][1])
                                                            d4=Point(self.xx2+6,self.arr2[p][3])

                                                            if(self.doOverlap(l3,d3,l4,d4) and not(l4.x==0 and l4.y==0) and z!=p and self.del_from_plan[z]==0):
                                                                zq=1
                                                                messagebox.showerror("Error occured","Door may overlap with objects")
                                                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                self.arr2[p][0]=self.r1
                                                                self.arr2[p][1]=self.r2
                                                                self.arr2[p][2]=self.r3
                                                                self.arr2[p][3]=self.r4
                                                                self.arr2[p][4]=1
                                                                for z1 in range(len(cfile['bbox_loc'])):
                                                                    self.room_doors2[z1]=self.room_doors[z1]

                                                            


                                                                self.canvas.delete("blucol")
                                                                break


                                                        if(zq==0):
                                                            p0=self.xx2+6-self.arr2[p][2]+self.arr2[p][0]
                                                            p1=self.arr2[p][1]
                                                            p2=self.xx2+6
                                                            p3=self.arr2[p][3]
                                                            ccc=0
                                                            for z1 in range(len(cfile['bbox_loc'])):
                                                                
                                                                cchck=0

                                                                if(1):
                                                                    for y111 in range(4):

                                                                        
                                                                        
                                                                        if(y111==0):
                                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                            d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                        if(y111==1):
                                                                            l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                        if(y111==2):
                                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                            d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                        if(y111==3):
                                                                            l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                        for y112 in range(4):
                                                                            if(y112==0):
                                                                                l6=Point(p0,p1)
                                                                                d6=Point(p0,p3)
                                                                            if(y112==1):
                                                                                l6=Point(p0,p3)
                                                                                d6=Point(p2,p3)
                                                                            if(y112==2):
                                                                                l6=Point(p2,p3)
                                                                                d6=Point(p2,p1)
                                                                            if(y112==3):
                                                                                l6=Point(p2,p1)
                                                                                d6=Point(p0,p1)
                                                      
                                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                                self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                                ccc=1
                                                                                break

                                                                        if(ccc==1):
                                                                            break

                                                            xlxl=0
                                                            for z1 in range(len(cfile['bbox_loc'])):
                                                                if(1):
                                                                    if(self.room_doors2[z1]==0):
                                                                        messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                                        xlxl=1
                                                                        for z2 in range(1000):
                                                                            self.room_doors2[z2]=self.room_doors[z2]
                                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                        self.arr2[p][0]=self.r1
                                                                        self.arr2[p][1]=self.r2
                                                                        self.arr2[p][2]=self.r3
                                                                        self.arr2[p][3]=self.r4
                                                                        break

                                                            if(xlxl==0):
                                                                
                                                                if(self.main_doors==1 and self.main_doors_check[p]==1):
                                                                    messagebox.showerror("Error Occured","There is no entry into the house plan")
                                                                    xlxl=1
                                                                    for z2 in range(1000):
                                                                        self.room_doors2[z2]=self.room_doors[z2]
                                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                    self.arr2[p][0]=self.r1
                                                                    self.arr2[p][1]=self.r2
                                                                    self.arr2[p][2]=self.r3
                                                                    self.arr2[p][3]=self.r4
                                                                    break



                                                            if(xlxl==0):
                                                                for z2 in range(1000):
                                                                    self.room_doors[z2]=self.room_doors2[z2]
                                                                juk=Image.open(PATH8+str(p)+".jpg")
                                                                jux=juk.convert('RGB')
                                                                iiux=ImageOps.mirror(jux)

                                                                if(self.main_doors_check[p]==1):
                                                                    self.main_doors_check[p]=0
                                                                    self.main_doors=self.main_doors-1

                                                                if(self.up_down[p]=='D'):
                                                                    iiux=iiux.rotate(-90,fillcolor='white',expand=True)
                                                                #if(self.up_down[p]=='R'):
                                                                iiux=iiux.rotate(-(2*self.theta),expand=True,fillcolor='white')

                                                                x66=iiux.width
                                                                y66=iiux.height
                                                                iiux.save(PATH8+str(p)+".jpg")

                                                                self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                
                                                                self.canvas.create_image(self.xx2-x66+6,self.arr2[p][1],image=self.canvas.iip,anchor="nw")
                                                                self.mylist.append(self.canvas.iip)
                                                                self.canvas.delete(self.iid)

                                                                self.arr2[p][0]=self.xx2-x66+6
                                                                self.arr2[p][3]=self.arr2[p][1]+y66
                                                                self.arr2[p][2]=self.xx2+6
                                                                self.arr2[p][4]=1

                                                                if(self.up_down[p]=='D'):
                                                                    self.up_down[p]='L'
                                                                else:
                                                                    if(self.up_down[p]=='R'):
                                                                        self.up_down[p]='L'

                                                                self.hor_ver[p]='V'
                                                                        
                                                                self.canvas.delete("blucol")
                                                                zq=1
                                                                break


                                        self.canvas.delete("blucol")
                                        if(zq==0):
                                            p0=self.xx1-6
                                            p1=self.arr2[p][1]
                                            p2=self.xx1-6+self.arr2[p][2]-self.arr2[p][0]
                                            p3=self.arr2[p][3]
                                            ccc=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                
                                                cchck=0

                                                if(1):
                                                    for y111 in range(4):

                                                        
                                                        
                                                        if(y111==0):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                        if(y111==1):
                                                            l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        if(y111==2):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                        if(y111==3):
                                                            l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        for y112 in range(4):
                                                            if(y112==0):
                                                                l6=Point(p0,p1)
                                                                d6=Point(p0,p3)
                                                            if(y112==1):
                                                                l6=Point(p0,p3)
                                                                d6=Point(p2,p3)
                                                            if(y112==2):
                                                                l6=Point(p2,p3)
                                                                d6=Point(p2,p1)
                                                            if(y112==3):
                                                                l6=Point(p2,p1)
                                                                d6=Point(p0,p1)
                                      
                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                ccc=1
                                                                break

                                                        if(ccc==1):
                                                            break


                                            xlxl=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                if(1):
                                                    if(self.room_doors2[z1]==0):
                                                        messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                        xlxl=1
                                                        for z2 in range(1000):
                                                            self.room_doors2[z2]=self.room_doors[z2]
                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                        self.arr2[p][0]=self.r1
                                                        self.arr2[p][1]=self.r2
                                                        self.arr2[p][2]=self.r3
                                                        self.arr2[p][3]=self.r4
                                                        break

                                            if(xlxl==0):
                                                if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                    messagebox.showerror("Error Occured","There is no entry into the houseplan")
                                                    xlxl=1
                                                    for z2 in range(1000):
                                                        self.room_doors2[z2]=self.room_doors[z2]
                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                    self.arr2[p][0]=self.r1
                                                    self.arr2[p][1]=self.r2
                                                    self.arr2[p][2]=self.r3
                                                    self.arr2[p][3]=self.r4
                                                    


                                            if(xlxl==0):
                                                for z2 in range(1000):
                                                    self.room_doors[z2]=self.room_doors2[z2]
                                                xe=self.arr2[p][2]-self.arr2[p][0]

                                                if(self.main_doors_check[p]==1):
                                                    self.main_doors_check[p]=0
                                                    self.main_doors=self.main_doors-1

                                                if(self.up_down[p]=='R'):
                                                    self.canvas.move(self.iid,(self.xx1-self.arr2[p][0]-6),0)
                                                    self.arr2[p][0]=self.xx1-6
                                                    self.arr2[p][2]=xe+self.xx1-6
                                                    self.arr2[p][4]=1

                                                if(self.up_down[p]=='D'):
                                                    self.up_down[p]='R'
                                                    self.hor_ver[p]='V'
                                                    juk=Image.open(PATH8+str(p)+".jpg")
                                                    jux=juk.convert('RGB')
                                                    
                                                    iiux=jux.rotate(90,fillcolor='white',expand=True)

                                                    x66=iiux.width
                                                    y66=iiux.height
                                                    iiux.save(PATH8+str(p)+".jpg")
                                                    self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                
                                                    self.canvas.create_image(self.xx1-6,self.arr2[p][1],image=self.canvas.iip,anchor="nw")
                                                    self.mylist.append(self.canvas.iip)
                                                    self.canvas.delete(self.iid)
                                                    self.arr2[p][0]=self.xx1-6
                                                    self.arr2[p][3]=self.arr2[p][1]+y66
                                                    self.arr2[p][2]=x66+self.xx1-6
                                                    self.arr2[p][4]=1

                                else:
                                    #print(1112)
                                    #print(self.xx1,self.xx2,1000000)
                                    k=self.xx1
                                    self.xx1=self.xx2
                                    self.xx2=k
                                    #print(self.yy2,self.arr2[p][3])]
                                    #print(111)
                                    zq=0
                                    if(self.up_down[p]=='U' or self.up_down[p]=='L'):

                                        for y in range(self.ro):
                                            l1=Point(self.arr2[y][0],self.arr2[y][1])
                                            d1=Point(self.arr2[y][2],self.arr2[y][3])
                                            l2=Point(self.arr2[p][0]+self.xx2-self.arr2[p][2]+6,self.arr2[p][1])
                                            d2=Point(self.xx2+6,self.arr2[p][3])


                                            if(self.doOverlap(l1, d1, l2, d2) and not((l2.x==0) and (l2.y==0)) and self.r1!=l2.x and self.r2!=l2.y and self.del_from_plan[y]==0): 
                                                #print(x)
                                                #print(p)
                                                #print(l1.x,l1.y,r1.x,r1.y,l2.x,l2.y,r2.x,r2.y)
                                                if(self.new_obj==0):
                                                    if(y!=p):
                                                        zq=0
                                                        for z in range(self.ro):
                                                            l3=Point(self.arr2[z][0],self.arr2[z][1])
                                                            d3=Point(self.arr2[z][2],self.arr2[z][3])
                                                            l4=Point(self.xx1-6,self.arr2[p][1])
                                                            d4=Point(self.arr2[p][2]+self.xx1-6-self.arr2[p][0],self.arr2[p][3])

                                                            if(self.doOverlap(l3,d3,l4,d4) and not(l4.x==0 and l4.y==0) and z!=p and self.del_from_plan[z]==0):
                                                                zq=1
                                                                messagebox.showerror("Error occured","Door may overlap with objects")
                                                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                self.arr2[p][0]=self.r1
                                                                self.arr2[p][1]=self.r2
                                                                self.arr2[p][2]=self.r3
                                                                self.arr2[p][3]=self.r4
                                                                self.arr2[p][4]=1
                                                                for z1 in range(len(cfile['bbox_loc'])):
                                                                    self.room_doors2[z1]=self.room_doors[z1]

                                                                self.canvas.delete("blucol")
                                                                break


                                                        if(zq==0):
                                                            p0=self.xx1-6
                                                            p1=self.arr2[p][1]
                                                            p2=self.xx1-6+self.arr2[p][2]-self.arr2[p][0]
                                                            p3=self.arr2[p][3]
                                                            ccc=0
                                                            for z1 in range(len(cfile['bbox_loc'])):
                                                                
                                                                cchck=0

                                                                if(1):
                                                                    for y111 in range(4):

                                                                        
                                                                        
                                                                        if(y111==0):
                                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                            d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                        if(y111==1):
                                                                            l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                        if(y111==2):
                                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                            d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                        if(y111==3):
                                                                            l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                        for y112 in range(4):
                                                                            if(y112==0):
                                                                                l6=Point(p0,p1)
                                                                                d6=Point(p0,p3)
                                                                            if(y112==1):
                                                                                l6=Point(p0,p3)
                                                                                d6=Point(p2,p3)
                                                                            if(y112==2):
                                                                                l6=Point(p2,p3)
                                                                                d6=Point(p2,p1)
                                                                            if(y112==3):
                                                                                l6=Point(p2,p1)
                                                                                d6=Point(p0,p1)
                                                      
                                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                                self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                                ccc=1
                                                                                break

                                                                        if(ccc==1):
                                                                            break


                                                            xlxl=0
                                                            for z1 in range(len(cfile['bbox_loc'])):
                                                                if(self.room_doors2[z1]==0):
                                                                    messagebox.showerror("Error Occured","Every room must have atleast one door")    

                                                                    xlxl=1
                                                                    for z2 in range(1000):
                                                                        self.room_doors2[z2]=self.room_doors[z2]
                                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                    self.arr2[p][0]=self.r1
                                                                    self.arr2[p][1]=self.r2
                                                                    self.arr2[p][2]=self.r3
                                                                    self.arr2[p][3]=self.r4
                                                                    break

                                                            if(xlxl==0):
                                                                if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                                    messagebox.showerror("Error Occured","There is no entry into the houseplan")    

                                                                    xlxl=1
                                                                    for z2 in range(1000):
                                                                        self.room_doors2[z2]=self.room_doors[z2]
                                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                    self.arr2[p][0]=self.r1
                                                                    self.arr2[p][1]=self.r2
                                                                    self.arr2[p][2]=self.r3
                                                                    self.arr2[p][3]=self.r4
                                                                    break


                                                            if(xlxl==0):
                                                                for z2 in range(1000):
                                                                    self.room_doors[z2]=self.room_doors2[z2]
                                                                juk=Image.open(PATH8+str(p)+".jpg")
                                                                jux=juk.convert('RGB')
                                                                iiux=ImageOps.mirror(jux)

                                                                if(self.main_doors_check[p]==1):
                                                                    self.main_doors_check[p]=0
                                                                    self.main_doors=self.main_doors-1

                                                                if(self.up_down[p]=='U'):
                                                                    iiux=iiux.rotate(-90,expand=True,fillcolor='white')
                                                                #if(self.up_down[p]=='L'):
                                                                iiux=iiux.rotate(-(2*self.theta),expand=True,fillcolor='white')


                                                                x66=iiux.width
                                                                y66=iiux.height
                                                                iiux.save(PATH8+str(p)+".jpg")
                                                                self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                print(2299)
                                                                self.canvas.create_image(self.xx1-6,self.arr2[p][1],image=self.canvas.iip,anchor="nw")
                                                                self.mylist.append(self.canvas.iip)
                                                                self.canvas.delete(self.iid)


                                                                xlxl=0



                                                                xe=self.arr2[p][2]-self.arr2[p][0]
                                                                self.arr2[p][0]=self.xx1-6
                                                                self.arr2[p][3]=self.arr2[p][1]+y66
                                                                self.arr2[p][2]=self.xx1-6+x66
                                                                self.arr2[p][4]=1
                                                

                                                                if(self.up_down[p]=='U'):
                                                                    self.up_down[p]='R'
                                                                else:
                                                                    if(self.up_down[p]=='L'):
                                                                        self.up_down[p]='R'

                                                                self.hor_ver[p]='V'

                                                                self.canvas.delete("blucol")
                                                                zq=1
                                                                break


                                        if(zq==0):
                                            p0=self.xx2+6-self.arr2[p][2]+self.arr2[p][0]
                                            p1=self.arr2[p][1]
                                            p2=self.xx2+6
                                            p3=self.arr2[p][3]
                                            ccc=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                
                                                cchck=0

                                                if(1):
                                                    for y111 in range(4):

                                                        
                                                        
                                                        if(y111==0):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                        if(y111==1):
                                                            l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        if(y111==2):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                        if(y111==3):
                                                            l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        for y112 in range(4):
                                                            if(y112==0):
                                                                l6=Point(p0,p1)
                                                                d6=Point(p0,p3)
                                                            if(y112==1):
                                                                l6=Point(p0,p3)
                                                                d6=Point(p2,p3)
                                                            if(y112==2):
                                                                l6=Point(p2,p3)
                                                                d6=Point(p2,p1)
                                                            if(y112==3):
                                                                l6=Point(p2,p1)
                                                                d6=Point(p0,p1)
                                      
                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                ccc=1
                                                                break

                                                        if(ccc==1):
                                                            break


                                            xlxl=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                if(1):
                                                    if(self.room_doors2[z1]==0):
                                                        messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                        xlxl=1
                                                        for z2 in range(1000):
                                                            self.room_doors2[z2]=self.room_doors[z2]
                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                        self.arr2[p][0]=self.r1
                                                        self.arr2[p][1]=self.r2
                                                        self.arr2[p][2]=self.r3
                                                        self.arr2[p][3]=self.r4
                                                        break

                                            if(xlxl==0):
                                                if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                    messagebox.showerror("Error Occured","There is no entry into the houseplan")
                                                    xlxl=1
                                                    for z2 in range(1000):
                                                        self.room_doors2[z2]=self.room_doors[z2]
                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                    self.arr2[p][0]=self.r1
                                                    self.arr2[p][1]=self.r2
                                                    self.arr2[p][2]=self.r3
                                                    self.arr2[p][3]=self.r4
                                                    

                                            if(xlxl==0):
                                                for z2 in range(1000):
                                                    self.room_doors[z2]=self.room_doors2[z2]

                                                if(self.main_doors_check[p]==1):
                                                    self.main_doors=self.main_doors-1
                                                    self.main_doors_check[p]=0

                                                if(self.up_down[p]=='U'):
                                                    juk=Image.open(PATH8+str(p)+".jpg")
                                                    #juk.show()
                                                    jux=juk.convert('RGB')
                                                    #iiux=ImageOps.flip(jux)
                                                   
                                                    iiux=jux.rotate(90,expand=True,fillcolor='white')
                                                    #iiux.show()
                                                    x66=iiux.width
                                                    y66=iiux.height
                                                    
                                                    iiux.save(PATH8+str(p)+".jpg")
                                                    self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                
                                                    self.canvas.create_image(self.xx2+6-x66,self.arr2[p][1],image=self.canvas.iip,anchor="nw")
                                                    self.mylist.append(self.canvas.iip)
                                                    self.canvas.delete(self.iid)

                                                if(self.up_down[p]=='L'):
                                                    self.canvas.move(self.iid,(self.xx2-self.arr2[p][2]+6),0)
                                                    self.arr2[p][0]=self.arr2[p][0]+self.xx2-self.arr2[p][2]+6
                                                    self.arr2[p][2]=self.xx2+6
                                                    self.arr2[p][4]=1
                                                    self.canvas.delete("blucol")
                                                else:
                                                    self.up_down[p]='L'
                                                    self.hor_ver[p]='V'
                                                    self.arr2[p][0]=self.xx2+6-x66
                                                    self.arr2[p][2]=self.xx2+6
                                                    self.arr2[p][3]=self.arr2[p][1]+y66
                                                    self.arr2[p][4]=1
                                                    self.canvas.delete("blucol")


                                    if(self.up_down[p]=='D' or self.up_down[p]=='R'):
                                        zq=0

                                        for y in range(self.ro):
                                            l1=Point(self.arr2[y][0],self.arr2[y][1])
                                            d1=Point(self.arr2[y][2],self.arr2[y][3])
                                            l2=Point(self.xx1-6,self.arr2[p][1])
                                            d2=Point(self.arr2[p][2]+self.xx1-6-self.arr2[p][0],self.arr2[p][3])


                                            if(self.doOverlap(l1, d1, l2, d2) and not((l2.x==0) and (l2.y==0)) and self.r1!=l2.x and self.r2!=l2.y and self.del_from_plan[y]==0): 
                                                #print(x)
                                                #print(p)
                                                #print(l1.x,l1.y,r1.x,r1.y,l2.x,l2.y,r2.x,r2.y)
                                                if(self.new_obj==0):
                                                    if(y!=p):
                                                        zq=0
                                                        for z in range(self.ro):
                                                            l3=Point(self.arr2[z][0],self.arr2[z][1])
                                                            d3=Point(self.arr2[z][2],self.arr2[z][3])
                                                            l4=Point(self.arr2[p][0]+self.xx2-self.arr2[p][2]+6,self.arr2[p][1])
                                                            d4=Point(self.xx2+6,self.arr2[p][3])

                                                            if(self.doOverlap(l3,d3,l4,d4) and not(l4.x==0 and l4.y==0) and z!=p and self.del_from_plan[z]==0):
                                                                zq=1
                                                                messagebox.showerror("Error occured","Door may overlap with objects")
                                                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                self.arr2[p][0]=self.r1
                                                                self.arr2[p][1]=self.r2
                                                                self.arr2[p][2]=self.r3
                                                                self.arr2[p][3]=self.r4
                                                                self.arr2[p][4]=1
                                                                for z1 in range(len(cfile['bbox_loc'])):
                                                                    self.room_doors2[z1]=self.room_doors[z1]

                                                            


                                                                self.canvas.delete("blucol")
                                                                break


                                                        if(zq==0):

                                                            p0=self.xx2+6-self.arr2[p][2]+self.arr2[p][0]
                                                            p1=self.arr2[p][1]
                                                            p2=self.xx2+6
                                                            p3=self.arr2[p][3]
                                                            ccc=0
                                                            for z1 in range(len(cfile['bbox_loc'])):
                                                                
                                                                cchck=0

                                                                if(1):
                                                                    for y111 in range(4):

                                                                        
                                                                        
                                                                        if(y111==0):
                                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                            d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                        if(y111==1):
                                                                            l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                        if(y111==2):
                                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                            d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                        if(y111==3):
                                                                            l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                        for y112 in range(4):
                                                                            if(y112==0):
                                                                                l6=Point(p0,p1)
                                                                                d6=Point(p0,p3)
                                                                            if(y112==1):
                                                                                l6=Point(p0,p3)
                                                                                d6=Point(p2,p3)
                                                                            if(y112==2):
                                                                                l6=Point(p2,p3)
                                                                                d6=Point(p2,p1)
                                                                            if(y112==3):
                                                                                l6=Point(p2,p1)
                                                                                d6=Point(p0,p1)
                                                      
                                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                                self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                                ccc=1
                                                                                break

                                                                        if(ccc==1):
                                                                            break


                                                            xlxl=0
                                                            for z1 in range(len(cfile['bbox_loc'])):
                                                                if(1):
                                                                    if(self.room_doors2[z1]==0):
                                                                        messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                                        xlxl=1
                                                                        for z2 in range(1000):
                                                                            self.room_doors2[z2]=self.room_doors[z2]
                                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                        self.arr2[p][0]=self.r1
                                                                        self.arr2[p][1]=self.r2
                                                                        self.arr2[p][2]=self.r3
                                                                        self.arr2[p][3]=self.r4
                                                                        break
                                                            if(xlxl==0):
                                                                if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                                    messagebox.showerror("Error Occured","There is no entry into the houseplan")
                                                                    xlxl=1
                                                                    for z2 in range(1000):
                                                                        self.room_doors2[z2]=self.room_doors[z2]
                                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                    self.arr2[p][0]=self.r1
                                                                    self.arr2[p][1]=self.r2
                                                                    self.arr2[p][2]=self.r3
                                                                    self.arr2[p][3]=self.r4
                                                                    break



                                                            if(xlxl==0):
                                                                for z2 in range(1000):
                                                                    self.room_doors[z2]=self.room_doors2[z2]
                                                                juk=Image.open(PATH8+str(p)+".jpg")
                                                                jux=juk.convert('RGB')
                                                                iiux=ImageOps.mirror(jux)

                                                                if(self.main_doors_check[p]==1):
                                                                    self.main_doors=self.main_doors-1
                                                                    self.main_doors_check[p]=0

                                                                if(self.up_down[p]=='D'):
                                                                    iiux=iiux.rotate(-90,fillcolor='white',expand=True)
                                                                #if(self.up_down[p]=='R'):
                                                                iiux=iiux.rotate(-(2*self.theta),expand=True,fillcolor='white')                                                                   

                                                                x66=iiux.width
                                                                y66=iiux.height
                                                                iiux.save(PATH8+str(p)+".jpg")
                                                                self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                
                                                                self.canvas.create_image(self.xx2-x66+6,self.arr2[p][1],image=self.canvas.iip,anchor="nw")
                                                                self.mylist.append(self.canvas.iip)
                                                                self.canvas.delete(self.iid)

                                                                self.arr2[p][0]=self.xx2-x66+6
                                                                self.arr2[p][3]=self.arr2[p][1]+y66
                                                                self.arr2[p][2]=self.xx2+6
                                                                self.arr2[p][4]=1

                                                                if(self.up_down[p]=='D'):
                                                                    self.up_down[p]='L'
                                                                else:
                                                                    if(self.up_down[p]=='R'):
                                                                        self.up_down[p]='L'

                                                                self.hor_ver[p]='V'
                                                                        
                                                                self.canvas.delete("blucol")
                                                                zq=1
                                                                break


                                        self.canvas.delete("blucol")
                                        if(zq==0):
                                            p0=self.xx1-6
                                            p1=self.arr2[p][1]
                                            p2=self.xx1-6+self.arr2[p][2]-self.arr2[p][0]
                                            p3=self.arr2[p][3]
                                            ccc=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                
                                                cchck=0

                                                if(1):
                                                    for y111 in range(4):

                                                        
                                                        
                                                        if(y111==0):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                        if(y111==1):
                                                            l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        if(y111==2):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                        if(y111==3):
                                                            l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        for y112 in range(4):
                                                            if(y112==0):
                                                                l6=Point(p0,p1)
                                                                d6=Point(p0,p3)
                                                            if(y112==1):
                                                                l6=Point(p0,p3)
                                                                d6=Point(p2,p3)
                                                            if(y112==2):
                                                                l6=Point(p2,p3)
                                                                d6=Point(p2,p1)
                                                            if(y112==3):
                                                                l6=Point(p2,p1)
                                                                d6=Point(p0,p1)
                                      
                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                ccc=1
                                                                break

                                                        if(ccc==1):
                                                            break



                                            xlxl=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                if(1):
                                                    if(self.room_doors2[z1]==0):
                                                        messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                        xlxl=1
                                                        for z2 in range(1000):
                                                            self.room_doors2[z2]=self.room_doors[z2]
                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                        self.arr2[p][0]=self.r1
                                                        self.arr2[p][1]=self.r2
                                                        self.arr2[p][2]=self.r3
                                                        self.arr2[p][3]=self.r4
                                                        break

                                            if(xlxl==0):
                                                if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                    messagebox.showerror("Error Occured","There is no entry into the houseplan")
                                                    xlxl=1
                                                    for z2 in range(1000):
                                                        self.room_doors2[z2]=self.room_doors[z2]
                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                    self.arr2[p][0]=self.r1
                                                    self.arr2[p][1]=self.r2
                                                    self.arr2[p][2]=self.r3
                                                    self.arr2[p][3]=self.r4
                                                    

                                            if(xlxl==0):
                                                for z2 in range(1000):
                                                    self.room_doors[z2]=self.room_doors2[z2]
                                                xe=self.arr2[p][2]-self.arr2[p][0]

                                                if(self.main_doors_check[p]==1):
                                                    self.main_doors=self.main_doors-1
                                                    self.main_doors_check[p]=0

                                                if(self.up_down[p]=='R'):
                                                    self.canvas.move(self.iid,(self.xx1-self.arr2[p][0]-6),0)
                                                    self.arr2[p][0]=self.xx1-6
                                                    self.arr2[p][2]=xe+self.xx1-6
                                                    self.arr2[p][4]=1

                                                if(self.up_down[p]=='D'):
                                                    self.up_down[p]='R'
                                                    self.hor_ver[p]='V'
                                                    juk=Image.open(PATH8+str(p)+".jpg")
                                                    jux=juk.convert('RGB')
                                                    
                                                    iiux=jux.rotate(90,fillcolor='white',expand=True)

                                                    x66=iiux.width
                                                    y66=iiux.height
                                                    iiux.save(PATH8+str(p)+".jpg")
                                                    self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                
                                                    self.canvas.create_image(self.xx1-6,self.arr2[p][1],image=self.canvas.iip,anchor="nw")
                                                    self.mylist.append(self.canvas.iip)
                                                    self.canvas.delete(self.iid)
                                                    self.arr2[p][0]=self.xx1-6
                                                    self.arr2[p][3]=self.arr2[p][1]+y66
                                                    self.arr2[p][2]=x66+self.xx1-6
                                                    self.arr2[p][4]=1
                            #print(self.first,self.sec)

                            if(self.secv==0 and self.firstv==1 and ccc==0 and not(c0==self.a1 and c1==self.a2)):
                                #print(self.yy1,self.h1)
                                #if(gap1>gap2):
                                #print(self.v1,self.xx1,self.xx2)
                                if(self.xx1==self.v1):
                                    print(2)
                                    #print(113)
                                    if(self.up_down[p]=='U' or self.up_down[p]=='L'):
                                        if(self.arr2[p][0]+self.xx1-self.arr2[p][2]+8 >= 0 and self.xx1+8 <= 1285 ):

                                            p0=self.xx1+8-self.arr2[p][2]+self.arr2[p][0]
                                            p1=self.arr2[p][1]
                                            p2=self.xx1+8
                                            p3=self.arr2[p][3]
                                            ccc=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                
                                                cchck=0

                                                if(1):
                                                    for y111 in range(4):

                                                        
                                                        
                                                        if(y111==0):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                        if(y111==1):
                                                            l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        if(y111==2):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                        if(y111==3):
                                                            l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        for y112 in range(4):
                                                            if(y112==0):
                                                                l6=Point(p0,p1)
                                                                d6=Point(p0,p3)
                                                            if(y112==1):
                                                                l6=Point(p0,p3)
                                                                d6=Point(p2,p3)
                                                            if(y112==2):
                                                                l6=Point(p2,p3)
                                                                d6=Point(p2,p1)
                                                            if(y112==3):
                                                                l6=Point(p2,p1)
                                                                d6=Point(p0,p1)
                                      
                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                ccc=1
                                                                break

                                                        if(ccc==1):
                                                            break


                                            xlxl=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                if(self.room_doors2[z1]==0):
                                                    messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                    xlxl=1
                                                    for z2 in range(1000):
                                                        self.room_doors2[z2]=self.room_doors[z2]
                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                    self.arr2[p][0]=self.r1
                                                    self.arr2[p][1]=self.r2
                                                    self.arr2[p][2]=self.r3
                                                    self.arr2[p][3]=self.r4
                                                    self.canvas.delete("blucol")
                                                    break

                                            if(xlxl==0):
                                                for z2 in range(1000):
                                                    self.room_doors[z2]=self.room_doors2[z2]

                                                if(self.main_doors_check[p]==0):
                                                    self.main_doors_check[p]=1
                                                    self.main_doors=self.main_doors+1

                                                if(self.up_down[p]=='U'):
                                                    ius=Image.open(PATH8+str(p)+".jpg")
                                                    ius=ius.convert('RGB')
                                                    ius=ius.rotate(90,expand=True,fillcolor='white')
                                                    ius.save(PATH8+str(p)+".jpg")
                                                    x66=ius.width
                                                    y66=ius.height
                                                    self.canvas.iik=ImageTk.PhotoImage(ius)
                                                    self.canvas.create_image(self.xx1+8-x66,self.arr2[p][1],image=self.canvas.iik,anchor="nw")
                                                    print(33338)
                                                    self.canvas.delete(self.iid)
                                                    self.mylist.append(self.canvas.iik)


                                                    self.up_down[p]='L'
                                                    self.hor_ver[p]='V'


                                                    #self.canvas.move(self.iid,0,self.yy1-self.arr2[p][3]+8)
                                                    self.arr2[p][0]=self.xx1-x66+8
                                                    self.arr2[p][3]=self.arr2[p][1]+y66
                                                    self.arr2[p][2]=self.xx1+8
                                                    self.canvas.delete("blucol")

                                                else:
                                                    self.canvas.move(self.iid,self.xx1-self.arr2[p][2]+8,0)
                                                    self.arr2[p][2]=self.xx1+8-x66
                                                       
                                                    self.arr2[p][0]=self.xx1+8
                                                    self.arr2[p][4]=1
                                                    self.canvas.delete("blucol")
                                        else:
                                            zzp=0
                                            for y in range(self.ro):
                                                l1=Point(self.arr2[y][0],self.arr2[y][1])
                                                d1=Point(self.arr2[y][2],self.arr2[y][3])
                                                l2=Point(self.xx1-22,self.arr2[p][1])
                                                d2=Point(self.xx1+22+self.arr2[p][2]-self.arr2[p][0],self.arr2[p][3])

                                                if(self.doOverlap(l1,d1,l2,d2) and not(l1.x==0 and l1.y==0) and y!=p and self.del_from_plan[y]==0):
                                                    zzp=1
                                                    break

                                            if(zzp==0):

                                                p0=self.xx1-22
                                                p1=self.arr2[p][1]
                                                p2=self.xx1-22+self.arr2[p][2]-self.arr2[p][0]
                                                p3=self.arr2[p][3]
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break



                                                xlxl=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    if(1):
                                                        if(self.room_doors2[z1]==0):
                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            self.canvas.delete("blucol")
                                                            break

                                                if(xlxl==0):
                                                    for z2 in range(1000):
                                                        self.room_doors[z2]=self.room_doors2[z2]

                                                    if(self.main_doors_check[p]==0):
                                                        self.main_doors_check[p]=1
                                                        self.main_doors=self.main_doors+1

                                                    juk=Image.open(PATH8+str(p)+".jpg")
                                                    jux=juk.convert('RGB')
                                                    jux=ImageOps.mirror(jux)
                                                    if(self.up_down[p]=='U'):
                                                        jux=jux.rotate(-90,expand=True,fillcolor='white')
                                                    #if(self.up_down[p]=='L'):
                                                    jux=jux.rotate(-(2*self.theta),expand=True,fillcolor='white')

                                                    x66=jux.width
                                                    y66=jux.height
                                                    jux.save(PATH8+str(p)+".jpg")

                                                    self.canvas.iik=ImageTk.PhotoImage(jux)
                                                    self.canvas.create_image(self.xx1-22,self.arr2[p][1],image=self.canvas.iik,anchor="nw")
                                                    self.canvas.delete(self.iid)
                                                    self.mylist.append(self.canvas.iik)

                                                    if(self.up_down[p]=='U'):
                                                        self.hor_ver[p]='V'

                                                    self.up_down[p]='R'

                                                    self.arr2[p][0]=self.xx1-22
                                                    self.arr2[p][3]=self.arr2[p][1]+y66
                                                    self.arr2[p][2]=self.xx1-22+x66
                                                    self.canvas.delete("blucol")


                                            if(zzp==1):

                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    self.room_doors2[z1]=self.room_doors[z1]

                                                xlxl=0
                                           

                                                messagebox.showerror("Error occured","Door cannot cross the dimension of the floorplan")
                                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                self.arr2[p][0]=self.r1
                                                self.arr2[p][1]=self.r2
                                                self.arr2[p][2]=self.r3
                                                self.arr2[p][3]=self.r4
                                                self.canvas.delete("blucol")


                                    if(self.up_down[p]=='D' or self.up_down[p]=='R'):
                                        if(self.v1-10 >= 0 and self.arr2[p][2]+self.v1-10-self.arr2[p][0] <= 1285):

                                            p0=self.v1-15
                                            p1=self.arr2[p][1]
                                            p2=self.v1-15+self.arr2[p][2]-self.arr2[p][0]
                                            p3=self.arr2[p][3]
                                            ccc=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                
                                                cchck=0

                                                if(1):
                                                    for y111 in range(4):

                                                        
                                                        
                                                        if(y111==0):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                        if(y111==1):
                                                            l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        if(y111==2):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                        if(y111==3):
                                                            l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        for y112 in range(4):
                                                            if(y112==0):
                                                                l6=Point(p0,p1)
                                                                d6=Point(p0,p3)
                                                            if(y112==1):
                                                                l6=Point(p0,p3)
                                                                d6=Point(p2,p3)
                                                            if(y112==2):
                                                                l6=Point(p2,p3)
                                                                d6=Point(p2,p1)
                                                            if(y112==3):
                                                                l6=Point(p2,p1)
                                                                d6=Point(p0,p1)
                                      
                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                ccc=1
                                                                break

                                                        if(ccc==1):
                                                            break


                                            xlxl=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                if(1):
                                                    if(self.room_doors2[z1]==0):
                                                        messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                        xlxl=1
                                                        for z2 in range(1000):
                                                            self.room_doors2[z2]=self.room_doors[z2]
                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                        self.arr2[p][0]=self.r1
                                                        self.arr2[p][1]=self.r2
                                                        self.arr2[p][2]=self.r3
                                                        self.arr2[p][3]=self.r4
                                                        self.canvas.delete("blucol")
                                                        break

                                            if(xlxl==0):
                                                for z2 in range(1000):
                                                    self.room_doors[z2]=self.room_doors2[z2]

                                                cccs=0
                                                for z1 in range(self.ro):
                                                    l5=Point(self.arr2[z1][0],self.arr2[z1][1])
                                                    d5=Point(self.arr2[z1][2],self.arr2[z1][3])
                                                    l6=Point(self.v1-20,self.arr2[p][1])
                                                    d6=Point(self.v1-20+self.arr2[p][2]-self.arr2[p][0],self.arr2[p][3])

                                                    if(self.doOverlap(l5,d5,l6,d6) and z1!=p and not(l6.x==0 and d6.x==0) and self.v1-self.arr2[p][2]+self.arr2[p][0]-5 < 0 and self.del_from_plan[z1]==0):
                                                        messagebox.showerror("Error Occured","Door overlaps with the object")
                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                        self.arr2[p][0]=self.r1
                                                        self.arr2[p][1]=self.r2
                                                        self.arr2[p][2]=self.r3
                                                        self.arr2[p][3]=self.r4
                                                        self.canvas.delete("blucol")
                                                        cccs=1
                                                        break
                                                
                                                    if(self.doOverlap(l5,d5,l6,d6) and self.v1-self.arr2[p][2]+self.arr2[p][0]-5 >= 0 and z1!=p and self.del_from_plan[z1]==0):
                                                        juk=Image.open(PATH8+str(p)+".jpg")
                                                        jux=juk.convert('RGB')
                                                        jux=ImageOps.mirror(jux)

                                                        if(self.up_down[p]=='D'):
                                                            jux=jux.rotate(-90,expand=True,fillcolor='white')
                                                        #if(self.up_down[p]=='R'):
                                                        jux=jux.rotate(-(2*self.theta),expand=True,fillcolor='white')


                                                        x66=jux.width
                                                        y66=jux.height

                                                        jux.save(PATH8+str(p)+".jpg")

                                                        if(self.main_doors_check[p]==0):
                                                            self.main_doors_check[p]=1
                                                            self.main_doors=self.main_doors+1
                                                        self.canvas.iik=ImageTk.PhotoImage(jux)
                                                        self.canvas.create_image(self.v1-self.arr2[p][2]+self.arr2[p][0]+15,self.arr2[p][1],image=self.canvas.iik,anchor="nw")
                                                        self.canvas.delete(self.iid)
                                                        self.mylist.append(self.canvas.iik)
                                                        self.up_down[p]='L'
                                                        self.hor_ver[p]='V'
                                                        cccs=1
                                                        
                                                        xe=self.arr2[p][2]-self.arr2[p][0]
                                                        self.arr2[p][0]=self.v1-xe+15
                                                        self.arr2[p][2]=self.v1+15+x66-xe
                                                        self.arr2[p][4]=1
                                                        self.canvas.delete("blucol")
                                                        break


                                                if(cccs==0):

                                                    if(self.main_doors_check[p]==0):
                                                        self.main_doors_check[p]=1
                                                        self.main_doors=self.main_doors+1
                                                    if(self.up_down[p]=='D'):
                                                        juk=Image.open(PATH8+str(p)+".jpg")
                                                        jux=juk.convert('RGB')
                                                        jux=jux.rotate(90,expand=True,fillcolor='white')
                                                        jux.save(PATH8+str(p)+".jpg")

                                                        x66=jux.width
                                                        y66=jux.height
                                                        self.canvas.iik=ImageTk.PhotoImage(jux)
                                                        self.canvas.create_image(self.v1-20+self.arr2[p][0],self.arr2[p][1],image=self.canvas.iik,anchor="nw")
                                                        self.canvas.delete(self.iid)
                                                        self.mylist.append(self.canvas.iik)
                                                        self.up_down[p]='R'
                                                        self.hor_ver[p]='V'
                                                        self.arr2[p][0]=self.v1-15
                                                        self.arr2[p][3]=self.arr2[p][1]+y66
                                                        self.arr2[p][2]=self.arr2[p][0]+x66
                                                        self.canvas.delete("blucol")

                                                    else:
                                                        self.canvas.move(self.iid,self.v1-20-self.arr2[p][0],0)
                                                        xe=self.arr2[p][2]-self.arr2[p][0]
                                                        self.arr2[p][0]=self.v1-15
                                                           
                                                        self.arr2[p][2]=self.v1-15+xe
                                                        self.arr2[p][4]=1
                                                        self.canvas.delete("blucol")
                                        else:
                                            zzp=0
                                            for y in range(self.ro):
                                                l1=Point(self.arr2[y][0],self.arr2[y][1])
                                                d1=Point(self.arr2[y][2],self.arr2[y][3])
                                                l2=Point(self.xx1+15-self.arr2[p][2]+self.arr2[p][0],self.arr2[p][1])
                                                d2=Point(self.xx1+15,self.arr2[p][3])

                                                if(self.doOverlap(l1,d1,l2,d2) and not(l1.x==0 and l1.y==0) and y!=p and self.del_from_plan[y]==0):
                                                    zzp=1
                                                    break

                                            if(zzp==0):

                                                p0=self.xx1+22-self.arr2[p][2]+self.arr2[p][0]
                                                p1=self.arr2[p][1]
                                                p2=self.xx1+22
                                                p3=self.arr2[p][3]
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break



                                                xlxl=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    if(1):
                                                        if(self.room_doors2[z1]==0):
                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            self.canvas.delete("blucol")
                                                            break

                                                if(xlxl==0):
                                                    for z2 in range(1000):
                                                        self.room_doors[z2]=self.room_doors2[z2]

                                                    if(self.main_doors_check[p]==0):
                                                        self.main_doors_check[p]=1
                                                        self.main_doors=self.main_doors+1

                                                    juk=Image.open(PATH8+str(p)+".jpg")
                                                    jux=juk.convert('RGB')
                                                    jux=ImageOps.mirror(jux)
                                                    if(self.up_down[p]=='D'):
                                                        jux=jux.rotate(-90,expand=True,fillcolor='white')
                                                    #if(self.up_down[p]=='R'):
                                                    jux=jux.rotate(-(2*self.theta),expand=True,fillcolor='white')

                                                    x66=jux.width
                                                    y66=jux.height
                                                    jux.save(PATH8+str(p)+".jpg")

                                                    self.canvas.iik=ImageTk.PhotoImage(jux)
                                                    self.canvas.create_image(self.xx1+22-x66,self.arr2[p][1],image=self.canvas.iik,anchor="nw")
                                                    self.canvas.delete(self.iid)
                                                    self.mylist.append(self.canvas.iik)

                                                    self.up_down[p]='R'
                                                    self.hor_ver[p]='V'

                                                    self.arr2[p][0]=self.xx1+22-x66
                                                    self.arr2[p][3]=self.arr2[p][1]+y66
                                                    self.arr2[p][2]=self.xx1+22
                                                    self.canvas.delete("blucol")


                                            if(zzp==1):

                                                p0=self.a1
                                                p1=self.a2
                                                p2=self.a3
                                                p3=self.a4
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break

                                            
                            
                                                        
                                                messagebox.showerror("Error occured","Door cannot cross the dimension of the floorplan")
                                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                self.arr2[p][0]=self.r1
                                                self.arr2[p][1]=self.r2
                                                self.arr2[p][2]=self.r3
                                                self.arr2[p][3]=self.r4
                                                self.canvas.delete("blucol")


                                if(self.xx1==self.v2):
                                    print(3)
                                    #print(114)
                                    if(self.up_down[p]=='U' or self.up_down[p]=='L'):

                                        if(self.arr2[p][0]+self.xx1-self.arr2[p][2]+20 >=0 and self.xx1+20 <= 1285):

                                            p0=self.xx1+20-self.arr2[p][2]+self.arr2[p][0]
                                            p1=self.arr2[p][1]
                                            p2=self.xx1+20
                                            p3=self.arr2[p][3]
                                            ccc=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                
                                                cchck=0

                                                if(1):
                                                    for y111 in range(4):

                                                        
                                                        
                                                        if(y111==0):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                        if(y111==1):
                                                            l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        if(y111==2):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                        if(y111==3):
                                                            l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        for y112 in range(4):
                                                            if(y112==0):
                                                                l6=Point(p0,p1)
                                                                d6=Point(p0,p3)
                                                            if(y112==1):
                                                                l6=Point(p0,p3)
                                                                d6=Point(p2,p3)
                                                            if(y112==2):
                                                                l6=Point(p2,p3)
                                                                d6=Point(p2,p1)
                                                            if(y112==3):
                                                                l6=Point(p2,p1)
                                                                d6=Point(p0,p1)
                                      
                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                ccc=1
                                                                break

                                                        if(ccc==1):
                                                            break


                                            xlxl=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                if(1):
                                                    if(self.room_doors2[z1]==0):
                                                        messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                        xlxl=1
                                                        for z2 in range(1000):
                                                            self.room_doors2[z2]=self.room_doors[z2]
                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                        self.arr2[p][0]=self.r1
                                                        self.arr2[p][1]=self.r2
                                                        self.arr2[p][2]=self.r3
                                                        self.arr2[p][3]=self.r4
                                                        self.canvas.delete("blucol")
                                                        break

                                            if(xlxl==0):
                                                for z2 in range(1000):
                                                    self.room_doors[z2]=self.room_doors2[z2]

                                                asa=0
                                                for z2 in range(self.ro):
                                                    l5=Point(self.arr2[z2][0],self.arr2[z2][1])
                                                    d5=Point(self.arr2[z2][2],self.arr2[z2][3])
                                                    l6=Point(self.xx1+20-self.arr2[p][2]+self.arr2[p][0],self.arr2[p][1])
                                                    d6=Point(self.xx1+20,self.arr2[p][3])

                                                    if(self.doOverlap(l5,d5,l6,d6) and not(l6.x==0 and l6.y==0) and z2!=p and self.xx1+self.arr2[p][2]-self.arr2[p][0]-5>1285 and self.del_from_plan[z2]==0):
                                                        messagebox.showerror("Error occured","Door overlaps with the object")
                                                        asa=1
                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                        self.arr2[p][0]=self.r1
                                                        self.arr2[p][1]=self.r2
                                                        self.arr2[p][2]=self.r3
                                                        self.arr2[p][3]=self.r4
                                                        self.canvas.delete("blucol")
                                                        asa=1
                                                        break

                                                    if(self.doOverlap(l5,d5,l6,d6) and self.xx1+self.arr2[p][2]-self.arr2[p][0]-5 <= 1285  and z2!=p and self.del_from_plan[z2]==0):
                                                        juk=Image.open(PATH8+str(p)+".jpg")
                                                        jux=juk.convert('RGB')

                                                        jux=ImageOps.mirror(jux)
                                                        if(self.up_down[p]=='U'):
                                                            jux=jux.rotate(-90,expand=True,fillcolor='white')
                                                        #if(self.up_down[p]=='L'):
                                                        jux=jux.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                        print(44400)


                                                        if(self.main_doors_check[p]==0):
                                                            self.main_doors_check[p]=1
                                                            self.main_doors=self.main_doors+1
                                                        x66=jux.width
                                                        y66=jux.height
                                                        jux.save(PATH8+str(p)+".jpg")

                                                        self.canvas.iik=ImageTk.PhotoImage(jux)
                                                        self.canvas.create_image(self.xx1-6,self.arr2[p][1],image=self.canvas.iik,anchor="nw")
                                                        self.canvas.delete(self.iid)
                                                        self.mylist.append(self.canvas.iik)
                                                        self.up_down[p]='R'
                                                        self.hor_ver[p]='V'
                                                        asa=1
                                                        
                                                        xe=self.arr2[p][2]-self.arr2[p][0]
                                                        self.arr2[p][0]=self.v1-x66-5
                                                        self.arr2[p][3]=self.arr2[p][1]+y66
                                                        self.arr2[p][2]=self.v1-5
                                                        self.arr2[p][4]=1
                                                        self.canvas.delete("blucol")
                                                        break




                                                if(asa==0):

                                                    if(self.main_doors_check[p]==0):
                                                        self.main_doors_check[p]=1
                                                        self.main_doors=self.main_doors+1
                                                    if(self.up_down[p]=='U'):

                                                        juk=Image.open(PATH8+str(p)+".jpg")
                                                        jux=juk.convert('RGB')

                                                    
                                                        jux=jux.rotate(90,expand=True,fillcolor='white')

                                                        x66=jux.width
                                                        y66=jux.height
                                                        jux.save(PATH8+str(p)+".jpg")

                                                        self.canvas.iik=ImageTk.PhotoImage(jux)
                                                        self.canvas.create_image(self.xx1+20-x66,self.arr2[p][1],image=self.canvas.iik,anchor="nw")
                                                        self.canvas.delete(self.iid)
                                                        self.mylist.append(self.canvas.iik)
                                                        self.up_down[p]='L'
                                                        self.hor_ver[p]='V'
                                                        asa=1
                                                        
                                                        xe=self.arr2[p][2]-self.arr2[p][0]
                                                        self.arr2[p][0]=self.xx1-x66+20
                                                        self.arr2[p][3]=self.arr2[p][1]+y66
                                                        self.arr2[p][2]=self.xx1+20
                                                        self.arr2[p][4]=1
                                                        self.canvas.delete("blucol")

                                                    else:

                                                        self.canvas.move(self.iid,self.xx1-self.arr2[p][2]+20,0)
                                                        self.arr2[p][0]=self.arr2[p][0]+self.xx1-self.arr2[p][2]+20
                                                       
                                                        self.arr2[p][2]=self.xx1+20
                                                        self.arr2[p][4]=1 
                                                        self.canvas.delete("blucol")
                                        else:
                                            p0=self.xx2+6-self.arr2[p][2]+self.arr2[p][0]
                                            p1=self.arr2[p][1]
                                            p2=self.xx2+6
                                            p3=self.arr2[p][3]
                                            ccc=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                
                                                cchck=0

                                                if(1):
                                                    for y111 in range(4):

                                                        
                                                        
                                                        if(y111==0):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                        if(y111==1):
                                                            l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        if(y111==2):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                        if(y111==3):
                                                            l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        for y112 in range(4):
                                                            if(y112==0):
                                                                l6=Point(p0,p1)
                                                                d6=Point(p0,p3)
                                                            if(y112==1):
                                                                l6=Point(p0,p3)
                                                                d6=Point(p2,p3)
                                                            if(y112==2):
                                                                l6=Point(p2,p3)
                                                                d6=Point(p2,p1)
                                                            if(y112==3):
                                                                l6=Point(p2,p1)
                                                                d6=Point(p0,p1)
                                      
                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                ccc=1
                                                                break

                                                        if(ccc==1):
                                                            break


                                            xlxl=0
                                   

                                            messagebox.showerror("Error occured","Door cannot cross the dimension of the floorplan")
                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                            self.arr2[p][0]=self.r1
                                            self.arr2[p][1]=self.r2
                                            self.arr2[p][2]=self.r3
                                            self.arr2[p][3]=self.r4
                                            self.canvas.delete("blucol")


                                    if(self.up_down[p]=='D' or self.up_down[p]=='R'):  
                                        if(self.v2-7 >=0 and self.xx1+self.arr2[p][2]-self.arr2[p][0] <= 1285):

                                            p0=self.v2-7
                                            p1=self.arr2[p][1]
                                            p2=self.v2-7+self.arr2[p][2]-self.arr2[p][0]
                                            p3=self.arr2[p][3]
                                            ccc=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                
                                                cchck=0

                                                if(1):
                                                    for y111 in range(4):

                                                        
                                                        
                                                        if(y111==0):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                        if(y111==1):
                                                            l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        if(y111==2):
                                                            l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                            d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                        if(y111==3):
                                                            l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                        for y112 in range(4):
                                                            if(y112==0):
                                                                l6=Point(p0,p1)
                                                                d6=Point(p0,p3)
                                                            if(y112==1):
                                                                l6=Point(p0,p3)
                                                                d6=Point(p2,p3)
                                                            if(y112==2):
                                                                l6=Point(p2,p3)
                                                                d6=Point(p2,p1)
                                                            if(y112==3):
                                                                l6=Point(p2,p1)
                                                                d6=Point(p0,p1)
                                      
                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                ccc=1
                                                                break

                                                        if(ccc==1):
                                                            break



                                            xlxl=0
                                            for z1 in range(len(cfile['bbox_loc'])):
                                                if(1):
                                                    if(self.room_doors2[z1]==0):
                                                        messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                        xlxl=1
                                                        for z2 in range(1000):
                                                            self.room_doors2[z2]=self.room_doors[z2]
                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                        self.arr2[p][0]=self.r1
                                                        self.arr2[p][1]=self.r2
                                                        self.arr2[p][2]=self.r3
                                                        self.arr2[p][3]=self.r4
                                                        self.canvas.delete("blucol")
                                                        break

                                            if(xlxl==0):
                                                for z2 in range(1000):
                                                    self.room_doors[z2]=self.room_doors2[z2]

                                                asa=0
                                                for z2 in range(self.ro):
                                                    l5=Point(self.arr2[z2][0],self.arr2[z2][1])
                                                    d5=Point(self.arr2[z2][2],self.arr2[z2][3])
                                                    l6=Point(self.xx1-6,self.arr2[p][1])
                                                    d6=Point(self.xx1-6+self.arr2[p][2]-self.arr2[p][0],self.arr2[p][3])

                                                    if(self.doOverlap(l5,d5,l6,d6) and not(l6.x==0 and l6.y==0) and z2!=p and self.xx1+1-self.arr2[p][2]+self.arr2[p][0]<0 and self.del_from_plan[z2]==0):
                                                        messagebox.showerror("Error occured","Door overlaps with the object")
                                                        asa=1
                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                        self.arr2[p][0]=self.r1
                                                        self.arr2[p][1]=self.r2
                                                        self.arr2[p][2]=self.r3
                                                        self.arr2[p][3]=self.r4
                                                        self.canvas.delete("blucol")
                                                        asa=1
                                                        break

                                                    if(self.doOverlap(l5,d5,l6,d6) and self.xx1+15-self.arr2[p][2]+self.arr2[p][0] >= 0 and z2!=p and self.del_from_plan[z2]==0):
                                                        juk=Image.open(PATH8+str(p)+".jpg")
                                                        jux=juk.convert('RGB')
                                                        jux=ImageOps.mirror(jux)
                                                        if(self.up_down[p]=='D'):
                                                            jux=jux.rotate(-90,expand=True,fillcolor='white')
                                                        #if(self.up_down[p]=='R'):
                                                        jux=jux.rotate(-(2*self.theta),expand=True,fillcolor='white')

                                                        x66=jux.width
                                                        y66=jux.height
                                                        jux.save(PATH8+str(p)+".jpg")

                                                        if(self.main_doors_check[p]==0):
                                                            self.main_doors_check[p]=1
                                                            self.main_doors=self.main_doors+1
                                                        self.canvas.iik=ImageTk.PhotoImage(jux)
                                                        self.canvas.create_image(self.v2+20-x66,self.arr2[p][1],image=self.canvas.iik,anchor="nw")
                                                        self.canvas.delete(self.iid)
                                                        self.mylist.append(self.canvas.iik)
                                                        self.up_down[p]='L'
                                                        self.hor_ver[p]='V'
                                                        asa=1
                                                        
                                                        xe=self.arr2[p][2]-self.arr2[p][0]
                                                        self.arr2[p][0]=self.v2+20-x66
                                                        self.arr2[p][3]=self.arr2[p][1]+y66
                                                        self.arr2[p][2]=self.v2+20
                                                        self.arr2[p][4]=1
                                                        self.canvas.delete("blucol")
                                                        break

                                                if(asa==0):

                                                    if(self.main_doors_check[p]==0):
                                                        self.main_doors_check[p]=1
                                                        self.main_doors=self.main_doors+1
                                                    if(self.up_down[p]=='D'):
                                                        juk=Image.open(PATH8+str(p)+".jpg")
                                                        jux=juk.convert('RGB')
                                                        #jux=ImageOps.mirror(jux)
                                                        
                                                        jux=jux.rotate(90,expand=True,fillcolor='white')

                                                        x66=jux.width
                                                        y66=jux.height
                                                        jux.save(PATH8+str(p)+".jpg")

                                                        self.canvas.iik=ImageTk.PhotoImage(jux)
                                                        self.canvas.create_image(self.v2-7,self.arr2[p][1],image=self.canvas.iik,anchor="nw")
                                                        self.canvas.delete(self.iid)
                                                        self.mylist.append(self.canvas.iik)
                                                        self.up_down[p]='R'
                                                        self.hor_ver[p]='V'
                                                        
                                                        
                                                        xe=self.arr2[p][2]-self.arr2[p][0]
                                                        self.arr2[p][0]=self.v2-7
                                                        self.arr2[p][3]=self.arr2[p][1]+y66
                                                        self.arr2[p][2]=self.v2-7+x66
                                                        self.arr2[p][4]=1
                                                        self.canvas.delete("blucol")

                                                    else:
                                                        self.canvas.move(self.iid,self.v2-self.arr2[p][0]-7,0)
                                                        xe=self.arr2[p][2]-self.arr2[p][0]
                                                        self.arr2[p][0]=self.v2-7
                                                           
                                                        self.arr2[p][2]=xe+self.v2--7
                                                        self.arr2[p][4]=1 
                                                        self.canvas.delete("blucol")   
                                        else:
                                            zzp=0
                                            juk=Image.open(PATH8+str(p)+".jpg")
                                            jux=juk.convert('RGB')
                                            for y in range(self.ro):
                                                l1=Point(self.arr2[y][0],self.arr2[y][1])
                                                d1=Point(self.arr2[y][2],self.arr2[y][3])
                                                l2=Point(self.xx1+15-jux.width,self.arr2[p][1])
                                                d2=Point(self.xx1+15,self.arr2[p][3])

                                                if(self.doOverlap(l1,d1,l2,d2) and not(l1.x==0 and l1.y==0) and y!=p and self.del_from_plan[y]==0):
                                                    zzp=1
                                                    self.canvas.delete("blucol")
                                                    break

                                            if(zzp==0):

                                                p0=self.xx1+20-self.arr2[p][2]+self.arr2[p][0]
                                                p1=self.arr2[p][1]
                                                p2=self.xx1+20
                                                p3=self.arr2[p][3]
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break



                                                xlxl=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    if(1):
                                                        if(self.room_doors2[z1]==0):
                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            self.canvas.delete("blucol")
                                                            break


                                                if(xlxl==0):
                                                    for z2 in range(1000):
                                                        self.room_doors[z2]=self.room_doors2[z2]
                                                    juk=Image.open(PATH8+str(p)+".jpg")
                                                    jux=juk.convert('RGB')
                                                    jux=ImageOps.mirror(jux)
                                                    if(self.up_down[p]=='D'):
                                                        jux=jux.rotate(-90,expand=True,fillcolor='white')
                                                    #if(self.up_down[p]=='R'):
                                                    jux=jux.rotate(-(2*self.theta),expand=True,fillcolor='white')

                                                    x66=jux.width
                                                    y66=jux.height
                                                    jux.save(PATH8+str(p)+".jpg")

                                                    if(self.main_doors_check[p]==0):
                                                        self.main_doors_check[p]=1
                                                        self.main_doors=self.main_doors+1
                                                    self.canvas.iik=ImageTk.PhotoImage(jux)
                                                    self.canvas.create_image(self.xx1+20-x66,self.arr2[p][1],image=self.canvas.iik,anchor="nw")
                                                    self.canvas.delete(self.iid)
                                                    self.mylist.append(self.canvas.iik)
                                                    self.arr2[p][0]=self.xx1+20-x66
                                                    self.arr2[p][3]=self.arr2[p][1]+y66
                                                    self.arr2[p][2]=self.xx1+20
                                                    self.canvas.delete("blucol")

                                                    self.up_down[p]='L'
                                                    self.hor_ver[p]='V'


                                            if(zzp==1):

                                                p0=self.a1
                                                p1=self.a2
                                                p2=self.a3
                                                p3=self.a4
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break

                                                xlxl=0
                                        

                                                messagebox.showerror("Error occured","Door cannot cross the dimension of the floorplan")
                                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                self.arr2[p][0]=self.r1
                                                self.arr2[p][1]=self.r2
                                                self.arr2[p][2]=self.r3
                                                self.arr2[p][3]=self.r4
                                                self.canvas.delete("blucol")











                        else:
                            if(self.firstv==0 and self.first==1 ):


                                if(self.sec==0 and self.first==1):
                                    #print(1)
                                    self.first=0
                                    self.sec=0
                                    self.yy1=0
                                    self.yy2=0
                                    #self.yy3=0








                                    if(1):

                                        for y in range(len(cfile['bbox_loc'])):
                                            chck=0
                                            ui2=0

                                            if(1):
                                                for y111 in range(4):

                                                                                                
                                                    if(y111==0):
                                                        l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                                        d1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                                    if(y111==1):
                                                        l1=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                                        d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                                                    if(y111==2):
                                                        l1=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                                        d1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                                    if(y111==3):
                                                        l1=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                                        d1=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                                                    for y112 in range(4):
                                                        if(y112==0):
                                                            if(gap1>gap2):
                                                                l2=Point(c0,c1+20)
                                                                d2=Point(c0,c3+20)
                                                            else:
                                                                l2=Point(c0,c1-20)
                                                                d2=Point(c0,c3-20)
                                                        if(y112==1):
                                                            if(gap1>gap2):
                                                                l2=Point(c0,c3+20)
                                                                d2=Point(c2,c3+20)
                                                            else:
                                                                l2=Point(c0,c3-20)
                                                                d2=Point(c2,c3-20)
                                                        if(y112==2):
                                                            if(gap1>gap2):
                                                                l2=Point(c2,c3+20)
                                                                d2=Point(c2,c1+20)
                                                            else:
                                                                l2=Point(c2,c3-20)
                                                                d2=Point(c2,c1-20)
                                                        if(y112==3):
                                                            if(gap1>gap2):
                                                                l2=Point(c2,c1+20)
                                                                d2=Point(c0,c1+20)
                                                            else:
                                                                l2=Point(c2,c1-20)
                                                                d2=Point(c0,c1-20)
                                  
                                                        if((self.doIntersect(l1,d1,l2,d2)) and (l2.x!=0) and (l2.y!=0) ):
                                                            ui2=1

                                                            if( (self.first==1 and self.sec==1)):
                                                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                self.arr2[p][0]=self.r1
                                                                self.arr2[p][1]=self.r2
                                                                self.arr2[p][2]=self.r3
                                                                self.arr2[p][3]=self.r4
                                                                self.arr2[p][4]=1
                                                                for z in range(len(cfile['bbox_loc'])):
                                                                    self.room_doors2[z]=self.room_doors[z]

                                                                messagebox.showerror("Error occured","Door cannot be connected at the corners")
                                                                print(self.first,self.firstv,self.sec,self.secv)
                                                                ccc=1
                                                                break
                                                            if(self.first==1):
                                                                self.sec=1
                                                            else:
                                                                if(self.first==0):
                                                                    self.first=1


                                                            chck2=0
                                                            zz=0
                                                            #print(111)
                                                            for z in range(4):
                                                                l3=(0,0)
                                                                d3=(0,0)
                                                                if(z==0):
                                                                    l3=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                                                    d3=Point(self.roomcoord3[y][2],self.roomcoord3[y][3]) 
                                                                if(z==1):
                                                                    l3=Point(self.roomcoord3[y][2],self.roomcoord3[y][3])
                                                                    d3=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                                                if(z==2):
                                                                    l3=Point(self.roomcoord3[y][4],self.roomcoord3[y][5])
                                                                    d3=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                                                if(z==3):
                                                                    l3=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                                                    d3=Point(self.roomcoord3[y][4],self.roomcoord3[y][5]) 

                                                                l4=Point(0,0)
                                                                d4=Point(0,0)
                                            
                                                                if(gap1>gap2):
                                                                    l4=Point(c0,c1+20)
                                                                    d4=Point(c2,c3+20)
                                                                else:
                                                                    l4=Point(c0,c1-20)
                                                                    d4=Point(c2,c3-20)
                                                                
                                                                #print(l4.x,l3.x,d4.x,d3.x)
                                                                if(l4.x<=l3.x and l3.x<=d4.x and (z==0 or z==2)):
                                                                    #print(1)
                                                                    chck2=chck2+1
                                                                    if(self.xx1!=0):
                                                                        self.xx2=l3.x
                                                                    else:
                                                                        self.xx1=l3.x
                                                                    

                                                                    #print(chck2)
                                                                    if(chck2==2):
                                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                        messagebox.showerror("Error occured","Door cannot be connected at the corners")
                                                                        print(self.first,self.firstv,self.sec,self.secv)
                                                                        
                                                                        self.arr2[p][0]=self.r1
                                                                        self.arr2[p][1]=self.r2
                                                                        self.arr2[p][2]=self.r3
                                                                        self.arr2[p][3]=self.r4
                                                                        self.arr2[p][4]=1
                                                                        for z1 in range(len(cfile['bbox_loc'])):
                                                                            self.room_doors2[z1]=self.room_doors[z1]

                                                                        ccc=1
                                                                        break


                                                                        

                                                                if(l4.y<=l3.y and l3.y<=d4.y and (z==1 or z==3)):
                                                                    #print(11)
                                                                    chck2=chck2+1
                                                                    #print(z,100)
                                                                    if(self.yy1!=0):
                                                                        self.yy2=l3.y
                                                                    else:
                                                                        self.yy1=l3.y
                                                                    #gap1=abs(l4.y-l3.y)
                                                                    #gap2=abs(l3.y-d4.y)
                                                                    #print(chck2)
                                                                    if(chck2==2):
                                                                        messagebox.showerror("Error occured","Door cannot be connected at the corners")
                                                                        print(self.first,self.firstv,self.sec,self.secv)
                                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                        self.arr2[p][0]=self.r1
                                                                        self.arr2[p][1]=self.r2
                                                                        self.arr2[p][2]=self.r3
                                                                        self.arr2[p][3]=self.r4
                                                                        self.arr2[p][4]=1
                                                                        for z1 in range(len(cfile['bbox_loc'])):
                                                                            self.room_doors2[z1]=self.room_doors[z1]
                                                                        ccc=1
                                                                        break
                                                            break

                                                        if(ui2==1):
                                                            break

                                                    if(ui2==1):
                                                        break

                                            if(ccc==1):
                                                break


                                #print(self.first,self.sec,self.yy1)
                                #print(self.first,self.yy3)
                                if(self.first==0 and self.yy3!=0):
                                    self.first=1
                                    self.yy1=self.yy3
                                    self.h3=self.yy3



                                if(self.sec==1 and ccc==0 and not(c0==self.a1 and c1==self.a2)):
                                    #print(1)
                                    if(self.yy2>self.yy1):
                                        #print(self.yy2,self.arr2[p][3])]
                                        #print(111)
                                        zq=0
                                        if(self.up_down[p]=='U' or self.up_down[p]=='L'):

                                            for y in range(self.ro):
                                                l1=Point(self.arr2[y][0],self.arr2[y][1])
                                                d1=Point(self.arr2[y][2],self.arr2[y][3])
                                                l2=Point(self.arr2[p][0],self.arr2[p][1]+self.yy2-self.arr2[p][3]+6)
                                                d2=Point(self.arr2[p][2],self.yy2+6)


                                                if(self.doOverlap(l1, d1, l2, d2) and (l2.x!=0) and (l2.y!=0) and self.r1!=l2.x and self.r2!=l2.y and self.del_from_plan[y]==0): 
                                                    #print(x)
                                                    #print(p)
                                                    #print(l1.x,l1.y,r1.x,r1.y,l2.x,l2.y,r2.x,r2.y)
                                                    if(self.new_obj==0):
                                                        if(y!=p):
                                                            zq=0
                                                            for z in range(self.ro):
                                                                l3=Point(self.arr2[z][0],self.arr2[z][1])
                                                                d3=Point(self.arr2[z][2],self.arr2[z][3])
                                                                l4=Point(self.arr2[p][0],self.yy1-6)
                                                                d4=Point(self.arr2[p][2],self.arr2[p][3]+self.yy1-6-self.arr2[p][1])

                                                                if(self.doOverlap(l3,d3,l4,d4) and l4.x!=0 and l4.y!=0 and z!=p and self.del_from_plan[z]==0):
                                                                    zq=1
                                                                    messagebox.showerror("Error occured","Door may overlap with objects")
                                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                    self.arr2[p][0]=self.r1
                                                                    self.arr2[p][1]=self.r2
                                                                    self.arr2[p][2]=self.r3
                                                                    self.arr2[p][3]=self.r4
                                                                    self.arr2[p][4]=1
                                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                                        self.room_doors2[z1]=self.room_doors[z1]
                                                                        #l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                        #d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                        #l6=Point(self.a1,self.a2)
                                                                        #d6=Point(self.a3,self.a4)
                                                                        #chck33=0
                                                                        #if((self.doOverlap(l5,d5,l6,d6)) and l6.x!=0 and l6.y!=0):
                                                                        #    self.room_doors2[z1]=self.room_doors2[z1]+1

                                                                    self.canvas.delete("blucol")
                                                                    break


                                                            if(zq==0):

                                                                p0=self.arr2[p][0]
                                                                p1=self.yy1-6
                                                                p2=self.arr2[p][2]
                                                                p3=self.yy1-6+self.arr2[p][3]-self.arr2[p][1]
                                                                ccc=0
                                                                for z1 in range(len(cfile['bbox_loc'])):
                                                                    
                                                                    cchck=0

                                                                    if(1):
                                                                        for y111 in range(4):

                                                                            
                                                                            
                                                                            if(y111==0):
                                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                            if(y111==1):
                                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                            if(y111==2):
                                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                            if(y111==3):
                                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                            for y112 in range(4):
                                                                                if(y112==0):
                                                                                    l6=Point(p0,p1)
                                                                                    d6=Point(p0,p3)
                                                                                if(y112==1):
                                                                                    l6=Point(p0,p3)
                                                                                    d6=Point(p2,p3)
                                                                                if(y112==2):
                                                                                    l6=Point(p2,p3)
                                                                                    d6=Point(p2,p1)
                                                                                if(y112==3):
                                                                                    l6=Point(p2,p1)
                                                                                    d6=Point(p0,p1)
                                                          
                                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                                    ccc=1
                                                                                    break

                                                                            if(ccc==1):
                                                                                break



                                                                xlxl=0
                                                                for z1 in range(len(cfile['bbox_loc'])):
                                                                    if(self.room_doors2[z1]==0):
                                                                        messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                                        xlxl=1
                                                                        for z2 in range(1000):
                                                                            self.room_doors2[z2]=self.room_doors[z2]
                                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                        self.arr2[p][0]=self.r1
                                                                        self.arr2[p][1]=self.r2
                                                                        self.arr2[p][2]=self.r3
                                                                        self.arr2[p][3]=self.r4
                                                                        break

                                                                if(xlxl==0):
                                                                    if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                                        messagebox.showerror("Error Occured","There is no entry into the houseplan")
                                                                        xlxl=1
                                                                        for z2 in range(1000):
                                                                            self.room_doors2[z2]=self.room_doors[z2]
                                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                        self.arr2[p][0]=self.r1
                                                                        self.arr2[p][1]=self.r2
                                                                        self.arr2[p][2]=self.r3
                                                                        self.arr2[p][3]=self.r4
                                                                        break  


                                                                if(xlxl==0):
                                                                    for z2 in range(1000):
                                                                        self.room_doors[z2]=self.room_doors2[z2]
                                                                        #print(self.room_doors[z2],100)
                                                                    juk=Image.open(PATH8+str(p)+".jpg")
                                                                    jux=juk.convert('RGB')
                                                                    iiux=ImageOps.flip(jux)

                                                                    if(self.main_doors_check[p]==1):
                                                                        self.main_doors_check[p]=0
                                                                        self.main_doors=self.main_doors-1

                                                                    if(self.up_down[p]=='L'):
                                                                        iiux=iiux.rotate(90,expand=True,fillcolor='white')
                                                                    #if(self.up_down[p]=='U'):
                                                                    iiux=iiux.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                                    print(67676)
                                                                    x66=iiux.width
                                                                    y66=iiux.height
                                                                    iiux.save(PATH8+str(p)+".jpg")
                                                                    self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                    
                                                                    self.canvas.create_image(self.arr2[p][0],self.yy1-6,image=self.canvas.iip,anchor="nw")
                                                                    self.mylist.append(self.canvas.iip)
                                                                    self.canvas.delete(self.iid)


                                                                    xlxl=0



                                                                    xe=self.arr2[p][3]-self.arr2[p][1]
                                                                    self.arr2[p][1]=self.yy1-6
                                                                    self.arr2[p][2]=self.arr2[p][0]+x66
                                                                    self.arr2[p][3]=self.yy1-6+y66
                                                                    self.arr2[p][4]=1
                                                    

                                                                    if(self.up_down[p]=='U'):
                                                                        self.up_down[p]='D'
                                                                    else:
                                                                        if(self.up_down[p]=='L'):
                                                                            self.up_down[p]='D'

                                                                    self.hor_ver[p]='H'

                                                                    self.canvas.delete("blucol")
                                                                    zq=1
                                                                    break


                                            if(zq==0):

                                                p0=self.arr2[p][0]
                                                p1=self.yy2+6-self.arr2[p][3]+self.arr2[p][1]
                                                p2=self.arr2[p][2]
                                                p3=self.yy2+6
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break



                                                xlxl=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    if(1):
                                                        if(self.room_doors2[z1]==0):
                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            break
                                                if(xlxl==0):
                                                    if(1):
                                                        if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                            messagebox.showerror("Error Occured","There is no entry into the houseplan")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            
                                                if(xlxl==0):
                                                    for z2 in range(1000):
                                                        self.room_doors[z2]=self.room_doors2[z2]

                                                    if(self.main_doors_check[p]==1):
                                                        self.main_doors=self.main_doors-1
                                                        self.main_doors_check[p]=0

                                                    if(self.up_down[p]=='L'):
                                                        juk=Image.open(PATH8+str(p)+".jpg")
                                                        #juk.show()
                                                        jux=juk.convert('RGB')
                                                        #iiux=ImageOps.flip(jux)
                                                       
                                                        iiux=jux.rotate(-90,expand=True,fillcolor='white')
                                                        #iiux.show()
                                                        x66=iiux.width
                                                        y66=iiux.height
                                                        
                                                        iiux.save(PATH8+str(p)+".jpg")
                                                        self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                    
                                                        self.canvas.create_image(self.arr2[p][0],self.yy2+6-y66,image=self.canvas.iip,anchor="nw")
                                                        self.mylist.append(self.canvas.iip)
                                                        self.canvas.delete(self.iid)

                                                    if(self.up_down[p]=='U'):
                                                        self.canvas.move(self.iid,0,(self.yy2-self.arr2[p][3]+6))
                                                        self.arr2[p][1]=self.arr2[p][1]+self.yy2-self.arr2[p][3]+6
                                                        self.arr2[p][3]=self.yy2+6
                                                        self.arr2[p][4]=1
                                                        self.canvas.delete("blucol")
                                                    else:
                                                        self.up_down[p]='U'
                                                        self.hor_ver[p]='H'
                                                        self.arr2[p][1]=self.yy2+6-y66
                                                        self.arr2[p][3]=self.yy2+6
                                                        self.arr2[p][2]=self.arr2[p][0]+x66
                                                        self.arr2[p][4]=1
                                                        self.canvas.delete("blucol")


                                        if(self.up_down[p]=='D' or self.up_down[p]=='R'):
                                            zq=0

                                            for y in range(self.ro):
                                                l1=Point(self.arr2[y][0],self.arr2[y][1])
                                                d1=Point(self.arr2[y][2],self.arr2[y][3])
                                                l2=Point(self.arr2[p][0],self.yy1-6)
                                                d2=Point(self.arr2[p][2],self.arr2[p][3]+self.yy1-6-self.arr2[p][1])


                                                if(self.doOverlap(l1, d1, l2, d2) and (l2.x!=0) and (l2.y!=0) and self.r1!=l2.x and self.r2!=l2.y and self.del_from_plan[y]==0): 
                                                    #print(x)
                                                    #print(p)
                                                    #print(l1.x,l1.y,r1.x,r1.y,l2.x,l2.y,r2.x,r2.y)
                                                    if(self.new_obj==0):
                                                        if(y!=p):
                                                            zq=0
                                                            for z in range(self.ro):
                                                                l3=Point(self.arr2[z][0],self.arr2[z][1])
                                                                d3=Point(self.arr2[z][2],self.arr2[z][3])
                                                                l4=Point(self.arr2[p][0],self.arr2[p][1]+self.yy2-self.arr2[p][3]+6)
                                                                d4=Point(self.arr2[p][2],self.yy2+6)

                                                                if(self.doOverlap(l3,d3,l4,d4) and l4.x!=0 and l4.y!=0 and z!=p and self.del_from_plan[z]==0):
                                                                    zq=1
                                                                    messagebox.showerror("Error occured","Door may overlap with objects")
                                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                    self.arr2[p][0]=self.r1
                                                                    self.arr2[p][1]=self.r2
                                                                    self.arr2[p][2]=self.r3
                                                                    self.arr2[p][3]=self.r4
                                                                    self.arr2[p][4]=1
                                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                                        self.room_doors2[z1]=self.room_doors[z1]

                                                                


                                                                    self.canvas.delete("blucol")
                                                                    break


                                                            if(zq==0):

                                                                p0=self.arr2[p][0]
                                                                p1=self.yy2+6-self.arr2[p][3]+self.arr2[p][1]
                                                                p2=self.arr2[p][2]
                                                                p3=self.yy2+6
                                                                ccc=0
                                                                for z1 in range(len(cfile['bbox_loc'])):
                                                                    
                                                                    cchck=0

                                                                    if(1):
                                                                        for y111 in range(4):

                                                                            
                                                                            
                                                                            if(y111==0):
                                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                            if(y111==1):
                                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                            if(y111==2):
                                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                            if(y111==3):
                                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                            for y112 in range(4):
                                                                                if(y112==0):
                                                                                    l6=Point(p0,p1)
                                                                                    d6=Point(p0,p3)
                                                                                if(y112==1):
                                                                                    l6=Point(p0,p3)
                                                                                    d6=Point(p2,p3)
                                                                                if(y112==2):
                                                                                    l6=Point(p2,p3)
                                                                                    d6=Point(p2,p1)
                                                                                if(y112==3):
                                                                                    l6=Point(p2,p1)
                                                                                    d6=Point(p0,p1)
                                                          
                                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                                    ccc=1
                                                                                    break

                                                                            if(ccc==1):
                                                                                break






                                                                xlxl=0
                                                                for z1 in range(len(cfile['bbox_loc'])):
                                                                    if(1):
                                                                        if(self.room_doors2[z1]==0):
                                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                                            xlxl=1
                                                                            for z2 in range(1000):
                                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                            self.arr2[p][0]=self.r1
                                                                            self.arr2[p][1]=self.r2
                                                                            self.arr2[p][2]=self.r3
                                                                            self.arr2[p][3]=self.r4
                                                                            break

                                                                if(xlxl==0):
                                                                    if(1):
                                                                        if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                                            messagebox.showerror("Error Occured","There is no entry into the houseplan")
                                                                            xlxl=1
                                                                            for z2 in range(1000):
                                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                            self.arr2[p][0]=self.r1
                                                                            self.arr2[p][1]=self.r2
                                                                            self.arr2[p][2]=self.r3
                                                                            self.arr2[p][3]=self.r4
                                                                            break

                                                                if(xlxl==0):
                                                                    for z2 in range(1000):
                                                                        self.room_doors[z2]=self.room_doors2[z2]
                                                                    juk=Image.open(PATH8+str(p)+".jpg")
                                                                    jux=juk.convert('RGB')
                                                                    iiux=ImageOps.flip(jux)

                                                                    if(self.main_doors_check[p]==1):
                                                                        self.main_doors=self.main_doors-1
                                                                        self.main_doors_check[p]=0

                                                                    if(self.up_down[p]=='R'):
                                                                        iiux=iiux.rotate(90,fillcolor='white',expand=True)
                                                                    #if(self.up_down[p]=='D'):
                                                                    iiux=iiux.rotate(-(2*self.theta),expand=True,fillcolor='white')

                                                                    x66=iiux.width
                                                                    y66=iiux.height
                                                                    iiux.save(PATH8+str(p)+".jpg")
                                                                    self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                    
                                                                    self.canvas.create_image(self.arr2[p][0],self.yy2-y66+6,image=self.canvas.iip,anchor="nw")
                                                                    self.mylist.append(self.canvas.iip)
                                                                    self.canvas.delete(self.iid)

                                                                    self.arr2[p][1]=self.yy2-y66+6
                                                                    self.arr2[p][2]=self.arr2[p][0]+x66
                                                                    self.arr2[p][3]=self.yy2+6
                                                                    self.arr2[p][4]=1

                                                                    if(self.up_down[p]=='D'):
                                                                        self.up_down[p]='U'
                                                                    else:
                                                                        if(self.up_down[p]=='R'):
                                                                            self.up_down[p]='U'

                                                                    self.hor_ver[p]='H'
                                                                            
                                                                    self.canvas.delete("blucol")
                                                                    zq=1
                                                                    break


                                            self.canvas.delete("blucol")
                                            if(zq==0):

                                                p0=self.arr2[p][0]
                                                p1=self.yy1-6
                                                p2=self.arr2[p][2]
                                                p3=self.yy1-6+self.arr2[p][3]-self.arr2[p][1]
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break



                                                xlxl=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    if(1):
                                                        if(self.room_doors2[z1]==0):
                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,sself.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            break

                                                if(xlxl==0):
                                                    if(1):
                                                        if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                            messagebox.showerror("Error Occured","There is no entry into the houseplan")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,sself.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            


                                                if(xlxl==0):
                                                    for z2 in range(1000):
                                                        self.room_doors[z2]=self.room_doors2[z2]
                                                    xe=self.arr2[p][3]-self.arr2[p][1]

                                                    if(self.main_doors_check[p]==1):
                                                        self.main_doors=self.main_doors-1
                                                        self.main_doors_check[p]=0

                                                    if(self.up_down[p]=='D'):
                                                        self.canvas.move(self.iid,0,(self.yy1-self.arr2[p][1]-6))
                                                        self.arr2[p][1]=self.yy1-6
                                                        self.arr2[p][3]=xe+self.yy1-6
                                                        self.arr2[p][4]=1

                                                    if(self.up_down[p]=='R'):
                                                        self.up_down[p]='D'
                                                        self.hor_ver[p]='H'
                                                        juk=Image.open(PATH8+str(p)+".jpg")
                                                        jux=juk.convert('RGB')
                                                        
                                                        iiux=jux.rotate(-90,fillcolor='white',expand=True)

                                                        x66=iiux.width
                                                        y66=iiux.height
                                                        iiux.save(PATH8+str(p)+".jpg")
                                                        self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                    
                                                        self.canvas.create_image(self.arr2[p][0],self.yy1-6,image=self.canvas.iip,anchor="nw")
                                                        self.mylist.append(self.canvas.iip)
                                                        self.canvas.delete(self.iid)
                                                        self.arr2[p][1]=self.yy1-6
                                                        self.arr2[p][2]=self.arr2[p][0]+x66
                                                        self.arr2[p][3]=y66+self.yy1-6
                                                        self.arr2[p][4]=1

                                    else:
                                        #print(1112)
                                        k=self.yy1
                                        self.yy1=self.yy2
                                        self.yy2=k

                                        zq=0
                                        if(self.up_down[p]=='U' or self.up_down[p]=='L'):

                                            for y in range(self.ro):
                                                l1=Point(self.arr2[y][0],self.arr2[y][1])
                                                d1=Point(self.arr2[y][2],self.arr2[y][3])
                                                l2=Point(self.arr2[p][0],self.arr2[p][1]+self.yy2-self.arr2[p][3]+6)
                                                d2=Point(self.arr2[p][2],self.yy2+6)


                                                if(self.doOverlap(l1, d1, l2, d2) and (l2.x!=0) and (l2.y!=0) and self.r1!=l2.x and self.r2!=l2.y and self.del_from_plan[y]==0): 
                                                    #print(x)
                                                    #print(p)
                                                    #print(l1.x,l1.y,r1.x,r1.y,l2.x,l2.y,r2.x,r2.y)
                                                    if(self.new_obj==0):
                                                        if(y!=p):
                                                            zq=0
                                                            for z in range(self.ro):
                                                                l3=Point(self.arr2[z][0],self.arr2[z][1])
                                                                d3=Point(self.arr2[z][2],self.arr2[z][3])
                                                                l4=Point(self.arr2[p][0],self.yy1-6)
                                                                d4=Point(self.arr2[p][2],self.arr2[p][3]+self.yy1-6-self.arr2[p][1])

                                                                if(self.doOverlap(l3,d3,l4,d4) and l4.x!=0 and l4.y!=0 and z!=p and self.del_from_plan[z]==0):
                                                                    zq=1
                                                                    messagebox.showerror("Error occured","Door may overlap with objects")
                                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                    self.arr2[p][0]=self.r1
                                                                    self.arr2[p][1]=self.r2
                                                                    self.arr2[p][2]=self.r3
                                                                    self.arr2[p][3]=self.r4
                                                                    self.arr2[p][4]=1
                                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                                        self.room_doors2[z1]=self.room_doors[z1]

                                                                    self.canvas.delete("blucol")
                                                                    break


                                                            if(zq==0):

                                                                p0=self.arr2[p][0]
                                                                p1=self.yy1-6
                                                                p2=self.arr2[p][2]
                                                                p3=self.yy1-6+self.arr2[p][3]-self.arr2[p][1]
                                                                ccc=0
                                                                for z1 in range(len(cfile['bbox_loc'])):
                                                                    
                                                                    cchck=0

                                                                    if(1):
                                                                        for y111 in range(4):

                                                                            
                                                                            
                                                                            if(y111==0):
                                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                            if(y111==1):
                                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                            if(y111==2):
                                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                            if(y111==3):
                                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                            for y112 in range(4):
                                                                                if(y112==0):
                                                                                    l6=Point(p0,p1)
                                                                                    d6=Point(p0,p3)
                                                                                if(y112==1):
                                                                                    l6=Point(p0,p3)
                                                                                    d6=Point(p2,p3)
                                                                                if(y112==2):
                                                                                    l6=Point(p2,p3)
                                                                                    d6=Point(p2,p1)
                                                                                if(y112==3):
                                                                                    l6=Point(p2,p1)
                                                                                    d6=Point(p0,p1)
                                                          
                                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                                    ccc=1
                                                                                    break

                                                                            if(ccc==1):
                                                                                break



                                                                xlxl=0
                                                                for z1 in range(len(cfile['bbox_loc'])):
                                                                    if(self.room_doors2[z1]==0):
                                                                        messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                                        xlxl=1
                                                                        for z2 in range(1000):
                                                                            self.room_doors2[z2]=self.room_doors[z2]
                                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                        self.arr2[p][0]=self.r1
                                                                        self.arr2[p][1]=self.r2
                                                                        self.arr2[p][2]=self.r3
                                                                        self.arr2[p][3]=self.r4
                                                                        break
                                                                if(xlxl==0):
                                                                    if(self.main_doors_check[p]==1 and self.main_doors[p]==1):
                                                                        messagebox.showerror("Error Occured","There is no entry into the houseplan")
                                                                        xlxl=1
                                                                        for z2 in range(1000):
                                                                            self.room_doors2[z2]=self.room_doors[z2]
                                                                        self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                        self.arr2[p][0]=self.r1
                                                                        self.arr2[p][1]=self.r2
                                                                        self.arr2[p][2]=self.r3
                                                                        self.arr2[p][3]=self.r4
                                                                        break


                                                                if(xlxl==0):
                                                                    for z2 in range(1000):
                                                                        self.room_doors[z2]=self.room_doors2[z2]

                                                                    if(self.main_doors_check[p]==1):
                                                                        self.main_doors=self.main_doors-1
                                                                        self.main_doors_check[p]=0

                                                                    juk=Image.open(PATH8+str(p)+".jpg")
                                                                    jux=juk.convert('RGB')
                                                                    iiux=ImageOps.flip(jux)
                                                                    if(self.up_down[p]=='L'):
                                                                        iiux=iiux.rotate(90,expand=True,fillcolor='white')
                                                                    #if(self.up_down[p]=='U'):
                                                                    iiux=iiux.rotate(-(2*self.theta),expand=True,fillcolor='white')

                                                                    x66=iiux.width
                                                                    y66=iiux.height
                                                                    iiux.save(PATH8+str(p)+".jpg")
                                                                    self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                    print(999033)
                                                                    self.canvas.create_image(self.arr2[p][0],self.yy1-6,image=self.canvas.iip,anchor="nw")
                                                                    self.mylist.append(self.canvas.iip)
                                                                    self.canvas.delete(self.iid)


                                                                    xlxl=0



                                                                    xe=self.arr2[p][3]-self.arr2[p][1]
                                                                    self.arr2[p][1]=self.yy1-6
                                                                    self.arr2[p][2]=self.arr2[p][0]+x66
                                                                    self.arr2[p][3]=self.yy1-6+y66
                                                                    self.arr2[p][4]=1
                                                    

                                                                    if(self.up_down[p]=='U'):
                                                                        self.up_down[p]='D'
                                                                    else:
                                                                        if(self.up_down[p]=='L'):
                                                                            self.up_down[p]='D'

                                                                    self.hor_ver[p]='H'

                                                                    self.canvas.delete("blucol")
                                                                    zq=1
                                                                    break


                                            if(zq==0):

                                                p0=self.arr2[p][0]
                                                p1=self.yy2+6-self.arr2[p][3]+self.arr2[p][1]
                                                p2=self.arr2[p][2]
                                                p3=self.yy2+6
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break



                                                xlxl=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    if(1):
                                                        if(self.room_doors2[z1]==0):
                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            break

                                                if(xlxl==0):
                                                    if(1):
                                                        if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                            messagebox.showerror("Error Occured","There is no entry into the houseplan")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            
                                                if(xlxl==0):
                                                    for z2 in range(1000):
                                                        self.room_doors[z2]=self.room_doors2[z2]

                                                    if(self.main_doors_check[p]==1):
                                                        self.main_doors=self.main_doors-1
                                                        self.main_doors_check[p]=0

                                                    if(self.up_down[p]=='L'):
                                                        juk=Image.open(PATH8+str(p)+".jpg")
                                                        #juk.show()
                                                        jux=juk.convert('RGB')
                                                        #iiux=ImageOps.flip(jux)
                                                       
                                                        iiux=jux.rotate(-90,expand=True,fillcolor='white')
                                                        #iiux.show()
                                                        x66=iiux.width
                                                        y66=iiux.height
                                                        
                                                        iiux.save(PATH8+str(p)+".jpg")
                                                        self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                    
                                                        self.canvas.create_image(self.arr2[p][0],self.yy2+6-y66,image=self.canvas.iip,anchor="nw")
                                                        self.mylist.append(self.canvas.iip)
                                                        self.canvas.delete(self.iid)

                                                    if(self.up_down[p]=='U'):
                                                        self.canvas.move(self.iid,0,(self.yy2-self.arr2[p][3]+6))
                                                        self.arr2[p][1]=self.yy2+6-y66
                                                        self.arr2[p][3]=self.yy2+6
                                                        self.arr2[p][4]=1
                                                        self.canvas.delete("blucol")
                                                    else:
                                                        self.up_down[p]='U'
                                                        self.hor_ver[p]='H'
                                                        self.arr2[p][1]=self.yy2+6-y66
                                                        self.arr2[p][3]=self.yy2+6
                                                        self.arr2[p][2]=self.arr2[p][0]+x66
                                                        self.arr2[p][4]=1
                                                        self.canvas.delete("blucol")


                                        if(self.up_down[p]=='D' or self.up_down[p]=='R'):
                                            zq=0

                                            for y in range(self.ro):
                                                l1=Point(self.arr2[y][0],self.arr2[y][1])
                                                d1=Point(self.arr2[y][2],self.arr2[y][3])
                                                l2=Point(self.arr2[p][0],self.yy1-6)
                                                d2=Point(self.arr2[p][2],self.arr2[p][3]+self.yy1-6-self.arr2[p][1])


                                                if(self.doOverlap(l1, d1, l2, d2) and (l2.x!=0) and (l2.y!=0) and self.r1!=l2.x and self.r2!=l2.y and self.del_from_plan[y]==0): 
                                                    #print(x)
                                                    #print(p)
                                                    #print(l1.x,l1.y,r1.x,r1.y,l2.x,l2.y,r2.x,r2.y)
                                                    if(self.new_obj==0):
                                                        if(y!=p):
                                                            zq=0
                                                            for z in range(self.ro):
                                                                l3=Point(self.arr2[z][0],self.arr2[z][1])
                                                                d3=Point(self.arr2[z][2],self.arr2[z][3])
                                                                l4=Point(self.arr2[p][0],self.arr2[p][1]+self.yy2-self.arr2[p][3]+6)
                                                                d4=Point(self.arr2[p][2],self.yy2+6)

                                                                if(self.doOverlap(l3,d3,l4,d4) and not(l4.x==0 and l4.y==0) and z!=p and self.del_from_plan[z]==0):
                                                                    zq=1
                                                                    messagebox.showerror("Error occured","Door may overlap with objects")
                                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                    self.arr2[p][0]=self.r1
                                                                    self.arr2[p][1]=self.r2
                                                                    self.arr2[p][2]=self.r3
                                                                    self.arr2[p][3]=self.r4
                                                                    self.arr2[p][4]=1

                                                                    p0=self.a1
                                                                    p1=self.a2
                                                                    p2=self.a3
                                                                    p3=self.a4
                                                                    ccc=0
                                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                                        
                                                                        cchck=0

                                                                        if(1):
                                                                            for y111 in range(4):

                                                                                
                                                                                
                                                                                if(y111==0):
                                                                                    l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                                    d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                                if(y111==1):
                                                                                    l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                                    d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                                if(y111==2):
                                                                                    l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                                    d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                                if(y111==3):
                                                                                    l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                                    d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                                for y112 in range(4):
                                                                                    if(y112==0):
                                                                                        l6=Point(p0,p1)
                                                                                        d6=Point(p0,p3)
                                                                                    if(y112==1):
                                                                                        l6=Point(p0,p3)
                                                                                        d6=Point(p2,p3)
                                                                                    if(y112==2):
                                                                                        l6=Point(p2,p3)
                                                                                        d6=Point(p2,p1)
                                                                                    if(y112==3):
                                                                                        l6=Point(p2,p1)
                                                                                        d6=Point(p0,p1)
                                                              
                                                                                    if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                                        self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                                        ccc=1
                                                                                        break

                                                                                if(ccc==1):
                                                                                    break

                                                                


                                                                    self.canvas.delete("blucol")
                                                                    break


                                                            if(zq==0):

                                                                p0=self.arr2[p][0]
                                                                p1=self.yy2+6-self.arr2[p][3]+self.arr2[p][1]
                                                                p2=self.arr2[p][2]
                                                                p3=self.yy2+6
                                                                ccc=0
                                                                for z1 in range(len(cfile['bbox_loc'])):
                                                                    
                                                                    cchck=0

                                                                    if(1):
                                                                        for y111 in range(4):

                                                                            
                                                                            
                                                                            if(y111==0):
                                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                            if(y111==1):
                                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                            if(y111==2):
                                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                            if(y111==3):
                                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                            for y112 in range(4):
                                                                                if(y112==0):
                                                                                    l6=Point(p0,p1)
                                                                                    d6=Point(p0,p3)
                                                                                if(y112==1):
                                                                                    l6=Point(p0,p3)
                                                                                    d6=Point(p2,p3)
                                                                                if(y112==2):
                                                                                    l6=Point(p2,p3)
                                                                                    d6=Point(p2,p1)
                                                                                if(y112==3):
                                                                                    l6=Point(p2,p1)
                                                                                    d6=Point(p0,p1)
                                                          
                                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                                    ccc=1
                                                                                    break

                                                                            if(ccc==1):
                                                                                break



                                                                xlxl=0
                                                                for z1 in range(len(cfile['bbox_loc'])):
                                                                    if(1):
                                                                        if(self.room_doors2[z1]==0):
                                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                                            xlxl=1
                                                                            for z2 in range(1000):
                                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                            self.arr2[p][0]=self.r1
                                                                            self.arr2[p][1]=self.r2
                                                                            self.arr2[p][2]=self.r3
                                                                            self.arr2[p][3]=self.r4
                                                                            break


                                                                if(xlxl==0):
                                                                    if(1):
                                                                        if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                                            xlxl=1
                                                                            for z2 in range(1000):
                                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                            self.arr2[p][0]=self.r1
                                                                            self.arr2[p][1]=self.r2
                                                                            self.arr2[p][2]=self.r3
                                                                            self.arr2[p][3]=self.r4
                                                                            break
                                                                if(xlxl==0):
                                                                    for z2 in range(1000):
                                                                        self.room_doors[z2]=self.room_doors2[z2]
                                                                    juk=Image.open(PATH8+str(p)+".jpg")
                                                                    jux=juk.convert('RGB')
                                                                    iiux=ImageOps.flip(jux)

                                                                    if(self.main_doors_check[p]==1):
                                                                        self.main_doors_check[p]=0
                                                                        self.main_doors=self.main_doors-1

                                                                    if(self.up_down[p]=='R'):
                                                                        iiux=iiux.rotate(90,fillcolor='white',expand=True)
                                                                    #if(self.up_down[p]=='D'):
                                                                    iiux=iiux.rotate(-(2*self.theta),expand=True,fillcolor='white')

                                                                    x66=iiux.width
                                                                    y66=iiux.height
                                                                    iiux.save(PATH8+str(p)+".jpg")
                                                                    self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                    
                                                                    self.canvas.create_image(self.arr2[p][0],self.yy2-y66-5,image=self.canvas.iip,anchor="nw")
                                                                    self.mylist.append(self.canvas.iip)
                                                                    self.canvas.delete(self.iid)

                                                                    self.arr2[p][1]=self.yy2-y66+6
                                                                    self.arr2[p][2]=self.arr2[p][0]+x66
                                                                    self.arr2[p][3]=self.yy2+6
                                                                    self.arr2[p][4]=1

                                                                    if(self.up_down[p]=='D'):
                                                                        self.up_down[p]='U'
                                                                    else:
                                                                        if(self.up_down[p]=='R'):
                                                                            self.up_down[p]='U'

                                                                    self.hor_ver[p]='H'
                                                                            
                                                                    self.canvas.delete("blucol")
                                                                    zq=1
                                                                    break


                                            self.canvas.delete("blucol")
                                            if(zq==0):

                                                p0=self.arr2[p][0]
                                                p1=self.yy1-6
                                                p2=self.arr2[p][2]
                                                p3=self.yy1-6+self.arr2[p][3]-self.arr2[p][1]
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break




                                                xlxl=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    if(1):
                                                        if(self.room_doors2[z1]==0):
                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            break

                                                if(xlxl==0):
                                                    if(1):
                                                        if(self.main_doors_check[p]==1 and self.main_doors==1):
                                                            messagebox.showerror("Error Occured","There is no entry into the houseplan")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            

                                                if(xlxl==0):
                                                    for z2 in range(1000):
                                                        self.room_doors[z2]=self.room_doors2[z2]
                                                    xe=self.arr2[p][3]-self.arr2[p][1]

                                                    if(self.main_doors_check[p]==1):
                                                        self.main_doors=self.main_doors-1
                                                        self.main_doors_check[p]=0

                                                    if(self.up_down[p]=='D'):
                                                        self.canvas.move(self.iid,0,(self.yy1-self.arr2[p][1]-6))
                                                        self.arr2[p][1]=self.yy1-6
                                                        self.arr2[p][3]=xe+self.yy1-6
                                                        self.arr2[p][4]=1

                                                    if(self.up_down[p]=='R'):
                                                        self.up_down[p]='D'
                                                        self.hor_ver[p]='H'
                                                        juk=Image.open(PATH8+str(p)+".jpg")
                                                        jux=juk.convert('RGB')
                                                        
                                                        iiux=jux.rotate(-90,fillcolor='white',expand=True)

                                                        x66=iiux.width
                                                        y66=iiux.height
                                                        iiux.save(PATH8+str(p)+".jpg")
                                                        self.canvas.iip=ImageTk.PhotoImage(iiux)
                                                                    
                                                        self.canvas.create_image(self.arr2[p][0],self.yy1-6,image=self.canvas.iip,anchor="nw")
                                                        self.mylist.append(self.canvas.iip)
                                                        self.canvas.delete(self.iid)
                                                        self.arr2[p][1]=self.yy1-6
                                                        self.arr2[p][2]=self.arr2[p][0]+x66
                                                        self.arr2[p][3]=y66+self.yy1-6
                                                        self.arr2[p][4]=1
                                #print(self.first,self.sec)







                                if(self.sec==0 and self.first==1 and ccc==0 and not(c0==self.a1 and c1==self.a2)):
                                    #print(self.yy1,self.h1)
                                    #if(gap1>gap2):
                                    if(self.yy1==self.h1):
                                        #print(113)
                                        if(self.up_down[p]=='U' or self.up_down[p]=='L'):
                                            if(self.arr2[p][1]+self.yy1-self.arr2[p][3]+8 >= 0 and self.yy1+8 <= 715 ):

                                                p0=self.arr2[p][0]
                                                p1=self.yy1+8-self.arr2[p][3]+self.arr2[p][1]
                                                p2=self.arr2[p][2]
                                                p3=self.yy1+8
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break



                                                xlxl=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    if(1):
                                                        if(self.room_doors2[z1]==0):
                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            self.canvas.delete("blucol")
                                                            break

                                                if(xlxl==0):
                                                    for z2 in range(1000):
                                                        self.room_doors[z2]=self.room_doors2[z2]

                                                    if(self.main_doors_check[p]==0):
                                                        self.main_doors=self.main_doors+1
                                                        self.main_doors_check[p]=1

                                                    if(self.up_down[p]=='L'):
                                                        ius=Image.open(PATH8+str(p)+".jpg")
                                                        ius=ius.convert('RGB')
                                                        ius=ius.rotate(-90,expand=True,fillcolor='white')
                                                        print(6000)
                                                        ius.save(PATH8+str(p)+".jpg")
                                                        x66=ius.width
                                                        y66=ius.height
                                                        self.canvas.iik=ImageTk.PhotoImage(ius)
                                                        self.canvas.create_image(self.arr2[p][0],self.yy1+8-y66,image=self.canvas.iik,anchor="nw")
                                                        self.canvas.delete(self.iid)
                                                        self.mylist.append(self.canvas.iik)


                                                        self.up_down[p]='U'
                                                        self.hor_ver[p]='H'


                                                        #self.canvas.move(self.iid,0,self.yy1-self.arr2[p][3]+8)
                                                        self.arr2[p][1]=self.yy1-y66+8
                                                        self.arr2[p][2]=self.arr2[p][0]+x66
                                                        self.arr2[p][3]=self.yy1+8
                                                        self.canvas.delete("blucol")

                                                    else:
                                                        self.canvas.move(self.iid,0,self.yy1-self.arr2[p][3]+8)
                                                        self.arr2[p][1]=self.arr2[p][1]+self.yy1-self.arr2[p][3]+8
                                                           
                                                        self.arr2[p][3]=self.yy1+8
                                                        self.arr2[p][4]=1
                                                        self.canvas.delete("blucol")

                                            else:
                                                zzp=0
                                                for y in range(self.ro):
                                                    l1=Point(self.arr2[y][0],self.arr2[y][1])
                                                    d1=Point(self.arr2[y][2],self.arr2[y][3])
                                                    l2=Point(self.arr2[p][0],self.yy1-22)
                                                    d2=Point(self.arr2[p][2],self.yy1+22+self.arr2[p][3]-self.arr2[p][1])

                                                    if(self.doOverlap(l1,d1,l2,d2) and l1.x!=0 and l1.y!=0 and y!=p and self.del_from_plan[y]==0):
                                                        zzp=1
                                                        break

                                                if(zzp==0):

                                                    p0=self.arr2[p][0]
                                                    p1=self.yy1-22
                                                    p2=self.arr2[p][2]
                                                    p3=self.yy1-22+self.arr2[p][3]-self.arr2[p][1]
                                                    ccc=0
                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                        
                                                        cchck=0

                                                        if(1):
                                                            for y111 in range(4):

                                                                
                                                                
                                                                if(y111==0):
                                                                    l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                    d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                if(y111==1):
                                                                    l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                    d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                if(y111==2):
                                                                    l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                    d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                if(y111==3):
                                                                    l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                    d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                for y112 in range(4):
                                                                    if(y112==0):
                                                                        l6=Point(p0,p1)
                                                                        d6=Point(p0,p3)
                                                                    if(y112==1):
                                                                        l6=Point(p0,p3)
                                                                        d6=Point(p2,p3)
                                                                    if(y112==2):
                                                                        l6=Point(p2,p3)
                                                                        d6=Point(p2,p1)
                                                                    if(y112==3):
                                                                        l6=Point(p2,p1)
                                                                        d6=Point(p0,p1)
                                              
                                                                    if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                        self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                        ccc=1
                                                                        break

                                                                if(ccc==1):
                                                                    break



                                                    xlxl=0
                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                        if(1):
                                                            if(self.room_doors2[z1]==0):
                                                                messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                                xlxl=1
                                                                for z2 in range(1000):
                                                                    self.room_doors2[z2]=self.room_doors[z2]
                                                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                self.arr2[p][0]=self.r1
                                                                self.arr2[p][1]=self.r2
                                                                self.arr2[p][2]=self.r3
                                                                self.arr2[p][3]=self.r4
                                                                self.canvas.delete("blucol")
                                                                break

                                                    if(xlxl==0):
                                                        for z2 in range(1000):
                                                            self.room_doors[z2]=self.room_doors2[z2]


                                                        if(self.main_doors_check[p]==0):
                                                            self.main_doors=self.main_doors+1
                                                            self.main_doors_check[p]=1
                                                        juk=Image.open(PATH8+str(p)+".jpg")
                                                        jux=juk.convert('RGB')
                                                        jux=ImageOps.flip(jux)
                                                        if(self.up_down[p]=='L'):
                                                            jux=jux.rotate(90,expand=True,fillcolor='white')
                                                        #if(self.up_down[p]=='U'):
                                                        jux=jux.rotate(-(2*self.theta),expand=True,fillcolor='white')

                                                        #print(10000)
                                                        x66=jux.width
                                                        y66=jux.height
                                                        jux.save(PATH8+str(p)+".jpg")

                                                        self.canvas.iik=ImageTk.PhotoImage(jux)
                                                        self.canvas.create_image(self.arr2[p][0],self.yy1-30,image=self.canvas.iik,anchor="nw")
                                                        print(5000)
                                                        self.canvas.delete(self.iid)
                                                        self.mylist.append(self.canvas.iik)

                                                        if(self.up_down[p]=='L'):
                                                            self.hor_ver[p]='H'

                                                        self.up_down[p]='D'

                                                        self.arr2[p][1]=self.yy1-30
                                                        self.arr2[p][2]=self.arr2[p][0]+x66
                                                        self.arr2[p][3]=self.yy1-30+y66
                                                        self.canvas.delete("blucol")


                                                if(zzp==1):

                                                    for z1 in range(len(cfile['bbox_loc'])):

                                                        p0=self.a1
                                                        p1=self.a2
                                                        p2=self.a3
                                                        p3=self.a4
                                                        ccc=0
                                                        for z1 in range(len(cfile['bbox_loc'])):
                                                            
                                                            cchck=0

                                                            if(1):
                                                                for y111 in range(4):

                                                                    
                                                                    
                                                                    if(y111==0):
                                                                        l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                        d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                    if(y111==1):
                                                                        l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                        d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                    if(y111==2):
                                                                        l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                        d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                    if(y111==3):
                                                                        l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                        d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                    for y112 in range(4):
                                                                        if(y112==0):
                                                                            l6=Point(p0,p1)
                                                                            d6=Point(p0,p3)
                                                                        if(y112==1):
                                                                            l6=Point(p0,p3)
                                                                            d6=Point(p2,p3)
                                                                        if(y112==2):
                                                                            l6=Point(p2,p3)
                                                                            d6=Point(p2,p1)
                                                                        if(y112==3):
                                                                            l6=Point(p2,p1)
                                                                            d6=Point(p0,p1)
                                                  
                                                                        if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                            self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                            ccc=1
                                                                            break

                                                                    if(ccc==1):
                                                                        break

                                                    xlxl=0
                                               

                                                    messagebox.showerror("Error occured","Door cannot cross the dimension of the floorplan")
                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                    self.arr2[p][0]=self.r1
                                                    self.arr2[p][1]=self.r2
                                                    self.arr2[p][2]=self.r3
                                                    self.arr2[p][3]=self.r4
                                                    self.canvas.delete("blucol")


                                        if(self.up_down[p]=='D' or self.up_down[p]=='R'):
                                            if(self.h1-10 >= 0 and self.arr2[p][3]+self.h1-10-self.arr2[p][1] <= 715):

                                                p0=self.arr2[p][0]
                                                p1=self.h1-10
                                                p2=self.arr2[p][2]
                                                p3=self.h1-10+self.arr2[p][3]-self.arr2[p][1]
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break



                                                xlxl=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    if(1):
                                                        if(self.room_doors2[z1]==0):
                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            self.canvas.delete("blucol")
                                                            break

                                                if(xlxl==0):
                                                    for z2 in range(1000):
                                                        self.room_doors[z2]=self.room_doors2[z2]

                                                    cccs=0
                                                    for z1 in range(self.ro):
                                                        l5=Point(self.arr2[z1][0],self.arr2[z1][1])
                                                        d5=Point(self.arr2[z1][2],self.arr2[z1][3])
                                                        l6=Point(self.arr2[p][0],self.h1-10)
                                                        d6=Point(self.arr2[p][2],self.h1-10+self.arr2[p][3]-self.arr2[p][1])

                                                        if(self.doOverlap(l5,d5,l6,d6) and z1!=p and not(l6.x==0 and d6.x==0) and self.h1-self.arr2[p][3]+self.arr2[p][1]-5 <= 0 and self.del_from_plan[z1]==0):
                                                            messagebox.showerror("Error Occured","Door overlaps with the object")
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            self.canvas.delete("blucol")
                                                            cccs=1
                                                            break
                                                    
                                                        if(self.doOverlap(l5,d5,l6,d6) and self.h1-self.arr2[p][3]+self.arr2[p][1]-5 > 0 and z1!=p and self.del_from_plan[z1]==0):
                                                            juk=Image.open(PATH8+str(p)+".jpg")
                                                            jux=juk.convert('RGB')
                                                            jux=ImageOps.flip(jux)

                                                            if(self.up_down[p]=='R'):
                                                                jux=jux.rotate(90,expand=True,fillcolor='white')
                                                            #if(self.up_down[p]=='D'):
                                                            jux=jux.rotate(-(2*self.theta),expand=True,fillcolor='white')

                                                            x66=jux.width
                                                            y66=jux.height

                                                            jux.save(PATH8+str(p)+".jpg")


                                                            if(self.main_doors_check[p]==0):
                                                                self.main_doors=self.main_doors+1
                                                                self.main_doors_check[p]=1
                                                            self.canvas.iik=ImageTk.PhotoImage(jux)
                                                            self.canvas.create_image(self.arr2[p][0],self.h1-self.arr2[p][3]+self.arr2[p][1]+11,image=self.canvas.iik,anchor="nw")
                                                            self.canvas.delete(self.iid)
                                                            self.mylist.append(self.canvas.iik)
                                                            self.up_down[p]='U'
                                                            self.hor_ver[p]='H'
                                                            cccs=1
                                                            
                                                            xe=self.arr2[p][3]-self.arr2[p][1]
                                                            self.arr2[p][1]=self.h1-xe+11
                                                            self.arr2[p][3]=self.h1+11+y66-xe
                                                            self.arr2[p][4]=1
                                                            self.canvas.delete("blucol")
                                                            break


                                                    if(cccs==0):


                                                        if(self.main_doors_check[p]==0):
                                                            self.main_doors=self.main_doors+1
                                                            self.main_doors_check[p]=1
                                                        if(self.up_down[p]=='R'):
                                                            juk=Image.open(PATH8+str(p)+".jpg")
                                                            jux=juk.convert('RGB')
                                                            jux=jux.rotate(-90,expand=True,fillcolor='white')
                                                            jux.save(PATH8+str(p)+".jpg")

                                                            x66=jux.width
                                                            y66=jux.height
                                                            self.canvas.iik=ImageTk.PhotoImage(jux)
                                                            self.canvas.create_image(self.arr2[p][0],self.h1-20,image=self.canvas.iik,anchor="nw")
                                                            self.canvas.delete(self.iid)
                                                            self.mylist.append(self.canvas.iik)
                                                            self.up_down[p]='D'
                                                            self.hor_ver[p]='H'
                                                            self.arr2[p][1]=self.h1-20
                                                            self.arr2[p][2]=self.arr2[p][0]+x66
                                                            self.arr2[p][3]=self.arr2[p][1]+y66
                                                            self.canvas.delete("blucol")

                                                        else:
                                                            self.canvas.move(self.iid,0,self.h1-20-self.arr2[p][1])
                                                            xe=self.arr2[p][3]-self.arr2[p][1]
                                                            self.arr2[p][1]=self.h1-20
                                                               
                                                            self.arr2[p][3]=self.h1-20+xe
                                                            self.arr2[p][4]=1
                                                            self.canvas.delete("blucol")
                                            else:
                                                zzp=0
                                                for y in range(self.ro):
                                                    l1=Point(self.arr2[y][0],self.arr2[y][1])
                                                    d1=Point(self.arr2[y][2],self.arr2[y][3])
                                                    l2=Point(self.arr2[p][0],self.yy1+15-self.arr2[p][3]+self.arr2[p][1])
                                                    d2=Point(self.arr2[p][2],self.yy1+15)

                                                    if(self.doOverlap(l1,d1,l2,d2) and l1.x!=0 and l1.y!=0 and y!=p and self.del_from_plan[y]==0):
                                                        zzp=1
                                                        break

                                                if(zzp==0):

                                                    p0=self.arr2[p][0]
                                                    p1=self.yy1+22-self.arr2[p][3]+self.arr2[p][1]
                                                    p2=self.arr2[p][2]
                                                    p3=self.yy1+22
                                                    ccc=0
                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                        
                                                        cchck=0

                                                        if(1):
                                                            for y111 in range(4):

                                                                
                                                                
                                                                if(y111==0):
                                                                    l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                    d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                if(y111==1):
                                                                    l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                    d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                if(y111==2):
                                                                    l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                    d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                if(y111==3):
                                                                    l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                    d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                for y112 in range(4):
                                                                    if(y112==0):
                                                                        l6=Point(p0,p1)
                                                                        d6=Point(p0,p3)
                                                                    if(y112==1):
                                                                        l6=Point(p0,p3)
                                                                        d6=Point(p2,p3)
                                                                    if(y112==2):
                                                                        l6=Point(p2,p3)
                                                                        d6=Point(p2,p1)
                                                                    if(y112==3):
                                                                        l6=Point(p2,p1)
                                                                        d6=Point(p0,p1)
                                              
                                                                    if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                        self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                        ccc=1
                                                                        break

                                                                if(ccc==1):
                                                                    break



                                                    xlxl=0
                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                        if(1):
                                                            if(self.room_doors2[z1]==0):
                                                                messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                                xlxl=1
                                                                for z2 in range(1000):
                                                                    self.room_doors2[z2]=self.room_doors[z2]
                                                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                self.arr2[p][0]=self.r1
                                                                self.arr2[p][1]=self.r2
                                                                self.arr2[p][2]=self.r3
                                                                self.arr2[p][3]=self.r4
                                                                self.canvas.delete("blucol")
                                                                break

                                                    if(xlxl==0):
                                                        for z2 in range(1000):
                                                            self.room_doors[z2]=self.room_doors2[z2]


                                                        if(self.main_doors_check[p]==0):
                                                            self.main_doors=self.main_doors+1
                                                            self.main_doors_check[p]=1
                                                        juk=Image.open(PATH8+str(p)+".jpg")
                                                        jux=juk.convert('RGB')
                                                        jux=ImageOps.flip(jux)
                                                        if(self.up_down[p]=='R'):
                                                            jux=jux.rotate(90,expand=True,fillcolor='white')
                                                        #if(self.up_down[p]=='D'):
                                                        jux=jux.rotate(-(2*self.theta),expand=True,fillcolor='white')

                                                        x66=jux.width
                                                        y66=jux.height
                                                        jux.save(PATH8+str(p)+".jpg")

                                                        self.canvas.iik=ImageTk.PhotoImage(jux)
                                                        self.canvas.create_image(self.arr2[p][0],self.yy1+22-y66,image=self.canvas.iik,anchor="nw")
                                                        self.canvas.delete(self.iid)
                                                        self.mylist.append(self.canvas.iik)

                                                        self.up_down[p]='U'
                                                        self.hor_ver[p]='H'

                                                        self.arr2[p][1]=self.yy1+22-y66
                                                        self.arr2[p][2]=self.arr2[p][0]+x66
                                                        self.arr2[p][3]=self.yy1+22
                                                        self.canvas.delete("blucol")


                                                if(zzp==1):

                                                    p0=self.a1
                                                    p1=self.a2
                                                    p2=self.a3
                                                    p3=self.a4
                                                    ccc=0
                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                        
                                                        cchck=0

                                                        if(1):
                                                            for y111 in range(4):

                                                                
                                                                
                                                                if(y111==0):
                                                                    l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                    d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                if(y111==1):
                                                                    l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                    d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                if(y111==2):
                                                                    l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                    d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                if(y111==3):
                                                                    l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                    d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                for y112 in range(4):
                                                                    if(y112==0):
                                                                        l6=Point(p0,p1)
                                                                        d6=Point(p0,p3)
                                                                    if(y112==1):
                                                                        l6=Point(p0,p3)
                                                                        d6=Point(p2,p3)
                                                                    if(y112==2):
                                                                        l6=Point(p2,p3)
                                                                        d6=Point(p2,p1)
                                                                    if(y112==3):
                                                                        l6=Point(p2,p1)
                                                                        d6=Point(p0,p1)
                                              
                                                                    if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                        self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                        ccc=1
                                                                        break

                                                                if(ccc==1):
                                                                    break


                                                
                                
                                                            
                                                    messagebox.showerror("Error occured","Door cannot cross the dimension of the floorplan")
                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                    self.arr2[p][0]=self.r1
                                                    self.arr2[p][1]=self.r2
                                                    self.arr2[p][2]=self.r3
                                                    self.arr2[p][3]=self.r4
                                                    self.canvas.delete("blucol")


                                    if(self.yy1==self.h2):
                                        #print(114)
                                        if(self.up_down[p]=='U' or self.up_down[p]=='L'):
                                            if(self.arr2[p][1]+self.yy1-self.arr2[p][3]+20 >=0 and self.yy1+20 <= 715):

                                                p0=self.arr2[p][0]
                                                p1=self.yy1+20-self.arr2[p][3]+self.arr2[p][1]
                                                p2=self.arr2[p][2]
                                                p3=self.yy1+20
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break



                                                xlxl=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    if(1):
                                                        if(self.room_doors2[z1]==0):
                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            self.canvas.delete("blucol")
                                                            break

                                                if(xlxl==0):
                                                    for z2 in range(1000):
                                                        self.room_doors[z2]=self.room_doors2[z2]

                                                    asa=0
                                                    for z2 in range(self.ro):
                                                        l5=Point(self.arr2[z2][0],self.arr2[z2][1])
                                                        d5=Point(self.arr2[z2][2],self.arr2[z2][3])
                                                        l6=Point(self.arr2[p][0],self.yy1+20-self.arr2[p][3]+self.arr2[p][1])
                                                        d6=Point(self.arr2[p][2],self.yy1+20)

                                                        if(self.doOverlap(l5,d5,l6,d6) and not(l6.x==0 and l6.y==0) and z2!=p and self.yy1+self.arr2[p][3]-self.arr2[p][1]>715 and self.del_from_plan[z2]==0):
                                                            messagebox.showerror("Error occured","Door overlaps with the object")
                                                            asa=1
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            self.canvas.delete("blucol")
                                                            asa=1
                                                            break

                                                        if(self.doOverlap(l5,d5,l6,d6) and self.yy1+self.arr2[p][3]-self.arr2[p][1] <= 715 and self.del_from_plan[z2]==0):
                                                            juk=Image.open(PATH8+str(p)+".jpg")
                                                            jux=juk.convert('RGB')

                                                            jux=ImageOps.flip(jux)
                                                            if(self.up_down[p]=='L'):
                                                                jux=jux.rotate(90,expand=True,fillcolor='white')
                                                            #if(self.up_down[p]=='U'):
                                                            jux=jux.rotate(-(2*self.theta),expand=True,fillcolor='white')

                                                            x66=jux.width
                                                            y66=jux.height
                                                            jux.save(PATH8+str(p)+".jpg")

                                                            #print(10000)
                                                            if(self.main_doors_check[p]==0):
                                                                self.main_doors=self.main_doors+1
                                                                self.main_doors_check[p]=1
                                                            self.canvas.iik=ImageTk.PhotoImage(jux)
                                                            #self.canvas.create_image(self.arr2[p][0],self.yy1-23,image=self.canvas.iik,anchor="nw")
                                                            print(399)
                                                            self.canvas.delete(self.iid)
                                                            self.mylist.append(self.canvas.iik)
                                                            self.up_down[p]='D'
                                                            self.hor_ver[p]='H'
                                                            asa=1
                                                            
                                                            xe=self.arr2[p][3]-self.arr2[p][1]
                                                            self.arr2[p][1]=self.yy1-6
                                                            self.arr2[p][2]=self.arr2[p][0]+x66
                                                            self.arr2[p][3]=self.yy1-6+y66
                                                            self.arr2[p][4]=1
                                                            self.canvas.delete("blucol")
                                                            break




                                                    if(asa==0):

                                                        if(self.main_doors_check[p]==0):
                                                            self.main_doors=self.main_doors+1
                                                            self.main_doors_check[p]=1

                                                        if(self.up_down[p]=='L'):

                                                            juk=Image.open(PATH8+str(p)+".jpg")
                                                            jux=juk.convert('RGB')

                                                        
                                                            jux=jux.rotate(-90,expand=True,fillcolor='white')

                                                            x66=jux.width
                                                            y66=jux.height
                                                            jux.save(PATH8+str(p)+".jpg")

                                                            self.canvas.iik=ImageTk.PhotoImage(jux)
                                                            self.canvas.create_image(self.arr2[p][0],self.yy1+20-y66,image=self.canvas.iik,anchor="nw")
                                                            self.canvas.delete(self.iid)
                                                            self.mylist.append(self.canvas.iik)
                                                            self.up_down[p]='U'
                                                            self.hor_ver[p]='H'
                                                            asa=1
                                                            print(299)
                                                            xe=self.arr2[p][3]-self.arr2[p][1]
                                                            self.arr2[p][1]=self.yy1-y66+20
                                                            self.arr2[p][2]=self.arr2[p][0]+x66
                                                            self.arr2[p][3]=self.yy1+20
                                                            self.arr2[p][4]=1
                                                            self.canvas.delete("blucol")

                                                        else:

                                                            self.canvas.move(self.iid,0,self.yy1-self.arr2[p][3]+20)
                                                            self.arr2[p][1]=self.arr2[p][1]+self.yy1-self.arr2[p][3]+20
                                                           
                                                            self.arr2[p][3]=self.yy1+20
                                                            self.arr2[p][4]=1 
                                                            self.canvas.delete("blucol")

                                            else:

                                                p0=self.arr2[p][0]
                                                p1=self.yy2+6-self.arr2[p][3]+self.arr2[p][1]
                                                p2=self.arr2[p][2]
                                                p3=self.yy2+6
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break



                                                xlxl=0
                                       

                                                messagebox.showerror("Error occured","Door cannot cross the dimension of the floorplan")
                                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                self.arr2[p][0]=self.r1
                                                self.arr2[p][1]=self.r2
                                                self.arr2[p][2]=self.r3
                                                self.arr2[p][3]=self.r4
                                                self.canvas.delete("blucol")


                                        if(self.up_down[p]=='D' or self.up_down[p]=='R'):


                                            if(self.h2-7 >=0 and self.yy1+self.arr2[p][3]-self.arr2[p][1] <= 715):

                                                p0=self.arr2[p][0]
                                                p1=self.h2-7
                                                p2=self.arr2[p][2]
                                                p3=self.h2-7+self.arr2[p][3]-self.arr2[p][1]
                                                ccc=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                    ccc=1
                                                                    break

                                                            if(ccc==1):
                                                                break


                                                xlxl=0
                                                for z1 in range(len(cfile['bbox_loc'])):
                                                    if(1):
                                                        if(self.room_doors2[z1]==0):
                                                            messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                            xlxl=1
                                                            for z2 in range(1000):
                                                                self.room_doors2[z2]=self.room_doors[z2]
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            self.canvas.delete("blucol")
                                                            break

                                                if(xlxl==0):

                                                    for z2 in range(1000):
                                                        self.room_doors[z2]=self.room_doors2[z2]

                                                    asa=0
                                                    for z2 in range(self.ro):
                                                        l5=Point(self.arr2[z2][0],self.arr2[z2][1])
                                                        d5=Point(self.arr2[z2][2],self.arr2[z2][3])
                                                        l6=Point(self.arr2[p][0],self.yy1-6)
                                                        d6=Point(self.arr2[p][2],self.yy1-6+self.arr2[p][3]-self.arr2[p][1])

                                                        if(self.doOverlap(l5,d5,l6,d6) and not(l6.x==0 and l6.y==0) and z2!=p and self.yy1+20-self.arr2[p][3]+self.arr2[p][1]<=0 and self.del_from_plan[z2]==0):
                                                            messagebox.showerror("Error occured","Door overlaps with the object")
                                                            asa=1
                                                            self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                            self.arr2[p][0]=self.r1
                                                            self.arr2[p][1]=self.r2
                                                            self.arr2[p][2]=self.r3
                                                            self.arr2[p][3]=self.r4
                                                            self.canvas.delete("blucol")
                                                            asa=1
                                                            break


                                                        if(self.doOverlap(l5,d5,l6,d6) and self.yy1+20-self.arr2[p][3]+self.arr2[p][1] >= 0 and z2!=p and self.del_from_plan[z2]==0):
                                                            #print(z2)
                                                            juk=Image.open(PATH8+str(p)+".jpg")
                                                            jux=juk.convert('RGB')
                                                            jux=ImageOps.flip(jux)
                                                            if(self.up_down[p]=='R'):
                                                                jux=jux.rotate(90,expand=True,fillcolor='white')
                                                            #if(self.up_down[p]=='D'):
                                                            jux=jux.rotate(-(2*self.theta),expand=True,fillcolor='white')

                                                            x66=jux.width
                                                            y66=jux.height
                                                            jux.save(PATH8+str(p)+".jpg")


                                                            if(self.main_doors_check[p]==0):
                                                                self.main_doors=self.main_doors+1
                                                                self.main_doors_check[p]=1
                                                            self.canvas.iik=ImageTk.PhotoImage(jux)
                                                            self.canvas.create_image(self.arr2[p][0],self.h2+20-y66,image=self.canvas.iik,anchor="nw")
                                                            self.canvas.delete(self.iid)
                                                            self.mylist.append(self.canvas.iik)
                                                            self.up_down[p]='U'
                                                            self.hor_ver[p]='H'
                                                            asa=1
                                                            
                                                            xe=self.arr2[p][3]-self.arr2[p][1]
                                                            self.arr2[p][1]=self.h2+20-y66
                                                            self.arr2[p][2]=self.arr2[p][0]+x66
                                                            self.arr2[p][3]=self.h2+20
                                                            self.arr2[p][4]=1
                                                            self.canvas.delete("blucol")
                                                            break

                                                    if(asa==0):


                                                        if(self.main_doors_check[p]==0):
                                                            self.main_doors=self.main_doors+1
                                                            self.main_doors_check[p]=1
                                                        if(self.up_down[p]=='R'):
                                                            juk=Image.open(PATH8+str(p)+".jpg")
                                                            jux=juk.convert('RGB')
                                                            jux=ImageOps.flip(jux)
                                                            
                                                            jux=jux.rotate(-90,expand=True,fillcolor='white')

                                                            x66=jux.width
                                                            y66=jux.height
                                                            jux.save(PATH8+str(p)+".jpg")

                                                            self.canvas.iik=ImageTk.PhotoImage(jux)
                                                            self.canvas.create_image(self.arr2[p][0],self.h2-26,image=self.canvas.iik,anchor="nw")
                                                            self.canvas.delete(self.iid)
                                                            self.mylist.append(self.canvas.iik)
                                                            self.up_down[p]='D'
                                                            self.hor_ver[p]='H'
                                                            
                                                            
                                                            xe=self.arr2[p][3]-self.arr2[p][1]
                                                            self.arr2[p][1]=self.h2-26
                                                            self.arr2[p][2]=self.arr2[p][0]+x66
                                                            self.arr2[p][3]=self.arr2[p][1]+y66
                                                            self.arr2[p][4]=1
                                                            self.canvas.delete("blucol")

                                                        else:

                                                            self.canvas.move(self.iid,0,self.h2-self.arr2[p][1]-7)
                                                            xe=self.arr2[p][3]-self.arr2[p][1]
                                                            self.arr2[p][1]=self.h2-7
                                                               
                                                            self.arr2[p][3]=xe+self.h2-7
                                                            self.arr2[p][4]=1 
                                                            self.canvas.delete("blucol")   
                                            else:
                                                zzp=0
                                                juk=Image.open(PATH8+str(p)+".jpg")
                                                jux=juk.convert('RGB')
                                                for y in range(self.ro):
                                                    l1=Point(self.arr2[y][0],self.arr2[y][1])
                                                    d1=Point(self.arr2[y][2],self.arr2[y][3])
                                                    l2=Point(self.arr2[p][0],self.yy1+15-jux.height)
                                                    d2=Point(self.arr2[p][2],self.yy1+15)

                                                    if(self.doOverlap(l1,d1,l2,d2) and l1.x!=0 and l1.y!=0 and y!=p and self.del_from_plan[y]==0):
                                                        zzp=1
                                                        self.canvas.delete("blucol")
                                                        break

                                                if(zzp==0):

                                                    p0=self.arr2[p][0]
                                                    p1=self.yy1+20-self.arr2[p][3]+self.arr2[p][1]
                                                    p2=self.arr2[p][2]
                                                    p3=self.yy1+20
                                                    ccc=0
                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                        
                                                        cchck=0

                                                        if(1):
                                                            for y111 in range(4):

                                                                
                                                                
                                                                if(y111==0):
                                                                    l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                    d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                if(y111==1):
                                                                    l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                    d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                if(y111==2):
                                                                    l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                    d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                if(y111==3):
                                                                    l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                    d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                for y112 in range(4):
                                                                    if(y112==0):
                                                                        l6=Point(p0,p1)
                                                                        d6=Point(p0,p3)
                                                                    if(y112==1):
                                                                        l6=Point(p0,p3)
                                                                        d6=Point(p2,p3)
                                                                    if(y112==2):
                                                                        l6=Point(p2,p3)
                                                                        d6=Point(p2,p1)
                                                                    if(y112==3):
                                                                        l6=Point(p2,p1)
                                                                        d6=Point(p0,p1)
                                              
                                                                    if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                        self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                        ccc=1
                                                                        break

                                                                if(ccc==1):
                                                                    break


                                                    xlxl=0
                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                        if(1):
                                                            if(self.room_doors2[z1]==0):
                                                                messagebox.showerror("Error Occured","Every room must have atleast one door")
                                                                xlxl=1
                                                                for z2 in range(1000):
                                                                    self.room_doors2[z2]=self.room_doors[z2]
                                                                self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                                self.arr2[p][0]=self.r1
                                                                self.arr2[p][1]=self.r2
                                                                self.arr2[p][2]=self.r3
                                                                self.arr2[p][3]=self.r4
                                                                self.canvas.delete("blucol")
                                                                break


                                                    if(xlxl==0):
                                                        for z2 in range(1000):
                                                            self.room_doors[z2]=self.room_doors2[z2]
                                                        juk=Image.open(PATH8+str(p)+".jpg")
                                                        jux=juk.convert('RGB')
                                                        jux=ImageOps.flip(jux)
                                                        if(self.up_down[p]=='R'):
                                                            jux=jux.rotate(90,expand=True,fillcolor='white')
                                                        #if(self.up_down[p]=='D'):
                                                        jux=jux.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                        x66=jux.width
                                                        y66=jux.height
                                                        jux.save(PATH8+str(p)+".jpg")


                                                        if(self.main_doors_check[p]==0):
                                                            self.main_doors=self.main_doors+1
                                                            self.main_doors_check[p]=1
                                                        self.canvas.iik=ImageTk.PhotoImage(jux)
                                                        self.canvas.create_image(self.arr2[p][0],self.yy1+20-y66,image=self.canvas.iik,anchor="nw")
                                                        self.canvas.delete(self.iid)
                                                        self.mylist.append(self.canvas.iik)
                                                        self.arr2[p][1]=self.yy1+20-y66
                                                        self.arr2[p][2]=self.arr2[p][0]+x66
                                                        self.arr2[p][3]=self.yy1+20
                                                        self.canvas.delete("blucol")

                                                        self.up_down[p]='U'
                                                        self.hor_ver[p]='H'


                                                if(zzp==1):

                                                    p0=self.a1
                                                    p1=self.a2
                                                    p2=self.a3
                                                    p3=self.a4
                                                    ccc=0
                                                    for z1 in range(len(cfile['bbox_loc'])):
                                                        
                                                        cchck=0

                                                        if(1):
                                                            for y111 in range(4):

                                                                
                                                                
                                                                if(y111==0):
                                                                    l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                    d5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                if(y111==1):
                                                                    l5=Point(self.roomcoord[z1][2],self.roomcoord[z1][3])
                                                                    d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                if(y111==2):
                                                                    l5=Point(self.roomcoord[z1][0],self.roomcoord[z1][1])
                                                                    d5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                if(y111==3):
                                                                    l5=Point(self.roomcoord[z1][4],self.roomcoord[z1][5])
                                                                    d5=Point(self.roomcoord[z1][6],self.roomcoord[z1][7])
                                                                for y112 in range(4):
                                                                    if(y112==0):
                                                                        l6=Point(p0,p1)
                                                                        d6=Point(p0,p3)
                                                                    if(y112==1):
                                                                        l6=Point(p0,p3)
                                                                        d6=Point(p2,p3)
                                                                    if(y112==2):
                                                                        l6=Point(p2,p3)
                                                                        d6=Point(p2,p1)
                                                                    if(y112==3):
                                                                        l6=Point(p2,p1)
                                                                        d6=Point(p0,p1)
                                              
                                                                    if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                        self.room_doors2[z1]=self.room_doors2[z1]+1
                                                                        ccc=1
                                                                        break

                                                                if(ccc==1):
                                                                    break



                                                    xlxl=0
                                            

                                                    messagebox.showerror("Error occured","Door cannot cross the dimension of the floorplan")
                                                    self.canvas.move(self.iid,self.a1-c0,self.a2-c1)
                                                    self.arr2[p][0]=self.r1
                                                    self.arr2[p][1]=self.r2
                                                    self.arr2[p][2]=self.r3
                                                    self.arr2[p][3]=self.r4
                                                    self.canvas.delete("blucol")



                    self.canvas.delete("blucol")
                    self.move_door_perm=0
                else:
                    if(c0<1270 and c1<700):
                        tpcc=0
                        self.yt=0
                        self.jki=0
                        c=self.ro
                        self.mylist.append(self.canvas.aimg)
                        self.arr2[c][0]=(c0-self.a1)+self.r1
                        self.arr2[c][1]=(c1-self.a2)+self.r2
                        self.arr2[c][2]=(c2-self.a3)+self.r3
                        self.arr2[c][3]=(c3-self.a4)+self.r4

                      


                        if(self.excep_fbox==1):
                            self.jki=1
                            self.arr2[c][4]=1

                            chch99=0
                            chc=0
                            self.yyy1=0
                            self.yyy2=0
                            self.yyy3=0

                            self.xxy1=0
                            self.xxy2=0
                            self.xxy3=0

                            self.first2=0
                            self.sec2=0

                            self.firstv2=0
                            self.secv2=0

                            gap1=0
                            gap2=0

                            gap3=0
                            gap4=0
                            tpcc=0


                            ccc=0
                            p0=self.arr2[c][0]
                            p1=self.arr2[c][1]
                            p2=self.arr2[c][2]
                            p3=self.arr2[c][3]



                            for y in range(len(cfile['bbox_loc'])):
                                
                                cchck=0
                                ccc=0

                                if(1):
                                    for y111 in range(4):

                                        
                                        
                                        if(y111==0):
                                            l5=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                            d5=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                        if(y111==1):
                                            l5=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                            d5=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                                        if(y111==2):
                                            l5=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                            d5=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                        if(y111==3):
                                            l5=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                            d5=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                                        for y112 in range(4):
                                            if(y112==0):
                                                l6=Point(p0,p1)
                                                d6=Point(p0,p3)
                                            if(y112==1):
                                                l6=Point(p0,p3)
                                                d6=Point(p2,p3)
                                            if(y112==2):
                                                l6=Point(p2,p3)
                                                d6=Point(p2,p1)
                                            if(y112==3):
                                                l6=Point(p2,p1)
                                                d6=Point(p0,p1)
                      
                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                ccc=1
                                                chck=chck+1
                                                chch99=chch99+1
                                                zz=0
                                                chc=0
                                                for z in range(4):
                                                    if(z==0):
                                                        l3=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                                        d3=Point(self.roomcoord3[y][2],self.roomcoord3[y][3]) 
                                                    if(z==1):
                                                        l3=Point(self.roomcoord3[y][2],self.roomcoord3[y][3])
                                                        d3=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                                    if(z==2):
                                                        l3=Point(self.roomcoord3[y][4],self.roomcoord3[y][5])
                                                        d3=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                                    if(z==3):
                                                        l3=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                                        d3=Point(self.roomcoord3[y][4],self.roomcoord3[y][5]) 
                                
                                                    l4=Point(self.arr2[c][0],self.arr2[c][1])
                                                    d4=Point(self.arr2[c][2],self.arr2[c][3])

                                                    if(l4.x<=l3.x and l3.x<=d4.x and (z==0 or z==2)):
                                                        self.hor_ver[c]='V'
                                                        chc=chc+1

                                                        if(chc>=2):
                                                            messagebox.showerror("Error Occured","Door cannot be placed there")
                                                            self.yt=1
                                                                    
                                                            self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                            self.canvas.delete("blucol")
                                                            tpcc=1
                                                            break


                                                        if((self.first2==1 and self.sec2==1) or (self.firstv2==1 and self.secv2==1)):
                                                            self.yt=1
                                                            messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                    
                                                            self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                            self.canvas.delete("blucol")
                                                            tpcc=1
                                                            break



                                                        if(chch99==1):
                                                            self.xxy1=l3.x
                                                            self.xxy3=self.xxy1
                                                            self.firstv2=1
                                                            gap3=abs(l4.x-l3.x)
                                                            gap4=abs(l3.x-d4.x)

                                                        else:
                                                            if(chch99==2):
                                                                self.xxy2=l3.x
                                                                self.secv2=1
                                                            else:
                                                                if(chch99>=3 or (self.xxy1!=0 and self.xxy2!=0) ):
                                                                    messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                    self.yt=1
                                                                    
                                                                    self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                    self.canvas.delete("blucol")
                                                                    tpcc=1
                                                                    break




                                                    if(l4.y<=l3.y and l3.y<=d4.y and (z==1 or z==3)):
                                                        self.hor_ver[c]='H'
                                                        chc=chc+1

                                                        if(chc>=2):
                                                            messagebox.showerror("Error Occured","Door cannot be placed there")
                                                            self.yt=1
                                                                    
                                                            self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                            self.canvas.delete("blucol")
                                                            tpcc=1
                                                            break

                                                        if(self.first2==1 and self.sec2==1):
                                                            messagebox.showerror("Error Occured","Door cannot be placed there")
                                                            self.yt=1
                                                                    
                                                            self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                            self.canvas.delete("blucol")
                                                            tpcc=1
                                                            break


                                                        if(chch99==1):
                                                            self.yyy1=l3.y
                                                            self.first2=1
                                                            self.yyy3=self.yyy1
                                                            gap1=abs(l4.y-l3.y)
                                                            gap2=abs(l3.y-d4.y)
                                                        else:
                                                            if(chch99==2):
                                                                self.yyy2=l3.y
                                                                self.sec2=1
                                                            else:
                                                                if(chch99>=3 or (self.yyy1!=0 and self.yyy2!=0) ):
                                                                    messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                    self.yt=1
                                                                    
                                                                    self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                    self.canvas.delete("blucol")
                                                                    tpcc=1
                                                                    break

                                                if(ccc==1):
                                                    break
                                            if(ccc==1):
                                                break
                                        if(ccc==1):
                                            break
                                    if(tpcc==1):
                                        break

                                                
                        


                        
                            if(tpcc==0):
                                if(self.firstv2==0 and self.first2==1):
                                    if(self.first2==1 and self.sec2==0):
                                        chch99=0
                                        chc=0
                                        self.yyy1=0
                                        self.yyy2=0
                                        self.first2=0
                                        self.sec2=0
                                        self.hh1=0
                                        self.hh2=0
                                        tpcc=0
                                        ui2=0

                                        c0=self.arr2[c][0]
                                        c1=self.arr2[c][1]
                                        c2=self.arr2[c][2]
                                        c3=self.arr2[c][3]

                                        for y in range(len(cfile['bbox_loc'])):
                                            chck=0
                                            ui2=0

                                            if(1):
                                                for y111 in range(4):

                                                                                                
                                                    if(y111==0):
                                                        l5=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                                        d5=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                                    if(y111==1):
                                                        l5=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                                        d5=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                                                    if(y111==2):
                                                        l5=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                                        d5=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                                    if(y111==3):
                                                        l5=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                                        d5=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                                                    for y112 in range(4):
                                                        if(y112==0):
                                                            if(gap1>gap2):
                                                                l6=Point(c0,c1+20)
                                                                d6=Point(c0,c3+20)
                                                            else:
                                                                l6=Point(c0,c1-20)
                                                                d6=Point(c0,c3-20)
                                                        if(y112==1):
                                                            if(gap1>gap2):
                                                                l6=Point(c0,c3+20)
                                                                d6=Point(c2,c3+20)
                                                            else:
                                                                l6=Point(c0,c3-20)
                                                                d6=Point(c2,c3-20)
                                                        if(y112==2):
                                                            if(gap1>gap2):
                                                                l6=Point(c2,c3+20)
                                                                d6=Point(c2,c1+20)
                                                            else:
                                                                l6=Point(c2,c3-20)
                                                                d6=Point(c2,c1-20)
                                                        if(y112==3):
                                                            if(gap1>gap2):
                                                                l6=Point(c2,c1+20)
                                                                d6=Point(c0,c1+20)
                                                            else:
                                                                l6=Point(c2,c1-20)
                                                                d6=Point(c0,c1-20)
                                  
                                                        if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):

                                                            ui2=1
                                                            chck=chck+1
                                                            chch99=chch99+1
                                                            zz=0
                                                            chc=0
                                                            for z in range(4):
                                                                if(z==0):
                                                                    l7=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                                                    d7=Point(self.roomcoord3[y][2],self.roomcoord3[y][3]) 
                                                                if(z==1):
                                                                    l7=Point(self.roomcoord3[y][2],self.roomcoord3[y][3])
                                                                    d7=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                                                if(z==2):
                                                                    l7=Point(self.roomcoord3[y][4],self.roomcoord3[y][5])
                                                                    d7=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                                                if(z==3):
                                                                    l7=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                                                    d7=Point(self.roomcoord3[y][4],self.roomcoord3[y][5]) 
                                            
                                                                l8=Point(0,0)
                                                                d8=Point(0,0)
                                                                if(gap1>gap2):
                                                                    l8=Point(self.arr2[c][0],self.arr2[c][1]+20)
                                                                    d8=Point(self.arr2[c][2],self.arr2[c][3]+20)
                                                                else:
                                                                    l8=Point(self.arr2[c][0],self.arr2[c][1]-20)
                                                                    d8=Point(self.arr2[c][2],self.arr2[c][3]-20)


                                                                if(l8.x<=l7.x and l7.x<=d8.x and (z==0 or z==2)):
                                                                    self.hor_ver[c]='V'
                                                                    chc=chc+1

                                                                    if(chc>=2):
                                                                        messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                        self.yt=1
                                                                                
                                                                        self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                        self.canvas.delete("blucol")
                                                                        tpcc=1
                                                                        break


                                                                    if((self.first2==1 and self.sec2==1) or (self.firstv2==1 and self.secv2==1)):
                                                                        messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                        self.yt=1
                                                                        self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                        self.canvas.delete("blucol")
                                                                        tpcc=1
                                                                        break



                                                                    if(chch99==1):
                                                                        self.xxy1=l7.x
                                                                        self.firstv2=1
                                                                        if(z==0):
                                                                            self.vv1=self.xxy1
                                                                        if(z==2):
                                                                            self.vv2=self.xxy1
                                                                    else:
                                                                        if(chch99==2):
                                                                            self.xxy2=l7.x
                                                                            self.secv2=1
                                                                        else:
                                                                            if(chch99>=3 or (self.xxy1!=0 and self.xxy2!=0) ):
                                                                                messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                                self.yt=1
                                                                                
                                                                                self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                                self.canvas.delete("blucol")
                                                                                tpcc=1
                                                                                break




                                                                if(l8.y<=l7.y and l7.y<=d8.y and (z==1 or z==3)):
                                                                    self.hor_ver[c]='H'
                                                                    chc=chc+1

                                                                    if(chc>=2):
                                                                        messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                        self.yt=1
                                                                                
                                                                        self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                        self.canvas.delete("blucol")
                                                                        tpcc=1
                                                                        break

                                                                    if(self.first2==1 and self.sec2==1):
                                                                        messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                        self.yt=1
                                                                                
                                                                        self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                        self.canvas.delete("blucol")
                                                                        tpcc=1
                                                                        break


                                                                    if(chch99==1):
                                                                        self.yyy1=l7.y
                                                                        self.first2=1
                                                                        if(z==1):
                                                                            self.hh1=self.yyy1


                                                                        if(z==3):
                                                                            self.hh2=self.yyy1
                                                                    else:
                                                                        if(chch99==2):
                                                                            self.yyy2=l7.y
                                                                            self.sec2=1
                                                                        else:
                                                                            if(chch99>=3 or (self.yyy1!=0 and self.yyy2!=0) ):
                                                                                messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                                self.yt=1
                                                                                
                                                                                self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                                self.canvas.delete("blucol")
                                                                                tpcc=1
                                                     
                                                                                break

                                                            if(tpcc==1):
                                                                break

                                                            if(ui2==1):
                                                                break

                                                    if(tpcc==1):
                                                        break

                                                    if(ui2==1):
                                                        break

                                            if(tpcc==1):
                                                break



                                    
                                    if(self.first2==0):
                                        self.yyy1=self.yyy3
                                        self.first2=1
                                        self.hh1=self.yyy1



                                    if(self.yyy2>self.yyy1 and self.sec2==1):
                                        #print(777)
                                        dfd=0
                                        efd=0
                                        cv=0
                                        for z1 in range(self.ro):
                                            l5=Point(self.arr2[z1][0],self.arr2[z1][1])
                                            d5=Point(self.arr2[z1][2],self.arr2[z1][3])
                                            l6=Point(self.arr2[c][0],self.yyy2-self.ha+5)
                                            d6=Point(self.arr2[c][2],self.yyy2+5)

                                            if(self.doOverlap(l5,d5,l6,d6) and not(l6.x==0 and l6.y==0) and z1!=c and self.del_from_plan[z1]==0):
                                                for z2 in range(self.ro):
                                                    l7=Point(self.arr2[z2][0],self.arr2[z2][1])
                                                    d7=Point(self.arr2[z2][2],self.arr2[z2][3])
                                                    #l8=Point(0,0)
                                                    #d8=Point(0,0)
                                                    #if(abs(self.arr2[c][1]-self.yyy1)>abs(self.yyy1-self.arr2[c][3])):
                                                    l8=Point(self.arr2[c][0],self.yyy1-7)
                                                    d8=Point(self.arr2[c][2],self.yyy1+self.ha-7)
                                                    #else:
                                                        #l8=Point(self.arr2[c][0],self.yyy1-7)
                                                        #d8=Point(self.arr2[c][2],self.yyy1+self.ha-7)
                                                        #cv=1

                                                    if(self.doOverlap(l7,d7,l8,d8) and not(l8.x==0 and l8.y==0) and z2!=c and self.del_from_plan[z2]==0):
                                                        efd=1
                                                        break
                                                dfd=1
                                                break



                                        if(dfd==0):
                                            ss=self.numindex
                                            jv=Image.open(PATH5+str(ss)+".tif")
                                            jv=jv.convert('RGB')
                                            jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                            jv.save(PATH8+str(c)+".jpg")
                                            self.canvas.move(self.iid,0,self.yyy2-self.ha+5-self.arr2[c][1])
                                            self.arr2[c][1]=self.yyy2-self.ha+5
                                            self.arr2[c][3]=self.yyy2+5
                                            self.hor_ver[c]='H'
                                            self.up_down[c]='U'

                                            p0=self.arr2[c][0]
                                            p1=self.arr2[c][1]
                                            p2=self.arr2[c][2]
                                            p3=self.arr2[c][3]
                                            ccc=0
                                            for z3 in range(len(cfile['bbox_loc'])):
                                                
                                                cchck=0

                                                if(1):
                                                    for y111 in range(4):

                                                        
                                                        
                                                        if(y111==0):
                                                            l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                            d5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                        if(y111==1):
                                                            l5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                            d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                        if(y111==2):
                                                            l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                            d5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                        if(y111==3):
                                                            l5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                            d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                        for y112 in range(4):
                                                            if(y112==0):
                                                                l6=Point(p0,p1)
                                                                d6=Point(p0,p3)
                                                            if(y112==1):
                                                                l6=Point(p0,p3)
                                                                d6=Point(p2,p3)
                                                            if(y112==2):
                                                                l6=Point(p2,p3)
                                                                d6=Point(p2,p1)
                                                            if(y112==3):
                                                                l6=Point(p2,p1)
                                                                d6=Point(p0,p1)
                                      
                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                self.room_doors2[z3]=self.room_doors2[z3]+1




                                        else:
                                            if(efd==0):
                                                ss=self.numindex
                                                jv=Image.open(PATH5+str(ss)+".tif")
                                                jv=jv.convert('RGB')
                                                jv=ImageOps.flip(jv)
                                                jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                jv.save(PATH8+str(c)+".jpg")
                                                self.canvas.uu=ImageTk.PhotoImage(jv)
                                                #if(cv==0):
                                                self.canvas.create_image(self.arr2[c][0],self.yyy1-7,image=self.canvas.uu,anchor="nw")
                                                self.canvas.delete(self.iid)
                                                self.mylist.append(self.canvas.uu)
                                                self.arr2[c][1]=self.yyy1-7
                                                self.arr2[c][3]=self.yyy1+self.ha-7
                                                self.hor_ver[c]='H'
                                                self.up_down[c]='D'

                                                p0=self.arr2[c][0]
                                                p1=self.arr2[c][1]
                                                p2=self.arr2[c][2]
                                                p3=self.arr2[c][3]
                                                ccc=0
                                                for z3 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                d5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                d5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z3]=self.room_doors2[z3]+1




                                            if(efd==1):
                                                messagebox.showerror("Error Occured","Door cannot be placed there")
                                                self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                self.yt=1
                                                self.canvas.delete("blucol")


                                                

                                    if(self.yyy1>self.yyy2 and self.sec2==1):
                                        sq=self.yyy1
                                        self.yyy1=self.yyy2
                                        self.yyy2=sq

                                        dfd=0
                                        efd=0
                                        for z1 in range(self.ro):
                                            l5=Point(self.arr2[z1][0],self.arr2[z1][1])
                                            d5=Point(self.arr2[z1][2],self.arr2[z1][3])
                                            l6=Point(self.arr2[c][0],self.yyy2-self.ha+5)
                                            d6=Point(self.arr2[c][2],self.yyy2+5)

                                            if(self.doOverlap(l5,d5,l6,d6) and not(l6.x==0 and l6.y==0) and z1!=c and self.del_from_plan[z1]==0):
                                                for z2 in range(self.ro):
                                                    l7=Point(self.arr2[z2][0],self.arr2[z2][1])
                                                    d7=Point(self.arr2[z2][2],self.arr2[z2][3])
                                                    l8=Point(0,0)
                                                    d8=Point(0,0)
                                                    #if(abs(self.arr2[c][1]-self.yyy1)>abs(self.yyy1-self.arr2[c][3])):
                                                    l8=Point(self.arr2[c][0],self.yyy1-7)
                                                    d8=Point(self.arr2[c][2],self.yyy1+self.ha-7)
                                                    #else:
                                                        #l8=Point(self.arr2[c][0],self.yyy2-self.ha+7)
                                                        #d8=Point(self.arr2[c][2],self.yyy2+7)


                                                    if(self.doOverlap(l7,d7,l8,d8) and not(l8.x==0 and l8.y==0) and z2!=c and self.del_from_plan[z2]==0):
                                                        efd=1
                                                        break
                                                dfd=1
                                                break



                                        if(dfd==0):
                                            
                                            ss=self.numindex
                                            jv=Image.open(PATH5+str(ss)+".tif")
                                            jv=jv.convert('RGB')
                                            jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                            jv.save(PATH8+str(c)+".jpg")
                                            self.canvas.move(self.iid,0,self.yyy2-self.ha+5-self.arr2[c][1])
                                            self.arr2[c][1]=self.yyy2-self.ha+5
                                            self.arr2[c][3]=self.yyy2+5
                                            self.hor_ver[c]='H'
                                            self.up_down[c]='U'
                                            p0=self.arr2[c][0]
                                            p1=self.arr2[c][1]
                                            p2=self.arr2[c][2]
                                            p3=self.arr2[c][3]
                                            ccc=0
                                            for z3 in range(len(cfile['bbox_loc'])):
                                                
                                                cchck=0

                                                if(1):
                                                    for y111 in range(4):

                                                        
                                                        
                                                        if(y111==0):
                                                            l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                            d5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                        if(y111==1):
                                                            l5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                            d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                        if(y111==2):
                                                            l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                            d5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                        if(y111==3):
                                                            l5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                            d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                        for y112 in range(4):
                                                            if(y112==0):
                                                                l6=Point(p0,p1)
                                                                d6=Point(p0,p3)
                                                            if(y112==1):
                                                                l6=Point(p0,p3)
                                                                d6=Point(p2,p3)
                                                            if(y112==2):
                                                                l6=Point(p2,p3)
                                                                d6=Point(p2,p1)
                                                            if(y112==3):
                                                                l6=Point(p2,p1)
                                                                d6=Point(p0,p1)
                                      
                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                self.room_doors2[z3]=self.room_doors2[z3]+1




                                        else:
                                            if(efd==0):
                                                
                                                ss=self.numindex
                                                jv=Image.open(PATH5+str(ss)+".tif")
                                                jv=jv.convert('RGB')
                                                jv=ImageOps.flip(jv)
                                                jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                jv.save(PATH8+str(c)+".jpg")
                                                self.canvas.uu=ImageTk.PhotoImage(jv)
                                                self.canvas.delete("blucol")
                                                #if(cv==0):
                                                self.canvas.create_image(self.arr2[c][0],self.yyy1-7,image=self.canvas.uu,anchor="nw")
                                                self.canvas.delete(self.iid)
                                                self.mylist.append(self.canvas.uu)
                                                self.arr2[c][1]=self.yyy1-7
                                                self.arr2[c][3]=self.yyy1+self.ha-7
                                                self.hor_ver[c]='H'
                                                self.up_down[c]='D'

                                                p0=self.arr2[c][0]
                                                p1=self.arr2[c][1]
                                                p2=self.arr2[c][2]
                                                p3=self.arr2[c][3]
                                                ccc=0
                                                for z3 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                d5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                d5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z3]=self.room_doors2[z3]+1


                                                if(efd==1):
                                                    self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                    messagebox.showerror("Error Occured","Door cannot be placed there")
                                                    self.yt=1
                                                    self.canvas.delete("blucol")
                                                



                                    if(self.first2==1 and self.sec2==0):
                                        if(self.yyy1==self.hh1):

                                            if(self.yyy1-self.ha >= 0):

                                                self.main_doors_check[c]=1
                                                self.main_doors=self.main_doors+1

                                                ss=self.numindex
                                                jv=Image.open(PATH5+str(ss)+".tif")
                                                jv=jv.convert('RGB')
                                                jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                jv.save(PATH8+str(c)+".jpg")


                                                self.canvas.iuy7=ImageTk.PhotoImage(jv)
                                                self.canvas.create_image(self.arr2[c][0],self.yyy1-15,image=self.canvas.iuy7,anchor="nw")
                                                self.mylist.append(self.canvas.iuy7)
                                                self.canvas.delete(self.iid)
                                                self.arr2[c][1]=self.yyy1-25
                                                self.arr2[c][3]=self.yyy1-25+self.ha


                                                #self.canvas.move(self.iid,0,self.yyy1-self.ha+7-self.arr2[c][1])
                                                #self.arr2[c][1]=self.yyy1-self.ha+7
                                                #self.arr2[c][3]=self.yyy1+7
                                                self.hor_ver[c]='H'
                                                self.up_down[c]='U'
                                                p0=self.arr2[c][0]
                                                p1=self.arr2[c][1]
                                                p2=self.arr2[c][2]
                                                p3=self.arr2[c][3]
                                                ccc=0
                                                for z3 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                d5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                            if(y111==1):
                                                                l5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                            if(y111==2):
                                                                l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                d5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                            if(y111==3):
                                                                l5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l6=Point(p0,p1)
                                                                    d6=Point(p0,p3)
                                                                if(y112==1):
                                                                    l6=Point(p0,p3)
                                                                    d6=Point(p2,p3)
                                                                if(y112==2):
                                                                    l6=Point(p2,p3)
                                                                    d6=Point(p2,p1)
                                                                if(y112==3):
                                                                    l6=Point(p2,p1)
                                                                    d6=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z3]=self.room_doors2[z3]+1


                                            else:
                                                yt=0
                                                for z2 in range(self.ro):
                                                    l1=Point(self.arr2[z2][0],self.arr2[z2][1])
                                                    d1=Point(self.arr2[z2][2],self.arr2[z2][3])
                                                    l2=Point(self.arr2[c][0],self.yyy1-15)
                                                    d2=Point(self.arr2[c][2],self.yyy1-15+self.ha)

                                                    if(self.doOverlap(l1,d1,l2,d2) and not(l2.x==0 and l2.y==0) and z2!=c and self.del_from_plan[z2]==0):
                                                        yt=1
                                                        self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                        messagebox.showerror("Error Occured","Door cannot cross the dimensions of floorplan")
                                                        self.canvas.delete("blucol")
                                                        self.yt=1
                                                        self.excep_fbox=0
                                                        break
                                                        


                                                if(yt==0):
                                                    self.main_doors_check[c]=1
                                                    self.main_doors=self.main_doors+1

                                                    ss=self.numindex
                                                    jv=Image.open(PATH5+str(ss)+".tif")
                                                    jv=jv.convert('RGB')
                                                    jv=ImageOps.flip(jv)
                                                    jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                    jv.save(PATH8+str(c)+".jpg")

                                                    self.canvas.iuy=ImageTk.PhotoImage(jv)
                                                    self.canvas.create_image(self.arr2[c][0],self.yyy1-25,image=self.canvas.iuy,anchor="nw")
                                                    self.mylist.append(self.canvas.iuy)
                                                    self.canvas.delete(self.iid)
                                                    self.arr2[c][1]=self.yyy1-25
                                                    self.arr2[c][3]=self.yyy1-25+self.ha

                                                    self.hor_ver[c]='H'
                                                    self.up_down[c]='D'

                                                    p0=self.arr2[c][0]
                                                    p1=self.arr2[c][1]
                                                    p2=self.arr2[c][2]
                                                    p3=self.arr2[c][3]
                                                    ccc=0
                                                    for z3 in range(len(cfile['bbox_loc'])):
                                                        
                                                        cchck=0

                                                        if(1):
                                                            for y111 in range(4):

                                                                
                                                                
                                                                if(y111==0):
                                                                    l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                    d5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                if(y111==1):
                                                                    l5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                    d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                if(y111==2):
                                                                    l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                    d5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                if(y111==3):
                                                                    l5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                    d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                for y112 in range(4):
                                                                    if(y112==0):
                                                                        l6=Point(p0,p1)
                                                                        d6=Point(p0,p3)
                                                                    if(y112==1):
                                                                        l6=Point(p0,p3)
                                                                        d6=Point(p2,p3)
                                                                    if(y112==2):
                                                                        l6=Point(p2,p3)
                                                                        d6=Point(p2,p1)
                                                                    if(y112==3):
                                                                        l6=Point(p2,p1)
                                                                        d6=Point(p0,p1)
                                              
                                                                    if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                        self.room_doors2[z3]=self.room_doors2[z3]+1





                                        if(self.yyy1==self.hh2):
                                            if(self.yyy1+5+self.ha <= 715):
                                            
                                                self.main_doors_check[c]=1
                                                self.main_doors=self.main_doors+1

                                                ss=self.numindex
                                                jv=Image.open(PATH5+str(ss)+".tif")
                                                jv=jv.convert('RGB')
                                                jv=ImageOps.flip(jv)
                                                jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                jv.save(PATH8+str(c)+".jpg")

                                                self.canvas.iuy=ImageTk.PhotoImage(jv)
                                                self.canvas.create_image(self.arr2[c][0],self.yyy1-38,image=self.canvas.iuy,anchor="nw")
                                                self.mylist.append(self.canvas.iuy)
                                                self.canvas.delete(self.iid)

                                                self.arr2[c][1]=self.yyy1-38
                                                self.arr2[c][3]=self.yyy1-38+self.ha
                                                self.hor_ver[c]='H'
                                                self.up_down[c]='D'
                                                p0=self.arr2[c][0]
                                                p1=self.arr2[c][1]
                                                p2=self.arr2[c][2]
                                                p3=self.arr2[c][3]
                                                ccc=0
                                                for z3 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                d9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                            if(y111==1):
                                                                l9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                            if(y111==2):
                                                                l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                d9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                            if(y111==3):
                                                                l9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l10=Point(p0,p1)
                                                                    d10=Point(p0,p3)
                                                                if(y112==1):
                                                                    l10=Point(p0,p3)
                                                                    d10=Point(p2,p3)
                                                                if(y112==2):
                                                                    l10=Point(p2,p3)
                                                                    d10=Point(p2,p1)
                                                                if(y112==3):
                                                                    l10=Point(p2,p1)
                                                                    d10=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l9,d9,l10,d10)) and (l10.x!=0) and (l10.y!=0) ):
                                                                    self.room_doors2[z3]=self.room_doors2[z3]+1




                                            else:
                                                self.yt=0
                                                for z2 in range(self.ro):
                                                    l1=Point(self.arr2[z2][0],self.arr2[z2][1])
                                                    d1=Point(self.arr2[z2][2],self.arr2[z2][3])
                                                    l2=Point(self.arr2[c][0],self.yyy1+20-self.ha)
                                                    d2=Point(self.arr2[c][2],self.yyy1+20)

                                                    if(self.doOverlap(l1,d1,l2,d2) and not(l2.x==0 and l2.y==0) and z2!=c and self.del_from_plan[z2]==0):
                                                        self.yt=1
                                                        self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                        messagebox.showerror("Error Occured","Door cannot cross the dimensions of floorplan")
                                                        self.canvas.delete("blucol")
                                                        self.yt=1
                                                        self.excep_fbox=0
                                            
                                                        break
                                                        


                                                if(self.yt==0):
                                            
                                                    self.main_doors_check[c]=1
                                                    self.main_doors=self.main_doors+1

                                                    ss=self.numindex
                                                    jv=Image.open(PATH5+str(ss)+".tif")
                                                    jv=jv.convert('RGB')
                                                    jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                    jv.save(PATH8+str(c)+".jpg")

                                                    self.canvas.iuy=ImageTk.PhotoImage(jv)
                                                    self.canvas.create_image(self.arr2[c][0],self.yyy1+20-self.ha,image=self.canvas.iuy,anchor="nw")
                                                    self.mylist.append(self.canvas.iuy)
                                                    self.canvas.delete(self.iid)
                                                    self.arr2[c][1]=self.yyy1+20-self.ha
                                                    self.arr2[c][3]=self.yyy1+20

                                                    self.hor_ver[c]='H'
                                                    self.up_down[c]='U'

                                                    p0=self.arr2[c][0]
                                                    p1=self.arr2[c][1]
                                                    p2=self.arr2[c][2]
                                                    p3=self.arr2[c][3]
                                                    ccc=0
                                                    for z3 in range(len(cfile['bbox_loc'])):
                                                        
                                                        cchck=0

                                                        if(1):
                                                            for y111 in range(4):

                                                                
                                                                
                                                                if(y111==0):
                                                                    l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                    d5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                if(y111==1):
                                                                    l5=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                    d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                if(y111==2):
                                                                    l5=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                    d5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                if(y111==3):
                                                                    l5=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                    d5=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                for y112 in range(4):
                                                                    if(y112==0):
                                                                        l6=Point(p0,p1)
                                                                        d6=Point(p0,p3)
                                                                    if(y112==1):
                                                                        l6=Point(p0,p3)
                                                                        d6=Point(p2,p3)
                                                                    if(y112==2):
                                                                        l6=Point(p2,p3)
                                                                        d6=Point(p2,p1)
                                                                    if(y112==3):
                                                                        l6=Point(p2,p1)
                                                                        d6=Point(p0,p1)
                                              
                                                                    if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                        self.room_doors2[z3]=self.room_doors2[z3]+1




                                else:
                                    if(self.firstv2==1 and self.first2==0):
                                        if(self.firstv2==1 and self.secv2==0):
                                            chch99=0
                                            chc=0
                                            self.xxy1=0
                                            self.xxy2=0
                                            self.firstv2=0
                                            self.secv2=0
                                            self.vv1=0
                                            self.vv2=0
                                            tpcc=0
                                            ui2=0

                                            c0=self.arr2[c][0]
                                            c1=self.arr2[c][1]
                                            c2=self.arr2[c][2]
                                            c3=self.arr2[c][3]

                                            for y in range(len(cfile['bbox_loc'])):
                                                chck=0
                                                ui2=0

                                                if(1):
                                                    for y111 in range(4):

                                                                                                    
                                                        if(y111==0):
                                                            l5=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                                            d5=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                                        if(y111==1):
                                                            l5=Point(self.roomcoord[y][2],self.roomcoord[y][3])
                                                            d5=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                                                        if(y111==2):
                                                            l5=Point(self.roomcoord[y][0],self.roomcoord[y][1])
                                                            d5=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                                        if(y111==3):
                                                            l5=Point(self.roomcoord[y][4],self.roomcoord[y][5])
                                                            d5=Point(self.roomcoord[y][6],self.roomcoord[y][7])
                                                        for y112 in range(4):
                                                            if(y112==0):
                                                                if(gap3>gap4):
                                                                    l6=Point(c0+20,c1)
                                                                    d6=Point(c0+20,c3)
                                                                else:
                                                                    l6=Point(c0-20,c1)
                                                                    d6=Point(c0-20,c3)
                                                            if(y112==1):
                                                                if(gap3>gap4):
                                                                    l6=Point(c0+20,c3)
                                                                    d6=Point(c2+20,c3)
                                                                else:
                                                                    l6=Point(c0-20,c3)
                                                                    d6=Point(c2-20,c3)
                                                            if(y112==2):
                                                                if(gap3>gap4):
                                                                    l6=Point(c2+20,c3)
                                                                    d6=Point(c2+20,c1)
                                                                else:
                                                                    l6=Point(c2-20,c3)
                                                                    d6=Point(c2-20,c1)
                                                            if(y112==3):
                                                                if(gap3>gap4):
                                                                    l6=Point(c2+20,c1)
                                                                    d6=Point(c0+20,c1)
                                                                else:
                                                                    l6=Point(c2-20,c1)
                                                                    d6=Point(c0-20,c1)
                                      
                                                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                chck=chck+1
                                                                ui2=1
                                                                chch99=chch99+1
                                                                zz=0
                                                                chc=0
                                                                for z in range(4):
                                                                    if(z==0):
                                                                        l7=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                                                        d7=Point(self.roomcoord3[y][2],self.roomcoord3[y][3]) 
                                                                    if(z==1):
                                                                        l7=Point(self.roomcoord3[y][2],self.roomcoord3[y][3])
                                                                        d7=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                                                    if(z==2):
                                                                        l7=Point(self.roomcoord3[y][4],self.roomcoord3[y][5])
                                                                        d7=Point(self.roomcoord3[y][6],self.roomcoord3[y][7]) 
                                                                    if(z==3):
                                                                        l7=Point(self.roomcoord3[y][0],self.roomcoord3[y][1])
                                                                        d7=Point(self.roomcoord3[y][4],self.roomcoord3[y][5]) 
                                                
                                                                    l8=Point(0,0)
                                                                    d8=Point(0,0)
                                                                    if(gap3>gap4):
                                                                        l8=Point(self.arr2[c][0]+20,self.arr2[c][1])
                                                                        d8=Point(self.arr2[c][2]+20,self.arr2[c][3])
                                                                    else:
                                                                        l8=Point(self.arr2[c][0]-20,self.arr2[c][1])
                                                                        d8=Point(self.arr2[c][2]-20,self.arr2[c][3])


                                                                    if(l8.x<=l7.x and l7.x<=d8.x and (z==0 or z==2)):
                                                                        self.hor_ver[c]='V'
                                                                        chc=chc+1

                                                                        if(chc>=2):
                                                                            messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                            self.yt=1
                                                                                    
                                                                            self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                            self.canvas.delete("blucol")
                                                                            tpcc=1
                                                                            break


                                                                        if((self.first2==1 and self.sec2==1) or (self.firstv2==1 and self.secv2==1)):
                                                                            messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                            self.yt=1
                                                                                    
                                                                            self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                            self.canvas.delete("blucol")
                                                                            tpcc=1
                                                                            break



                                                                        if(chch99==1):
                                                                            self.xxy1=l7.x
                                                                            self.firstv2=1
                                                                            if(z==0):
                                                                                self.vv1=self.xxy1
                                                                            if(z==2):
                                                                                self.vv2=self.xxy1
                                                                        else:
                                                                            if(chch99==2):
                                                                                self.xxy2=l7.x
                                                                                self.secv2=1
                                                                            else:
                                                                                if(chch99>=3 or (self.xxy1!=0 and self.xxy2!=0) ):
                                                                                    messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                                    self.yt=1
                                                                                    self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                                    self.canvas.delete("blucol")
                                                                                    tpcc=1
                                                                                    break




                                                                    if(l8.y<=l7.y and l7.y<=d8.y and (z==1 or z==3)):
                                                                        self.hor_ver[c]='H'
                                                                        chc=chc+1

                                                                        if(chc>=2):
                                                                            messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                            self.yt=1
                                                                                    
                                                                            self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                            self.canvas.delete("blucol")
                                                                            tpcc=1
                                                                            break

                                                                        if(self.first2==1 and self.sec2==1):
                                                                            messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                            self.yt=1
                                                                                    
                                                                            self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                            self.canvas.delete("blucol")
                                                                            tpcc=1
                                                                            break


                                                                        if(chch99==1):
                                                                            self.yyy1=l7.y
                                                                            self.first2=1
                                                                            if(z==1):
                                                                                self.hh1=self.yyy1
                                                                            if(z==3):
                                                                                self.hh2=self.yyy1
                                                                        else:
                                                                            if(chch99==2):
                                                                                self.yyy2=l7.y
                                                                                self.sec2=1
                                                                            else:
                                                                                if(chch99>=3 or (self.yyy1!=0 and self.yyy2!=0) ):
                                                                                    messagebox.showerror("Error Occured","Door cannot be placed there")
                                                                                    self.yt=1
                                                                                    
                                                                                    self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                                                    self.canvas.delete("blucol")
                                                                                    tpcc=1
                                                                                    break

                                                                if(tpcc==1):
                                                                    break

                                                                if(ui2==1):
                                                                    break

                                                        if(tpcc==1):
                                                            break

                                                        if(ui2==1):
                                                            break

                                                    if(tpcc==1):
                                                        break

                                                        


                                        
                                        if(self.firstv2==0):
                                            self.xxy1=self.xxy3
                                            self.firstv2=1
                                            self.vv1=self.xxy1



                                        if(self.xxy2>self.xxy1 and self.secv2==1):
                                        
                                            #print(777)
                                            dfd=0
                                            efd=0
                                            cv=0
                                            for z1 in range(self.ro):
                                                l5=Point(self.arr2[z1][0],self.arr2[z1][1])
                                                d5=Point(self.arr2[z1][2],self.arr2[z1][3])
                                                l6=Point(self.xxy2-self.na+5,self.arr2[c][1])
                                                d6=Point(self.xxy2+5,self.arr2[c][3])

                                                if(self.doOverlap(l5,d5,l6,d6) and not(l6.x==0 and l6.y==0) and z1!=c and self.del_from_plan[z1]==0):
                                                    for z2 in range(self.ro):
                                                        l7=Point(self.arr2[z2][0],self.arr2[z2][1])
                                                        d7=Point(self.arr2[z2][2],self.arr2[z2][3])
                                                        #l8=Point(0,0)
                                                        #d8=Point(0,0)
                                                        #if(abs(self.arr2[c][0]-self.xxy1)>abs(self.xxy1-self.arr2[c][2])):
                                                        l8=Point(self.xxy1-7,self.arr2[c][1])
                                                        d8=Point(self.xxy1+self.na-7,self.arr2[c][3])
                                                        #else:
                                                         #   l8=Point(self.xxy2-self.na+7,self.arr2[c][1])
                                                          #  d8=Point(self.xxy2+7,self.arr2[c][3])
                                                           # cv=1

                                                        if(self.doOverlap(l7,d7,l8,d8) and not(l8.x==0 and l8.y==0) and z2!=c and self.del_from_plan[z2]==0):
                                                            efd=1
                                                            break
                                                    dfd=1
                                                    break



                                            if(dfd==0):
                                                ss=self.numindex
                                                jv=Image.open(PATH5+str(ss)+".tif")
                                                jv=jv.convert('RGB')
                                                jv=jv.rotate(90,expand=True,fillcolor='white')
                                                jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                self.ha=jv.height
                                                self.na=jv.width
                                                jv.save(PATH8+str(c)+".jpg")
                                                self.canvas.iop=ImageTk.PhotoImage(jv)
                                                self.canvas.create_image(self.xxy2-self.na+5,self.arr2[c][1],image=self.canvas.iop,anchor="nw")
                                                self.canvas.delete(self.iid)
                                                self.mylist.append(self.canvas.iop)
                                                
                                                #self.canvas.move(self.iid,self.xxy2-self.na+5-self.arr2[c][0],0)

                                                self.arr2[c][0]=self.xxy2-self.na+5
                                                self.arr2[c][2]=self.xxy2+5
                                                self.hor_ver[c]='V'
                                                self.up_down[c]='L'
                                                p0=self.arr2[c][0]
                                                p1=self.arr2[c][1]
                                                p2=self.arr2[c][2]
                                                p3=self.arr2[c][3]
                                                ccc=0
                                                for z3 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                d9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                            if(y111==1):
                                                                l9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                            if(y111==2):
                                                                l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                d9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                            if(y111==3):
                                                                l9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l10=Point(p0,p1)
                                                                    d10=Point(p0,p3)
                                                                if(y112==1):
                                                                    l10=Point(p0,p3)
                                                                    d10=Point(p2,p3)
                                                                if(y112==2):
                                                                    l10=Point(p2,p3)
                                                                    d10=Point(p2,p1)
                                                                if(y112==3):
                                                                    l10=Point(p2,p1)
                                                                    d10=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z3]=self.room_doors2[z3]+1



                                            else:
                                                if(efd==0):
                                                    ss=self.numindex
                                                    jv=Image.open(PATH5+str(ss)+".tif")
                                                    jv=jv.convert('RGB')
                                                    #jv=ImageOps.flip(jv)

                                                    #if(cv==0):
                                                        
                                                    jv=jv.rotate(-90,expand=True,fillcolor='white')
                                                    jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                    self.na=jv.width
                                                    self.ha=jv.height
                                                    jv.save(PATH8+str(c)+".jpg")
                                                    self.canvas.uu=ImageTk.PhotoImage(jv)
                                                    self.canvas.create_image(self.xxy1-7,self.arr2[c][1],image=self.canvas.uu,anchor="nw")
                                                    self.canvas.delete(self.iid)
                                                    self.mylist.append(self.canvas.uu)
                                                    self.arr2[c][0]=self.xxy1-7
                                                    self.arr2[c][2]=self.xxy1+self.na-7
                                                    self.hor_ver[c]='V'
                                                    self.up_down[c]='R'

                                                    p0=self.arr2[c][0]
                                                    p1=self.arr2[c][1]
                                                    p2=self.arr2[c][2]
                                                    p3=self.arr2[c][3]
                                                    ccc=0
                                                    for z3 in range(len(cfile['bbox_loc'])):
                                                        
                                                        cchck=0

                                                        if(1):
                                                            for y111 in range(4):

                                                                
                                                                
                                                                if(y111==0):
                                                                    l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                    d9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                if(y111==1):
                                                                    l9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                    d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                if(y111==2):
                                                                    l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                    d9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                if(y111==3):
                                                                    l9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                    d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                for y112 in range(4):
                                                                    if(y112==0):
                                                                        l10=Point(p0,p1)
                                                                        d10=Point(p0,p3)
                                                                    if(y112==1):
                                                                        l10=Point(p0,p3)
                                                                        d10=Point(p2,p3)
                                                                    if(y112==2):
                                                                        l10=Point(p2,p3)
                                                                        d10=Point(p2,p1)
                                                                    if(y112==3):
                                                                        l10=Point(p2,p1)
                                                                        d10=Point(p0,p1)
                                              
                                                                    if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                        self.room_doors2[z3]=self.room_doors2[z3]+1

                                                if(efd==1):
                                                    self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                    messagebox.showerror("Error Occured","Door cannot be placed there")
                                                    self.yt=1
                                                    self.canvas.delete("blucol")
                                                    

                                        if(self.xxy1>self.xxy2 and self.secv2==1):
                                            sq=self.xxy1
                                            self.xxy1=self.xxy2
                                            self.xxy2=sq

                                            dfd=0
                                            efd=0
                                            for z1 in range(self.ro):
                                                l5=Point(self.arr2[z1][0],self.arr2[z1][1])
                                                d5=Point(self.arr2[z1][2],self.arr2[z1][3])
                                                l6=Point(self.xxy2-self.na+5,self.arr2[c][1])
                                                d6=Point(self.xxy2+5,self.arr2[c][3])

                                                if(self.doOverlap(l5,d5,l6,d6) and not(l6.x==0 and l6.y==0) and z1!=c and self.del_from_plan[z1]==0):
                                                    for z2 in range(self.ro):
                                                        l7=Point(self.arr2[z2][0],self.arr2[z2][1])
                                                        d7=Point(self.arr2[z2][2],self.arr2[z2][3])
                                                        #l8=Point(0,0)
                                                        #d8=Point(0,0)
                                                        #if(abs(self.arr2[c][0]-self.xxy1)>abs(self.xxy1-self.arr2[c][2])):
                                                        l8=Point(self.xxy1-7,self.arr2[c][1])
                                                        d8=Point(self.xxy1+self.na-7,self.arr2[c][3])
                                                        #else:
                                                         #   l8=Point(self.xxy2-self.na+7,self.arr2[c][1])
                                                          #  d8=Point(self.xxy2+7,self.arr2[c][3])


                                                        if(self.doOverlap(l7,d7,l8,d8) and not(l8.x==0 and l8.y==0) and z2!=c and self.del_from_plan[z2]==0):
                                                            efd=1
                                                            break
                                                    dfd=1
                                                    break



                                            if(dfd==0):
                                                
                                                ss=self.numindex
                                                jv=Image.open(PATH5+str(ss)+".tif")
                                                jv=jv.convert('RGB')
                                                jv=jv.rotate(90,expand=True,fillcolor='white')
                                                jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                self.na=jv.width
                                                self.ha=jv.height
                                                jv.save(PATH8+str(c)+".jpg")
                                                self.canvas.oip=ImageTk.PhotoImage(jv)
                                                self.canvas.create_image(self.xxy2-self.na+5,self.arr2[c][1],image=self.canvas.oip,anchor="nw")
                                                self.canvas.delete(self.iid)
                                                self.mylist.append(self.canvas.oip)
                                                #self.canvas.move(self.iid,self.xxy2-self.na+5-self.arr2[c][0],0)
                                                self.arr2[c][0]=self.xxy2-self.na+5
                                                self.arr2[c][2]=self.xxy2+5
                                                self.hor_ver[c]='V'
                                                self.up_down[c]='L'
                                                p0=self.arr2[c][0]
                                                p1=self.arr2[c][1]
                                                p2=self.arr2[c][2]
                                                p3=self.arr2[c][3]
                                                ccc=0
                                                for z3 in range(len(cfile['bbox_loc'])):
                                                    
                                                    cchck=0

                                                    if(1):
                                                        for y111 in range(4):

                                                            
                                                            
                                                            if(y111==0):
                                                                l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                d9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                            if(y111==1):
                                                                l9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                            if(y111==2):
                                                                l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                d9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                            if(y111==3):
                                                                l9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                            for y112 in range(4):
                                                                if(y112==0):
                                                                    l10=Point(p0,p1)
                                                                    d10=Point(p0,p3)
                                                                if(y112==1):
                                                                    l10=Point(p0,p3)
                                                                    d10=Point(p2,p3)
                                                                if(y112==2):
                                                                    l10=Point(p2,p3)
                                                                    d10=Point(p2,p1)
                                                                if(y112==3):
                                                                    l10=Point(p2,p1)
                                                                    d10=Point(p0,p1)
                                          
                                                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                    self.room_doors2[z3]=self.room_doors2[z3]+1


                                            else:
                                                if(efd==0):
                                                    
                                                    ss=self.numindex
                                                    jv=Image.open(PATH5+str(ss)+".tif")
                                                    jv=jv.convert('RGB')
                                                    #jv=ImageOps.flip(jv)

                                                    #if(cv==0):
                                                    jv=jv.rotate(-90,expand=True,fillcolor='white')
                                                    jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                    self.na=jv.width
                                                    self.ha=jv.height
                                                    jv.save(PATH8+str(c)+".jpg")
                                                    self.canvas.uu=ImageTk.PhotoImage(jv)
                                                    self.canvas.delete("blucol")
                                                    self.canvas.create_image(self.xxy1-7,self.arr2[c][1],image=self.canvas.uu,anchor="nw")
                                                    self.canvas.delete(self.iid)
                                                    self.mylist.append(self.canvas.uu)
                                                    self.arr2[c][0]=self.xxy1-7
                                                    self.arr2[c][2]=self.xxy1+self.na-7
                                                    self.hor_ver[c]='V'
                                                    self.up_down[c]='R'
                                                    p0=self.arr2[c][0]
                                                    p1=self.arr2[c][1]
                                                    p2=self.arr2[c][2]
                                                    p3=self.arr2[c][3]
                                                    ccc=0
                                                    for z3 in range(len(cfile['bbox_loc'])):
                                                        
                                                        cchck=0

                                                        if(1):
                                                            for y111 in range(4):

                                                                
                                                                
                                                                if(y111==0):
                                                                    l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                    d9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                if(y111==1):
                                                                    l9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                    d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                if(y111==2):
                                                                    l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                    d9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                if(y111==3):
                                                                    l9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                    d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                for y112 in range(4):
                                                                    if(y112==0):
                                                                        l10=Point(p0,p1)
                                                                        d10=Point(p0,p3)
                                                                    if(y112==1):
                                                                        l10=Point(p0,p3)
                                                                        d10=Point(p2,p3)
                                                                    if(y112==2):
                                                                        l10=Point(p2,p3)
                                                                        d10=Point(p2,p1)
                                                                    if(y112==3):
                                                                        l10=Point(p2,p1)
                                                                        d10=Point(p0,p1)
                                              
                                                                    if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                        self.room_doors2[z3]=self.room_doors2[z3]+1

                                                if(efd==1):
                                                    messagebox.showerror("Error Occured","Door cannot be placed there")
                                                    self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                    self.yt=1
                                                    self.canvas.delete("blucol")
                                                   


                                        #print(self.firstv2,self.secv2,self.xxy1,self.vv1,self.vv2)

                                        if(self.firstv2==1 and self.secv2==0):
                                            if(self.xxy1==self.vv1):

                                                if(self.xxy1-self.na >= 0):
                                                    self.main_doors_check[c]=1
                                                    self.main_doors=self.main_doors+1
                                                    ss=self.numindex
                                                    jv=Image.open(PATH5+str(ss)+".tif")
                                                    jv=jv.convert('RGB')
                                                    jv=jv.rotate(90,expand=True,fillcolor='white')
                                                    jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                    self.na=jv.width
                                                    self.ha=jv.height
                                                    jv.save(PATH8+str(c)+".jpg")
                                                    self.canvas.oip=ImageTk.PhotoImage(jv)
                                                    self.canvas.create_image(self.xxy1-self.na+7,self.arr2[c][1],image=self.canvas.oip,anchor="nw")
                                                    self.canvas.delete(self.iid)
                                                    self.mylist.append(self.canvas.oip)

                                                    #jv.save(PATH8+str(c)+".jpg")

                                                    #self.canvas.move(self.iid,0,self.yyy1-self.ha+7-self.arr2[c][1])
                                                    self.arr2[c][0]=self.xxy1-self.na+7
                                                    self.arr2[c][2]=self.xxy1+7
                                                    self.hor_ver[c]='V'
                                                    self.up_down[c]='L'
                                                    p0=self.arr2[c][0]
                                                    p1=self.arr2[c][1]
                                                    p2=self.arr2[c][2]
                                                    p3=self.arr2[c][3]
                                                    ccc=0
                                                    for z3 in range(len(cfile['bbox_loc'])):
                                                        
                                                        cchck=0

                                                        if(1):
                                                            for y111 in range(4):

                                                                
                                                                
                                                                if(y111==0):
                                                                    l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                    d9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                if(y111==1):
                                                                    l9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                    d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                if(y111==2):
                                                                    l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                    d9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                if(y111==3):
                                                                    l9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                    d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                for y112 in range(4):
                                                                    if(y112==0):
                                                                        l10=Point(p0,p1)
                                                                        d10=Point(p0,p3)
                                                                    if(y112==1):
                                                                        l10=Point(p0,p3)
                                                                        d10=Point(p2,p3)
                                                                    if(y112==2):
                                                                        l10=Point(p2,p3)
                                                                        d10=Point(p2,p1)
                                                                    if(y112==3):
                                                                        l10=Point(p2,p1)
                                                                        d10=Point(p0,p1)
                                              
                                                                    if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                        self.room_doors2[z3]=self.room_doors2[z3]+1


                                            

                                                else:
                                                    self.yt=0
                                                    for z2 in range(self.ro):
                                                        l1=Point(self.arr2[z2][0],self.arr2[z2][1])
                                                        d1=Point(self.arr2[z2][2],self.arr2[z2][3])
                                                        l2=Point(self.xxy1-15,self.arr2[c][1])
                                                        d2=Point(self.xxy1-15+self.na,self.arr2[c][3])

                                                        if(self.doOverlap(l1,d1,l2,d2) and not(l2.x==0 and l2.y==0) and z2!=c and self.del_from_plan[z2]==0):
                                                            self.yt=1
                                                            self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                            messagebox.showerror("Error Occured","Door cannot cross the dimensions of floorplan")
                                                            self.canvas.delete("blucol")
                                                            self.excep_fbox=0
                                                            break
                                                            


                                                    if(self.yt==0):

                                                        self.main_doors_check[c]=1
                                                        self.main_doors=self.main_doors+1
                                                        ss=self.numindex
                                                        jv=Image.open(PATH5+str(ss)+".tif")
                                                        jv=jv.convert('RGB')
                                                        jv=jv.rotate(-90,expand=True,fillcolor='white')
                                                        jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                        self.na=jv.width
                                                        self.ha=jv.height
                                                        #jv=ImageOps.flip(jv)
                                                        jv.save(PATH8+str(c)+".jpg")
                                                        self.canvas.iuy=ImageTk.PhotoImage(jv)
                                                        self.canvas.create_image(self.xxy1-15,self.arr2[c][1],image=self.canvas.iuy,anchor="nw")
                                                        self.mylist.append(self.canvas.iuy)
                                                        self.canvas.delete(self.iid)
                                                        self.arr2[c][0]=self.xxy1-15
                                                        self.arr2[c][2]=self.xxy1-15+self.na

                                                        self.hor_ver[c]='V'
                                                        self.up_down[c]='R'
                                                        p0=self.arr2[c][0]
                                                        p1=self.arr2[c][1]
                                                        p2=self.arr2[c][2]
                                                        p3=self.arr2[c][3]
                                                        ccc=0
                                                        for z3 in range(len(cfile['bbox_loc'])):
                                                            
                                                            cchck=0

                                                            if(1):
                                                                for y111 in range(4):

                                                                    
                                                                    
                                                                    if(y111==0):
                                                                        l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                        d9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                    if(y111==1):
                                                                        l9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                        d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                    if(y111==2):
                                                                        l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                        d9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                    if(y111==3):
                                                                        l9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                        d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                    for y112 in range(4):
                                                                        if(y112==0):
                                                                            l10=Point(p0,p1)
                                                                            d10=Point(p0,p3)
                                                                        if(y112==1):
                                                                            l10=Point(p0,p3)
                                                                            d10=Point(p2,p3)
                                                                        if(y112==2):
                                                                            l10=Point(p2,p3)
                                                                            d10=Point(p2,p1)
                                                                        if(y112==3):
                                                                            l10=Point(p2,p1)
                                                                            d10=Point(p0,p1)
                                                  
                                                                        if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                            self.room_doors2[z3]=self.room_doors2[z3]+1



                                            if(self.xxy1==self.vv2):
                                                if(self.xxy1+5+self.na <= 1285):
                                                

                                                    self.main_doors_check[c]=1
                                                    self.main_doors=self.main_doors+1                                                
                                                    ss=self.numindex
                                                    jv=Image.open(PATH5+str(ss)+".tif")
                                                    jv=jv.convert('RGB')
                                                    jv=jv.rotate(-90,expand=True,fillcolor='white')
                                                    jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                    self.na=jv.width
                                                    self.ha=jv.height
                                                    #jv=ImageOps.flip(jv)
                                                    jv.save(PATH8+str(c)+".jpg")
                                                    self.canvas.iuy=ImageTk.PhotoImage(jv)
                                                    self.canvas.create_image(self.xxy1-5,self.arr2[c][1],image=self.canvas.iuy,anchor="nw")
                                                    self.mylist.append(self.canvas.iuy)
                                                    self.canvas.delete(self.iid)

                                                    self.arr2[c][0]=self.xxy1-5
                                                    self.arr2[c][2]=self.xxy1-5+self.na
                                                    self.hor_ver[c]='V'
                                                    self.up_down[c]='R'
                                                    p0=self.arr2[c][0]
                                                    p1=self.arr2[c][1]
                                                    p2=self.arr2[c][2]
                                                    p3=self.arr2[c][3]
                                                    ccc=0
                                                    for z3 in range(len(cfile['bbox_loc'])):
                                                        
                                                        cchck=0

                                                        if(1):
                                                            for y111 in range(4):

                                                                
                                                                
                                                                if(y111==0):
                                                                    l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                    d9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                if(y111==1):
                                                                    l9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                    d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                if(y111==2):
                                                                    l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                    d9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                if(y111==3):
                                                                    l9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                    d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                for y112 in range(4):
                                                                    if(y112==0):
                                                                        l10=Point(p0,p1)
                                                                        d10=Point(p0,p3)
                                                                    if(y112==1):
                                                                        l10=Point(p0,p3)
                                                                        d10=Point(p2,p3)
                                                                    if(y112==2):
                                                                        l10=Point(p2,p3)
                                                                        d10=Point(p2,p1)
                                                                    if(y112==3):
                                                                        l10=Point(p2,p1)
                                                                        d10=Point(p0,p1)
                                              
                                                                    if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                        self.room_doors2[z3]=self.room_doors2[z3]+1

                                                else:
                                                    self.yt=0
                                                    for z2 in range(self.ro):
                                                        l1=Point(self.arr2[z2][0],self.arr2[z2][1])
                                                        d1=Point(self.arr2[z2][2],self.arr2[z2][3])
                                                        l2=Point(self.xxy1+20-self.na,self.arr2[c][1])
                                                        d2=Point(self.xxy1+20,self.arr2[c][3])

                                                        if(self.doOverlap(l1,d1,l2,d2) and not(l2.x==0 and l2.y==0) and z2!=c and self.del_from_plan[z2]==0):
                                                            self.yt=1
                                                            self.canvas.move(self.iid,self.a1-self.arr2[c][0],self.a2-self.arr2[c][1])
                                                            messagebox.showerror("Error Occured","Door cannot cross the dimensions of floorplan")
                                                            self.canvas.delete("blucol")
                                                            self.excep_fbox=0
                                                
                                                            break
                                                            


                                                    if(self.yt==0):

                                                        self.main_doors_check[c]=1
                                                        self.main_doors=self.main_doors+1
                                                        ss=self.numindex
                                                        jv=Image.open(PATH5+str(ss)+".tif")
                                                        jv=jv.convert('RGB')
                                                        jv=jv.rotate(90,expand=True,fillcolor='white')
                                                        jv=jv.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                                        self.na=jv.width
                                                        self.ha=jv.height
                                                        jv.save(PATH8+str(c)+".jpg")

                                                        self.canvas.iuy=ImageTk.PhotoImage(jv)
                                                        self.canvas.create_image(self.xxy1+20-self.na,self.arr2[c][1],image=self.canvas.iuy,anchor="nw")
                                                        self.mylist.append(self.canvas.iuy)
                                                        self.canvas.delete(self.iid)
                                                        self.arr2[c][0]=self.xxy1+20-self.na
                                                        self.arr2[c][2]=self.xxy1+20

                                                        self.hor_ver[c]='V'
                                                        self.up_down[c]='L'
                                                        p0=self.arr2[c][0]
                                                        p1=self.arr2[c][1]
                                                        p2=self.arr2[c][2]
                                                        p3=self.arr2[c][3]
                                                        ccc=0
                                                        for z3 in range(len(cfile['bbox_loc'])):
                                                            
                                                            cchck=0

                                                            if(1):
                                                                for y111 in range(4):

                                                                    
                                                                    
                                                                    if(y111==0):
                                                                        l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                        d9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                    if(y111==1):
                                                                        l9=Point(self.roomcoord[z3][2],self.roomcoord[z3][3])
                                                                        d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                    if(y111==2):
                                                                        l9=Point(self.roomcoord[z3][0],self.roomcoord[z3][1])
                                                                        d9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                    if(y111==3):
                                                                        l9=Point(self.roomcoord[z3][4],self.roomcoord[z3][5])
                                                                        d9=Point(self.roomcoord[z3][6],self.roomcoord[z3][7])
                                                                    for y112 in range(4):
                                                                        if(y112==0):
                                                                            l10=Point(p0,p1)
                                                                            d10=Point(p0,p3)
                                                                        if(y112==1):
                                                                            l10=Point(p0,p3)
                                                                            d10=Point(p2,p3)
                                                                        if(y112==2):
                                                                            l10=Point(p2,p3)
                                                                            d10=Point(p2,p1)
                                                                        if(y112==3):
                                                                            l10=Point(p2,p1)
                                                                            d10=Point(p0,p1)
                                                  
                                                                        if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                                                            self.room_doors2[z3]=self.room_doors2[z3]+1







                        if(self.yt==0):
                            self.canvas.delete("blucol")
                            self.excep_fbox=0

                            for z3 in range(1000):
                                self.room_doors[z3]=self.room_doors2[z3]

                            self.ro=(self.ro)+1
                            self.adddel.destroy()
                            kk=self.numindex
                            if(self.jki==0):
                                inj=Image.open(PATH5+str(kk)+".tif")
                                inj=inj.convert('RGB')
                                inj=inj.resize((self.na,self.ha),Image.ANTIALIAS)
                                inj=inj.rotate(-(2*self.theta),expand=True,fillcolor='white')
                                inj.save(PATH8+str(c)+".jpg")
                            self.num_new2[c]=self.na
                            self.num_new1[c]=kk
                                
                            self.num_new3[c]=self.ha
                                #print(self.num_new[c][0],22)
                            self.numindex=0
                            #self.popup.add_command(label="delete",command=lambda: self.dele(id))
                            #self.popup.add_command(label="Rotate",command= lambda: root.bind("<Button-1>",self.rotate))
                            #self.popup.add_command(label="Rotate")
                            #self.popup.entryconfig("Rotate",command= lambda: self.rotate(event))
                            #self.delcom=1

                            #self.I2.save(PATH8+str(c)+".jpg")
                        #print(self.ro)

                #print(p)

            #print(ey2.get())
            #print(ey1.get())
            # reset the drag information
            self._drag_data["item"] = None
            self._drag_data["x"] = 0
            self._drag_data["y"] = 0
            self.canvas.dtag("drag","drag")


    def doOverlap(self, l1, d1, l2, d2): 
      
    # If one rectangle is on left side of other

        if( ((l2.x <= d1.x) and (l1.y <= d2.y) and (l2.y <= d1.y) and (l1.x <= d2.x)) or ((l1.x <= d2.x) and (l2.y <= d1.y) and (l1.y <= d2.y) and (l2.x <= d1.x))  ): 
            return True
  
    # If one rectangle is above other 
        #if((l1.y <= r2.y) or (l2.y <= r1.y)): 
        return False
  
        #return True
    def onSegment(self, p, q, r): 
        if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
               (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))): 
            return True
        return False
      

    # The main function that returns true if  
    # the line segment 'p1q1' and 'p2q2' intersect. 
    def doIntersect(self,p1,q1,p2,q2): 
          
        # Find the 4 orientations required for  
        # the general and special cases 
        o1 = self.orientation(p1, q1, p2) 
        o2 = self.orientation(p1, q1, q2) 
        o3 = self.orientation(p2, q2, p1) 
        o4 = self.orientation(p2, q2, q1) 
      
        # General case 
        if ((o1 != o2) and (o3 != o4)): 
            return True
      
        # Special Cases 
      
        # p1 , q1 and p2 are colinear and p2 lies on segment p1q1 
        if ((o1 == 0) and self.onSegment(p1, p2, q1)): 
            return True
      
        # p1 , q1 and q2 are colinear and q2 lies on segment p1q1 
        if ((o2 == 0) and self.onSegment(p1, q2, q1)): 
            return True
      
        # p2 , q2 and p1 are colinear and p1 lies on segment p2q2 
        if ((o3 == 0) and self.onSegment(p2, p1, q2)): 
            return True
      
        # p2 , q2 and q1 are colinear and q1 lies on segment p2q2 
        if ((o4 == 0) and self.onSegment(p2, q1, q2)): 
            return True
      
        # If none of the cases 
        return False

    def orientation(self, p, q, r): 
        # to find the orientation of an ordered triplet (p,q,r) 
        # function returns the following values: 
        # 0 : Colinear points 
        # 1 : Clockwise points 
        # 2 : Counterclockwise 
          
        # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/  
        # for details of below formula.  
          
        val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y)) 
        if (val > 0): 
              
            # Clockwise orientation 
            return 1
        elif (val < 0): 
              
            # Counterclockwise orientation 
            return 2
        else: 
              
            # Colinear orientation 
            return 0

    def doInside(self,l1,d1,l2,d2):
        if(l1.x<=l2.x and l2.x<=d2.x and d2.x<=d1.x and l1.y<=l2.y and l2.y<=d2.y and d2.y<=d1.y):
            return True
        return False
      




    def walloverlap(self,l1,d1,l2,d2):

        if(l1.y==d1.y):
            if(((l1.y<l2.y) and (l1.y<d2.y)) or ((l1.y>l2.y) and (l1.y>d2.y))):
                return False
            else:
                if(((l1.x<l2.x) and (l1.x<d2.x) and (d1.x<l2.x) and (d1.x<d2.x)) or ((l1.x>l2.x) and (l1.x>d2.x) and (d1.x>l2.x) and (d1.x>d2.x))):
                    return False
                else:
                    return True
        else:
            if(l1.x==d1.x):
                if(((l1.x<l2.x) and (l1.x<d2.x)) or ((l1.x>l2.x) and (l1.x>d2.x))):
                    return False
                else:
                    if(((l1.y<l2.y) and (l1.y<d2.y) and (d1.y<l2.y) and (d1.y<d2.y)) or ((l1.y>l2.y) and (l1.y>d2.y) and (d1.y>l2.y) and (d1.y>d2.y))):
                        return False
                    else:
                        return True



    def fliphorfun(self,y,x):
        z22=self.arr2[y][2]
        z11=self.arr2[y][0]

        for z in range(self.ro):
            if(z!=y and z!=x and self.flipcheck2[z]==0 and self.del_from_plan[z]==0):
                l2=Point(1270-z22,self.arr2[y][1])
                r2=Point(1270-z11,self.arr2[y][3])
                l1=Point(self.arr2[z][0],self.arr2[z][1])
                r1=Point(self.arr2[z][2],self.arr2[z][3])
                if(self.doOverlap(l1,r1,l2,r2) ):
                    friid3=self.canvas.find_closest((self.arr2[z][0]+self.arr2[z][2])/2,(self.arr2[z][1]+self.arr2[z][3])/2)[0]
                    jux3=Image.open(PATH8+str(z)+".jpg")
                                #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                                
                    #jux2=iiux2
                    iiux3=ImageOps.mirror(jux3)
                    iiux3=iiux3.convert('RGB')
                    iiux3.save(PATH8+str(z)+".jpg")
                                #iiux=iiux.rotate(-self.angar[x],fillcolor='white',expand=True)
                    #iiux2=ImageOps.flip(iiux2)
                                #self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                    self.canvas.delete(friid3)
                    self.canvas.kux33=ImageTk.PhotoImage(iiux3)
                    self.canvas.create_image((self.arr2[z][0],self.arr2[z][1]),image=self.canvas.kux33,anchor="nw")
                    self.mylist.append(self.canvas.kux33)
                    friid3=self.canvas.find_closest((self.arr2[z][0]+self.arr2[z][2])/2,(self.arr2[z][1]+self.arr2[z][3])/2)[0]
                    self.flipcheck2[z]=1
                    if(self.arr2[z][0]<635 and self.arr2[z][2]>635):
                        self.fliphorfun2(z,y,self.arr2[z][2]-635,635-self.arr2[z][0])
                    else:
                        self.fliphorfun(z,y)
                    #self.flipfun(z,y)
                    #if(self.flipcheck[z]==0):
                    self.canvas.move(friid3,1270-self.arr2[z][2]-(self.arr2[z][0]),0)
                        
                    x22=self.arr2[z][2]
                    x11=self.arr2[z][0]
                    self.arr2[z][0]=1270-x22
                    self.arr2[z][2]=1270-x11
            
        #if(self.flipcheck[y]==0):        




    def fliphorfun2(self,y,x,testng2,testng):
        z22=self.arr2[y][2]
        z11=self.arr2[y][0]                    

        for z in range(self.ro):
            if(z!=y and z!=x and self.flipcheck2[z]==0 and self.del_from_plan[z]==0):
                l2=Point(635-testng2,self.arr2[y][1])
                r2=Point(635+testng,self.arr2[y][3])
                l1=Point(self.arr2[z][0],self.arr2[z][1])
                r1=Point(self.arr2[z][2],self.arr2[z][3])
                if(self.doOverlap(l1,r1,l2,r2) ):
                    friid3=self.canvas.find_closest((self.arr2[z][0]+self.arr2[z][2])/2,(self.arr2[z][1]+self.arr2[z][3])/2)[0]
                    jux3=Image.open(PATH8+str(z)+".jpg")
                                #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                                
                    #jux2=iiux2
                    iiux3=ImageOps.mirror(jux3)
                    iiux3=iiux3.convert('RGB')
                    iiux3.save(PATH8+str(z)+".jpg")
                                #iiux=iiux.rotate(-self.angar[x],fillcolor='white',expand=True)
                    #iiux2=ImageOps.flip(iiux2)
                                #self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                    self.canvas.delete(friid3)
                    self.canvas.kux33=ImageTk.PhotoImage(iiux3)
                    self.canvas.create_image((self.arr2[z][0],self.arr2[z][1]),image=self.canvas.kux33,anchor="nw")
                    self.mylist.append(self.canvas.kux33)
                    friid3=self.canvas.find_closest((self.arr2[z][0]+self.arr2[z][2])/2,(self.arr2[z][1]+self.arr2[z][3])/2)[0]
                    self.flipcheck2[z]=1
                    if(self.arr2[z][0]<635 and self.arr2[z][2]>635):
                        self.fliphorfun2(z,y,self.arr2[z][2]-635,635-self.arr2[z][0])
                    else:
                        self.fliphorfun(z,y)                    
                    #self.flipfun2(z,y,testng2,testng)
                    #if(self.flipcheck[z]==0):
                    self.canvas.move(friid3,1270-self.arr2[z][2]-(self.arr2[z][0]),0)
                        
                    x22=self.arr2[z][2]
                    x11=self.arr2[z][0]
                    self.arr2[z][0]=1270-x22
                    self.arr2[z][2]=1270-x11






    def fliphordef(self):
        #print(1)
        self.flipcheck2=[0]*1000
        self.canvas.delete("colour")
        self.canvas.delete(self.canvas_img2)
        walflip=Image.open(PATH7)
        walflip=ImageOps.mirror(walflip)
        walflip.save(PATH7)
        walflip2=walflip.resize((1270,700),Image.ANTIALIAS)
        self.canvas.kmj=ImageTk.PhotoImage(walflip2)
        self.canvas_img2=self.canvas.create_image(0,0,image=self.canvas.kmj,anchor="nw")
        self.canvas.tag_lower(self.canvas_img2)

        for x in range(self.ro):
            if(self.hor_ver[x]=='V' and self.del_from_plan[x]==0):
                if(self.up_down[x]=='L'):
                    self.up_down[x]='R'
                else:
                    if(self.up_down[x]=='R'):
                        self.up_down[x]='L'

            #print(self.hor_ver[x],self.up_down[x])


            if(self.flipcheck2[x]==0 and self.del_from_plan[x]==0):
                jux=Image.open(PATH8+str(x)+".jpg")
                #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                
            
                iiux=ImageOps.mirror(jux)
                iiux.save(PATH8+str(x)+".jpg")
                #iiux=iiux.rotate(-self.angar[x],fillcolor='white',expand=True)
                #iiux=ImageOps.flip(iiux)
                self.friid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                self.canvas.delete(self.friid)
                self.canvas.kux3=ImageTk.PhotoImage(iiux)
                self.canvas.create_image(((self.arr2[x][0]),(self.arr2[x][1])),image=self.canvas.kux3,anchor="nw")
                self.mylist.append(self.canvas.kux3)

                if(self.arr2[x][0]>=635):
                    self.friid1=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                    self.flipcheck2[x]=1
                    y22=self.arr2[x][2]
                    y11=self.arr2[x][0]
                    for y in range(self.ro):
                        if(y!=x and self.flipcheck2[y]==0 and self.del_from_plan[y]==0):
                            l2=Point(1270-y22,self.arr2[x][1])
                            r2=Point(1270-y11,self.arr2[x][3])
                            l1=Point(self.arr2[y][0],self.arr2[y][1])
                            r1=Point(self.arr2[y][2],self.arr2[y][3])
                            if(self.doOverlap(l1,r1,l2,r2)):
                                self.friid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                jux2=Image.open(PATH8+str(y)+".jpg")
                                #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                                
                                #jux2=iiux2
                                iiux2=ImageOps.mirror(jux2)
                                iiux2=iiux2.convert('RGB')
                                iiux2.save(PATH8+str(y)+".jpg")
                                #iiux=iiux.rotate(-self.angar[x],fillcolor='white',expand=True)
                                #iiux2=ImageOps.flip(iiux2)
                                #self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                                self.canvas.delete(self.friid2)
                                self.canvas.kux32=ImageTk.PhotoImage(iiux2)
                                self.canvas.create_image((self.arr2[y][0],self.arr2[y][1]),image=self.canvas.kux32,anchor="nw")
                                self.mylist.append(self.canvas.kux32)
                                self.friid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                self.flipcheck2[y]=1
                                if(self.arr2[y][0]<635 and self.arr2[y][2]>635):
                                 
                                    self.fliphorfun2(y,x,self.arr2[y][2]-635,635-self.arr2[y][0])
                                else:
                                    self.fliphorfun(y,x)                                
                                #print(x,y)
                                #self.flipfun(y,x)
                                self.canvas.move(self.friid2,1270-self.arr2[y][2]-self.arr2[y][0],0)
                                
                                x22=self.arr2[y][2]
                                x11=self.arr2[y][0]
                                self.arr2[y][0]=1270-x22
                                self.arr2[y][2]=1270-x11

                    self.canvas.move(self.friid1,1270-self.arr2[x][2]-self.arr2[x][0],0)
                    
                    #self.canvas.tag_lower(self.triid)
                    #self.canvas.tag_lower(self.canvas_img2)

                    self.arr2[x][0]=1270-y22
                    self.arr2[x][2]=1270-y11
                else:
                    if(self.arr2[x][2]<=635):

                        y22=self.arr2[x][2]
                        y11=self.arr2[x][0]
                        self.friid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                        self.flipcheck2[x]=1
                        for y in range(self.ro):
                            if(y!=x and self.flipcheck2[y]==0 and self.del_from_plan[y]==0):
                                l2=Point(1270-y22,self.arr2[x][1])
                                r2=Point(1270-y11,self.arr2[x][3])
                                l1=Point(self.arr2[y][0],self.arr2[y][1])
                                r1=Point(self.arr2[y][2],self.arr2[y][3])
                                if(self.doOverlap(l1,r1,l2,r2)  ):
                                    self.friid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                    jux2=Image.open(PATH8+str(y)+".jpg")
                                    #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                                    self.flipcheck2[y]=1
                                    #jux2=iiux2
                                    iiux2=ImageOps.mirror(jux2)
                                    iiux2=iiux2.convert('RGB')
                                    iiux2.save(PATH8+str(y)+".jpg")
                                    #iiux=iiux.rotate(-self.angar[x],fillcolor='white',expand=True)
                                    #iiux2=ImageOps.flip(iiux2)
                                    #self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                                    self.canvas.delete(self.friid2)
                                    self.canvas.kux32=ImageTk.PhotoImage(iiux2)
                                    self.canvas.create_image((self.arr2[y][0],self.arr2[y][1]),image=self.canvas.kux32,anchor="nw")
                                    self.mylist.append(self.canvas.kux32)
                                    self.friid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                    #print(x)
                                    if(self.arr2[y][0]<635 and self.arr2[y][2]>635):
                                        self.fliphorfun2(y,x,self.arr2[y][2]-635,635-self.arr2[y][0])
                                    else:
                                        self.fliphorfun(y,x)
                                    
                                    self.canvas.move(self.friid2,1270-self.arr2[y][2]-(self.arr2[y][0]),0)
                                    
                                    x22=self.arr2[y][2]
                                    x11=self.arr2[y][0]
                                    self.arr2[y][0]=1270-x22
                                    self.arr2[y][2]=1270-x11
                                                                          




                        #self.angar[x]=self.angar[x]+180
                        self.canvas.move(self.friid,1270-self.arr2[x][2]-self.arr2[x][0],0)
                        

                        self.arr2[x][0]=1270-y22
                        self.arr2[x][2]=1270-y11
                    else:
                        if(self.arr2[x][0]<635 and self.arr2[x][2]>635):
                            testng=635-(self.arr2[x][0])
                            testng2=(self.arr2[x][2])-635
                            if(testng>testng2):
                                self.friid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                                self.flipcheck2[x]=1
                                y22=self.arr2[x][2]
                                y11=self.arr2[x][0]
                                for y in range(self.ro):
                                    if(y!=x and self.flipcheck2[y]==0 and self.del_from_plan[y]==0):
                                        l2=Point(635-testng2,self.arr2[x][1])
                                        r2=Point(635+testng,self.arr2[x][3])
                                        l1=Point(self.arr2[y][0],self.arr2[y][1])
                                        r1=Point(self.arr2[y][2],self.arr2[y][3])
                                        if(self.doOverlap(l1,r1,l2,r2) ):
                                            self.friid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                            jux2=Image.open(PATH8+str(y)+".jpg")
                                            #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                                            self.flipcheck2[y]=1
                                            #jux2=iiux2
                                            iiux2=ImageOps.mirror(jux2)
                                            iiux2=iiux2.convert('RGB')
                                            iiux2.save(PATH8+str(y)+".jpg")
                                            #iiux=iiux.rotate(-self.angar[x],fillcolor='white',expand=True)
                                            #iiux2=ImageOps.flip(iiux2)
                                            #self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                                            self.canvas.delete(self.friid2)
                                            self.canvas.kux32=ImageTk.PhotoImage(iiux2)
                                            self.canvas.create_image((self.arr2[y][0],self.arr2[y][1]),image=self.canvas.kux32,anchor="nw")
                                            self.mylist.append(self.canvas.kux32)
                                            self.friid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                            if(self.arr2[y][0]<635 and self.arr2[y][2]>635):
                                                self.fliphorfun2(y,x,self.arr2[y][2]-635,635-self.arr2[y][0])
                                            else:
                                                self.fliphorfun(y,x)
                                            self.canvas.move(self.friid2,1270-self.arr2[y][2]-(self.arr2[y][0]),0)
                                            
                                            x22=self.arr2[y][2]
                                            x11=self.arr2[y][0]
                                            self.arr2[y][0]=1270-x22
                                            self.arr2[y][2]=1270-x11



                                self.canvas.move(self.friid,635-testng2-(self.arr2[x][0]),0)
                                
                                self.arr2[x][0]=635-testng2
                                self.arr2[x][2]=635+testng
                                
                            else:
                                if(testng2>testng):
                                    self.friid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                                    self.flipcheck2[x]=1
                                    for y in range(self.ro):
                                        if(y!=x and self.flipcheck2[y]==0 and self.del_from_plan[y]==0):
                                            l2=Point(635-testng2,self.arr2[x][1])
                                            r2=Point(635+testng,self.arr2[x][3])
                                            l1=Point(self.arr2[y][0],self.arr2[y][1])
                                            r1=Point(self.arr2[y][2],self.arr2[y][3])
                                            if(self.doOverlap(l1,r1,l2,r2) ):
                                                self.friid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                                jux2=Image.open(PATH8+str(y)+".jpg")
                                                #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                                                
                                                #jux2=iiux2
                                                self.flipcheck2[y]=1
                                                iiux2=ImageOps.mirror(jux2)
                                                iiux2=iiux2.convert('RGB')
                                                iiux2.save(PATH8+str(y)+".jpg")
                                                #iiux=iiux.rotate(-self.angar[x],fillcolor='white',expand=True)
                                                #iiux2=ImageOps.flip(iiux2)
                                                #self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                                                self.canvas.delete(self.friid2)
                                                self.canvas.kux32=ImageTk.PhotoImage(iiux2)
                                                self.canvas.create_image((self.arr2[y][0],self.arr2[y][1]),image=self.canvas.kux32,anchor="nw")
                                                self.mylist.append(self.canvas.kux32)
                                                self.friid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                                self.flipcheck2[y]=1
                                                if(self.arr2[y][0]<635 and self.arr2[y][2]>635):
                                                    self.fliphorfun2(y,x,self.arr2[y][2]-635,635-self.arr2[y][0])
                                                else:
                                                    self.fliphorfun(y,x)                                                
                                                #self.flipfun2(y,x,testng2,testng)
                                                self.canvas.move(self.friid2,1270-self.arr2[y][2]-(self.arr2[y][0]),0)
                                                
                                                x22=self.arr2[y][2]
                                                x11=self.arr2[y][0]
                                                self.arr2[y][0]=1270-x22
                                                self.arr2[y][2]=1270-x11

                                    self.canvas.move(self.friid,635-testng2-(self.arr2[x][0]),0)
                                    
                                    self.arr2[x][0]=635-testng2
                                    self.arr2[x][2]=635+testng

        for x in range(len(cfile['bbox_loc'])):
            testx=self.roomcoord[x][0]
            testy=self.roomcoord[x][2]

            self.roomcoord[x][0]=(1270-self.roomcoord[x][6])
            self.roomcoord[x][2]=(1270-self.roomcoord[x][4])
            self.roomcoord[x][4]=1270-testy
            self.roomcoord[x][6]=1270-testx

            self.roomcoord3[x][0]=self.roomcoord[x][0]
            self.roomcoord3[x][2]=self.roomcoord[x][2]
            self.roomcoord3[x][4]=self.roomcoord[x][4]
            self.roomcoord3[x][6]=self.roomcoord[x][6]

















    def flipfun(self,y,x):
        z22=self.arr2[y][3]
        z11=self.arr2[y][1]

        for z in range(self.ro):
            #print(z,1)
            if(z!=y and z!=x and self.flipcheck[z]==0 and self.del_from_plan[z]==0):
                l2=Point(self.arr2[y][0],700-z22)
                r2=Point(self.arr2[y][2],700-z11)
                l1=Point(self.arr2[z][0],self.arr2[z][1])
                r1=Point(self.arr2[z][2],self.arr2[z][3])
                if(self.doOverlap(l1,r1,l2,r2) ):
                    triid3=self.canvas.find_closest((self.arr2[z][0]+self.arr2[z][2])/2,(self.arr2[z][1]+self.arr2[z][3])/2)[0]
                    jux3=Image.open(PATH8+str(z)+".jpg")
                                #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                                
                    #jux2=iiux2
                    iiux3=ImageOps.flip(jux3)
                    iiux3=iiux3.convert('RGB')
                    iiux3.save(PATH8+str(z)+".jpg")
                                #iiux=iiux.rotate(-self.angar[x],fillcolor='white',expand=True)
                    #iiux2=ImageOps.flip(iiux2)
                                #self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                    self.canvas.delete(triid3)
                    self.canvas.iux33=ImageTk.PhotoImage(iiux3)
                    self.canvas.create_image((self.arr2[z][0],self.arr2[z][1]),image=self.canvas.iux33,anchor="nw")
                    self.mylist.append(self.canvas.iux33)
                    triid3=self.canvas.find_closest((self.arr2[z][0]+self.arr2[z][2])/2,(self.arr2[z][1]+self.arr2[z][3])/2)[0]
                    self.flipcheck[z]=1
                    if(self.arr2[z][1]<350 and self.arr2[z][3]>350):
                        self.flipfun2(z,y,self.arr2[z][3]-350,350-self.arr2[z][1])
                    else:
                        self.flipfun(z,y)
                    #self.flipfun(z,y)
                    #if(self.flipcheck[z]==0):
                    self.canvas.move(triid3,0,700-self.arr2[z][3]-(self.arr2[z][1]))
                        
                    x22=self.arr2[z][3]
                    x11=self.arr2[z][1]
                    self.arr2[z][1]=700-x22
                    self.arr2[z][3]=700-x11
            
        #if(self.flipcheck[y]==0):        




    def flipfun2(self,y,x,testng2,testng):
        z22=self.arr2[y][3]
        z11=self.arr2[y][1]                    

        for z in range(self.ro):
            if(z!=y and z!=x and self.flipcheck[z]==0 and self.del_from_plan[z]==0):
                l2=Point(self.arr2[y][0],350-testng2)
                r2=Point(self.arr2[y][2],350+testng)
                l1=Point(self.arr2[z][0],self.arr2[z][1])
                r1=Point(self.arr2[z][2],self.arr2[z][3])
                if(self.doOverlap(l1,r1,l2,r2) ):
                    triid3=self.canvas.find_closest((self.arr2[z][0]+self.arr2[z][2])/2,(self.arr2[z][1]+self.arr2[z][3])/2)[0]
                    jux3=Image.open(PATH8+str(z)+".jpg")
                                #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                                
                    #jux2=iiux2
                    iiux3=ImageOps.flip(jux3)
                    iiux3=iiux3.convert('RGB')
                    iiux3.save(PATH8+str(z)+".jpg")
                                #iiux=iiux.rotate(-self.angar[x],fillcolor='white',expand=True)
                    #iiux2=ImageOps.flip(iiux2)
                                #self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                    self.canvas.delete(triid3)
                    self.canvas.iux33=ImageTk.PhotoImage(iiux3)
                    self.canvas.create_image((self.arr2[z][0],self.arr2[z][1]),image=self.canvas.iux33,anchor="nw")
                    self.mylist.append(self.canvas.iux33)
                    triid3=self.canvas.find_closest((self.arr2[z][0]+self.arr2[z][2])/2,(self.arr2[z][1]+self.arr2[z][3])/2)[0]
                    self.flipcheck[z]=1
                    if(self.arr2[z][1]<350 and self.arr2[z][3]>350):
                        self.flipfun2(z,y,self.arr2[z][3]-350,350-self.arr2[z][1])
                    else:
                        self.flipfun(z,y)                    
                    #self.flipfun2(z,y,testng2,testng)
                    #if(self.flipcheck[z]==0):
                    self.canvas.move(triid3,0,700-self.arr2[z][3]-(self.arr2[z][1]))
                        
                    x22=self.arr2[z][3]
                    x11=self.arr2[z][1]
                    self.arr2[z][1]=700-x22
                    self.arr2[z][3]=700-x11

                                





    def flipdef(self):
        self.canvas.delete("colour")
        self.flipcheck=[0]*1000


        #print(120)
        self.canvas.delete(self.canvas_img2)
        walflip=Image.open(PATH7)
        walflip=ImageOps.flip(walflip)
        walflip.save(PATH7)
        walflip2=walflip.resize((1270,700),Image.ANTIALIAS)
        self.canvas.imj=ImageTk.PhotoImage(walflip2)
        self.canvas_img2=self.canvas.create_image(0,0,image=self.canvas.imj,anchor="nw")
        self.canvas.tag_lower(self.canvas_img2)


        for x in range(self.ro):
            if(self.hor_ver[x]=='H' and self.del_from_plan[x]==0):
                if(self.up_down[x]=='U'):
                    self.up_down[x]='D'
                else:
                    if(self.up_down[x]=='D'):
                        self.up_down[x]='U'

#            print(self.hor_ver[x],self.up_down[x])

            if(self.flipcheck[x]==0 and self.del_from_plan[x]==0):
                #ux=Image.open("C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Dataset_3roomsmall\\Cat1_1.jpg")
                #wdth.ht=ux.size
                #iiux=ux.resize((1350,700),Image.ANTIALIAS)
                #iux=iiux.crop((self.arr1[x][0],self.arr1[x][1],self.arr1[x][2],self.arr1[x][3]))
                #wid,ht=iux.size
                jux=Image.open(PATH8+str(x)+".jpg")
                #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                
            
                iiux=ImageOps.flip(jux)
                iiux.save(PATH8+str(x)+".jpg")
                #iiux=iiux.rotate(-self.angar[x],fillcolor='white',expand=True)
                #iiux=ImageOps.flip(iiux)
                self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                self.canvas.delete(self.triid)
                self.canvas.iux3=ImageTk.PhotoImage(iiux)
                self.canvas.create_image(((self.arr2[x][0]),(self.arr2[x][1])),image=self.canvas.iux3,anchor="nw")
                self.mylist.append(self.canvas.iux3)
                if(self.arr2[x][1]>=350):
                    #self.triid=self.canvas.find_closest((self.arr2[x][0]+1),(self.arr2[x][1]+1))[0]
                    self.triid1=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                    self.flipcheck[x]=1
                    y22=self.arr2[x][3]
                    y11=self.arr2[x][1]
                    for y in range(self.ro):
                        if(y!=x and self.flipcheck[y]==0 and self.del_from_plan[y]==0):
                            l2=Point(self.arr2[x][0],700-y22)
                            r2=Point(self.arr2[x][2],700-y11)
                            l1=Point(self.arr2[y][0],self.arr2[y][1])
                            r1=Point(self.arr2[y][2],self.arr2[y][3])
                            if(self.doOverlap(l1,r1,l2,r2)):
                                self.triid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                
                                
                                jux2=Image.open(PATH8+str(y)+".jpg")
                                    #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                                    
                                    #jux2=iiux2
                                iiux2=ImageOps.flip(jux2)
                                iiux2=iiux2.convert('RGB')
                                iiux2.save(PATH8+str(y)+".jpg")

                                #self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                                self.canvas.delete(self.triid2)
                                self.canvas.iux32=ImageTk.PhotoImage(iiux2)
                                self.canvas.create_image((self.arr2[y][0],self.arr2[y][1]),image=self.canvas.iux32,anchor="nw")
                                self.mylist.append(self.canvas.iux32)
                                self.triid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                self.flipcheck[y]=1
                                if(self.arr2[y][1]<350 and self.arr2[y][3]>350):
                                 
                                    self.flipfun2(y,x,self.arr2[y][3]-350,350-self.arr2[y][1])
                                else:
                                    self.flipfun(y,x)                                
                                #print(x,y)
                                #self.flipfun(y,x)
                                self.canvas.move(self.triid2,0,700-self.arr2[y][3]-(self.arr2[y][1]))
                                
                                x22=self.arr2[y][3]
                                x11=self.arr2[y][1]
                                self.arr2[y][1]=700-x22
                                self.arr2[y][3]=700-x11


                    #self.angar[x]=self.angar[x]+180
                    self.canvas.move(self.triid1,0,700-self.arr2[x][3]-(self.arr2[x][1]))
                    
                    #self.canvas.tag_lower(self.triid)
                    #self.canvas.tag_lower(self.canvas_img2)

                    self.arr2[x][1]=700-y22
                    self.arr2[x][3]=700-y11
                    #print(self.arr2[x][1],self.arr2[x][3],self.arr2[x][1]+self.arr2[x][3]-700)
                else:
                    if(self.arr2[x][3]<=350):

                        y22=self.arr2[x][3]
                        y11=self.arr2[x][1]
                        self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                        self.flipcheck[x]=1
                        for y in range(self.ro):
                            if(y!=x and self.flipcheck[y]==0 and self.del_from_plan[y]==0):
                                l2=Point(self.arr2[x][0],700-y22)
                                r2=Point(self.arr2[x][2],700-y11)
                                l1=Point(self.arr2[y][0],self.arr2[y][1])
                                r1=Point(self.arr2[y][2],self.arr2[y][3])
                                if(self.doOverlap(l1,r1,l2,r2)  ):
                                    self.triid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                    jux2=Image.open(PATH8+str(y)+".jpg")
                                    #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                                    self.flipcheck[y]=1
                                    #jux2=iiux2
                                    iiux2=ImageOps.flip(jux2)
                                    iiux2=iiux2.convert('RGB')
                                    iiux2.save(PATH8+str(y)+".jpg")
                                    #iiux=iiux.rotate(-self.angar[x],fillcolor='white',expand=True)
                                    #iiux2=ImageOps.flip(iiux2)
                                    #self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                                    self.canvas.delete(self.triid2)
                                    self.canvas.iux32=ImageTk.PhotoImage(iiux2)
                                    self.canvas.create_image((self.arr2[y][0],self.arr2[y][1]),image=self.canvas.iux32,anchor="nw")
                                    self.mylist.append(self.canvas.iux32)
                                    self.triid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                    #print(x)
                                    if(self.arr2[y][1]<350 and self.arr2[y][3]>350):
                                        self.flipfun2(y,x,self.arr2[y][3]-350,350-self.arr2[y][1])
                                    else:
                                        self.flipfun(y,x)
                                    
                                    self.canvas.move(self.triid2,0,700-self.arr2[y][3]-(self.arr2[y][1]))
                                    
                                    x22=self.arr2[y][3]
                                    x11=self.arr2[y][1]
                                    self.arr2[y][1]=700-x22
                                    self.arr2[y][3]=700-x11
                                                                          




                        #self.angar[x]=self.angar[x]+180
                        self.canvas.move(self.triid,0,700-self.arr2[x][3]-self.arr2[x][1])
                        

                        self.arr2[x][1]=700-y22
                        self.arr2[x][3]=700-y11
                    else:
                        if(self.arr2[x][1]<350 and self.arr2[x][3]>350):
                            testng=350-(self.arr2[x][1])
                            testng2=(self.arr2[x][3])-350
                            if(testng>testng2):
                                self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                                self.flipcheck[x]=1
                                y22=self.arr2[x][3]
                                y11=self.arr2[x][1]
                                for y in range(self.ro):
                                    if(y!=x and self.flipcheck[y]==0 and self.del_from_plan[y]==0):
                                        l2=Point(self.arr2[x][0],350-testng2)
                                        r2=Point(self.arr2[x][2],350+testng)
                                        l1=Point(self.arr2[y][0],self.arr2[y][1])
                                        r1=Point(self.arr2[y][2],self.arr2[y][3])
                                        if(self.doOverlap(l1,r1,l2,r2) ):
                                            self.triid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                            jux2=Image.open(PATH8+str(y)+".jpg")
                                            #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                                            self.flipcheck[y]=1
                                            #jux2=iiux2
                                            iiux2=ImageOps.flip(jux2)
                                            iiux2=iiux2.convert('RGB')
                                            iiux2.save(PATH8+str(y)+".jpg")
                                            #iiux=iiux.rotate(-self.angar[x],fillcolor='white',expand=True)
                                            #iiux2=ImageOps.flip(iiux2)
                                            #self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                                            self.canvas.delete(self.triid2)
                                            self.canvas.iux32=ImageTk.PhotoImage(iiux2)
                                            self.canvas.create_image((self.arr2[y][0],self.arr2[y][1]),image=self.canvas.iux32,anchor="nw")
                                            self.mylist.append(self.canvas.iux32)
                                            self.triid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                            if(self.arr2[y][1]<350 and self.arr2[y][3]>350):
                                                self.flipfun2(y,x,self.arr2[y][3]-350,350-self.arr2[y][1])
                                            else:
                                                self.flipfun(y,x)
                                            self.canvas.move(self.triid2,0,700-self.arr2[y][3]-(self.arr2[y][1]))
                                            
                                            x22=self.arr2[y][3]
                                            x11=self.arr2[y][1]
                                            self.arr2[y][1]=700-x22
                                            self.arr2[y][3]=700-x11



                                self.canvas.move(self.triid,0,350-testng2-(self.arr2[x][1]))
                                
                                self.arr2[x][1]=350-testng2
                                self.arr2[x][3]=350+testng
                                
                            else:
                                if(testng2>testng):
                                    self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                                    self.flipcheck[x]=1
                                    for y in range(self.ro):
                                        if(y!=x and self.flipcheck[y]==0 and self.del_from_plan[y]==0):
                                            l2=Point(self.arr2[x][0],350-testng2)
                                            r2=Point(self.arr2[x][2],350+testng)
                                            l1=Point(self.arr2[y][0],self.arr2[y][1])
                                            r1=Point(self.arr2[y][2],self.arr2[y][3])
                                            if(self.doOverlap(l1,r1,l2,r2)  ):
                                                self.triid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                                jux2=Image.open(PATH8+str(y)+".jpg")
                                                #iiux=ux.resize((wid,ht),Image.ANTIALIAS)
                                                
                                                #jux2=iiux2
                                                iiux2=ImageOps.flip(jux2)
                                                self.flipcheck[y]=1
                                                iiux2=iiux2.convert('RGB')
                                                iiux2.save(PATH8+str(y)+".jpg")
                                                #iiux=iiux.rotate(-self.angar[x],fillcolor='white',expand=True)
                                                #iiux2=ImageOps.flip(iiux2)
                                                #self.triid=self.canvas.find_closest((self.arr2[x][0]+self.arr2[x][2])/2,(self.arr2[x][1]+self.arr2[x][3])/2)[0]
                                                self.canvas.delete(self.triid2)
                                                self.canvas.iux32=ImageTk.PhotoImage(iiux2)
                                                self.canvas.create_image((self.arr2[y][0],self.arr2[y][1]),image=self.canvas.iux32,anchor="nw")
                                                self.mylist.append(self.canvas.iux32)
                                                self.triid2=self.canvas.find_closest((self.arr2[y][0]+self.arr2[y][2])/2,(self.arr2[y][1]+self.arr2[y][3])/2)[0]
                                                self.flipcheck[y]=1
                                                if(self.arr2[y][1]<350 and self.arr2[y][3]>350):
                                                    self.flipfun2(y,x,self.arr2[y][3]-350,350-self.arr2[y][1])
                                                else:
                                                    self.flipfun(y,x)                                                
                                                #self.flipfun2(y,x,testng2,testng)
                                                self.canvas.move(self.triid2,0,700-self.arr2[y][3]-(self.arr2[y][1]))
                                                
                                                x22=self.arr2[y][3]
                                                x11=self.arr2[y][1]
                                                self.arr2[y][1]=700-x22
                                                self.arr2[y][3]=700-x11

                                    self.canvas.move(self.triid,0,350-testng2-(self.arr2[x][1]))
                                    
                                    self.arr2[x][1]=350-testng2
                                    self.arr2[x][3]=350+testng








        for x in range(len(cfile['bbox_loc'])):
            testx=self.roomcoord[x][1]
            testy=self.roomcoord[x][3]
            self.roomcoord[x][1]=(700-self.roomcoord[x][7])
            self.roomcoord[x][3]=(700-self.roomcoord[x][5])
            self.roomcoord[x][5]=700-testy
            self.roomcoord[x][7]=700-testx

            self.roomcoord3[x][1]=self.roomcoord[x][1]
            self.roomcoord3[x][3]=self.roomcoord[x][3]
            self.roomcoord3[x][5]=self.roomcoord[x][5]
            self.roomcoord3[x][7]=self.roomcoord[x][7]





                #self.roomcoord[x][1]=
                #self.roomcoord[x][0]=cfile['bbox_loc'][0][x][0][0]*(1350/self.width)
                #self.roomcoord[x][1]=cfile['bbox_loc'][0][x][0][1]*(700/self.height)
                #self.roomcoord[x][2]=(cfile['bbox_loc'][0][x][0][2]+cfile['bbox_loc'][0][x][0][0])*(1350/self.width)
                #self.roomcoord[x][3]=(cfile['bbox_loc'][0][x][0][3]+cfile['bbox_loc'][0][x][0][1])*(700/self.height)






    def dele(self,xd):
    #canvas.tag_bind(id,"<Button-1>")
        if(self.excep==0):
            self.canvas.delete("DEL")
            self.canvas.dtag("DEL","DEL")
            self.del_from_plan[xd]=1

        self.canvas.delete("colour")
        
        self.edty5=self.canvas.find_closest((self.arr2[xd][0]+self.arr2[xd][2])/2,(self.arr2[xd][1]+self.arr2[xd][3])/2)[0]
        edty6=self.canvas.bbox(self.edty5)
        if(self.excep==1):
            k=0

            p0=edty6[0]
            p1=edty6[1]
            p2=edty6[2]
            p3=edty6[3]
            ui2=0
            ccc=0
            for x in range(len(cfile['bbox_loc'])):

                cchck=0
                ui2=0

                if(1):
                    for y111 in range(4):

                        
                        
                        if(y111==0):
                            l5=Point(self.roomcoord[x][0],self.roomcoord[x][1])
                            d5=Point(self.roomcoord[x][2],self.roomcoord[x][3])
                        if(y111==1):
                            l5=Point(self.roomcoord[x][2],self.roomcoord[x][3])
                            d5=Point(self.roomcoord[x][6],self.roomcoord[x][7])
                        if(y111==2):
                            l5=Point(self.roomcoord[x][0],self.roomcoord[x][1])
                            d5=Point(self.roomcoord[x][4],self.roomcoord[x][5])
                        if(y111==3):
                            l5=Point(self.roomcoord[x][4],self.roomcoord[x][5])
                            d5=Point(self.roomcoord[x][6],self.roomcoord[x][7])
                        for y112 in range(4):
                            if(y112==0):
                                l6=Point(p0,p1)
                                d6=Point(p0,p3)
                            if(y112==1):
                                l6=Point(p0,p3)
                                d6=Point(p2,p3)
                            if(y112==2):
                                l6=Point(p2,p3)
                                d6=Point(p2,p1)
                            if(y112==3):
                                l6=Point(p2,p1)
                                d6=Point(p0,p1)

                            if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                ui2=1
                                self.room_doors2[x]=self.room_doors2[x]-1
                                if(self.room_doors2[x]==0 ):
                                    messagebox.showerror("Error Occured","A Room must have atleat one door")
                                    self.canvas.dtag("DEL","DEL")
                                    for y in range(len(cfile['bbox_loc'])):
                                        #print(self.room_doors2[y])
                                        self.room_doors2[y]=self.room_doors[y]
                                    break
                                else:
                                    k=k+1
                                break
                        if(ui2==1):
                            break

                    if(ui2==0):
                        k=k+1

        

            #print(k)
            if(self.main_doors==1 and self.main_doors_check[xd]==1):
                messagebox.showerror("Error Occured","A House Plan must have atleast one main door")
                self.canvas.dtag("DEL","DEL")
                k=-1

            if(k==len(cfile['bbox_loc'])):
                #print(1111)
                for y in range(len(cfile['bbox_loc'])):
                    #print(self.room_doors2[y],11)
                    self.room_doors[y]=self.room_doors2[y]
                self.canvas.delete("DEL")
                self.canvas.dtag("DEL","DEL")
                self.del_from_plan[xd]=1
                if(self.main_doors_check[xd]==1):
                    self.main_doors=self.main_doors-1

           #for y in range(len(cfile['bbox_loc'])):
            #    print(self.room_doors2[y],self.room_doors[y])

        #self.canvas.dtag("DEL","DEL")
 






    def rotate(self,event):
        #canvas.create_rectangle(event.x,event.y,event.x+25,event.y+25,fill='red',tags=("DnD","token"))
        if(self.delcom==1):
            self.popup.delete("Delete")
            self.popup.delete("Rotate")
            self.delcom=0        

        self.ent=1
        self.my_entry = Entry(root, width=11, borderwidth=3,font=('Helvetica',12))
    #my_entry.grid(row=10,column=2)
        #self.my_entry.pack()
        self.my_entry.place(x=self.r1,y=(self.r4)+5)
        self.my_entry.insert(0, "Enter the angle")
        self.my_entry.configure(state=DISABLED)
        self.my_entry.config(background="white",disabledbackground="white")


        self.mybutton=Button(root,text="Go",state=DISABLED,bg="green yellow",fg="black",font="Times 10 bold")
        
        #self.mybutton.entryconfig("Go",command=self.fangle)                l2=Point(self.a1,self.a2)
                
        self.mybutton.place(x=(self.r1)+115,y=self.r4+5)

        self.canbut=Button(root,text="Cancel",bg="red",fg="white",font="Times 10 bold")
        
        self.canbut.place(x=(self.r1)+145,y=self.r4+5)


        self.my_entry.bind('<Button-1>', self.on_click)
        self.canbut.bind('<Button-1>',self.cancel)
        self.ent2=1
        #self.canvas.unbind("<Button-1>")

    def on_click(self,event):
        self.my_entry.configure(state=NORMAL)
        self.mybutton.configure(state=NORMAL)
        self.my_entry.delete(0, END)
        self.my_entry.unbind('<Button-1>')
        self.mybutton.bind('<Button-1>',self.fangle)
        self.canbut.bind('<Button-1>',self.cancel)



    def fangle(self,event):

        self.mybutton.unbind('<Button-1>')
        self.canbut.unbind('<Button-1>')
        root.unbind('<Button-1>')

        try:
            xio=int(self.my_entry.get())
            #xio=int(self.my_entry.get())
            #print(xio)
            x5=self.imp

            self.mybutton.unbind('<Button-1>')
            self.canbut.unbind('<Button-1>')
            root.unbind('<Button-1>')
            self.ent=0
            
            self.my_entry.destroy()
            self.mybutton.destroy()
            self.canbut.destroy()
            self.ent2=0

            x2=root.winfo_rootx()+self.canvas.winfo_x()
            y2=root.winfo_rooty()+self.canvas.winfo_y()
            #ImageGrab.grab().crop((x2+1,y2,x2+1607,y2+881)).save("C:\\Users\\User\\Desktop\\tkinter_codes\\test.jpg")

            if(x5<len(mfile['bbox_loc'][0])):
                iux=Image.open(PATH8+str(x5)+".jpg")
                #wdth.ht=ux.size
                #iiux=ux.resize((1270,700),Image.ANTIALIAS)
                #iux=iiux.crop((self.arr1[x5][0],self.arr1[x5][1],self.arr1[x5][2],self.arr1[x5][3]))
            else:
                opx=self.num_new1[x5]
                ux=Image.open(PATH5+str(opx)+".tif")
                ux=ux.convert('RGB')
                iux=ux.resize((self.num_new2[x5],self.num_new3[x5]),Image.ANTIALIAS)

            iux=iux.rotate(-xio-self.angar[x5],fillcolor='white',expand=True)
                
            #print(iux.width,iux.height)

            qh=0

            for x in range(self.ro):
                l1=Point(self.arr2[x][0],self.arr2[x][1])
                d1=Point(self.arr2[x][2],self.arr2[x][3])
                l2=Point(self.a1,self.a2)
                d2=Point(self.a1+iux.width,self.a2+iux.height)


                if(self.doOverlap(l1, d1, l2, d2) and (x!=x5) and (l2.x!=0) and (l2.y!=0)  and self.del_from_plan[x]==0): 
                    #print(x)
                    #print(p)
                    #print(l1.x,l1.y,r1.x,r1.y,l2.x,l2.y,r2.x,r2.y)
                    #self.canvas.move(self.iid,(self.r1)-recti[0],(self.r2)-recti[1])
                    self.canvas.delete("blucol")
                    qh=1
                    messagebox.showerror("Error occured","Object overlaps after rotation")
                    #print("Rectangles Overlap")
                    break

            if(qh==0):

                p0=self.a1
                p1=self.a2
                p2=self.a1+iux.width
                p3=self.a2+iux.height
                ui2=0
                ccc=0
                for x in range(len(cfile['bbox_loc'])):

                    cchck=0
                    ui2=0

                    if(1):
                        for y111 in range(4):

                            
                            
                            if(y111==0):
                                l5=Point(self.roomcoord[x][0],self.roomcoord[x][1])
                                d5=Point(self.roomcoord[x][2],self.roomcoord[x][3])
                            if(y111==1):
                                l5=Point(self.roomcoord[x][2],self.roomcoord[x][3])
                                d5=Point(self.roomcoord[x][6],self.roomcoord[x][7])
                            if(y111==2):
                                l5=Point(self.roomcoord[x][0],self.roomcoord[x][1])
                                d5=Point(self.roomcoord[x][4],self.roomcoord[x][5])
                            if(y111==3):
                                l5=Point(self.roomcoord[x][4],self.roomcoord[x][5])
                                d5=Point(self.roomcoord[x][6],self.roomcoord[x][7])
                            for y112 in range(4):
                                if(y112==0):
                                    l6=Point(p0,p1)
                                    d6=Point(p0,p3)
                                if(y112==1):
                                    l6=Point(p0,p3)
                                    d6=Point(p2,p3)
                                if(y112==2):
                                    l6=Point(p2,p3)
                                    d6=Point(p2,p1)
                                if(y112==3):
                                    l6=Point(p2,p1)
                                    d6=Point(p0,p1)

                                if((self.doIntersect(l5,d5,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                    if((self.new_obj==0 and self.excep==0) or (self.new_obj==1 and self.excep_fbox==0)):
                                        qh=1
                                        messagebox.showerror("Error Occured","Object is overlapping with wall")
                                        break            
                            if(qh==1):
                                break
                        if(qh==1):
                            break 










               # for x in range(len(self.skelarr)):
                #    l1=Point(self.skelarr[x][0],self.skelarr[x][1])
                 #   r1=Point(self.skelarr[x][2],self.skelarr[x][3])
                  #  l2=Point(self.a1,self.a2)
                   # r2=Point(self.a1+iux.width,self.a2+iux.height)

                    #if(self.walloverlap(l1,r1,l2,r2) and (self.excep==0) and (l2.x!=0) and (l2.y!=0)):
                        #self.canvas.move(self.iid,self.r1-recti[0],self.r2-recti[1])
                     #   qh=1
                      #  messagebox.showerror("Error Occured","Object overlaps with wall after rotation")
                    #print("Rectangles Overlap")
                    #    break


            if(qh==0):
                iux=iux.convert('RGB')
                iux.save(PATH8+str(x5)+".jpg")

                self.canvas.iux2=ImageTk.PhotoImage(iux)
                self.canvas.create_image((self.r1,self.r2),image=self.canvas.iux2,anchor="nw")
                self.mylist.append(self.canvas.iux2)

                self.angar[x5]=self.angar[x5]+xio

                self.arr2[x5][0]=self.r1
                self.arr2[x5][1]=self.r2
                self.arr2[x5][2]=self.r1+iux.width
                self.arr2[x5][3]=self.r2+iux.height


                self.canvas.delete(self.iid)


            #ux=self.canvas.find_closest((self.r1+self.r2)//2,(self.r2+self.r4)//2)[0]
            #ux=self.canvas.find_closest(event.x,event.y)[0]
            #rect=self.canvas.bbox(ux)
            #print(rect[0],rect[1],rect[2],rect[3])



            #we=pyautogui.screenshot()
            #we.save("C:\\Users\\User\\Desktop\\tkinter_codes\\test.jpg")
            
            #ux=self.images[x5]
            #self.canvas.update()
            #self.canvas.postscript(file="C:\\Users\\User\\Desktop\\tkinter_codes\\test.jpg")
            
            #start=time()
            #self.canvas.after(5000)
            #dux=ux.rotate(60,fillcolor='white',expand=True)
            
            #resz=

        except ValueError:
            messagebox.showerror("Error occured","Input is not a valid angle")

    def cancel(self,event):

        self.mybutton.unbind('<Button-1>')
        self.canbut.unbind('<Button-1>')
        root.unbind('<Button-1>')
        self.ent=0
        
        self.my_entry.destroy()
        self.mybutton.destroy()
        self.canbut.destroy()
        self.ent2=0

    def flip_door(self,event,alp):
        if(self.delcom2==1):
            self.popup.delete("Move the Door")
            self.popup.delete("Ignore")
            self.popup.delete("Delete")
            self.popup.delete("Horizontal Flip")
            self.popup.delete("Vertical Flip")
            self.delcom2=0

        x5=self.imp
        jux=Image.open(PATH8+str(x5)+".jpg")


        if(alp=='V'):

            q=0
            check=0
            xuu0=self.arr2[x5][0]
            xuu1=self.arr2[x5][1]
            xuu2=self.arr2[x5][2]
            xuu3=self.arr2[x5][3]

            if(self.up_down[x5]=='U'):
                if(xuu1+jux.height-28 <=0 or xuu3+jux.height-28 >=720 ):
                    q=1
                    messagebox.showerror("Error Occured","Door cannot croos the floorplan dimensions")

            if(self.up_down[x5]=='D'):
                if(xuu1-jux.height+24 <= 0 or xuu3-jux.height+24 >= 720):
                    q=1
                    messagebox.showerror("Error Occured","Door cannot croos the floorplan dimensions")

            if(q==0):
                for x in range(self.ro):
                    l1=Point(self.arr2[x][0],self.arr2[x][1])
                    d1=Point(self.arr2[x][2],self.arr2[x][3])
                    l2=Point(0,0)
                    d2=Point(0,0)
                    if(self.up_down[x5]=='U' ):
                        l2=Point(xuu0,xuu1+jux.height-28)
                        d2=Point(xuu2,xuu3+jux.height-28)
                    else:
                        if(self.up_down[x5]=='D' ):
                            l2=Point(xuu0,xuu1-jux.height+24)
                            d2=Point(xuu2,xuu3-jux.height+24)



                    if(self.doOverlap(l1, d1, l2, d2) and (l2.x!=0) and (l2.y!=0)  and self.del_from_plan[x]==0): 
                        #print(x)
                        #print(p)
                        #print(l1.x,l1.y,r1.x,r1.y,l2.x,l2.y,r2.x,r2.y)
                        if(self.new_obj==0):
                            if(x!=x5 ):
                                
                                #self.canvas.move(self.iid,(self.a1)-recti[0],(self.a2)-recti[1])
                                self.canvas.delete("blucol")
                                q=1
                                messagebox.showerror("Error occured","Door may overlap with other object after flipping")
                                #print("Rectangles Overlap")
                                break

            check=0
            if(q==0):

                ui2=0
                ccc=0
                check=0
                
                for x in range(len(cfile['bbox_loc'])):

                    cchck=0
                    ui2=0

                    if(1):
                        for y111 in range(4):

                            
                            l6=Point(0,0)
                            d6=Point(0,0)
                            if(y111==0):
                                l5=Point(self.roomcoord[x][0],self.roomcoord[x][1])
                                d5=Point(self.roomcoord[x][2],self.roomcoord[x][3])
                            if(y111==1):
                                l5=Point(self.roomcoord[x][2],self.roomcoord[x][3])
                                d5=Point(self.roomcoord[x][6],self.roomcoord[x][7])
                            if(y111==2):
                                l5=Point(self.roomcoord[x][0],self.roomcoord[x][1])
                                d5=Point(self.roomcoord[x][4],self.roomcoord[x][5])
                            if(y111==3):
                                l5=Point(self.roomcoord[x][4],self.roomcoord[x][5])
                                d5=Point(self.roomcoord[x][6],self.roomcoord[x][7])
                            for y112 in range(4):
                                if(y112==0):
                                    if(self.up_down[x5]=='U'):
                                        l6=Point(xuu0,xuu1+jux.height-28)
                                        d6=Point(xuu0,xuu3+jux.height-28)
                                    else:
                                        if(self.up_down[x5]=='D'):
                                            l6=Point(xuu0,xuu1-jux.height+24)
                                            d6=Point(xuu0,xuu3-jux.height+24)


                                if(y112==1):
                                    if(self.up_down[x5]=='U'):
                                        l6=Point(xuu0,xuu3+jux.height-28)
                                        d6=Point(xuu2,xuu3+jux.height-28)
                                    else:
                                        if(self.up_down[x5]=='D'):
                                            l6=Point(xuu0,xuu3-jux.height+24)
                                            d6=Point(xuu2,xuu3-jux.height+24)

                                
                                if(y112==2):
                                    if(self.up_down[x5]=='U'):
                                        l6=Point(xuu2,xuu3+jux.height-28)
                                        d6=Point(xuu2,xuu1+jux.height-28)
                                    else:
                                        if(self.up_down[x5]=='D'):
                                            l6=Point(xuu2,xuu3-jux.height+24)
                                            d6=Point(xuu2,xuu1-jux.height+24)


                                if(y112==3):
                                    if(self.up_down[x5]=='U'):
                                        l6=Point(xuu2,xuu1+jux.height-28)
                                        d6=Point(xuu0,xuu1+jux.height-28)
                                    else:
                                        if(self.up_down[x5]=='D'):
                                            l6=Point(xuu2,xuu1-jux.height+24)
                                            d6=Point(xuu0,xuu1-jux.height+24)

                                l1=Point(min(self.roomcoord[x][0],self.roomcoord[x][2],self.roomcoord[x][4],self.roomcoord[x][6]),min(self.roomcoord[x][1],self.roomcoord[x][3],self.roomcoord[x][5],self.roomcoord[x][7]))
                                d1=Point(max(self.roomcoord[x][0],self.roomcoord[x][2],self.roomcoord[x][4],self.roomcoord[x][6]),max(self.roomcoord[x][1],self.roomcoord[x][3],self.roomcoord[x][5],self.roomcoord[x][7]))


                                if(not(self.doIntersect(l5,d5,l6,d6)) and not(self.doInside(l1,d1,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                    cchck=cchck+1

                        if(cchck==16):
                            check=check+1




            #print(l2.x,check)
            if(check==len(cfile['bbox_loc']) and self.r1!=xuu0 and self.r2!=xuu1):
                #self.canvas.move(self.iid,self.a1-recti[0],self.a2-recti[1])
                messagebox.showerror("Error occured","Door may cross the boundary after flipping")
                check=0
                q=1




            if(q==0):
                iiux=ImageOps.flip(jux)
                iiux.save(PATH8+str(x5)+".jpg")
                self.friidd=self.canvas.find_closest((self.arr2[x5][0]+self.arr2[x5][2])/2,(self.arr2[x5][1]+self.arr2[x5][3])/2)[0]
                self.canvas.delete(self.friidd)
                self.canvas.kux3d=ImageTk.PhotoImage(iiux)
                self.xcv=self.canvas.create_image(((self.arr2[x5][0]),(self.arr2[x5][1])),image=self.canvas.kux3d,anchor="nw")
                self.mylist.append(self.canvas.kux3d)

                if(self.up_down[x5]=='U'):
                    self.canvas.move(self.xcv,0,iiux.height-28)
                    self.up_down[x5]='D'
                    self.arr2[x5][1]=self.arr2[x5][1]+iiux.height-28
                    self.arr2[x5][3]=self.arr2[x5][3]+iiux.height-28
                else:
                    if(self.up_down[x5]=='D'):
                        self.canvas.move(self.xcv,0,-iiux.height+24)
                        self.up_down[x5]='U'
                        self.arr2[x5][1]=self.arr2[x5][1]-iiux.height+24
                        self.arr2[x5][3]=self.arr2[x5][3]-iiux.height+24


            #iux=iux.rotate(-180-self.angar[x5],fillcolor='white',expand=True)
        if(alp=='H'):

            q=0
            check=0
            xuu0=self.arr2[x5][0]
            xuu1=self.arr2[x5][1]
            xuu2=self.arr2[x5][2]
            xuu3=self.arr2[x5][3]

            if(self.up_down[x5]=='L'):
                if(xuu0+jux.width-28 <=0 or xuu2+jux.width-28 >= 1285):
                    q=1
                    messagebox.showerror("Error Occured","Door cannot cross the floorplan dimensions")

            if(self.up_down[x5]=='R'):
                if(xuu0-jux.width+24 <= 0 or xuu2-jux.width+24 >= 1285):
                    q=1
                    messagebox.showerror("Error Occured","Door cannot cross the floorplan dimensions")

            if(q==0):
                for x in range(self.ro):
                    l1=Point(self.arr2[x][0],self.arr2[x][1])
                    d1=Point(self.arr2[x][2],self.arr2[x][3])
                    l2=Point(0,0)
                    d2=Point(0,0)
                    if(self.up_down[x5]=='L'):
                        l2=Point(xuu0+jux.width-28,xuu1)
                        d2=Point(xuu2+jux.width-28,xuu3)
                    else:
                        if(self.up_down[x5]=='R'):
                            l2=Point(xuu0-jux.width+24,xuu1)
                            d2=Point(xuu2-jux.width+24,xuu3)



                    if(self.doOverlap(l1, d1, l2, d2) and (l2.x!=0) and (l2.y!=0) and self.del_from_plan[x]==0  ): 
                        #print(x)
                        #print(p)
                        
                        if(self.new_obj==0):
                            #print(l1.x,l1.y,d1.x,d1.y,l2.x,l2.y,d2.x,d2.y)
                            p=self.imp
                            if(x!=p):
                                #self.canvas.move(self.iid,(self.a1)-recti[0],(self.a2)-recti[1])
                                self.canvas.delete("blucol")
                                q=1
                                messagebox.showerror("Error occured","Door may overlap with other object after flipping")
                                break
                            #print("Rectangles Overlap")
                            
            check=0
            if(q==0):

                check=0
                for x in range(len(cfile['bbox_loc'])):

                    cchck=0
                    ui2=0


                    if(1):
                        for y111 in range(4):

                            
                            l6=Point(0,0)
                            d6=Point(0,0)
                            if(y111==0):
                                l5=Point(self.roomcoord[x][0],self.roomcoord[x][1])
                                d5=Point(self.roomcoord[x][2],self.roomcoord[x][3])
                            if(y111==1):
                                l5=Point(self.roomcoord[x][2],self.roomcoord[x][3])
                                d5=Point(self.roomcoord[x][6],self.roomcoord[x][7])
                            if(y111==2):
                                l5=Point(self.roomcoord[x][0],self.roomcoord[x][1])
                                d5=Point(self.roomcoord[x][4],self.roomcoord[x][5])
                            if(y111==3):
                                l5=Point(self.roomcoord[x][4],self.roomcoord[x][5])
                                d5=Point(self.roomcoord[x][6],self.roomcoord[x][7])
                            for y112 in range(4):
                                if(y112==0):
                                    if(self.up_down[x5]=='U'):
                                        l6=Point(xuu0+jux.width-28,xuu1)
                                        d6=Point(xuu0+jux.width-28,xuu3)
                                    else:
                                        if(self.up_down[x5]=='D'):
                                            l6=Point(xuu0-jux.width+24,xuu1)
                                            d6=Point(xuu0-jux.width+24,xuu3)


                                if(y112==1):
                                    if(self.up_down[x5]=='U'):
                                        l6=Point(xuu0+jux.width-28,xuu3)
                                        d6=Point(xuu2+jux.width-28,xuu3)
                                    else:
                                        if(self.up_down[x5]=='D'):
                                            l6=Point(xuu0-jux.width+24,xuu3)
                                            d6=Point(xuu2-jux.width+24,xuu3)

                                
                                if(y112==2):
                                    if(self.up_down[x5]=='U'):
                                        l6=Point(xuu2+jux.width-28,xuu3)
                                        d6=Point(xuu2+jux.width-28,xuu1)
                                    else:
                                        if(self.up_down[x5]=='D'):
                                            l6=Point(xuu2-jux.width+24,xuu3)
                                            d6=Point(xuu2-jux.width+24,xuu1)


                                if(y112==3):
                                    if(self.up_down[x5]=='U'):
                                        l6=Point(xuu2+jux.width-28,xuu1)
                                        d6=Point(xuu0+jux.width-28,xuu1)
                                    else:
                                        if(self.up_down[x5]=='D'):
                                            l6=Point(xuu2-jux.width+24,xuu1)
                                            d6=Point(xuu0-jux.width+24,xuu1)

                                l1=Point(min(self.roomcoord[x][0],self.roomcoord[x][2],self.roomcoord[x][4],self.roomcoord[x][6]),min(self.roomcoord[x][1],self.roomcoord[x][3],self.roomcoord[x][5],self.roomcoord[x][7]))
                                d1=Point(max(self.roomcoord[x][0],self.roomcoord[x][2],self.roomcoord[x][4],self.roomcoord[x][6]),max(self.roomcoord[x][1],self.roomcoord[x][3],self.roomcoord[x][5],self.roomcoord[x][7]))


                                if(not(self.doIntersect(l5,d5,l6,d6)) and not(self.doInside(l1,d1,l6,d6)) and (l6.x!=0) and (l6.y!=0) ):
                                    cchck=cchck+1

                        if(cchck==16):
                            check=check+1




            if(check==len(cfile['bbox_loc']) and self.r1!=xuu0 and self.r2!=xuu1):
                #self.canvas.move(self.iid,self.a1-recti[0],self.a2-recti[1])
                messagebox.showerror("Error occured","Door may cross the boundary after flipping")
                check=0
                q=1



            if(q==0):
                iiux=ImageOps.mirror(jux)
                iiux.save(PATH8+str(x5)+".jpg")
                #iux=iux.rotate(-180-self.angar[x5],fillcolor='white',expand=True)
                self.friidd=self.canvas.find_closest((self.arr2[x5][0]+self.arr2[x5][2])/2,(self.arr2[x5][1]+self.arr2[x5][3])/2)[0]
                self.canvas.delete(self.friidd)
                self.canvas.kux3d=ImageTk.PhotoImage(iiux)
                self.xcv=self.canvas.create_image(((self.arr2[x5][0]),(self.arr2[x5][1])),image=self.canvas.kux3d,anchor="nw")
                self.mylist.append(self.canvas.kux3d)

                if(self.up_down[x5]=='L'):
                    self.canvas.move(self.xcv,iiux.width-28,0)
                    self.up_down[x5]='R'
                    self.arr2[x5][0]=self.arr2[x5][0]+iiux.width-28
                    self.arr2[x5][2]=self.arr2[x5][2]+iiux.width-28
                else:
                    if(self.up_down[x5]=='R'):
                        self.canvas.move(self.xcv,-iiux.width+24,0)
                        self.up_down[x5]='L'
                        self.arr2[x5][0]=self.arr2[x5][0]-iiux.width+24
                        self.arr2[x5][2]=self.arr2[x5][2]-iiux.width+24






    

Example(root)#pack(fill="both", expand=True)

root.mainloop()
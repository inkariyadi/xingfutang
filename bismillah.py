from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
from time import sleep
from PIL import ImageTk,Image  
import kode
import vektor 
from scipy.misc.pilutil import imread
import matplotlib.pyplot as plt

class SampleApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title_font = font.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.helv36 = font.Font(family = "Helvetica",size = 36,weight = "bold")
        self.helv15 = font.Font(family = "Helvetica",size = 15)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
    # for F in (StartPage):
        page_name = StartPage.__name__
        frame = StartPage(parent=container, master=self)
        self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(Frame):

    def __init__(self, parent, master):
        global bg1
        global image_exit_resize
        global image_submit_resize
        global image_choosefile_resize
        global image_method_resize
        global image_cosine_resize
        global image_euclidean_resize
        global image_count_resize

        def choosefile():
            global filename
            filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

        def opt_je():
            global metode
            button_method.configure(image=image_euclidean_resize) 
            metode = "je"
        
        def opt_cs():
            global metode
            button_method.configure(image=image_cosine_resize)
            metode = "cs"

        def count_pic1():
            global jumlah
            jumlah = 1
        
        def count_pic2():
            global jumlah
            jumlah = 2
        def count_pic3():
            global jumlah
            jumlah = 3
        
        def count_pic4():
            global jumlah
            jumlah = 4
        def count_pic5():
            global jumlah
            jumlah = 5
        
        def count_pic6():
            global jumlah
            jumlah = 6
        def count_pic7():
            global jumlah
            jumlah = 7
        
        def count_pic8():
            global jumlah
            jumlah = 8
        def count_pic9():
            global jumlah
            jumlah = 9
        
        def count_pic10():
            global jumlah
            jumlah = 10

        def submit():
            master.show_frame("PageOne")
        
        def msg_quit():
            if messagebox.askokcancel("Program", "Are you sure you want to exit the program?"):
                master.destroy()
            
        def quit():
            master.destroy()
        
        Frame.__init__(self, parent)
        self.master = master
        master.geometry("350x450+200+100")
        master.resizable(0,0)
      
        master.title("Programnya Chacha, Gill, Inka neehhhh")


        canvas = Canvas(self, width = 350, height = 238)
        canvas.grid(row=0,column=0)
        bg = Image.open("startpage_1.png")
        bg = bg.resize((350, 238), Image.ANTIALIAS)
        bg1 = ImageTk.PhotoImage(bg)
        canvas.create_image(0, 0, anchor = NW, image = bg1)


        image_choosefile = PhotoImage(file="startpage_choosefile.png")
        image_choosefile_resize = image_choosefile.subsample(5,5)
        button_choosefile = Button(self, image=image_choosefile_resize,command =choosefile).grid(row=1,column=0,pady=2)

        image_cosine = PhotoImage(file="startpage_cosine.png")
        image_cosine_resize = image_cosine.subsample(5,5)
        image_euclidean = PhotoImage(file="startpage_euclidean.png")
        image_euclidean_resize = image_euclidean.subsample(5,5)
        image_method = PhotoImage(file="startpage_method.png")
        image_method_resize = image_method.subsample(5,5)
        image_count = PhotoImage(file="startpage_result.png")
        image_count_resize = image_count.subsample(5,5)

        button_method =  Menubutton ( self, text = "-",image=image_method_resize, relief = SUNKEN )
        button_method.grid(row = 2,column = 0,pady=2)
        button_method.menu  =  Menu ( button_method,tearoff=0)
        button_method["menu"]  =  button_method.menu
        button_method.menu.add_command(label = "Euclidean Distance", command=opt_je)
        button_method.menu.add_command( label = "Cosine Similarity",command=opt_cs)

        button_count =  Menubutton ( self, text = "-",image=image_count_resize, relief = SUNKEN )
        button_count.grid(row = 3,column = 0,pady=2)
        button_count.menu  =  Menu ( button_count,tearoff=0)
        button_count["menu"]  =  button_count.menu
        button_count.menu.add_command(label = "1",command=count_pic1)
        button_count.menu.add_command(label = "2",command=count_pic2)
        button_count.menu.add_command(label = "3",command=count_pic3)
        button_count.menu.add_command(label = "4",command=count_pic4)
        button_count.menu.add_command(label = "5",command=count_pic5)
        button_count.menu.add_command(label = "6",command=count_pic6)
        button_count.menu.add_command(label = "7",command=count_pic7)
        button_count.menu.add_command(label = "8",command=count_pic8)
        button_count.menu.add_command(label = "9",command=count_pic9)
        button_count.menu.add_command(label = "10",command=count_pic10)

        image_submit =PhotoImage(file="startpage_submit.png")
        image_submit_resize = image_submit.subsample(5,5)
        button_submit = Button(self,image = image_submit_resize,command=quit).grid(row=4,column =0,pady=20)

        image_exit= PhotoImage(file="startpage_buttonexit_copy.png")
        image_exit_resize = image_exit.subsample(5,5)
        button_exit = Button(self,image=image_exit_resize,highlightthickness = 0, bd = 0,command=msg_quit).grid(row=0,column=0,sticky= NE,padx=20,pady=10)

class SecondWindow(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PageOne,PageTwo,PageThree,PageFour,PageFive,PageSix,PageSeven,PageEight,PageNine,PageTen):
            page_name = F.__name__
            frame = F(parent=container, master=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageOne")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class PageOne(Frame):

    def __init__(self, parent, master):
        global bg1_rank1
        global img_rank1_raw
        global img1_rank1
        global image_next1_raw
        global image_next1_resize
        global image_bth1_resize

        
        Frame.__init__(self, parent)
        self.master = master
        master.geometry("350x450+200+100")
        master.resizable(0,0)

        canvas = Canvas(self, width = 350, height = 125)
        canvas.grid(row=0,column=0)
        bg_rank1 = Image.open("rank1.png")
        bg_rank1 = bg_rank1.resize((350, 125), Image.ANTIALIAS)
        bg1_rank1 = ImageTk.PhotoImage(bg_rank1)
        canvas.create_image(0, 0, anchor = NW, image = bg1_rank1)
        
        canvas2 = Canvas(self, width = 230, height = 230)
        canvas2.grid(row=1,column=0)
        image_next2_raw = "rank1_next.png"
        img_rank1 = Image.open(img_rank1_raw)
        img_rank1 = img_rank1.resize((230, 230), Image.ANTIALIAS)  
        img1_rank1 = ImageTk.PhotoImage(img_rank1)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank1)

        
        if (exit1==1):
            image_next1_raw = "page_exit.png"
        else:
            image_next1_raw = "rank1_next.png"
        image_next1 =PhotoImage(file = image_next1_raw)
        image_next1_resize = image_next1.subsample(5,5)
        if (image_next1_raw=="page_exit.png"):
            button_next1 = Button(self,text="Exit",image = image_next1_resize,command=quit).grid(row=2,column=0)
        else:
            button_next1 = Button(self,text="Next",image = image_next1_resize,command=lambda: master.show_frame("PageTwo")).grid(row=2,column=0)

        # image_bth1 = PhotoImage(file="rank1_backtohome.png")
        # image_bth1_resize = image_bth1.subsample(5,5)
        # button_bth1 = Button(self,image=image_bth1_resize,command=lambda: master.show_frame("PageOne")).grid(row=3,column=0)

class PageTwo(Frame):

    def __init__(self, parent, master):
        global bg1_rank2
        global img_rank2_raw
        global img1_rank2
        global image_next2_raw
        global image_next2_resize
        global image_bth2_resize
        Frame.__init__(self, parent)
        self.master = master

        canvas = Canvas(self, width = 350, height = 125)
        canvas.grid(row=0,column=0)
        bg_rank2 = Image.open("rank2.png")
        bg_rank2 = bg_rank2.resize((350, 125), Image.ANTIALIAS)  
        bg1_rank2 = ImageTk.PhotoImage(bg_rank2)
        canvas.create_image(0, 0, anchor = NW, image = bg1_rank2)
        
        canvas2 = Canvas(self, width = 230, height = 230)
        canvas2.grid(row=1,column=0)
        img_rank2 = Image.open(img_rank2_raw)
        img_rank2 = img_rank2.resize((230, 230), Image.ANTIALIAS)  
        img1_rank2 = ImageTk.PhotoImage(img_rank2)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank2)
        

        if (exit2==1):
            image_next2_raw = "page_exit.png"
        else:
            image_next2_raw = "rank1_next.png"
        image_next2 =PhotoImage(file = image_next2_raw)
        image_next2_resize = image_next2.subsample(5,5)
        if (image_next2_raw=="page_exit.png"):
            button_next2 = Button(self,text="Exit",image = image_next2_resize,command=quit).grid(row=2,column=0)
        else:
            button_next2 = Button(self,text="Next",image = image_next2_resize,command=lambda: master.show_frame("PageThree")).grid(row=2,column=0)
        # image_bth2 = PhotoImage(file="rank1_backtohome.png")
        # image_bth2_resize = image_bth2.subsample(5,5)
        # button_bth2 = Button(self,image=image_bth2_resize,command=lambda: master.show_frame("PageOne")).grid(row=3,column=0)
 
class PageThree(Frame):

    def __init__(self, parent, master):
        global bg1_rank3
        global img_rank3_raw
        global img1_rank3
        global image_next3_raw
        global image_next3_resize
        global image_bth3_resize
        Frame.__init__(self, parent)
        self.master = master

        canvas = Canvas(self, width = 350, height = 125)
        canvas.grid(row=0,column=0)
        bg_rank3 = Image.open("rank3.png")
        bg_rank3 = bg_rank3.resize((350, 125), Image.ANTIALIAS)  
        bg1_rank3 = ImageTk.PhotoImage(bg_rank3)
        canvas.create_image(0, 0, anchor = NW, image = bg1_rank3)
        
        canvas2 = Canvas(self, width = 230, height = 230)
        canvas2.grid(row=1,column=0)
        img_rank3 = Image.open(img_rank3_raw)
        img_rank3 = img_rank3.resize((230, 230), Image.ANTIALIAS)  
        img1_rank3 = ImageTk.PhotoImage(img_rank3)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank3)

        if (exit3==1):
            image_next3_raw = "page_exit.png"
        else:
            image_next3_raw = "rank1_next.png"
        image_next3 =PhotoImage(file = image_next3_raw)
        image_next3_resize = image_next3.subsample(5,5)
        if (image_next3_raw=="page_exit.png"):
            button_next3 = Button(self,text="Exit",image = image_next3_resize,command=quit).grid(row=2,column=0)
        else:
            button_next3 = Button(self,text="Next",image = image_next3_resize,command=lambda: master.show_frame("PageFour")).grid(row=2,column=0)
        # image_bth3 = PhotoImage(file="rank1_backtohome.png")
        # image_bth3_resize = image_bth3.subsample(5,5)
        # button_bth3 = Button(self,image=image_bth3_resize,command=lambda: master.show_frame("PageOne")).grid(row=3,column=0)

class PageFour(Frame):

    def __init__(self, parent, master):
        global bg1_rank4
        global img_rank4_raw
        global img1_rank4
        global image_next4_raw
        global image_next4_resize
        global image_bth4_resize
        Frame.__init__(self, parent)
        self.master = master

        canvas = Canvas(self, width = 350, height = 125)
        canvas.grid(row=0,column=0)
        bg_rank4 = Image.open("rank4.png")
        bg_rank4 = bg_rank4.resize((350, 125), Image.ANTIALIAS)  
        bg1_rank4 = ImageTk.PhotoImage(bg_rank4)
        canvas.create_image(0, 0, anchor = NW, image = bg1_rank4)

        canvas2 = Canvas(self, width = 230, height = 230)
        canvas2.grid(row=1,column=0)
        img_rank4 = Image.open(img_rank4_raw)
        img_rank4 = img_rank4.resize((230, 230), Image.ANTIALIAS)  
        img1_rank4 = ImageTk.PhotoImage(img_rank4)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank4)
        
        if (exit4==1):
            image_next4_raw = "page_exit.png"
        else:
            image_next4_raw = "rank1_next.png"
        image_next4 =PhotoImage(file = image_next4_raw)
        image_next4_resize = image_next4.subsample(5,5)
        if (image_next4_raw=="page_exit.png"):
            button_next4 = Button(self,text="Exit",image = image_next4_resize,command=quit).grid(row=2,column=0)
        else:
            button_next4 = Button(self,text="Next",image = image_next4_resize,command=lambda: master.show_frame("PageFive")).grid(row=2,column=0)

        # image_bth4 = PhotoImage(file="rank1_backtohome.png")
        # image_bth4_resize = image_bth4.subsample(5,5)
        # button_bth4 = Button(self,image=image_bth4_resize,command=lambda: master.show_frame("PageOne")).grid(row=3,column=0)

class PageFive(Frame):

    def __init__(self, parent, master):
        global bg1_rank5
        global img_rank5_raw
        global img1_rank5
        global image_next5_raw
        global image_next5_resize
        global image_bth5_resize
        Frame.__init__(self, parent)
        self.master = master

        canvas = Canvas(self, width = 350, height = 125)
        canvas.grid(row=0,column=0)
        bg_rank5 = Image.open("rank5.png")
        bg_rank5 = bg_rank5.resize((350, 125), Image.ANTIALIAS)  
        bg1_rank5 = ImageTk.PhotoImage(bg_rank5)
        canvas.create_image(0, 0, anchor = NW, image = bg1_rank5)
        
        canvas2 = Canvas(self, width = 230, height = 230)
        canvas2.grid(row=1,column=0)
        img_rank5 = Image.open(img_rank5_raw)
        img_rank5 = img_rank5.resize((230, 230), Image.ANTIALIAS)  
        img1_rank5 = ImageTk.PhotoImage(img_rank5)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank5)

        if (exit5==1):
            image_next5_raw = "page_exit.png"
        else:
            image_next5_raw = "rank1_next.png"
        image_next5 =PhotoImage(file = image_next5_raw)
        image_next5_resize = image_next5.subsample(5,5)
        if (image_next5_raw=="page_exit.png"):
            button_next5 = Button(self,text="Exit",image = image_next5_resize,command=quit).grid(row=2,column=0)
        else:
            button_next5 = Button(self,text="Next",image = image_next5_resize,command=lambda: master.show_frame("PageSix")).grid(row=2,column=0)
        # image_bth5 = PhotoImage(file="rank1_backtohome.png")
        # image_bth5_resize = image_bth5.subsample(5,5)
        # button_bth5 = Button(self,image=image_bth5_resize,command=lambda: master.show_frame("PageOne")).grid(row=3,column=0)

class PageSix(Frame):

    def __init__(self, parent, master):
        global bg1_rank6
        global img_rank6_raw
        global img1_rank6
        global image_next6_raw
        global image_next6_resize
        global image_bth6_resize
        Frame.__init__(self, parent)
        self.master = master

        canvas = Canvas(self, width = 350, height = 125)
        canvas.grid(row=0,column=0)
        bg_rank6 = Image.open("rank6.png")
        bg_rank6 = bg_rank6.resize((350, 125), Image.ANTIALIAS)  
        bg1_rank6 = ImageTk.PhotoImage(bg_rank6)
        canvas.create_image(0, 0, anchor = NW, image = bg1_rank6)

        canvas2 = Canvas(self, width = 230, height = 230)
        canvas2.grid(row=1,column=0)
        img_rank6 = Image.open(img_rank6_raw)
        img_rank6 = img_rank6.resize((230, 230), Image.ANTIALIAS)  
        img1_rank6 = ImageTk.PhotoImage(img_rank6)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank6)
        
        if (exit6==1):
            image_next6_raw = "page_exit.png"
        else:
            image_next6_raw = "rank1_next.png"
        image_next6 =PhotoImage(file = image_next6_raw)
        image_next6_resize = image_next6.subsample(5,5)
        if (image_next6_raw=="page_exit.png"):
            button_next6 = Button(self,text="Exit",image = image_next6_resize,command=quit).grid(row=2,column=0)
        else:
            button_next6 = Button(self,text="Next",image = image_next6_resize,command=lambda: master.show_frame("PageSeven")).grid(row=2,column=0)
        # image_bth6 = PhotoImage(file="rank1_backtohome.png")
        # image_bth6_resize = image_bth6.subsample(5,5)
        # button_bth6 = Button(self,image=image_bth6_resize,command=lambda: master.show_frame("PageOne")).grid(row=3,column=0)
 
class PageSeven(Frame):

    def __init__(self, parent, master):
        global bg1_rank7
        global img_rank7_raw
        global img1_rank7
        global image_next7_raw
        global image_next7_resize
        global image_bth7_resize
        Frame.__init__(self, parent)
        self.master = master

        canvas = Canvas(self, width = 350, height = 125)
        canvas.grid(row=0,column=0)
        bg_rank7 = Image.open("rank7.png")
        bg_rank7 = bg_rank7.resize((350, 125), Image.ANTIALIAS)  
        bg1_rank7 = ImageTk.PhotoImage(bg_rank7)
        canvas.create_image(0, 0, anchor = NW, image = bg1_rank7)

        canvas2 = Canvas(self, width = 230, height = 230)
        canvas2.grid(row=1,column=0)
        img_rank7 = Image.open(img_rank7_raw)
        img_rank7 = img_rank7.resize((230, 230), Image.ANTIALIAS)  
        img1_rank7 = ImageTk.PhotoImage(img_rank7)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank7)
        
        if (exit7==1):
            image_next7_raw = "page_exit.png"
        else:
            image_next7_raw = "rank1_next.png"
        image_next7 =PhotoImage(file = image_next7_raw)
        image_next7_resize = image_next7.subsample(5,5)
        if (image_next7_raw=="page_exit.png"):
            button_next7 = Button(self,text="Exit",image = image_next7_resize,command=quit).grid(row=2,column=0)
        else:
            button_next7 = Button(self,text="Next",image = image_next7_resize,command=lambda: master.show_frame("PageEight")).grid(row=2,column=0)
        # image_bth7 = PhotoImage(file="rank1_backtohome.png")
        # image_bth7_resize = image_bth7.subsample(5,5)
        # button_bth7 = Button(self,image=image_bth7_resize,command=lambda: master.show_frame("PageOne")).grid(row=3,column=0)

class PageEight(Frame):

    def __init__(self, parent, master):
        global bg1_rank8
        global img_rank8_raw
        global img1_rank8
        global image_next8_raw
        global image_next8_resize
        global image_bth8_resize
        Frame.__init__(self, parent)
        self.master = master

        canvas = Canvas(self, width = 350, height = 125)
        canvas.grid(row=0,column=0)
        bg_rank8 = Image.open("rank8.png")
        bg_rank8 = bg_rank8.resize((350, 125), Image.ANTIALIAS)  
        bg1_rank8 = ImageTk.PhotoImage(bg_rank8)
        canvas.create_image(0, 0, anchor = NW, image = bg1_rank8)

        canvas2 = Canvas(self, width = 230, height = 230)
        canvas2.grid(row=1,column=0)
        img_rank8 = Image.open(img_rank8_raw)
        img_rank8 = img_rank8.resize((230, 230), Image.ANTIALIAS)  
        img1_rank8 = ImageTk.PhotoImage(img_rank8)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank8)
        
        if (exit8==1):
            image_next8_raw = "page_exit.png"
        else:
            image_next8_raw = "rank1_next.png"
        image_next8 =PhotoImage(file = image_next8_raw)
        image_next8_resize = image_next8.subsample(5,5)
        if (image_next8_raw=="page_exit.png"):
            button_next8 = Button(self,text="Exit",image = image_next8_resize,command=quit).grid(row=2,column=0)
        else:
            button_next8 = Button(self,text="Next",image = image_next8_resize,command=lambda: master.show_frame("PageNine")).grid(row=2,column=0)
        # image_bth8 = PhotoImage(file="rank1_backtohome.png")
        # image_bth8_resize = image_bth8.subsample(5,5)
        # button_bth8 = Button(self,image=image_bth8_resize,command=lambda: master.show_frame("PageOne")).grid(row=3,column=0)

class PageNine(Frame):

    def __init__(self, parent, master):
        global bg1_rank9
        global img_rank9_raw
        global img1_rank9
        global image_next9_raw
        global image_next9_resize
        global image_bth9_resize
        Frame.__init__(self, parent)
        self.master = master

        canvas = Canvas(self, width = 350, height = 125)
        canvas.grid(row=0,column=0)
        bg_rank9 = Image.open("rank9.png")
        bg_rank9 = bg_rank9.resize((350, 125), Image.ANTIALIAS)  
        bg1_rank9 = ImageTk.PhotoImage(bg_rank9)
        canvas.create_image(0, 0, anchor = NW, image = bg1_rank9)

        canvas2 = Canvas(self, width = 230, height = 230)
        canvas2.grid(row=1,column=0)
        img_rank9 = Image.open(img_rank9_raw)
        img_rank9 = img_rank9.resize((230, 230), Image.ANTIALIAS)  
        img1_rank9 = ImageTk.PhotoImage(img_rank9)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank9)
        
        if (exit9==1):
            image_next9_raw = "page_exit.png"
        else:
            image_next9_raw = "rank1_next.png"
        image_next9 =PhotoImage(file = image_next9_raw)
        image_next9_resize = image_next9.subsample(5,5)
        if (image_next9_raw=="page_exit.png"):
            button_next9 = Button(self,text="Exit",image = image_next9_resize,command=quit).grid(row=2,column=0)
        else:
            button_next9 = Button(self,text="Next",image = image_next9_resize,command=lambda: master.show_frame("PageTen")).grid(row=2,column=0)
        # image_bth9 = PhotoImage(file="rank1_backtohome.png")
        # image_bth9_resize = image_bth9.subsample(5,5)
        # button_bth9 = Button(self,image=image_bth9_resize,command=lambda: master.show_frame("PageOne")).grid(row=3,column=0)
 
class PageTen(Frame):  
    
    
    def __init__(self, parent, master):
        global bg1_rank10
        global img_rank10_raw
        global img1_rank10
        global image_next10_raw
        global image_next10_resize
        global image_bth10_resize
        Frame.__init__(self, parent)
        self.master = master

        canvas = Canvas(self, width = 350, height = 125)
        canvas.grid(row=0,column=0)
        bg_rank10 = Image.open("rank10.png")
        bg_rank10 = bg_rank10.resize((350, 125), Image.ANTIALIAS)  
        bg1_rank10 = ImageTk.PhotoImage(bg_rank10)
        canvas.create_image(0, 0, anchor = NW, image = bg1_rank10)

        canvas2 = Canvas(self, width = 230, height = 230)
        canvas2.grid(row=1,column=0)
        

        img_rank10 = Image.open(img_rank10_raw)
        img_rank10 = img_rank10.resize((230, 230), Image.ANTIALIAS)  
        img1_rank10 = ImageTk.PhotoImage(img_rank10)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank10)

        image_next10 =PhotoImage(file="page_exit.png")
        image_next10_resize = image_next10.subsample(5,5)
        button_next10 = Button(self,text="Next",image=image_next10_resize,command=quit).grid(row=2,column=0)


        # image_bth10 = PhotoImage(file="rank1_backtohome.png")
        # image_bth10_resize = image_bth10.subsample(5,5)
        # button_bth10 = Button(self,image=image_bth10_resize,command=lambda: master.show_frame("PageOne")).grid(row=3,column=0)
   

       
if __name__ == "__main__":
    global img_rank1_raw
    global img_rank2_raw
    global img_rank3_raw
    global img_rank4_raw
    global img_rank5_raw
    global img_rank6_raw
    global img_rank7_raw
    global img_rank8_raw
    global img_rank9_raw
    global img_rank10_raw

    global image_next1_raw
    global image_next2_raw
    global image_next3_raw
    global image_next4_raw
    global image_next5_raw
    global image_next6_raw
    global image_next7_raw
    global image_next8_raw
    global image_next9_raw

    global exit1
    global exit2
    global exit3
    global exit4
    global exit5
    global exit6
    global exit7
    global exit8
    global exit9
    global exit10

    

    app = SampleApp()
    app.mainloop()
    print(filename)
    print(jumlah)

    if (jumlah==1):
        exit1 = 1
        exit2 = 0
        exit3 = 0
        exit4 = 0
        exit5 = 0
        exit6 = 0
        exit7 = 0
        exit8 = 0
        exit9 = 0
        exit10 = 0
    elif (jumlah==2):
        exit1 = 0
        exit2 = 1
        exit3 = 0
        exit4 = 0
        exit5 = 0
        exit6 = 0
        exit7 = 0
        exit8 = 0
        exit9 = 0
        exit10 = 0
    elif (jumlah==3):
        exit1 = 0
        exit2 = 0
        exit3 = 1
        exit4 = 0
        exit5 = 0
        exit6 = 0
        exit7 = 0
        exit8 = 0
        exit9 = 0
        exit10 = 0
    elif (jumlah==4):
        exit1 = 0
        exit2 = 0
        exit3 = 0
        exit4 = 1
        exit5 = 0
        exit6 = 0
        exit7 = 0
        exit8 = 0
        exit9 = 0
        exit10 = 0
    elif (jumlah==5):
        exit1 = 0
        exit2 = 0
        exit3 = 0
        exit4 = 0
        exit5 = 1
        exit6 = 0
        exit7 = 0
        exit8 = 0
        exit9 = 0
        exit10 = 0
    elif (jumlah==6):
        exit1 = 0
        exit2 = 0
        exit3 = 0
        exit4 = 0
        exit5 = 0
        exit6 = 1
        exit7 = 0
        exit8 = 0
        exit9 = 0
        exit10 = 0
    elif (jumlah==7):
        exit1 = 0
        exit2 = 0
        exit3 = 0
        exit4 = 0
        exit5 = 0
        exit6 = 0
        exit7 = 1
        exit8 = 0
        exit9 = 0
        exit10 = 0
    elif (jumlah==8):
        exit1 = 0
        exit2 = 0
        exit3 = 0
        exit4 = 0
        exit5 = 0
        exit6 = 0
        exit7 = 0
        exit8 = 1
        exit9 = 0
        exit10 = 0
    elif (jumlah==9):
        exit1 = 0
        exit2 = 0
        exit3 = 0
        exit4 = 0
        exit5 = 0
        exit6 = 0
        exit7 = 0
        exit8 = 0
        exit9 = 1
        exit10 = 0
    elif (jumlah==10):
        exit1 = 0
        exit2 = 0
        exit3 = 0
        exit4 = 0
        exit5 = 0
        exit6 = 0
        exit7 = 0
        exit8 = 0
        exit9 = 0
        exit10 = 1
        
    #je : euclidean
    #cs : cosin
    vector = []
    fileimg = []

    folder = "dataset/"

    vector = kode.loadVector() #mindahin ke array 
    fileimg = kode.loadNamaFile() #mindahin ke array

    vInit = kode.extract_features(filename) #hasil vektor yg mau di compare

    hasilje = [0 for i in range(len(vector))] #nyimpen hasil jarak euclidean
    hasilcs = [0 for i in range(len(vector))] #nyimpen hasil cosin

    hasil = ["" for i in range(10)]
    if(metode=="je"):
        for i in range (len(vector)):
            hasilje[i] = vektor.euclidean(vInit,vector[i])

        for i in range (10):
            maks = vektor.haslowest(hasilje)
            hasilje[maks]=1000
            hasil[i]=fileimg[maks]
            # img = imread(folder+hasil[i], mode="RGB")
            # plt.imshow(img)
            # plt.show()
    else:
        for i in range (len(vector)):
            hasilje[i] = vektor.cosine(vInit,vector[i])

        for i in range (10):
            maks = vektor.hashighest(hasilje)
            hasilje[maks]=-1000
            hasil[i]=fileimg[maks]
            # img = imread(folder+hasil[i], mode="RGB")
            # plt.imshow(img)
            # plt.show()

    # if (jumlah==2):
    #     image_next2_raw = "page_exit.png" 
    
    img_rank1_raw = folder+hasil[0]
    img_rank2_raw = folder+hasil[1]
    img_rank3_raw = folder+hasil[2]
    img_rank4_raw = folder+hasil[3]
    img_rank5_raw = folder+hasil[4]
    img_rank6_raw = folder+hasil[5]
    img_rank7_raw = folder+hasil[6]
    img_rank8_raw = folder+hasil[7]
    img_rank9_raw = folder+hasil[8]
    img_rank10_raw = folder+hasil[9]
   
    app2 = SecondWindow()
    app2.mainloop()


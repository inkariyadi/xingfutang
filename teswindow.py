from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
from time import sleep
from PIL import ImageTk,Image 
import kode
import vektor 

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
        for F in (StartPage, PageOne,PageTwo,PageThree,PageFour,PageFive,PageSix,PageSeven,PageEight,PageNine,PageTen):
            page_name = F.__name__
            frame = F(parent=container, master=self)
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
        
        def submit():
            master.show_frame("PageOne")

        def quit():
            master.destroy()
        
        Frame.__init__(self, parent)
        self.master = master
        master.geometry("350x450+200+100")
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

        button_method =  Menubutton ( self, text = "-",image=image_method_resize, relief = SUNKEN )
        button_method.grid(row = 2,column = 0,pady=2)
        button_method.menu  =  Menu ( button_method,tearoff=0)
        button_method["menu"]  =  button_method.menu
        button_method.menu.add_command(label = "Euclidean Distance", command=opt_je)
        button_method.menu.add_command( label = "Cosine Similarity",command=opt_cs)

        image_submit =PhotoImage(file="startpage_submit.png")
        image_submit_resize = image_submit.subsample(5,5)
        button_submit = Button(self,image = image_submit_resize,command=lambda : submit()).grid(row=3,column =0,pady=20)

        image_exit= PhotoImage(file="startpage_buttonexit.png")
        image_exit_resize = image_exit.subsample(5,5)
        button_exit = Button(self,image=image_exit_resize,highlightthickness = 0, bd = 0,command=quit).grid(row=0,column=0,sticky= NE,padx=20,pady=10)


class PageOne(Frame):

    def __init__(self, parent, master):
        global bg1_rank1
        global img1_rank1
        global image_next1_resize
        global image_bth1_resize
        Frame.__init__(self, parent)
        self.master = master

        canvas = Canvas(self, width = 350, height = 125)
        canvas.grid(row=0,column=0)
        bg_rank1 = Image.open("rank1.png")
        bg_rank1 = bg_rank1.resize((350, 125), Image.ANTIALIAS)
        bg1_rank1 = ImageTk.PhotoImage(bg_rank1)
        canvas.create_image(0, 0, anchor = NW, image = bg1_rank1)
        
        canvas2 = Canvas(self, width = 230, height = 230)
        canvas2.grid(row=1,column=0)
        img_rank1 = Image.open("1.png")
        img_rank1 = img_rank1.resize((230, 230), Image.ANTIALIAS)  
        img1_rank1 = ImageTk.PhotoImage(img_rank1)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank1)

        image_next1 =PhotoImage(file="rank1_next.png")
        image_next1_resize = image_next1.subsample(5,5)
        button_next1 = Button(self,text="Next",image=image_next1_resize,command=lambda: master.show_frame("PageTwo")).grid(row=2,column=0)

        image_bth1 = PhotoImage(file="rank1_backtohome.png")
        image_bth1_resize = image_bth1.subsample(5,5)
        button_bth1 = Button(self,image=image_bth1_resize,command=lambda: master.show_frame("StartPage")).grid(row=3,column=0)

class PageTwo(Frame):

    def __init__(self, parent, master):
        global bg1_rank2
        global img1_rank2
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
        img_rank2 = Image.open("2.png")
        img_rank2 = img_rank2.resize((230, 230), Image.ANTIALIAS)  
        img1_rank2 = ImageTk.PhotoImage(img_rank2)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank2)

        image_next2 =PhotoImage(file="rank1_next.png")
        image_next2_resize = image_next2.subsample(5,5)
        button_next2 = Button(self,text="Next",image=image_next2_resize,command=lambda: master.show_frame("PageThree")).grid(row=2,column=0)

        image_bth2 = PhotoImage(file="rank1_backtohome.png")
        image_bth2_resize = image_bth2.subsample(5,5)
        button_bth2 = Button(self,image=image_bth2_resize,command=lambda: master.show_frame("StartPage")).grid(row=3,column=0)
 
class PageThree(Frame):

    def __init__(self, parent, master):
        global bg1_rank3
        global img1_rank3
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
        img_rank3 = Image.open("3.png")
        img_rank3 = img_rank3.resize((230, 230), Image.ANTIALIAS)  
        img1_rank3 = ImageTk.PhotoImage(img_rank3)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank3)

        image_next3 =PhotoImage(file="rank1_next.png")
        image_next3_resize = image_next3.subsample(5,5)
        button_next3 = Button(self,text="Next",image=image_next3_resize,command=lambda: master.show_frame("PageFour")).grid(row=2,column=0)

        image_bth3 = PhotoImage(file="rank1_backtohome.png")
        image_bth3_resize = image_bth3.subsample(5,5)
        button_bth3 = Button(self,image=image_bth3_resize,command=lambda: master.show_frame("StartPage")).grid(row=3,column=0)

class PageFour(Frame):

    def __init__(self, parent, master):
        global bg1_rank4
        global img1_rank4
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
        img_rank4 = Image.open(".png")
        img_rank4 = img_rank4.resize((230, 230), Image.ANTIALIAS)  
        img1_rank4 = ImageTk.PhotoImage(img_rank4)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank4)
        
        image_next4 =PhotoImage(file="rank1_next.png")
        image_next4_resize = image_next4.subsample(5,5)
        button_next4 = Button(self,text="Next",image=image_next4_resize,command=lambda: master.show_frame("PageFive")).grid(row=2,column=0)

        image_bth4 = PhotoImage(file="rank1_backtohome.png")
        image_bth4_resize = image_bth4.subsample(5,5)
        button_bth4 = Button(self,image=image_bth4_resize,command=lambda: master.show_frame("StartPage")).grid(row=3,column=0)

class PageFive(Frame):

    def __init__(self, parent, master):
        global bg1_rank5
        global img1_rank5
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
        img_rank5 = Image.open("5.png")
        img_rank5 = img_rank5.resize((230, 230), Image.ANTIALIAS)  
        img1_rank5 = ImageTk.PhotoImage(img_rank5)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank5)

        image_next5 =PhotoImage(file="rank1_next.png")
        image_next5_resize = image_next5.subsample(5,5)
        button_next5 = Button(self,text="Next",image=image_next5_resize,command=lambda: master.show_frame("PageSix")).grid(row=2,column=0)

        image_bth5 = PhotoImage(file="rank1_backtohome.png")
        image_bth5_resize = image_bth5.subsample(5,5)
        button_bth5 = Button(self,image=image_bth5_resize,command=lambda: master.show_frame("StartPage")).grid(row=3,column=0)

class PageSix(Frame):

    def __init__(self, parent, master):
        global bg1_rank6
        global img1_rank6
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
        img_rank6 = Image.open("6.png")
        img_rank6 = img_rank6.resize((230, 230), Image.ANTIALIAS)  
        img1_rank6 = ImageTk.PhotoImage(img_rank6)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank6)
        
        image_next6 =PhotoImage(file="rank1_next.png")
        image_next6_resize = image_next6.subsample(5,5)
        button_next6 = Button(self,text="Next",image=image_next6_resize,command=lambda: master.show_frame("PageSeven")).grid(row=2,column=0)

        image_bth6 = PhotoImage(file="rank1_backtohome.png")
        image_bth6_resize = image_bth6.subsample(5,5)
        button_bth6 = Button(self,image=image_bth6_resize,command=lambda: master.show_frame("StartPage")).grid(row=3,column=0)
 
class PageSeven(Frame):

    def __init__(self, parent, master):
        global bg1_rank7
        global img1_rank7
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
        img_rank7 = Image.open("7.png")
        img_rank7 = img_rank7.resize((230, 230), Image.ANTIALIAS)  
        img1_rank7 = ImageTk.PhotoImage(img_rank7)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank7)
        
        image_next7 =PhotoImage(file="rank1_next.png")
        image_next7_resize = image_next7.subsample(5,5)
        button_next7 = Button(self,text="Next",image=image_next7_resize,command=lambda: master.show_frame("PageEight")).grid(row=2,column=0)

        image_bth7 = PhotoImage(file="rank1_backtohome.png")
        image_bth7_resize = image_bth7.subsample(5,5)
        button_bth7 = Button(self,image=image_bth7_resize,command=lambda: master.show_frame("StartPage")).grid(row=3,column=0)

class PageEight(Frame):

    def __init__(self, parent, master):
        global bg1_rank8
        global img1_rank8
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
        img_rank8 = Image.open("8.png")
        img_rank8 = img_rank8.resize((230, 230), Image.ANTIALIAS)  
        img1_rank8 = ImageTk.PhotoImage(img_rank8)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank8)
        
        image_next8 =PhotoImage(file="rank1_next.png")
        image_next8_resize = image_next8.subsample(5,5)
        button_next8 = Button(self,text="Next",image=image_next8_resize,command=lambda: master.show_frame("PageNine")).grid(row=2,column=0)

        image_bth8 = PhotoImage(file="rank1_backtohome.png")
        image_bth8_resize = image_bth8.subsample(5,5)
        button_bth8 = Button(self,image=image_bth8_resize,command=lambda: master.show_frame("StartPage")).grid(row=3,column=0)

class PageNine(Frame):

    def __init__(self, parent, master):
        global bg1_rank9
        global img1_rank9
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
        img_rank9 = Image.open("9.png")
        img_rank9 = img_rank9.resize((230, 230), Image.ANTIALIAS)  
        img1_rank9 = ImageTk.PhotoImage(img_rank9)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank9)
        
        image_next9 =PhotoImage(file="rank1_next.png")
        image_next9_resize = image_next9.subsample(5,5)
        button_next9 = Button(self,text="Next",image=image_next9_resize,command=lambda: master.show_frame("PageTen")).grid(row=2,column=0)

        image_bth9 = PhotoImage(file="rank1_backtohome.png")
        image_bth9_resize = image_bth9.subsample(5,5)
        button_bth9 = Button(self,image=image_bth9_resize,command=lambda: master.show_frame("StartPage")).grid(row=3,column=0)
 
class PageTen(Frame):

    def __init__(self, parent, master):
        global bg1_rank10
        global img1_rank10
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
        img_rank10 = Image.open("10.png")
        img_rank10 = img_rank10.resize((230, 230), Image.ANTIALIAS)  
        img1_rank10 = ImageTk.PhotoImage(img_rank10)
        canvas2.create_image(0, 0, anchor = NW, image = img1_rank10)
        
        image_next10 =PhotoImage(file="rank1_next.png")
        image_next10_resize = image_next10.subsample(5,5)
        button_next10 = Button(self,text="Next",image=image_next10_resize,command=quit).grid(row=2,column=0)

        image_bth10 = PhotoImage(file="rank1_backtohome.png")
        image_bth10_resize = image_bth10.subsample(5,5)
        button_bth10 = Button(self,image=image_bth10_resize,command=lambda: master.show_frame("StartPage")).grid(row=3,column=0)
 


       
if __name__ == "__main__":
    app = SampleApp()
    
    
    # #je : euclidean
    # #cs : cosin
    # vektor = []
    # fileimg = []

    # folder = "dataset/"

    # kode.saveVector() #save array of vector ke file vector.pck
    # kode.saveNamaFile() #save array of nama file ke file nama_file.pck
    # vektor = kode.loadVector() #mindahin ke array 
    # fileimg = kode.loadNamaFile() #mindahin ke array

    # vInit = kode.extract_features(filename) #hasil vektor yg mau di compare
    
    # hasilje = [] #nyimpen hasil jarak euclidean
    # hasilcs = [] #nyimpen hasil cosin
    # for i in range (len(vektor)):
    #     hasilje[i] = vektor.euclidean(vInit[i],vektor[i],2048)
    #     hasilcs[i] = vektor.cosine(vInit[i],vektor[i],2048)

    # hasilje.sort() #sort menaik
    # hasilcs.sort(reverse=True) #sort menurun
    # sortfileje = [x for _,x in sorted(zip(hasilje,fileimg))]
    # sortfilecs = [x for _,x in sorted(zip(hasilcs,fileimg))]

    # global hasil
    # hasil = []
    # if(metode=="je"):
    #     for i in range (10):
    #         hasil[i]=sortfileje[i]
    # else:
    #     for i in range (10):
    #         hasil[i]=sortfilecs[i]

    app.mainloop()
    

    
    

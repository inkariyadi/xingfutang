from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
from time import sleep
from PIL import ImageTk,Image  

root = Tk()
root.title("Face Recoginition-nya Chacha Gill Inka")
root.geometry("350x450+200+150")

helv36 = font.Font(family = "Helvetica",size = 36,weight = "bold")
helv15 = font.Font(family = "Helvetica",size = 15)

def close_window (): 
    root.destroy()

def choosefile():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print (root.filename)

def opt_je():
    button_method.configure(text="Jarak Euclidean")
    return;
def opt_cs():
    button_method.configure(text="Cosine Similarity")
    return;

def opt_cf():
    button_choosefile.configure(text="")
def submit():
    top = Toplevel()
    top.title("Python")

    label = Label(top, text="Waiting for task to finish.")
    label.pack()

    top.after(200, task )
    top.mainloop()

def task():
    sleep(2) # Replace this with the code you want to run
    top.destroy()


label_header = Label(root, text="Face Recognition",font = helv36).grid(row=0,columnspan=2)

label_entry = Label( root, text="Masukkan nama image file: ",font=helv15).grid(row=3, sticky=E, padx=4)

#entry_file = Entry(root).grid(row=3, column=1, sticky=E, pady=4)
button_choosefile = Button(root, text="Choose file",command =choosefile).grid(row=3,column=1,sticky=W,pady=4)

label_button = Label(root, text="Metode: ").grid(row=4,column=0,sticky=E, padx=4)
button_method =  Menubutton ( root, text = "-", relief = SUNKEN )
button_method.grid(row = 4,column = 1,sticky = W)
button_method.menu  =  Menu ( button_method,tearoff=0)
button_method["menu"]  =  button_method.menu
button_method.menu.add_command(label = "Jarak Euclidean", command=opt_je)
button_method.menu.add_command ( label = "Cosine Similarity",command=opt_cs)

img = PhotoImage(file='press1.png')
imgresize = img.subsample(5,5)
button_submit = Button(root, text="Submit",command=submit,image=imgresize).grid(row=5,column =1,sticky=E)

button_exit = Button(root, text="Exit",command=close_window).grid(row=5,column =0,sticky=E)
 

root.mainloop()

res = Tk()
res.geometry("350x450+200+150")

helv36 = font.Font(family = "Helvetica",size = 36,weight = "bold")
helv15 = font.Font(family = "Helvetica",size = 15)


res.title("Python")
label_header = Label(res, text="Face Recognition",font = helv36).grid(row=0,columnspan=10)
label_top10 = Label(res, text ="Hasil dari Face Recognition: ", font = helv15).grid(row=1,sticky = W,columnspan=10)
label_top1 = Label(res, text = "Rank 1: ", font = helv15).grid(row = 2,column = 0,sticky = W)
# label_top2 = Label(res, text = "Rank 2: ", font = helv15).grid(row = 3,column = 0,sticky = W)
# label_top3 = Label(res, text = "Rank 3: ", font = helv15).grid(row = 4,column = 0,sticky = W)
# label_top4 = Label(res, text = "Rank 4: ", font = helv15).grid(row = 5,column = 0,sticky = W)
# label_top5 = Label(res, text = "Rank 5: ", font = helv15).grid(row = 6,column = 0,sticky = W)
# label_top6 = Label(res, text = "Rank 6: ", font = helv15).grid(row = 7,column = 0,sticky = W)
# label_top7 = Label(res, text = "Rank 7: ", font = helv15).grid(row = 8,column = 0,sticky = W)
# label_top8 = Label(res, text = "Rank 8: ", font = helv15).grid(row = 9,column = 0,sticky = W)
# label_top9 = Label(res, text = "Rank 9: ", font = helv15).grid(row = 10,column = 0,sticky = W)
# label_top10 = Label(res, text = "Rank 10: ", font = helv15).grid(row = 11,column = 0,sticky = W)

label_nama1 = Label(res, text = "<namafile1>", font = helv15).grid(row= 2,column=1,sticky = W)
# label_nama2 = Label(res, text = "<namafile2>", font = helv15).grid(row= 3,column=1,sticky = W)
# label_nama3 = Label(res, text = "<namafile3>", font = helv15).grid(row= 4,column=1,sticky = W)
# label_nama4 = Label(res, text = "<namafile4>", font = helv15).grid(row= 5,column=1,sticky = W)
# label_nama5 = Label(res, text = "<namafile5>", font = helv15).grid(row= 6,column=1,sticky = W)
# label_nama6 = Label(res, text = "<namafile6>", font = helv15).grid(row= 7,column=1,sticky = W)
# label_nama7 = Label(res, text = "<namafile7>", font = helv15).grid(row= 8,column=1,sticky = W)
# label_nama8 = Label(res, text = "<namafile8>", font = helv15).grid(row= 9,column=1,sticky = W)
# label_nama9 = Label(res, text = "<namafile9>", font = helv15).grid(row= 10,column=1,sticky = W)
# label_nama10 = Label(res, text = "<namafile10>", font = helv15).grid(row= 11,column=1,sticky = W)

canvas = Canvas(res, width = 300, height = 300)
canvas.grid(row=3,column=0,columnspan=10)
image = Image.open("instagram.jpg")
image = image.resize((300, 300), Image.ANTIALIAS) ## The (250, 250) is (height, width)
img = ImageTk.PhotoImage(image)
canvas.create_image(20,5,anchor=NW, image=img) 

button_next = Button(res,text="Next",bg="pink").grid(row=4,columnspan=10,sticky=E)
res.mainloop()
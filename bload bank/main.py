from re import L
from tkinter import *
import pyttsx3
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import qrcode
import time
from tkinter import messagebox
from PIL import ImageTk, Image
import cv2
from tkinter import filedialog
import os

root = Tk()
im1_0=Image.open('C:\\Users\\pc\\Desktop\\bload bank\\img\\logo2.jpg')
bn1_0=ImageTk.PhotoImage(im1_0)

root.iconbitmap('C:\\Users\\pc\\Desktop\\bload bank\\img\\ml.ico')
root.title('Bload Bank')
root.geometry('800x700+500+100')
lb1_0=Label(root , image=bn1_0)
lb1_0.place(x=0 ,y=0)
root.resizable(False,False)
wel = pyttsx3.init() # نجهز المكتبة
voices = wel.getProperty('voices')
wel.setProperty('voice',voices[1].id) # هات خاصة الصوت 

#------------def Speak-------------------
def Speak(audio):
    wel.say(audio) # اذا كان جاهز
    wel.runAndWait() # شغل وانتضر الاوامر مني 

#------------TakeCommands----------------
def TakeCommands():
    command= sr.Recognizer() # امر استدعاء
    with sr.Microphone() as mic:  # مع فتح المكرفون
        command.phrase_threshold= 0.1 # دقة التسجيل
        audio = command.listen(mic)
        try:
            query = command.recognize_google(audio, language='ar')
        except Exception as Error:
            print(Error)
        return query.lower()


#------------funcation for 🔊---------------------
def b1():
    query = TakeCommands()
    name = query
    E1.insert(0,name)
def b2():
    query = TakeCommands()
    name = query
    E2.insert(0,name)
def b3():
    query = TakeCommands()
    name = query
    E3.insert(0,name)
def b4():
    query = TakeCommands()
    name = query
    E4.insert(0,name)
def b5():
    query = TakeCommands()
    name = query
    E5.insert(0,name)
  
#------------Sv for save in picatuer 🖼----------------          
def Sv():
    namefile = E1.get()
    name = E1.get()
    co   = E2.get()
    job  = E3.get()
    job1 = E4.get()
    job2  = E5.get()
    sp='  ,  '
    go='   👍🏻'
    a1=' NAME : '
    a2=' , OLD : '
    a3=' , ADDERS : '
    a4=' , Quantity : '
    a5=' , PHAON : '
    info = qrcode.make(a1 + name + a2 + co + a3 + job + a4 + job1 + a5  + job2 + go)
    info.save('Donors//'+namefile+'.jpg')
    messagebox.showinfo('Save','Save [' +namefile+ '] Donors')

  
#--------------------- program Qr-code scanner 😍------------------
def Qr_code(): 
    
    window = Tk()
    window.geometry('310x435+500+100')
    window.iconbitmap('C:\\Users\\pc\\Desktop\\bload bank\\img\\ml.ico')
    window.title('Qr-code scanner')
#--------open ------------------
    def open():
        file = filedialog.askopenfile(mode='r',filetypes=[('Files','*.jpg')])
        if file:
            filepath =os.path.abspath(file.name)
            Ent1.insert(0,str(filepath))
#-------scan -------------------
    def scan():
        d = Ent1.get()
        res = cv2.QRCodeDetector()
        val , points , s_qr = res.detectAndDecode(cv2.imread(d))
        messagebox.showinfo('Qr-Scan',val)        


#------------start program Qr-code 😁

    #photo = PhotoImage(file='C:\\Users\\pc\\Desktop\\bload bank\\img\\logo 10.png')
    #imo = Label(window, image=photo)
    #imo.place(x=40,y=40,width=230,height=190)
    #lbl1.place(x=70,y=280)

    text = Label(window,text='QR_SCANNER',fg='white',bg='red')
    text.pack(fill=X)

    lbl1 = Label(window, text='QR-code Scanner',font=('Stencil',15)) 
    lbl1.place(x=40,y=40,width=230,height=190)
    
    Ent1 = Entry(window,font=('Tajawal',12),width=31)
    #Ent1.place(x=15,y=290)

    btn = Button(window, text='Select Image',fg='white',bg='red',width=30,font=('Tajawal',12),command=open)
    btn.place(x=10,y=340)

    btn1 = Button(window, text='Read QR-code',fg='white',bg='red',width=30,font=('Tajawal',12),command=scan)
    btn1.place(x=10,y=383)
    
    window.mainloop()

#-------------- end program Qr-code 😉

#----------start program blaod bank 😁
photo = PhotoImage(file='C:\\Users\\pc\\Desktop\\bload bank\\img\\W1.png') # حق الصورة
l_img = Label(root, image=photo)
l_img.place(x=100,y=5,width=330,height=150)

                          #Label-main
l = Label(root, text='Donors name :', fg='black',bg='white',font=('Stencil',12))
l.place(x=70,y=190)

l1 = Label(root, text='the age :', fg='black',bg='white',font=('Stencil',12))
l1.place(x=70,y=230)

l2 = Label(root, text='the address :', fg='black',bg='white',font=('Stencil',12))
l2.place(x=70,y=270)

l3 = Label(root, text='Quantity :', fg='black',bg='white',font=('Stencil',12))
l3.place(x=70,y=310)

l4 = Label(root, text='the phone :', fg='black',bg='white',font=('Stencil',12))
l4.place(x=70,y=350)

                        #Entry -main
E1 = Entry(root,font=('Tajawal',14))
E1.place(x=200,y=190)

E2 = Entry(root,font=('Tajawal',14))
E2.place(x=200,y=230)

E3 = Entry(root,font=('Tajawal',14))
E3.place(x=200,y=270)
 
E4 = Entry(root,font=('Tajawal',14))
E4.place(x=200,y=310)

E5 = Entry(root,font=('Tajawal',14))
E5.place(x=200,y=350)

                      #Button-main
b1=Button(root,text='🔊 ',bg='black',fg='white',font=('Tajawal',9),command=b1)
b1.place(x=410,y=190)

b2=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b2)
b2.place(x=410,y=230)

b3=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b3)
b3.place(x=410,y=270)

b4=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b4)
b4.place(x=410,y=310)

b4=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b5)
b4.place(x=410,y=350)

                      #Button - save-main
b_save=Button(root,text='Save ✔',fg='black',bg='white',font=('Stencil',10),command=Sv)
b_save.place(x=450,y=350)

b_save2=Button(root,text='Select code-Image',fg='white',bg='red',font=('Stencil',10),command=Qr_code )
b_save2.place(x=650,y=10)


root.mainloop()
#-------------- end program blaod bank 😉
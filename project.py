from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) # o for male, 1 for female

mixer.init()



mixer.music.load('panchkoti_mahamani.mp3')
mixer.music.play()

def select(event):
    ProgressbarA.place_forget()
    ProgressbarB.place_forget()
    ProgressbarC.place_forget()
    ProgressbarD.place_forget()
    
    PBarLAbelA.place_forget()
    PBarLAbelB.place_forget()
    PBarLAbelC.place_forget()
    PBarLAbelD.place_forget()
    b=event.widget
    value=b['text']
    
    CallBut.place_forget()
    

    for i in range(15):
        if value==AnsKey[i]:
            QuesArea.delete(1.0,END)
            QuesArea.insert(END, question[i+1])
            OptBut1.config(text=opt1[i+1])
            OptBut2.config(text=opt2[i+1])
            OptBut3.config(text=opt3[i+1])
            OptBut4.config(text=opt4[i+1])
            AmtLabel.config(image=AmtImg[i])

        if value==AnsKey[15]:
            root2=Toplevel()
            root2.overrideredirect(True)
            root2.config(bg='black')
            root2.geometry('500x400+140+30')
           
            LogLabel=Label(root2, image=logo, bd=0)
            LogLabel.pack(pady=30)
            mixer.music.load('kbcwon.mp3')
            mixer.music.play(-1)
            winLabel=Label(root2, text='CONGRATULATIONS! \n You Won the Game', 
                           font=('Cooper Black',20, 'bold'), bg='black', fg='gold')
            winLabel.pack()

            def Exit():
                root2.destroy()
                root.destroy()
            exitBut=Button(root2, text='EXIT', font=('arial', 15, 'bold'),pady=10, bg='black', fg='darkred', 
                           cursor='hand2', activebackground='black', activeforeground='white', command=Exit)
            exitBut.pack()

               
        if value not in AnsKey:
            def close():
                root1.destroy()
                root.destroy()


            def TryAgain():
                lifeline50Button.config(state=NORMAL, image=img50)
                AudPollButton.config(state=NORMAL,image=AudPoll)
                PhoneAFriendButton.config(state=NORMAL, image=PhoneAFriend)
                root1.destroy()
                QuesArea.delete(1.0, END)
                QuesArea.insert(END, question[0])
                OptBut1.config(text=opt1[0])
                OptBut2.config(text=opt2[0])
                OptBut3.config(text=opt3[0])
                OptBut4.config(text=opt4[0])
                AmtLabel.config(image=amount1)

            


            root1=Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title(' ')
            imgLabel=Label(root1, image=logo, bd=0)
            imgLabel.pack(pady=30)
            loseLabel=Label(root1, text='You Lost the Game \n Better Luck next time', 
                            font=('Cooper Black',20, 'bold'), bg='black', fg='white')
            loseLabel.pack()

            tryagainBut=Button(root1, text='Try Again', font=('arial', 15, 'bold'), 
                               bg='black', fg='white', cursor='hand2', 
                               bd=0, activebackground='black', activeforeground='white', command=TryAgain)
            tryagainBut.pack()

            closeBut=Button(root1, text='Close Game :(', font=('arial', 15, 'bold'), 
                            bg='black', fg='white', cursor='hand2', 
                            bd=0, activebackground='black', activeforeground='white', command=close)
            closeBut.pack()



            root1.mainloop()
            break # so that it doesn't run 15 times


#50-50 lifeline

def life50():
    mixer.music.load('netflix.mp3')
    mixer.music.play()
    lifeline50Button.config(image=img50x, state=DISABLED)
    if QuesArea.get(1.0,'end-1c')==question[0]:
        OptBut1.config(text=' ')
        OptBut4.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[1]:
        OptBut1.config(text=' ')
        OptBut3.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[2]:
        OptBut4.config(text=' ')
        OptBut2.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[3]:
        OptBut1.config(text=' ')
        OptBut4.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[4]:
        OptBut2.config(text=' ')
        OptBut4.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[5]:
        OptBut2.config(text=' ')
        OptBut1.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[6]:
        OptBut1.config(text=' ')
        OptBut2.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[7]:
        OptBut1.config(text=' ')
        OptBut3.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[8]:
        OptBut3.config(text=' ')
        OptBut2.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[9]:
        OptBut3.config(text=' ')
        OptBut4.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[10]:
        OptBut1.config(text=' ')
        OptBut4.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[11]:
        OptBut3.config(text=' ')
        OptBut4.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[12]:
        OptBut2.config(text=' ')
        OptBut4.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[13]:
        OptBut3.config(text=' ')
        OptBut4.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[14]:
        OptBut1.config(text=' ')
        OptBut2.config(text=' ')
    if QuesArea.get(1.0,'end-1c')==question[15]:
        OptBut1.config(text=' ')
        OptBut4.config(text=' ')



#Audience poll lifeline

def audPolLifeline():
    mixer.music.load('audience-poll_53mp5bCl.mp3')
    mixer.music.play()
    AudPollButton.config(image=AudPollX, state=DISABLED)
    ProgressbarA.place(x=580,y=190)
    ProgressbarB.place(x=620,y=190)
    ProgressbarC.place(x=660,y=190)
    ProgressbarD.place(x=700,y=190)

    PBarLAbelA.place(x=580, y=320)
    PBarLAbelB.place(x=620, y=320)
    PBarLAbelC.place(x=660, y=320)
    PBarLAbelD.place(x=700, y=320)

    if QuesArea.get(1.0, 'end-1c')==question[0]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=40)
        ProgressbarC.config(value=90)
        ProgressbarD.config(value=40)
    if QuesArea.get(1.0, 'end-1c')==question[1]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=40)
        ProgressbarC.config(value=20)
        ProgressbarD.config(value=90)
    if QuesArea.get(1.0, 'end-1c')==question[2]:
        ProgressbarA.config(value=90)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=30)
        ProgressbarD.config(value=50)
    if QuesArea.get(1.0, 'end-1c')==question[3]:
        ProgressbarA.config(value=20)
        ProgressbarB.config(value=90)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=40)
    if QuesArea.get(1.0, 'end-1c')==question[4]:
        ProgressbarA.config(value=40)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=95)
        ProgressbarD.config(value=20)
    if QuesArea.get(1.0, 'end-1c')==question[5]:
        ProgressbarA.config(value=0)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=40)
        ProgressbarD.config(value=98)
    if QuesArea.get(1.0, 'end-1c')==question[6]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=40)
        ProgressbarC.config(value=20)
        ProgressbarD.config(value=90)
    if QuesArea.get(1.0, 'end-1c')==question[7]:
        ProgressbarA.config(value=25)
        ProgressbarB.config(value=40)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=95)
    if QuesArea.get(1.0, 'end-1c')==question[8]:
        ProgressbarA.config(value=20)
        ProgressbarB.config(value=40)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=85)
    if QuesArea.get(1.0, 'end-1c')==question[9]:
        ProgressbarA.config(value=70)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=30)
        ProgressbarD.config(value=25)
    if QuesArea.get(1.0, 'end-1c')==question[10]:
        ProgressbarA.config(value=40)
        ProgressbarB.config(value=90)
        ProgressbarC.config(value=50)
        ProgressbarD.config(value=40)
    if QuesArea.get(1.0, 'end-1c')==question[11]:
        ProgressbarA.config(value=20)
        ProgressbarB.config(value=80)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=5)
    if QuesArea.get(1.0, 'end-1c')==question[12]:
        ProgressbarA.config(value=10)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=50)
        ProgressbarD.config(value=20)
    if QuesArea.get(1.0, 'end-1c')==question[13]:
        ProgressbarA.config(value=90)
        ProgressbarB.config(value=2)
        ProgressbarC.config(value=30)
        ProgressbarD.config(value=40)
    if QuesArea.get(1.0, 'end-1c')==question[14]:
        ProgressbarA.config(value=70)
        ProgressbarB.config(value=40)
        ProgressbarC.config(value=20)
        ProgressbarD.config(value=90)
    if QuesArea.get(1.0, 'end-1c')==question[15]:
        ProgressbarA.config(value=70)
        ProgressbarB.config(value=90)
        ProgressbarC.config(value=40)
        ProgressbarD.config(value=10)

#phone a friend lifeline

def PhoneLifeline():
    CallBut.place(x=70, y=260)
    PhoneAFriendButton.config(image=PhoneAFriendX, state=DISABLED)
    mixer.music.load('kbc-idea-phone-a-frd-1_kTEpiLHQ.mp3')
    mixer.music.play()

def PhoneClick():
    for i in range(16):
        if QuesArea.get(1.0, 'end-1c')==question[i]:
            engine.say(f'the answer is {AnsKey[i]}')
            engine.runAndWait()

#Answer key
AnsKey=["Indira Gandhi \nInstitute of Technology","Nile","Param8000","Chinese","Kharai","Manmohan Singh","Secured loan",
        "Aam Aadmi Party","25","Nitrogen","Wind Power","United States","Virendra Sehwag","22 April","Halloween","Gabbar"]

#List of questions

question=["IGDTUW was formerly known as?", "Which is the longest river in the world?", "India\'s first super computer is: ", 
          "Which is the most widely spoken \nlanguage in the world?","what kind of camel can swim?","who amongst them is NOT a \nstand up comdeian?",
          "What is the term used to describe a \nloan that is backed by collateral?","What is the name of the political \nparty founded by Arvind Kejriwal?",
          " What is the minimum age for \nbecoming a member of the Lok Sabha?","What is the most abundant \ngas in the Earth\'s atmosphere?", 
          "Which of the following is a \nrenewable energy source?","Which country has won the most \nOlympic gold medals?",
          "Which Indian cricketer has the \nhighest individual score in Test cricket?","When is Earth Day celebrated?",
          "What day is celebrated on October \n31st every year?","who said the famous dialoge \n\' Ye hath mujhe dede Thakur\'?"]


#Different list of options

opt1=["Indira Gandhi \nDelhi University","Congo river","Param8000","English","Dromedory","Anubhav Singh Bassi","Installment loan",
      "National Trinamool \nCongress","18","Nitrogen","Nuclear Energy","China","Rahul Dravid","22 April","Laughter day","Jai"]

opt2=["Indira Gandhi \nEngineering College","Yamuna","AIRAWAT","Chinese","cama","Aakash Gupta","Recourse Loan","Akhil Bhartiya \nVidya Parishad",
      "21","Oxygen","Wind Power","United States","Virat Kohli","22 January","Peace Day","Gabbar"]

opt3=["Indira Gandhi \nInstitute of Technology","Amazon River","Param800","German","Kharai","Zakir Khan","Credit Collateral","Bhartiya Janta Party",
      "30","Carbon Dioxide","Natural Gas","India","Virendra Sehwag","22 March","Diwali","veeru"]

opt4=["Indira Gandhi \nTechnical Insititue","Nile","Mihir","French","None of \nthe above","Manmohan Singh","Secured loan","Aam Aadmi Party",
      "25","Helium","Coal","Soviet Union","Sachin tendulkar","22 May","Halloween","Sambha"]

#('height x width + distance from origin)

root=Tk()
root.geometry('1270x650+0+0') 
root.title('KAUN BANEGA CROREPATI By Sommay Shivangi')

root.config(bg='black') # background color

#Frames

leftframe=Frame(root, padx=90, bg='black')
leftframe.grid(row=0, column=0) #by default counted as 0

topframe=Frame(leftframe, pady=15, bg='black')
topframe.grid(row=0, column=0)

centreframe=Frame(leftframe, pady=15, bg='black')
centreframe.grid(row=1, column=0)

bottomframe=Frame(leftframe)
bottomframe.grid(row=2, column=0)

rightframe=Frame(root, pady=25, padx=50, bg='black')
rightframe.grid(row=0, column=1)


#Images

img50=PhotoImage(file='50-50.png')
img50x=PhotoImage(file='50-50-X.png')
AudPoll=PhotoImage(file='audiencePole.png')
AudPollX=PhotoImage(file='audiencePoleX.png')
PhoneAFriend=PhotoImage(file='phoneAFriend.png')
PhoneAFriendX=PhotoImage(file='phoneAFriendX.png')
CallImg=PhotoImage(file='telep.png')
logo=PhotoImage(file='logo.png')
layout=PhotoImage(file='lay.png')

amount1=PhotoImage(file='Picture0.png')
amount2=PhotoImage(file='Picture1.png')
amount3=PhotoImage(file='Picture2.png')
amount4=PhotoImage(file='Picture3.png')
amount5=PhotoImage(file='Picture4.png')
amount6=PhotoImage(file='Picture5.png')
amount7=PhotoImage(file='Picture6.png')
amount8=PhotoImage(file='Picture7.png')
amount9=PhotoImage(file='Picture8.png')
amount10=PhotoImage(file='Picture9.png')
amount11=PhotoImage(file='Picture10.png')
amount12=PhotoImage(file='Picture11.png')
amount13=PhotoImage(file='Picture12.png')
amount14=PhotoImage(file='Picture13.png')
amount15=PhotoImage(file='Picture14.png')
amount16=PhotoImage(file='Picture15.png')

AmtImg=[amount2, amount3, amount4, amount5, amount6, amount7, amount8, amount9, 
        amount10, amount11, amount12, amount13, amount14, amount15, amount16]

#Buttons and Labels

lifeline50Button=Button(topframe, image=img50, bg='black', bd=0, 
                        activebackground='black', width=180, height=80, command=life50)
lifeline50Button.grid(row=0, column=0) 

AudPollButton=Button(topframe, image=AudPoll, bg='black', bd=0, 
                     activebackground='black', width=180, height=80, command=audPolLifeline)
AudPollButton.grid(row=0, column=1) 

PhoneAFriendButton=Button(topframe, image=PhoneAFriend, bg='black', bd=0, 
                          activebackground='black', width=180, height=80, command=PhoneLifeline)
PhoneAFriendButton.grid(row=0, column=2) 

CallBut=Button(root, image=CallImg, bd=0, bg='Black', 
               activebackground='black',width=150,height= 70, cursor='hand2', command=PhoneClick)

logoLabel=Label(centreframe, image=logo, bg='black', width=300, height=200) 
logoLabel.grid(row=0, column=0) 

AmtLabel=Label(rightframe, image=amount1, bg='black') 
AmtLabel.grid(row=0, column=0) 

layoutLabel=Label(bottomframe, image=layout, bg='black') 
layoutLabel.grid(row=0, column=0) 


#questions in display

QuesArea=Text(bottomframe, font=('Cooper Black',15), width=30, 
              height=2, pady=5, wrap='word',bg='black', fg='white', bd=0) 
QuesArea.place(x=70, y=10)

QuesArea.insert(END, question[0])


#option no. in display

labelA=Label(bottomframe, text='A. ', bg='black', bd=0, fg='white', font=('arial', 10, 'bold'))
labelA.place(x=60, y=110)

labelb=Label(bottomframe, text='B. ', bg='black', bd=0, fg='white', font=('arial', 10, 'bold'))
labelb.place(x=330, y=110)

labelc=Label(bottomframe, text='C. ', bg='black', bd=0, fg='white', font=('arial', 10, 'bold'))
labelc.place(x=60, y=190)

labeld=Label(bottomframe, text='D. ', bg='black', bd=0, fg='white', font=('arial', 10, 'bold'))
labeld.place(x=330, y=190)


#option button in display

OptBut1=Button(bottomframe, text=opt1[0], font=('arial', 10, 'bold'), bg='black', fg='white', 
               bd=0, activebackground='black', activeforeground='white', cursor='hand2')
OptBut1.place(x=100, y=100)

OptBut2=Button(bottomframe, text=opt2[0], font=('arial', 10, 'bold'), bg='black', fg='white', 
               bd=0, activebackground='black', activeforeground='white', cursor='hand2')
OptBut2.place(x=370, y=100)

OptBut3=Button(bottomframe, text=opt3[0], font=('arial', 10, 'bold'), bg='black', fg='white', 
               bd=0, activebackground='black', activeforeground='white', cursor='hand2')
OptBut3.place(x=100, y=180)

OptBut4=Button(bottomframe, text=opt4[0], font=('arial', 10, 'bold'), bg='black', fg='white', 
               bd=0, activebackground='black', activeforeground='white', cursor='hand2')
OptBut4.place(x=370, y=180)

ProgressbarA=Progressbar(root, orient=VERTICAL, length=120)
ProgressbarB=Progressbar(root, orient=VERTICAL, length=120)
ProgressbarC=Progressbar(root, orient=VERTICAL, length=120)
ProgressbarD=Progressbar(root, orient=VERTICAL, length=120)

PBarLAbelA=Label(root, text='A', font=('arial',20, 'bold'),bg='black',fg='white')
PBarLAbelB=Label(root, text='B', font=('arial',20, 'bold'),bg='black',fg='white')
PBarLAbelC=Label(root, text='C', font=('arial',20, 'bold'),bg='black',fg='white')
PBarLAbelD=Label(root, text='D', font=('arial',20, 'bold'),bg='black',fg='white')


OptBut1.bind('<Button-1>',select)
OptBut2.bind('<Button-1>',select)
OptBut3.bind('<Button-1>',select)
OptBut4.bind('<Button-1>',select)
root.mainloop()




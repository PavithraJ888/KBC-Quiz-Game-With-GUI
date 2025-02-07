from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

mixer.init()
mixer.music.load("Images and Audio/kbc.mp3")
mixer.music.play(-1)
  
# Function to handle the button click events
def select(event):
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()
    progressbarlabelA.place_forget()
    progressbarlabelB.place_forget()
    progressbarlabelC.place_forget()
    progressbarlabelD.place_forget()
    b = event.widget
    value = b['text']
    for i in range(15):
        if value == correct_answers[i]:
            if value==correct_answers[14]:
                def close():
                    root2.destroy()
                    root.destroy()
                def playagain():
                    mixer.music.stop()
                    mixer.music.load("Images and Audio/kbc.mp3")
                    mixer.music.play()
                    lifeline50Button.config(state=NORMAL,image=image50)
                    phoneoffriendButton.config(state=NORMAL,image=phoneoffriend)
                    audienecepollButton.config(state=NORMAL,image= audiencepoll)
                    root2.destroy()
                    questionarea.delete(1.0, END)
                    questionarea.insert(END,questions[0])
                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    amountLabel.config(image=money_tree_images[0])

                mixer.music.stop()
                mixer.music.load("Images and Audio/kbcwon.mp3")
                mixer.music.play()
                root2=Toplevel()
                root2.overrideredirect(True)
                root2.config(bg="black",)
                root2.geometry("500x400+140+30")
                root2.title("You won 0 Rupees")
                imgLabel=Label(root2,image=logoimage,bd=0,width=370,height=240)
                imgLabel.pack(pady=10)
                winLabel=Label(root2,text="YOU WON",font=("arial",37,"bold"),bg="black",fg="white")
                winLabel.pack()
                playagainButtom=Button(root2,text="PLAY AGAIN",font=("arail",20,"bold"),bg="black",fg="white",bd=0,activebackground="black",activeforeground="white",cursor="hand2",command=playagain)
                playagainButtom.pack()
                closeButtom=Button(root2,text="CLOSE",font=("arail",15,"bold"),bg="black",fg="white",bd=0,activebackground="black",activeforeground="white",cursor="hand2",command=close)
                closeButtom.pack()
                happyimage1=PhotoImage(file="Images and Audio/Happy.png")
                happylabel1=Label(root2,image=happyimage1,bd=0)
                happylabel1.place(x=35,y=320)
                happyimage=PhotoImage(file="Images and Audio/Happy.png")
                happylabel=Label(root2,image=happyimage,bd=0)
                happylabel.place(x=370,y=320)
                root2.mainloop()
                break
                

            questionarea.delete(1.0, END)
            questionarea.insert(END, questions[i + 1])

            optionButton1.config(text=first_option[i + 1])
            optionButton2.config(text=second_option[i + 1])
            optionButton3.config(text=third_option[i + 1])
            optionButton4.config(text=fourth_option[i + 1])
            amountLabel.config(image=money_tree_images[i+1])  # Update the image based on the answer
        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()
            def tryagain():
                mixer.music.play()
                lifeline50Button.config(state=NORMAL,image=image50)
                phoneoffriendButton.config(state=NORMAL,image=phoneoffriend)
                audienecepollButton.config(state=NORMAL,image= audiencepoll)
                root1.destroy()
                questionarea.delete(1.0, END)
                questionarea.insert(END,questions[0])
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                amountLabel.config(image=money_tree_images[0])

                
            root1=Toplevel()
            root1.overrideredirect(True)
            root1.config(bg="black",)
            root1.geometry("500x400+140+30")
            root1.title("You won 0 Rupees")
            imgLabel=Label(root1,image=logoimage,bd=0,width=370,height=240)
            imgLabel.pack(pady=10)
            loseLabel=Label(root1,text="YOU LOSE",font=("arial",37,"bold"),bg="black",fg="white")
            loseLabel.pack()
            tryagainButtom=Button(root1,text="TRY AGAIN",font=("arail",20,"bold"),bg="black",fg="white",bd=0,activebackground="black",activeforeground="white",cursor="hand2",command=tryagain)
            tryagainButtom.pack()
            closeButtom=Button(root1,text="CLOSE",font=("arail",15,"bold"),bg="black",fg="white",bd=0,activebackground="black",activeforeground="white",cursor="hand2",command=close)
            closeButtom.pack()
            sadimage1=PhotoImage(file="Images and Audio/sad.png")
            sadlabel1=Label(root1,image=sadimage1,bd=0)
            sadlabel1.place(x=35,y=320)
            sadimage=PhotoImage(file="Images and Audio/sad.png")
            sadlabel=Label(root1,image=sadimage,bd=0)
            sadlabel.place(x=370,y=320)
            root1.mainloop()
            break
def lifeline5050():
    lifeline50Button.config(image=image50X,state=DISABLED)
    if questionarea.get(1.0,'end-1c')==questions[0]:
        optionButton2.config(text='')
        optionButton4.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[1]:
        optionButton1.config(text='')
        optionButton4.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[2]:
        optionButton2.config(text='')
        optionButton3.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[3]:
        optionButton2.config(text='')
        optionButton4.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[4]:
        optionButton3.config(text='')
        optionButton4.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[5]:
        optionButton1.config(text='')
        optionButton4.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[6]:
        optionButton2.config(text='')
        optionButton4.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[7]:
        optionButton3.config(text='')
        optionButton4.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[8]:
        optionButton3.config(text='')
        optionButton4.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[9]:
        optionButton2.config(text='')
        optionButton1.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[10]:
        optionButton1.config(text='')
        optionButton3.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[11]:
        optionButton1.config(text='')
        optionButton4.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[12]:
        optionButton3.config(text='')
        optionButton4.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[13]:
        optionButton2.config(text='')
        optionButton3.config(text='')
    if questionarea.get(1.0,'end-1c')==questions[14]:
        optionButton2.config(text='')
        optionButton3.config(text='')
    mixer.music.play()
def audiencepolllifeline():
    audienecepollButton.config(image=audiencepollX,state=DISABLED)
    progressbarA.place(x=680,y=190)
    progressbarB.place(x=720,y=190)
    progressbarC.place(x=760,y=190)
    progressbarD.place(x=800,y=190)

    progressbarlabelA.place(x=680,y=350)
    progressbarlabelB.place(x=720,y=350)
    progressbarlabelC.place(x=760,y=350)
    progressbarlabelD.place(x=800,y=350)

    if questionarea.get(1.0,"end-1c")==questions[0]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=70)
        progressbarD.config(value=20)
    if questionarea.get(1.0,"end-1c")==questions[1]:
        progressbarA.config(value=40)
        progressbarB.config(value=80)
        progressbarC.config(value=60)
        progressbarD.config(value=50)
    if questionarea.get(1.0,"end-1c")==questions[2]:
        progressbarA.config(value=20)
        progressbarB.config(value=40)
        progressbarC.config(value=45)
        progressbarD.config(value=90)
    if questionarea.get(1.0,"end-1c")==questions[3]:
        progressbarA.config(value=60)
        progressbarB.config(value=42)
        progressbarC.config(value=90)
        progressbarD.config(value=20)
    if questionarea.get(1.0,"end-1c")==questions[4]:
        progressbarA.config(value=94)
        progressbarB.config(value=50)
        progressbarC.config(value=70)
        progressbarD.config(value=37)
    if questionarea.get(1.0,"end-1c")==questions[5]:
        progressbarA.config(value=50)
        progressbarB.config(value=70)
        progressbarC.config(value=40)
        progressbarD.config(value=20)
    if questionarea.get(1.0,"end-1c")==questions[6]:
        progressbarA.config(value=20)
        progressbarB.config(value=40)
        progressbarC.config(value=90)
        progressbarD.config(value=70)
    if questionarea.get(1.0,"end-1c")==questions[7]:
        progressbarA.config(value=40)
        progressbarB.config(value=80)
        progressbarC.config(value=45)
        progressbarD.config(value=20)
    if questionarea.get(1.0,"end-1c")==questions[8]:
        progressbarA.config(value=85)
        progressbarB.config(value=40)
        progressbarC.config(value=70)
        progressbarD.config(value=20)
    if questionarea.get(1.0,"end-1c")==questions[9]:
        progressbarA.config(value=50)
        progressbarB.config(value=60)
        progressbarC.config(value=30)
        progressbarD.config(value=90)
    if questionarea.get(1.0,"end-1c")==questions[10]:
        progressbarA.config(value=40)
        progressbarB.config(value=90)
        progressbarC.config(value=30)
        progressbarD.config(value=55)
    if questionarea.get(1.0,"end-1c")==questions[11]:
        progressbarA.config(value=40)
        progressbarB.config(value=70)
        progressbarC.config(value=20)
        progressbarD.config(value=40)
    if questionarea.get(1.0,"end-1c")==questions[12]:
        progressbarA.config(value=88)
        progressbarB.config(value=55)
        progressbarC.config(value=40)
        progressbarD.config(value=60)
    if questionarea.get(1.0,"end-1c")==questions[13]:
        progressbarA.config(value=50)
        progressbarB.config(value=40)
        progressbarC.config(value=45)
        progressbarD.config(value=90)
    if questionarea.get(1.0,"end-1c")==questions[14]:
        progressbarA.config(value=42)
        progressbarB.config(value=35)
        progressbarC.config(value=40)
        progressbarD.config(value=80)
    mixer.music.play()
def phoneofffriendlifeline():
    mixer.music.load("Images and Audio/calling.mp3")
    mixer.music.play()
    callButton.place(x=70,y=260)
    phoneoffriendButton.config(image=phoneoffriendX,state=DISABLED)

def phoneclick():
    for i in range(15):
        if questionarea.get(1.0,'end-1c')==questions[i]: 
            engine.say(f"Hi Thank you for calling me The answer is {correct_answers[i]}")
            engine.runAndWait()
    mixer.music.load("Images and Audio/kbc.mp3")
    mixer.music.play()
# Correct answers for each question
correct_answers = ["Dosa", "Neil Armstrong", "Skin", "Mercury",
                   "1000 rupees", "42", "Google", "1950", "Au",
                   "Agra", "W.Shakespeare",
                   "Blue Whale", "Paris", "Time", "Switzerland"]

# Questions
questions = ["which of these is not a Gujarati snack?",
             "Who was the first man to step on the moon?",
             "Which is the largest organ in the human body?",
             " Which planet is closest to the sun?",
             "If two pencils cost 20 rupees, how much would 100 pencils cost?",
             "Which number comes next in the sequence? 2, 6, 12, 20, 30, __?",
             "Which company is known for its search engine and has the motto Don’t be evil?",
             "In which year did India become a republic?",
             " What is the chemical symbol for gold?",
             "Which city is famous for the Taj Mahal?",
             "Who wrote the famous play Romeo and Juliet?",
             "What is the largest mammal in the world?",
             "What is the capital of France?",
             "The purpose of an hourglass is to measure which of these?",
             "Which country is the largest producer of chocolate?"]

# Option sets
first_option = ["Dosa", "Buzz Aldrin", "Heart", "Earth",
                "1000 rupees", "36", "Microsoft", "1947",
                "Au", "Mumbai", "Charles Dickens", "Elephant", "Paris",
                "Weight", "France"]
second_option = ["Dhokla", "Neil Armstrong", "Brain", "Venus",
                 "900 rupees", "42", "Facebook", "1950", "Ag",
                 "Kolkata", "W.Shakespeare",
                 "Blue Whale", "Rome", "Distance", "Belgium"]
third_option = ["Khaman", "Yuri Gagarin","Liver", "Mercury",
                "100 rupees", "40", "Google", "1942", "Pb",
                "Delhi", "Jane Austen", "Giraffe", "Madrid",
                "Temperature","Ivory Coast"]
fourth_option = ["Fafda", "John Glenn", "Skin", "Mars",
                 "200 rupees", "38", "Apple", "1952", "Fe",
                 "Agra", "Leo Tolstoy", "Hippopotamus", "Berlin",
                 "Time", "Switzerland"]

# Create the main window
root = Tk()
root.geometry('1470x1620+0+0')
root.title("Kaun Benega Corepathi")
root.config(bg='black')

# Frames for layout
leftframe = Frame(root, bg='black', padx=70)
leftframe.grid(row=0, column=0, sticky="nsew")
topFrame = Frame(leftframe, bg='black', pady=10)
topFrame.grid(row=0, column=0, sticky="nsew")
centerFrame = Frame(leftframe, bg='black', pady=4, padx=240)
centerFrame.grid(row=1, column=0, sticky="nsew")
bottomFrame = Frame(leftframe, bg='black', pady=4, padx=80)
bottomFrame.grid(row=2, column=0, sticky="nsew")
rightframe = Frame(root, bg='black',pady=20,padx=5)
rightframe.grid(row=0, column=1, sticky="snew")

audiencepoll=PhotoImage(file='Images and Audio/AudiencePoll.png')
audiencepollX=PhotoImage(file='Images and Audio/AudiencePoll(X).png')
audienecepollButton=Button(topFrame,image=audiencepoll,bg='black',bd=0,activebackground='black',width=240,height=120,command=audiencepolllifeline)
audienecepollButton.grid(row=0,column=0)
phoneoffriend=PhotoImage(file='Images and Audio/PhoneOfFriend.png')
phoneoffriendX=PhotoImage(file='Images and Audio/PhoneOfFriend(X).png')
phoneoffriendButton=Button(topFrame,image=phoneoffriend,bg='black',bd=0,activebackground='black',width=240,height=120,command=phoneofffriendlifeline)
phoneoffriendButton.grid(row=0,column=1)
callimage=PhotoImage(file="Images and Audio/phone.png")
callButton=Button(root,image=callimage,bd=0,bg="black",activebackground="black",cursor="hand2",command=phoneclick)
image50=PhotoImage(file='Images and Audio/50-50.png')
image50X=PhotoImage(file='Images and Audio/50-50(X).png')
lifeline50Button=Button(topFrame,image=image50,bg='black',bd=0,activebackground='black',width=240,height=120,command=lifeline5050)
lifeline50Button.grid(row=0,column=2)
logoimage=PhotoImage(file='Images and Audio/logo(kbc).png')
logoLabel=Label(centerFrame,image=logoimage,bg='black',width=260,height=240)
logoLabel.grid(row=0,column=0)
# Load images
money_tree_image = Image.open('Images and Audio/Money Tree.png')
money_tree_image1 = Image.open('Images and Audio/Money Tree1.png')
money_tree_image2 = Image.open('Images and Audio/Money Tree2.png')
money_tree_image3 = Image.open('Images and Audio/Money Tree3.png')
money_tree_image4 = Image.open('Images and Audio/Money Tree4.png')
money_tree_image5 = Image.open('Images and Audio/Money Tree5.png')
money_tree_image6 = Image.open('Images and Audio/Money Tree6.png')
money_tree_image7 = Image.open('Images and Audio/Money Tree7.png')
money_tree_image8 = Image.open('Images and Audio/Money Tree8.png')
money_tree_image9 = Image.open('Images and Audio/Money Tree9.png')
money_tree_image10 = Image.open('Images and Audio/Money Tree10.png')
money_tree_image11 = Image.open('Images and Audio/Money Tree11.png')
money_tree_image12 = Image.open('Images and Audio/Money Tree12.png')
money_tree_image13 = Image.open('Images and Audio/Money Tree13.png')
money_tree_image14 = Image.open('Images and Audio/Money Tree14.png')
money_tree_image15 = Image.open('Images and Audio/Money Tree15.png')

# Convert images to PhotoImage objects
money_tree_images = [
    ImageTk.PhotoImage(money_tree_image),
    ImageTk.PhotoImage(money_tree_image1),
    ImageTk.PhotoImage(money_tree_image2),
    ImageTk.PhotoImage(money_tree_image3),
    ImageTk.PhotoImage(money_tree_image4),
    ImageTk.PhotoImage(money_tree_image5),
    ImageTk.PhotoImage(money_tree_image6),
    ImageTk.PhotoImage(money_tree_image7),
    ImageTk.PhotoImage(money_tree_image8),
    ImageTk.PhotoImage(money_tree_image9),
    ImageTk.PhotoImage(money_tree_image10),
    ImageTk.PhotoImage(money_tree_image11),
    ImageTk.PhotoImage(money_tree_image12),
    ImageTk.PhotoImage(money_tree_image13),
    ImageTk.PhotoImage(money_tree_image14),
    ImageTk.PhotoImage(money_tree_image15)
]

# Amount label that shows the money tree images
amountLabel = Label(rightframe, image=money_tree_images[0], bg='black')
amountLabel.grid(row=0, column=0, sticky="nsew")

# Layout image at the bottom
layoutimage = PhotoImage(file="Images and Audio/lay.png")
layoutlabel = Label(bottomFrame, image=layoutimage, bg='black')
layoutlabel.grid(row=0, column=0)

# Question area (Text widget)
questionarea = Text(bottomFrame, font=('arial', 18, 'bold'), width=34, height=2, wrap='word', bg='black', fg='white', bd=0)
questionarea.place(x=70, y=10)
questionarea.insert(END, questions[0])

# Option buttons and their labels
labelA = Label(bottomFrame, text='A:', bg="black", fg="white", font=("arial", 16, "bold"), bd=0)
labelA.place(x=50, y=110)
optionButton1 = Button(bottomFrame, text=first_option[0], font=("arial", 18, "bold"), bg="black", fg="white", bd=0, activebackground="black", activeforeground="white", cursor="hand2")
optionButton1.place(x=70, y=100)

labelB = Label(bottomFrame, text='B:', bg="black", fg="white", font=("arial", 16, "bold"), bd=0)
labelB.place(x=330, y=110)
optionButton2 = Button(bottomFrame, text=second_option[0], font=("arial", 18, "bold"), bg="black", fg="white", bd=0, activebackground="black", activeforeground="white", cursor="hand2")
optionButton2.place(x=350, y=100)

labelC = Label(bottomFrame, text='C:', bg="black", fg="white", font=("arial", 16, "bold"), bd=0)
labelC.place(x=50, y=190)
optionButton3 = Button(bottomFrame, text=third_option[0], font=("arial", 18, "bold"), bg="black", fg="white", bd=0, activebackground="black", activeforeground="white", cursor="hand2")
optionButton3.place(x=70, y=180)

labelD = Label(bottomFrame, text='D:', bg="black", fg="white", font=("arial", 16, "bold"), bd=0)
labelD.place(x=330, y=190)
optionButton4 = Button(bottomFrame, text=fourth_option[0], font=("arial", 18, "bold"), bg="black", fg="white", bd=0, activebackground="black", activeforeground="white", cursor="hand2")
optionButton4.place(x=350, y=180)

progressbarA=Progressbar(root,orient=VERTICAL,length=150)
progressbarB=Progressbar(root,orient=VERTICAL,length=150)
progressbarC=Progressbar(root,orient=VERTICAL,length=150)
progressbarD=Progressbar(root,orient=VERTICAL,length=150)

progressbarlabelA=Label(root,text='A',font=("arial",18,"bold"),bg="black",fg="white")
progressbarlabelB=Label(root,text='B',font=("arial",18,"bold"),bg="black",fg="white")
progressbarlabelC=Label(root,text='C',font=("arial",18,"bold"),bg="black",fg="white")
progressbarlabelD=Label(root,text='D',font=("arial",18,"bold"),bg="black",fg="white")

# Bind the buttons to the select function
optionButton1.bind('<Button>', select)
optionButton2.bind('<Button>', select)
optionButton3.bind('<Button>', select)
optionButton4.bind('<Button>', select)

# Start the Tkinter main loop
root.mainloop()
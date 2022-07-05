from tkinter import *
from tkinter import messagebox as mb
import csv

window = Tk()
window.geometry("800x600")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

##window.state('zoomed')class Quiz:

page1 = Frame(window, width=700, height=500)
page2 = Frame(window, width=700, height=500)
page3 = Frame(window, width=700, height=500)

for frame in (page1, page2, page3):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

def checkna():

#To Check user's name
    namea = name.get()
    while True:
        if all(letter.isalpha() or letter.isspace() for letter in namea):
            name_check = True
            break
        
        elif namea == "":
            mb.showwarning("Name is empty", "Please do not leave this field empty.")
            name_check = False
            break
                
        elif type(name) is not str:
            mb.showwarning('Name is inappropriate', 'please enter your real name.')
            name_check = False
            break

    year_lv = yr_level.get()
    if year_lv == None:
        year_lv = 0
    
    while True:
        try:
            if year_lv <= 11 and year_lv >= 0:
                mb.showwarning("Age below range", "Sorry, you are too young for this quiz.")
                break

            elif year_lv >= 19:
                mb.showwarning("Age over range", "Sorry, you are too experienced for this quiz.")
                break

            elif year_lv <= 0:
                mb.showwarning("Age inappropriate", "Please enter your age in positive integers.")
                break

            else:
                if name_check == True:
                    show_frame(page2)
                    break

        except ValueError:
            mb.showwarning("Age inappropriate", "Please enter your age in integers")
        

show_frame(page1)
name = StringVar()
yr_level = IntVar()
 

# ============= Page 1 =========

pag1_label = Label(page1, text='Name', font=('Arial', 15, 'bold'))
pag1_label.place(x=50, y=100)

pag1_entry = Entry(page1,textvariable = name)
pag1_entry.place(x=170, y=106)

pag1_label2 = Label(page1, text='Yr_Level', font=('Arial', 15, 'bold'))
pag1_label2.place(x=50, y=150)

pag1_entry2 = Entry(page1,textvariable = yr_level)
pag1_entry2.place(x=170, y=155)

pg1_button = Button(page1, text='NEXT', font=('Arial', 13, 'bold'), command=checkna)
pg1_button.place(x=170, y=200)

pag1_label3 = Label(page1, text='Sign in to QuuizQuizz', font=('Times', 20, 'bold'))
pag1_label3.place(x=300, y=20)

# ======== Page 2 =========== 

pag2_label = Label(page2, fg = "#D284AC", text='WELCOME TO', font=('Arial', 30, 'bold'))
pag2_label.grid(row = 0,column=1)

openingtitle = Label(page2, fg = "#9A4794", text = "Science Quiz", font = ("Times", "40"))
openingtitle.grid(row = 2, column = 1)

opening_sub = Label(page2, fg = "#D284AC", text = "Welcome to Science quiz", font = ("Times", "20"))
opening_sub.grid(row = 3, column = 1)

login_registers = Label(page2, fg = "#D284AC", text = "Quiz",  font = ("Times", "20"))
login_registers.grid(row = 4, column = 1)

pg2_button = Button(page2, text='NEXT', font=('Arial', 13, 'bold'), command=lambda: show_frame(page3))
pg2_button.grid(row = 5, column = 1)

#show_frame(page2)

# ======== Page 3 ===========

page3.config(background='#E1B0DE')

##pag3_label = Label(page3, text='WELCOME TO PAGE 3', font=('Arial', 30, 'bold'))

##pag3_label.place(x=50, y=100)

#QUIZ NEEDS TO GO HERE

#storing questions in a list variable called q
q=["Question 1. What is the formula for water?",
   "Question 2. What is the study of life?",
   "Question 3. Who is the father of Genetics?",
   "Question 4. Who discovered Pencillin?",
   "Question 5. Who invented Telephone?",
   "Question 6. Who discorvered radio active material?"]

#storing answer options in options list
options=[
         ['1.H2O','2.NO2','3.CO2','4.H2O2'],
         ['1.Physics','2.Chemistry','3.Biology','4.Bio-Chemistry',],
         ['1.Gregor Mendel','2.Archimedes','3.Alexander','4.Rutherford'],
         ['1,Alex','2.Roentgen','3.Hamilton','4.Alexander Fleming'],
         ['1,Alex','2.Roentgen','3.Graham Bell','4.Alexander Fleming'],
         ['1,Alex','2.Madam Curie','3.Hamilton','4.Alexander Fleming']]

#storing the right questions in a list variable called a
a=[1,3,1,4,3,2]

class Quiz:

    def __init__(self):

        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):

        t = Label(page3, text="Women in Computing", width=50, bg="blue", fg="white", font=("times", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(page3, text=q[qn], width=60, font=("times", 16, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radiobtns(self):

        val = 0
        b = []
        yp = 150

        while val < 4:

            btn = Radiobutton(page3, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):

        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]

        for op in options[qn]:

              self.opts[val]['text'] = op
              val += 1

  

    def buttons(self):

        nbutton = Button(page3, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))
        nbutton.place(x=200,y=380)

        quitbutton = Button(page3, text="Quit", command=window.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
        quitbutton.place(x=380,y=380)

 

    def checkans(self, qn):

        if self.opt_selected.get() == a[qn]:
            mb.showinfo("Correct","Good job! You have answered this question correctly.")
            return True
        
        elif self.opt_selected.get()!= a[qn]:
            mb.showinfo("Incorrect","You can do better in the next question.")
            
    def nextbtn(self):
        while True:
            try:
                if self.checkans(self.qn):
                    self.correct += 1

                self.qn += 1

                if self.qn == len(q):
                    self.display_result()
                    break

                else:
                    self.display_options(self.qn)
                    break
            except IndexError:

                mb.showwarning("The End","This quiz has ended, thank you for playing!")
                break

    def display_result(self):

        score = int(self.correct / len(q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)

        mb.showinfo("Result", "\n".join([result, correct, wrong]))
        mname = name.get()
        myear = yr_level.get()
        row =  "Name:"+mname+" | "+"Score:"+str(score)

## -------writing score to file-------------
        
        with open('myscore.txt', 'a') as f:      
            f.write('\n'+(row))
## -------------------------------------

quiz=Quiz()

#window.mainloop()

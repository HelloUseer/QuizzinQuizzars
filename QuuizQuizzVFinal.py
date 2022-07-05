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
    
#Check user's year level
    year_lv = yr_level.get()
    if year_lv == None:
        year_lv = 0
    
    while True:
        try:
            if year_lv <= 8 and year_lv >= 1:
                mb.showwarning("Year Level below range", "Sorry, you are too young for this quiz.")
                break

            elif year_lv >= 14:
                mb.showwarning("Year Level over range", "Sorry, you are too experienced for this quiz.")
                break

            elif year_lv <= 0:
                mb.showwarning("Year Level inappropriate", "Please enter your age in positive integers.")
                break

            else:
                if name_check == True:
                    show_frame(page2)
                    break

        except ValueError:
            mb.showwarning("Year Level inappropriate", "Please enter your age in integers")
        

show_frame(page1)
name = StringVar()
yr_level = IntVar()
 

# ============= Page 1 =========

page1.config(background='#842D5B')

pag1_label = Label(page1, text='Name', font=('Arial', 15, 'bold'), fg = "black")
pag1_label.place(x=50, y=100)

pag1_entry = Entry(page1,textvariable = name)
pag1_entry.place(x=170, y=106)

pag1_label2 = Label(page1, text='Yr_Level', font=('Arial', 15, 'bold'), fg="black")
pag1_label2.place(x=50, y=150)

pag1_entry2 = Entry(page1,textvariable = yr_level)
pag1_entry2.place(x=170, y=155)

pg1_button = Button(page1, text='NEXT', font=('Arial', 13, 'bold'), fg="black", command=checkna)
pg1_button.place(x=170, y=200)

pag1_label3 = Label(page1, text='Sign in to QuuizQuizz', font=('Times', 20, 'bold'))
pag1_label3.place(x=300, y=20)

# ======== Page 2 ===========

page2.config(background='#842D5B')

#storing questions in a list variable called q
q=["Question 1. In which year was BDSC opened?",
   "Question 2. How many Whanaus do we have?",
   "Question 3. What does Whanau mean in english?",
   "Question 4. What does the 'B' in BDSC Our Way stand for?",
   "Question 5. Which is the correct address of our school?",
   "Question 6. What colour is Koru whanau?",
   "Question 7. Where is the Career Centre located?",
   "Question 8. What is the name of the national qualification system students year level 11 and above need to partake in?",
   "Question 9. What does NCEA stand for?",
   "Question 10. How many credits do you need in total to pass level 1 of NCEA?"]

#storing answer options in options list
options=[
         ['1.2004','2.2005','3.2002','4.2003'],
         ['1.3','2.5','3.6','4.4',],
         ['1.Extended family','2.Family','3.House','4.Home'],
         ['1.Brave','2.Be caring','3.Best','4.Be respectful'],
         ['1.39 Chapel Road','2.148 Chapel Road','3.575 Chapel Road','4.It is not on Chapel Road'],
         ['1.Purple','2.Green','3.Red','4.Blue'],
         ['1.Beside Britten Whanau','2.Above the canteen, inside the conference center','3.Between Canteen and Spirit Whanau','4.Above reception'],
         ['1.NZQA','2.IKEA','3.ICAS','4.NCEA'],
         ['1.Nation Certificate Education Award','2.Nationwide Certificates for Education Achievements','3.National Certificate of Education Achievement','4.New Zealand Qualifications Authority'],
         ['1.80 Credits','2.60 Credits','3.40 Credits','4.20 Credits']]

#storing the right questions in a list variable called a
a=[1,3,1,4,3,2,2,4,3,1]

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

        t = Label(page2, text="QuuizQuizz:How Much Do You Know About BDSC?", width=50, bg="#C2E9FB", fg="black", font=("times", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(page2, text=q[qn], width=60, font=("times", 16, "bold"), fg="black", anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radiobtns(self):

        val = 0
        b = []
        yp = 150

        while val < 4:

            btn = Radiobutton(page2, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
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

        nbutton = Button(page2, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))
        nbutton.place(x=200,y=380)

        quitbutton = Button(page2, text="Quit", command=window.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
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

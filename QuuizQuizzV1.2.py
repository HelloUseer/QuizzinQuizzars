# this program is a quiz program
# importing tkinter from external library

from tkinter import *
from tkinter import messagebox # importing messagebox to display messages like score

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

#storing explanations for each question
exp=[
    ["This is the correct answer for question 1:..."],
    ["This is the correct answer:for question 2:..."],
    ["This is the correct answer:for question 3:..."],
    ["This is the correct answer:for question 4:..."],
    ["This is the correct answer:for question 5:..."],
    ["This is the correct answer:for question 6:..."]]

#to run the window called root
root = Tk()

#setting the window measurements
root.geometry("800x500")

#calling the functions
root.title("Quiz")
 
#the quiz is under one class called Quiz. This creates an object
class Quiz:
#construction
    def __init__(self):
#Set answered questions to 0
        self.qn = 0

        self.ques = self.question(self.qn)
 
        self.opt_selected = IntVar()

        self.opts = self.radiobtns()

#Displaying the options according to the current question
        self.display_options(self.qn)

#Creating the buttons for next and quit
        self.buttons()

#Set amount of correct answers to 0
        self.correct = 0

#Choosing which example out of list of explanations to be displayable
        self.explanation = self.explntns(self.qn)

 

#Methods under the class called quiz
#to display the question
    def question(self, qn):

        t = Label(root, text="QuuizQuizz", width=50, bg="blue", fg="white", font=("times", 20, "bold"))

        t.place(x=0, y=2)

        qn = Label(root, text=q[qn], width=60, font=("times", 16, "bold"), anchor="w")

        qn.place(x=70, y=100)

        return qn

 
#to display radio buttons
    def radiobtns(self):

        val = 0

        b = []

        yp = 150

        while val < 4:

            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))

            b.append(btn)

            btn.place(x=100, y=yp)

            val += 1

            yp += 40

        return b

 
#display option list
    def display_options(self, qn):

        val = 0

        self.opt_selected.set(0)

        self.ques['text'] = q[qn]

        for op in options[qn]:

              self.opts[val]['text'] = op

              val += 1

   
                 
#to make a button to go to the next question or leave the program
    def buttons(self):

        nbutton = Button(root, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))

        nbutton.place(x=200,y=380)

        quitbutton = Button(root, text="Quit", command=root.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))

        quitbutton.place(x=380,y=380)

 
#to check if user selected answer is correct
    def checkans(self, qn):

        if self.opt_selected.get() == a[qn]:
             messagebox.showinfo("Correct","Good job! You have answered this question correctly.")
             return True
           
        elif self.opt_selected.get()!= a[qn]:
            messagebox.showinfo("Incorrect","You can find the explanation for this question at the end of this quiz.")
           
             
#To move on to the next question or display result
    def nextbtn(self):
       
       
       
        if self.checkans(self.qn):

            self.correct += 1

        self.qn += 1

        if self.qn == len(q):#display user's result if user has answered all the questions in dictionary named q

            self.display_result(self.qn)
         

        else:

            self.display_options(self.qn)#display the options for the next question            

#displaying the result message box
    def display_result(self,qn):

        score = int(self.correct / len(q) * 100)

        result = "Score: " + str(score) + "%"

        wc = len(q) - self.correct

        correct = "No. of correct answers: " + str(self.correct)

        wrong = "No. of wrong answers: " + str(wc)

        messagebox.showinfo("Result", "\n".join([result, correct, wrong]))


#to explain why correct answer is correct
    def display_explanations(self):

        self.explanation['text'] = exp[qn]
       
        if self.opt_selected.get() != a[qn]:
            messagebox.showinfo("You can check the explanation below.","/n".join(self.explanation))
            
           
        else:
            messagebox.showinfo("Congradulations","Good job, you have answered all questions correctly!")
           


quiz=Quiz()

root.mainloop()

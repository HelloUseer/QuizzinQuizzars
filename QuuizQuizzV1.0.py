# this program is a quiz program
# importing tkinter from external library

from tkinter import *
from tkinter import messagebox as mb # importing messagebox to display messages like score

#storing questions in a list variable called q
q=["Question 1. What is the first answer to this question?",

   "Question 2. What is the third answer to this question?",

   "Question 3. What is the first answer to this question?",

   "Question 4. What is the fourth answer to this question?",

   "Question 5. What is the first answer to this question?",

   "Question 6. What is the second answer to this question?"]

 
#storing answer options in options list 
options=[

         ['1.H2O','2.NO2','3.CO2','4.H2O2'],['1.Physics','2.Chemistry','3.Biology','4.Bio-Chemistry',],

         ['1.Gregor Mendel','2.Archimedes','3.Alexander','4.Rutherford'],['1,Alex','2.Roentgen','3.Hamilton','4.Alexander Fleming'],

         ['1','2','3','4'],['1','2','3','4']]

 
#storing the right questions in a list variable called a
a=[1,3,1,4,1,2]

#To store all the answer explanations
explntns=[
    ["This answer is correct because bala bala bala"],
    ["This answer is correct because bala bala bala..."],
    ["This answer is right because..."],
    ["This answer is the right answer because bala bala..."],
    ["This is the right answer because bala..."],
    ["This is correct because bla bla..."]]

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

##        self.images=images

      
        self.opt_selected = IntVar()

        self.opts = self.radiobtns()

#Displaying the options according to the current question
        self.display_options(self.qn)

#Creating the buttons for next and quit
        self.buttons()

#Set amount of correct answers to 0
        self.correct = 0

#Choosing which example out of list of explanations to be displayable
        self.display_explntns(self.qn)

 

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

             return True

       
#To move on to the next question or display result
    def nextbtn(self):

        if self.checkans(self.qn):

            self.correct += 1

        self.qn += 1

        if self.qn == len(q):#display user's result if user has answered all the questions in dictionary named q

            self.display_result()

        else:

            self.display_options(self.qn)#display the options for the next question            


#to explain why correct answer is correct
    def ansexpln(self):

        congrats = "Congratulations! You answered all the questions correctly!"
        explanation = explntns[qn]
        
        if self.opt_selected.get() == a[qn]:
            mb.showinfo("Congradulations","/n".join(congrats))
            
        else:
            mb.showinfo("You can check the explanation below.","/n".join(explanation))
            

#displaying the result message box
    def display_result(self):

        score = int(self.correct / len(q) * 100)

        result = "Your accuracy is: " + str(score) + "%"

        wc = len(q) - self.correct

        correct = "No. of correct answers: " + str(self.correct)

        wrong = "No. of wrong answers: " + str(wc)

        mb.showinfo("Result", "\n".join([result, correct, wrong]))




 

 

quiz=Quiz()

root.mainloop()

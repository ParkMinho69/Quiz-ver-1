from tkinter import *
import random

names = []
global questions_answers
asked =[]
score =0
questions_answers = {
  1:["According to Roman mythology, who was the father of Romulus and Remus?",#item1, index 0 will be the question
      'A wolf', #item 2, index 1 will be first choice
      'Mars', #item 3, index 2 will be first choice
      'King Numitor', #item 3, index 3 will ve first choice
      'Jupitor', #item 4, index 4 will be first choice
      ], #item 5, index 5 will be the postion of the right answer (index where the right answer sits), this will be our check if answer is correct or not
 }


class Quizstarter:
      def __init__ (self, parent):
        background_color="#c299ff"

        #frame set up
        self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #widgets go below
        self.intro_label = Label(self.quiz_frame, text=" ", bg="#c299ff")
        self.intro_label.grid(row=1, padx=20)

        self.intro_label = Label(self.quiz_frame, text=" ", bg="#c299ff")
        self.intro_label.grid(row=2, padx=20)

        self.intro_label = Label(self.quiz_frame, text=" ", bg="#c299ff")
        self.intro_label.grid(row=3, padx=20)

        self.intro_label = Label(self.quiz_frame, text=" ", bg="#c299ff")
        self.intro_label.grid(row=4, padx=20)

        # label to ask for permison to continue
        self.user_label = Label(self.quiz_frame, text="Would you like to continue:",bg="#c299ff")
        self.user_label.grid(row=5, padx=20, pady=10)

        #create yes Button
        self.yes_button = Button(self.quiz_frame, text="Yes", font=("mishka family", "13", "normal"), bg="#878CE3", command=self.name_collection)
        self.yes_button.grid(row=6, padx=12, pady=5,)
        
        #create No Button
        self.no_button = Button(self.quiz_frame, text="No", font=("mishka family", "13", "normal"), bg="#878CE3", command=self.name_collection)
        self.no_button.grid(row=7, padx=12, pady=5)



      def name_collection(self):
        self.yes_button.destroy()
        self.no_button.destroy()
        self.quiz_frame.destroy()
        #Quiz(root)

        
if __name__ == "__main__":
      root= Tk()
      root.title("Roman and Greek History")
      quiz_instance = Quizstarter(root)
      root.mainloop()#to make sure the window doesn't disappear  



class Quiz:
      def __init__ (self, parent):
        background_color="#c299ff"
        #frame set up
        self.quiz_frame =Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #question
        self.questions_label=Label(self.quiz_frame, text=questions_answers[qnum][0],fomt=("Tw Cen MT", "16"),bg=background_color)
        self.questions_label.grid(row=1, padx=10, pady=10)

        #holds value of radio buttons
        self.varl=IntVar()

        #holds the value of the radio buttons
        self.varl=IntVar()

        #radio button 1
        self.rb1 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.varl1, padx=10,pady=10)
        self.rb1.grid(row=1, sticky=W)

        #radio button 2
        self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, variable=self.varl1, padx=10, pady=10)
        self.rb2.grid(row=2, sticky=W)

        #radio button 3
        self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, variable=self.varl1, padx=10,pady=10)
        self.rb3.grid(row=3, sticky=W)

        #radio button 4
        self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, variable=self.varl1, padx=10, pady=10)
        self.rb4.grid(row=4, sticky=W)

        #confirm button
        self.quiz_instance= Button(self.quiz_frame, text="Confirm", font=("Helvetica", "12", "bold"), bg="blue")
                    
        #score label 
        self.score_label = Label(self.quiz_frame, text="SCORE", font=("Tm Cen MT","12"), bg=background_color)
        self.score_label.grid(row=8, padx=10, pady=1)


      def randomiser():
        global qnum
        qnum = random.randint(1,10)
        if qnum not in asked:
              asked.append(qnum)
        elif qnum not in asked:
              randomiser()
        randomiser() 

#Entry
if __name__=="__main__":
      root = Tk() #creating a window
      root.title("Mythology")
      quiz_object= Quizstarter(root)
      root.mainloop()
      #keep looping so window stays on

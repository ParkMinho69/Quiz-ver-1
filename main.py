
from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, askquestion

def __init__ (self, parent):
      self.geometry('600x400')



global questions_answers
names_list = []
asked =[]
score =0
questions_answers = {

 }

def randomiser():
      global qnum
      qnum = random.randint(1,10)
      if qnum not in asked:
            asked.append(qnum)
      elif qnum not in asked:
            randomiser()


class Quizstarter:
      def __init__ (self, parent):
            background_color="#AC77E9"
            
            #frame set up
            self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
            self.quiz_frame.grid()
            
            background_color="OldLace"#background for all the widgets

            #widgets go below
            self.heading_label = Label(self.quiz_frame, text="Welcome to Mythology Quiz", bg="#AC77E9")
            self.heading_label.grid(row=0, padx=20)

            self.intro_label = Label(self.quiz_frame, text="Myth is a folklore genre consisting of narratives that play a fundamental role in society,", bg="#AC77E9")
            self.intro_label.grid(row=1, padx=20)

            self.intro_label = Label(self.quiz_frame, text="are usually not humans like gods, demigods, and supernatural figures.", bg="#AC77E9")
            self.intro_label.grid(row=2, padx=20)   
            
            # label to ask for permission to continue
            self.user_label = Label(self.quiz_frame, text="Would you like to continue:",bg="#AC77E9")
            self.user_label.grid(row=3, padx=20, pady=20)

            #create a Button
            self.yes_button = Button(self.quiz_frame, text="Yes", font=("mishka family", "13", "normal"), bg="#878CE3", command=self.name_collection)
            self.yes_button.grid(row=5, column=0, padx=20, pady=20)
            
            #create a Button
            self.no_button = Button(self.quiz_frame, text="No", font=("mishka family", "13", "normal"), bg="#878CE3", command=self.name_collection)
            self.no_button.grid(row=5, column=1, padx=20, pady=20)
            
            answer = askyesno(title='Confirmation',
                              message='Are you sure that you want to quit?')
            if answer:
                  self.destroy()

            # Quit button
            quit_button = ttk.Button(self, text='Quit', command=self.confirm)
            quit_button.pack(expand=True)

def name_collection(self):
            name=self.entry_box.get() 
            names_list.append(name) 
            print(names_list) #testing
            self.quiz_frame.destroy()
            Quiz(root) #we destroy starter quiz_frame and open the questions quiz_frame isntead which will be part of the Quiz object



class Quiz:
      def __init__ (self, parent):
                  background_color="#c299ff"
                  #frame set up
                  self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
                  self.quiz_frame.grid()

                  #randomiser will randomly pick a question number which is qnum
                  randomiser()
                  
                  #label widget for our heading
                  self.question_label = Label(self.quiz_frame, text = questions_answers[qnum][0], font=("Garamond", "14") , bg="#ccf5ff")
                  self.question_label.grid(row=0)

                  #confirm answer button
                  self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="white")
                  self.confirm_button.grid(row=5)



#Entry
if __name__=="__main__":
      root = Tk() #creating a window
      root.title("Mythology")
      quiz_object= Quizstarter(root)
      root.mainloop()
      #keep looping so window stays on
      


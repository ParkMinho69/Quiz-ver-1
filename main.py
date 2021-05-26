from tkinter import *


#questions
global questions_answers
names_list = []
asked =[]
score =0

#Dictinary has key of number and : the value for each is a list that has 7 items, so index 0 to 6
questions_answers = {
  1:["According to Roman mythology, who was the father of Romulus and Remus?",#item1, index 0 will be the question
      'A wolf', #item 2, index 1 will be first choice
      'Mars', #item 3, index 2 will be first choice
      'King Numitor', #item 3, index 3 will ve first choice
      'Jupitor', #item 4, index 4 will be first choice
      ], #item 5, index 5 will be the postion of the right answer (index where the right answer sits), this will be our check if answer is correct or not
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
        background_color="#c299ff"

        #frame set up
        self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #widgets go below
        self.intro_label = Label(self.quiz_frame, text="This quiz is about the histroy of the Roman and Greece.", bg="#c299ff")
        self.intro_label.grid(row=1, padx=20)

        self.intro_label = Label(self.quiz_frame, text="You may not find it interesting because it's about history,", bg="#c299ff")
        self.intro_label.grid(row=2, padx=20)

        self.intro_label = Label(self.quiz_frame, text="I also thought it would be boring but, surpringily, the more I", bg="#c299ff")
        self.intro_label.grid(row=3, padx=20)

        self.intro_label = Label(self.quiz_frame, text="researched I found some of the fcats to be interesting oddly enough.", bg="#c299ff")
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
        self.user_label.destroy()


class Quiz:
      def __init__ (self, parent):
                  background_color="#c299ff"
                  #frame set up
                  self.quiz_frame = tk.Frame(parent, bg = background_color, padx=100, pady=100)
                  self.quiz_frame.place()

                  #randomiser will randomly pick a question number which is qnum
                  randomiser()
          

#Entry
if __name__=="__main__":
      root = Tk() #creating a window
      root.title("Roman & Greek History")
      quiz_object= Quizstarter(root)
      root.mainloop()
      #keep looping so window stays on
      

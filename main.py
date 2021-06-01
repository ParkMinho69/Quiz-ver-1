from tkinter import *
import random

names = []
asked =[]
score =0
questions_answers = {
  1:["According to Roman mythology, who was the father of Romulus and Remus?",#item1, index 0 will be the question
      'A wolf', #item 2, index 1 will be first choice
      'Mars', #item 3, index 2 will be first choice
      'King Numitor', #item 4, index 3 will be first choice
      'Jupitor', #item 5, index 4 will be first choice
      ],
  2:["According to Roman mythology, who was the father of Romulus and Remus?",#item1, index 0 will be the question
      'A wolf', #item 2, index 1 will be first choice
      'Mars', #item 3, index 2 will be first choice
      'King Numitor', #item 3, index 3 will be first choice
      'Jupitor', #item 4, index 4 will be first choice
      ],

  3:["According to Roman mythology, who was the father of Romulus and Remus?",#item1, index 0 will be the question
      'A wolf', #item 2, index 1 will be first choice
      'Mars', #item 3, index 2 will be first choice
      'King Numitor', #item 3, index 3 will be first choice
      'Jupitor', #item 4, index 4 will be first choice
      ],

  4:["According to Roman mythology, who was the father of Romulus and Remus?",#item1, index 0 will be the question
      'A wolf', #item 2, index 1 will be first choice
      'Mars', #item 3, index 2 will be first choice
      'King Numitor', #item 3, index 3 will be first choice
      'Jupitor', #item 4, index 4 will be first choice
      ],

  5:["According to Roman mythology, who was the father of Romulus and Remus?",#item1, index 0 will be the question
      'A wolf', #item 2, index 1 will be first choice
      'Mars', #item 3, index 2 will be first choice
      'King Numitor', #item 3, index 3 will be first choice
      'Jupitor', #item 4, index 4 will be first choice
      ],
 }


def randomiser():
  global qnum
  qnum = random.randint(1,5)
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
    self.yes_button = Button(self.quiz_frame, text="Yes", font=("Helvetica", "13", "normal"), bg="#878CE3", command=self.name_collection)
    self.yes_button.grid(row=6, padx=12, pady=5,)
        
    #create No Button
    self.no_button = Button(self.quiz_frame, text="No", font=("Helvetica", "13", "normal"), bg="#878CE3", command=self.name_collection)
    self.no_button.grid(row=7, padx=12, pady=5)



  def name_collection(self):
    self.yes_button.destroy()
    self.no_button.destroy()
    self.quiz_frame.destroy()
    Quiz(root)




class Quiz:
  def __init__ (self, parent):
    background_color="#c299ff"
    #frame set up
    self.quiz_frame =Frame(parent, bg = background_color, padx=100, pady=100)
    self.quiz_frame.grid()
    randomiser()
       
    #question
    self.questions_label=Label(self.quiz_frame, text=questions_answers[qnum][0], bg=background_color)
    self.questions_label.grid(row=1, padx=10, pady=10)


    #holds the value of the radio buttons
    self.bar=IntVar()

    #radio button 1
    self.rb1 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.bar, padx=10,pady=10)
    self.rb1.grid(row=1, sticky=W)

    #radio button 2
    self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, variable=self.bar, padx=10, pady=10)
    self.rb2.grid(row=2, sticky=W)

    #radio button 3
    self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, variable=self.bar, padx=10,pady=10)
    self.rb3.grid(row=3, sticky=W)

    #radio button 4
    self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, variable=self.bar, padx=10, pady=10)
    self.rb4.grid(row=4, sticky=W)

    #confirm button
    self.quiz_instance= Button(self.quiz_frame, text="Confirm", font=("Helvetica", "12", "bold"), bg="blue")
                
    #score label 
    self.score_label = Label(self.quiz_frame, text="SCORE", font=("Tm Cen MT","12"), bg=background_color)
    self.score_label.grid(row=8, padx=10, pady=1)


  def questions_setup(self):
    randomiser()
    self.bar1.set(0)
    self.question_label.config(text=questions_answers[qnum][0])
    self.rb1.config(text=questions_answers[qnum][1])
    self.rb2.config(text=questions_answers[qnum][2])
    self.rb3.config(text=questions_answers[qnum][3])
    self.rb4.config(text=questions_answers[qnum][4])


    def test_progress(self):
      global score
      scr_label=self.score_label
      choice=self.bar1.get()
      if len(asked)>5:
        if choice == questions_answers[qnum][4]:
          score+=1
          scr_label.configure(text=score)
          self.quiz_instance.config(text=confirm)
          self.endscreen()
        
        else:
          print(choice)
          score+=0
          scr_label.configure(text="The correct answer is" + questions_answers[qnum][5])
          self.quiz_instance.config(text="Confirm")
          self.endscreen()

      else:
        if choice==0:
          self.quiz_instance.config(text="Please try again")
          choice=self.bar1.get()
          
        else:
          if choice == questions_answers[qnum][4]:
            score+=1
            scr_label.configure(text=score)
            self.quiz-instance.config(test="Confirm")
            self.questions_setup()

          else:
            print(choice)
            score+=0
            scr_label.configure(text="the correct answer is" + questions_answers[qnum][1])
            self.quiz_instance.config(text="Confirm")
            self.questions_setup()

  def endScreen(self):
        root.withdraw()
        name=names[0]
        file=open("leaderBoard.txt", "a")
        file.write(str(score))
        file.write(" - ")
        file.write(name+"\n")
        file.close()

        inputFile = open("leaderBoard.txt", 'r')
        lineList = inputFile.readlines()
        lineList.sort()
        top=[]
        top5=(lineList[-5:])
        for line in top5:
          point=line.split(" - ")
          top.append((int(point[0]), point[1]))
        file.close()
        top.sort()
        top.reberse()
        return_string =""
        for i in range (len(top)):
          return_string +="{} - {}\n".format(top[i][0], top[i][1])
          print (return_string)




class End:
  def __init__(self, parent): 
    background ="white"
    self.end_box= Toplabel(root)
    self.end_box.title("End Box")

    self.end_frame = Frame(self.end_box, width=1000, height=1000, bg=background)
    self.end_frame.grid_info

    end_heading = Label (self.end_frame, text='Well Done', font=("Comic Sans MS", "11"), bg=background, pady=15)
    end_heading.grid(row=0)

    exit_button = Button (self.end_frame, text='Exit', width=10, bg="lightblue", font=("Comic Sans MS", "11"), command=self.close_end)
    exit_button.grid(row=4, pady=20)

    self.quit = Button(self.quiz_frame, text="quit", font=("Comic Sans MS", "11"), bg="lightblue", command=self.endscreen)
    self.quit.grid(row=7, column=3, padx=5, pady=5)

    self.listLabel = Label(self.end_frame, text="1st place abailable", font=("Comic Sans MS", "11"), width=40, bg=background, padx=10, pady=10)
    self.listLabel.grid(row=2)

  def close_end(self):
    self.end_box.destroy()
    root.withdraw()

#Entry
if __name__=="__main__":
      root = Tk() #creating a window
      root.title("Mythology")
      quiz_object= Quizstarter(root)
      root.mainloop()
      #keep looping so window stays on

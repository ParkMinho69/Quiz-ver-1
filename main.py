from tkinter import *
import random
from PIL import ImageTk, Image


names = []
names_list = []
asked =[]
score =0
questions_answers = {
  1:["Who is the king of gods and the god of the sky and thunder?",
      'Zeus', 'Hermes', 'Minotaur', 'Aptoide', 1
    ],

  2:["How long did the Trojan war last?",
      '10 years', '20 years', '5 years', '6 years', 1
      ],

  3:["Which goddess is Apollo’s twin sister?",
      'Artemis', 'Asteria', 'Athena', 'Aphrodite', 1
      ],

  4:["What is Demeter the goddess of?",
      'Agriculture', 'Destruction', 'The moonr', 'Oracles', 1
      ],

  5:["Which of these things was the only one left in Pandora’s box?",
      'Hope', 'Trust', 'Joy', 'Wisdom', 1
    ],
  
  6:["What is the name of Hades’ three-headed dog?",
      'Cerberus', 'Mars', 'Charon', 'Charybdis', 1
    ],

  7:["who is the god of the sea?",
      'Poseidon', 'Zeus', 'Athena', 'Hades', 1
    ],

  8:["How was Athena born?",
      'From Zeus head', 'From flowers', 'Hera womb', 'From the Ocean', 1
    ],

  9:["Zeus and Hades were brothers with which god?",
      'Poseidon', 'Hermes', 'Apollo', 'Ares', 1
    ],

  10:["What did Eros golden arrow make people do?",
      'Fall in love', 'Intelligent', 'Swim', 'Dance', 1
    ],
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
    background_color="#9982E6"
    
    self.bg_image = Image.open("mpic.jpg")#adding a background image to the quiz program for the first screen 
    self.bg_image = self.bg_image.resize((650, 500), Image.ANTIALIAS)#the sizing for the image 
    self.bg_image = ImageTk.PhotoImage(self.bg_image)
     

            #frame set up
    self.quiz_frame = Frame(parent, bg = background_color, padx=0, pady=0)
    self.quiz_frame.grid()
    self.image_label = Label(self.quiz_frame, image=self.bg_image)
    self.image_label.place(x=0, y=0, relwidth=1, relheight=1)


    #widgets go below
    self.intro_label = Label(self.quiz_frame, text="This is a little introduction to the Greek Mythology Gods and Goddesses: ", bg="#878CE3")
    self.intro_label.grid(row=0, padx=20, pady=20)


    self.intro_label = Label(self.quiz_frame, text="The Greeks were polytheistic in their religious beliefs. ", bg="#9982E6")
    self.intro_label.grid(row=1, padx=20)

    self.intro_label = Label(self.quiz_frame, text="Meaning that they believed in and worshiped many different gods. ", bg="#9982E6")
    self.intro_label.grid(row=2, padx=20)

    self.intro_label = Label(self.quiz_frame, text="In Greek mythology, the gods often represented different forms of nature.", bg="#9982E6")
    self.intro_label.grid(row=3, padx=20)

    self.intro_label = Label(self.quiz_frame, text="Their religion/mythology had no formal structure with the exception", bg="#9982E6")
    self.intro_label.grid(row=4, padx=20)

    self.intro_label = Label(self.quiz_frame, text="of various festivals held in honor of the gods.", bg="#9982E6")
    self.intro_label.grid(row=5, padx=20)

    self.intro_label = Label(self.quiz_frame, text="There was no sacred book or code of conduct to live by like the bible for example.", bg="#9982E6")
    self.intro_label.grid(row=6, padx=20)

    self.intro_label = Label(self.quiz_frame, text="The most powerful Greek gods were known as the Olympians, who live on ", bg="#9982E6")
    self.intro_label.grid(row=7, padx=20)

    self.intro_label = Label(self.quiz_frame, text="the highest mountain in Greece, called Mount Olympus", bg="#9982E6")
    self.intro_label.grid(row=8, padx=20)


    #label to ask for permison to continue
    self.user_label = Label(self.quiz_frame, text="Would you like to continue:",bg="#9982E6")
    self.user_label.grid(row=9, padx=20, pady=10)

    #create yes Button
    self.yes_button = Button(self.quiz_frame, text="Yes", font=("Helvetica", "13", "normal"), bg="#878CE3", command=self.yes)
    self.yes_button.grid(row=10, padx=12, pady=5,)
        
    #create No Button
    self.no_button = Button(self.quiz_frame, text="No", font=("Helvetica", "13", "normal"), bg="#878CE3", command=self.no)
    self.no_button.grid(row=11, padx=12, pady=5,)

  def yes(self):
    self.yes_button.destroy()
    self.quiz_frame.destroy()
    username(root)

  def no(self):
    self.no_button.destroy()
    self.quiz_frame.destroy()
    

class username:
  def __init__ (self, parent):
    background_color="#9982E6"

    #frame set up
    self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
    self.quiz_frame.grid()

    #label to ask for user's name
    self.quiz_label = Label( self.quiz_frame, text="What is your name:",bg="#9982E6")
    self.quiz_label.grid(row=1, padx=20, pady=10)

    #entry box
    self.entry_box = Entry( self.quiz_frame)
    self.entry_box.grid(row=2, padx=20, pady=10)

    #confirm button
    self.confirm_button = Button( self.quiz_frame, text="Confirm", font=("Helvetica", "12",), bg="#B8C0FF", command=self.name_collection)
    self.confirm_button.grid(row=3)


  def name_collection(self):
    name=self.entry_box.get()
    names_list.append(name)
    print(names_list) #testing
    self.quiz_frame.destroy()
    #we destroy starter quiz_frame and open the questions quiz_frame isntead which will be part of the Quiz object
    Quiz(root)


class Quiz:
  def __init__ (self, parent):
    background_color="#9982E6"
    #frame set up
    self.quiz_frame =Frame(parent, bg = background_color, padx=100, pady=100)
    self.quiz_frame.grid()
    randomiser()
       
    #question
    self.questions_label=Label(self.quiz_frame, text=questions_answers[qnum][0], bg=background_color)
    self.questions_label.grid(row=0, padx=10, pady=10)

    #holds the value of the radio buttons
    self.var=IntVar()

    #radio button 1
    self.rb1 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var)
    self.rb1.grid(row=1)

    #radio button 2
    self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, variable=self.var)
    self.rb2.grid(row=2)

    #radio button 3
    self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, variable=self.var)
    self.rb3.grid(row=3)

    #radio button 4
    self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, variable=self.var)
    self.rb4.grid(row=4)

    #answer confirm button
    self.confirm_button = Button(self.quiz_frame, text="Confirm", font=("Helvetica", "12", ), bg="#B8C0FF", command=self.test_progress)
    self.confirm_button.grid(row=6)

    #score label 
    self.score_label = Label(self.quiz_frame, text="SCORE", font=("Tm Cen MT","12"), bg=background_color)
    self.score_label.grid(row=8)

   
#the question label to new questions and possible answers as new radio button choices
  def question_setup(self):
          randomiser()
          self.var.set(0)
          self.questions_label.config(text=questions_answers[qnum][0])
          self.rb1.config(text=questions_answers[qnum][1])
          self.rb2.config(text=questions_answers[qnum][2])
          self.rb3.config(text=questions_answers[qnum][3])
          self.rb4.config(text=questions_answers[qnum][4])



#confirm button for the questions window to be better 
  def test_progress(self):#pass the users choice
    global score#this score us there to be acessed to everyone 
    scr_label = self.score_label#shhowing the score because it will be different each time a question is answered 
    choice = self.var.get()#get the users choice
    if len(asked)>9:#to determine it its the last question to end the quiz after
      if choice == questions_answers[qnum][5]:#cheking the qnum has the correct answer that is stored in index 6
        score+=1#adding a point after each correct answer 
        scr_label.configure(text=score)#it will change the score to the new score each time 
        self.confirm_button.config(text="confirm")#will change the test on the button to confirm
        self.endScreen()#to open endScreen when quiz is completed 
      
      else:
        print(choice)
        score+=0#score will stay the same if the questions is answered inccorectly 
        scr_label.configure(text="Incorrect the answer was:  " + questions_answers[qnum][5])#sayin the incorrect answer the the question that the end user put wrong 
        self.confirm_button.config(text="Confirm")#will change the test on the button to confirm
        self.endScreen()#to open endScreen when quiz is completed 

    else:
      if choice == 0:#if the user doesnt select and option
        self.confirm_button.config(text="Pick an option")#then the confirm button will say plase try again until the questions is answered and an option is selected
        choice=self.var.get()#still get the answer if they chose it
       
        
      else:#if choice is correct
        if choice == questions_answers[qnum][5]:#if the choice is correct
          score+=1
          scr_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
          self.question_setup()#to move on to the next question

        else:#if the choice was inccorect
          print(choice)
          score+=0
          scr_label.configure(text="Incorrect! The answer was:" + questions_answers[qnum][1])#telling the correct answer 
          self.confirm_button.config(text="Confirm")
          self.question_setup()#moving to the next question


  def endScreen(self):
    root.withdraw()
    name = names[0]
    file = open("leaderBoard.txt", "a")#opens highscores, text file in append mode
    if name == "admin_reset":#to wipe scores in the list, admin eneters with the name
      file = open("leaderBoard.txt", "w")
    
    else:
      file.write(str(score))#turns the sucess rate into a string 
      file.write(" - ")#writes into the text file
      file.write(name+"\n")#writes the names into the text files and goes to a new line (\n)
      file.close()#closes the file

    inputFile = open("leaderBoard.txt", 'r')#opens the highscore files in read mode 
    lineList = inputFile.readlines()#linelist equals the each lines in the lists
    lineList.sort()#sorts the line alpabetically
    top=[]#display top scores 
    top5=(lineList[-5:])#the last 10 values in the list for top 10
    for line in top5:
      point=line.split(" - ")
      top.append((int(point[0]), point[1]))
    file.close()#closes the files 
    top.sort()
    top.reverse()
    return_string = "Your final score is: "
    for i in range (len(top)):
      return_string += "{} - {}\n".format(top[i][0], top[i][1])
      print(return_string)#for testing to show on the console
      
      open_endscreen = End(root)
      open_endscreen.listLabel.config(text=return_string)#this will config the label in the end screen class which is displaying the names of the top 5

class End:
  def __init__(self, parent): # this function is called every time the class is being used to create a new object
    background ="#62E4CF"
    self.end_box = Toplevel(root)
    self.end_box.title("End Box")

    self.end_frame = Frame(self.end_box, pady=70, padx=45, bg=background)
    self.end_frame.grid()
      
    #end heading 
    end_heading = Label (self.end_frame, text='You have now Completed the quiz', font=("Comic Sans MS", "11"), bg=background, pady=15)
    end_heading.grid(row=0)
    #exit button to end the quiz 
    exit_button = Button (self.end_frame, text='Exit quiz>>', width=10, font=("Comic Sans MS", "11"), command=self.close_end, pady=10, padx=10)
    exit_button.grid(row=4, pady=20, padx=5, sticky=E)

    #if 1st place is available/ what they got 
    self.listLabel = Label(self.end_frame, text="You are in 1st place", font=("Comic Sans MS", "11"), width=40, bg=background, padx=10, pady=10)
    self.listLabel.grid(row=2)



  def close_end(self):
    self.end_frame.destroy()
    self.end_box.destroy()
    root.withdraw()



#Entry
if __name__=="__main__":
      root = Tk() #creating a window
      root.title("Greek History")
      Quizstarter_object= Quizstarter(root)  #object 1
      root.mainloop()
      #keep looping so window stays on

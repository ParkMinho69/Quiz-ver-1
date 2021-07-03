from tkinter import *
import random
from PIL import ImageTk, Image


class Create:
  def __init__ (self, parent):
    background_color="seashell3"
    
    self.bg_image = Image.open("cookingearth.jpg")#adding a background image to the quiz program for the first screen 
    self.bg_image = self.bg_image.resize((548, 315), Image.ANTIALIAS)
    #the sizing for the image 
    self.bg_image = ImageTk.PhotoImage(self.bg_image)  

            #frame set up
    self.quiz_frame = Frame(parent, bg = background_color, padx=0, pady=0)
    self.quiz_frame.grid()

    self.image_label = Label(self.quiz_frame, image=self.bg_image)
    self.image_label.place(x=0, y=0, relwidth=1, relheight=1)

    #widgets go below
    self.intro_label = Label(self.quiz_frame, text="This is a little introduction to the Greek Mythology Gods and Goddesses: ", bg="seashell3" )
    self.intro_label.grid(row=0, padx=20, pady=20)


    self.intro_label = Label(self.quiz_frame, text="The Greeks were polytheistic in their religious beliefs. ", bg="seashell3")
    self.intro_label.grid(row=1, padx=20)

    self.intro_label = Label(self.quiz_frame, text="Meaning that they believed in and worshiped many different gods. ", bg="seashell3")
    self.intro_label.grid(row=2, padx=20)

    self.intro_label = Label(self.quiz_frame, text="In Greek mythology, the gods often represented different forms of nature.", bg="seashell3")
    self.intro_label.grid(row=3, padx=20)

    self.intro_label = Label(self.quiz_frame, text="Their religion/mythology had no formal structure with the exception", bg="seashell3")
    self.intro_label.grid(row=4, padx=20)

    self.intro_label = Label(self.quiz_frame, text="of various festivals held in honor of the gods.", bg="seashell3")
    self.intro_label.grid(row=5, padx=20)

    #label to ask for permission to continue
    self.user_label = Label(self.quiz_frame, text="Would you like to continue:",bg="seashell3")
    self.user_label.grid(row=9, padx=20, pady=10)

    #Create yes Button
    self.yes_button = Button(self.quiz_frame, text="Yes", font=("Helvetica","12", "normal"), bg="#FFD6FF", command=self.yes)
    self.yes_button.grid(row=10, padx=12, pady=5,)
        
    #Create No Button
    self.no_button = Button(self.quiz_frame, text="No", font=("Helvetica","12", "normal"), bg="#BBD0FF", command=self.no)
    self.no_button.grid(row=11, padx=12, pady=5,)

  def yes(self):
    self.yes_button.destroy()
    self.quiz_frame.destroy()
    username(root)

  def no(self):
    self.no_button.destroy()
    self.quiz_frame.destroy()
    
#starting window
class username:
  def __init__ (self, parent):
    background_color="darkorchid1"
   
   #background image
    self.bg_image = Image.open("wall.jpg") #same image for the 2nd component  
    self.bg_image = self.bg_image.resize((548, 309), Image.ANTIALIAS) #sizing of the background image 
    self.bg_image = ImageTk.PhotoImage(self.bg_image)
     
    #frame set up
    self.quiz_frame = Frame(parent, bg = background_color, padx=0,pady=0)
    self.quiz_frame.grid() 
        
     #image Label   
    self.image_label = Label(self.quiz_frame, image=self.bg_image)
    self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    #exit button 
    self.exit_button = Button(self.quiz_frame,text="Exit Quiz", font=("Helvetica","12", "normal"), command=root.destroy)
    self.exit_button.grid(row=4, sticky=E, padx=10, pady=0)#sizing of the exit button

    #username label
    self.user_label = Label(self.quiz_frame, text="What is your name: ", font=("Helvetica","12", "normal"), bg="seashell3")
    self.user_label.grid(row=2, padx=90, pady=25)#placing of the username label
    
    #continue button to continue on to the next component where the questions are asked 
    self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica","12", "normal"), bg="sienna1",  command=self.contbutton)
    self.continue_button.grid(row=4, padx=0, pady=35)#plaing of the continue button
 
    #entry box to enter the username 
    self.entry_box = Entry(self.quiz_frame)
    self.entry_box.grid(row=3, padx=90, pady=25)

  #trial and error for the continue button so it the user left the box empty then 
  def contbutton(self):
    if len(self.entry_box.get()) ==  0:
      self.continue_button.config(text="Please enter a Username", font=("Helvetica","12", "normal"))

    else:#the user can only have 10 values 
      if len(self.entry_box.get()) > 15:
        self.continue_button.config(text="username has to be \nunder 15 values", font=("Helvetica","12", "normal"))

      else:#the user can only have 2 values
       if len(self.entry_box.get()) <= 2:
         self.continue_button.config(text="username has to be \n more than 2 values", font=("Helvetica","12", "normal"))
            
       else:
         self.name_collection()#coninuation from the continue button to the next compnent(the questions)
  
  def name_collection(self):
    names_list
    name=self.entry_box.get()
    names_list.append(name)
    print(names_list) #testing
    self.quiz_frame.destroy()
    #we destroy starter quiz_frame and open the questions quiz_frame instead which will be part of the Quiz object
    Quiz(root)


names_list = []
asked =[]
score =0

def randomiser():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
      asked.append(qnum)
  elif qnum in asked:
    randomiser()

#quiz window
class Quiz:
  def __init__ (self, parent):
    background_color="#E7C6FF"
    self.questions_answers = {
  1:["Who is the king of gods and the god of the sky and thunder?",
      'Zeus', 'Hermes', 'Minotaur', 'Aptoide', 'Zeus', 1
    ],

  2:["How long did the Trojan war last?",
       '20 years', '10 years', '5 years', '6 years', '10 years', 2
      ],

  3:["Which goddess is Apollo’s twin sister?",
       'Asteria', 'Athena', 'Artemis', 'Aphrodite', 'Artemis', 3
      ],

  4:["What is Demeter the goddess of?",
       'Destruction', 'The mooner', 'Oracles', 'Agriculture', 'Agriculture', 4
      ],

  5:["Which of these things was the only one left in Pandora’s box?",
       'Trust', 'Joy', 'Hope', 'Wisdom', 'Hope', 3
    ],
  
  6:["What is the name of Hades’ three-headed dog?",
      'Cerberus', 'Mars', 'Charon', 'Charybdis', 'Cerberus', 1
    ],

  7:["who is the god of the sea?",
       'Zeus', 'Poseidon', 'Athena', 'Hades', 'Poseidon', 2
    ],

  8:["How was Athena born?",
       'From flowers', 'Hera womb', 'From Zeus head', 'From the Ocean', 'From Zeus head', 3
    ],

  9:["Zeus and Hades were brothers with which god?",
      'Poseidon', 'Hermes', 'Apollo', 'Ares', 'Poseidon', 1
    ],

  10:["What did Eros golden arrow make people do?",
      'Intelligent', 'Swim', 'Dance', 'Fall in love',  'Fall in love', 4
    ],
 }

    #frame set up
    self.quiz_frame = Frame(parent, bg = background_color, padx=0,pady=0, width=50, height=50)
    self.quiz_frame.grid() 
    randomiser()
    
    #question
    self.questions_label=Label(self.quiz_frame, text= self.questions_answers[qnum][0], bg = background_color,)
    self.questions_label.grid(row=0, padx=10, pady=10)

    #holds the value of the radio buttons
    self.var=IntVar()

    #radio button 1
    self.rb1 = Radiobutton(self.quiz_frame, text = self.questions_answers[qnum][1], font=("Helvetica","12", "normal"), bg=background_color,value=1, variable=self.var)
    self.rb1.grid(row=1, padx=5, pady=5)

    #radio button 2
    self.rb2 = Radiobutton (self.quiz_frame, text = self.questions_answers[qnum][2], font=("Helvetica","12", "normal"), bg=background_color,  value=2, variable=self.var)
    self.rb2.grid(row=2, padx=5, pady=5)

    #radio button 3
    self.rb3 = Radiobutton (self.quiz_frame, text =self.questions_answers[qnum][3], font=("Helvetica","12", "normal"), bg=background_color, value=3, variable=self.var)
    self.rb3.grid(row=3, padx=5, pady=5)

    #radio button 4
    self.rb4 = Radiobutton (self.quiz_frame, text =self.questions_answers[qnum][4], font=("Helvetica","12", "normal"), bg=background_color, value=4, variable=self.var)
    self.rb4.grid(row=4, padx=5, pady=5)

    #answer confirm button
    self.confirm_button = Button(self.quiz_frame, text="Confirm", font=("Helvetica","12", "normal", ), bg="#B8C0FF", command=self.test_progress)
    self.confirm_button.grid(row=6, padx=5, pady=5)

    #score label 
    self.score_label = Label(self.quiz_frame, text="SCORE", font=("Tm Cen MT","12", "normal" ), bg=background_color)
    self.score_label.grid(row=8, padx=10, pady=10)
   
#the question label to new questions and possible answers as new radio button choices
  def question_setup(self):
          randomiser()
          self.var.set(0)
          self.questions_label.config(text = self.questions_answers[qnum][0])
          self.rb1.config(text = self.questions_answers[qnum][1])
          self.rb2.config(text = self.questions_answers[qnum][2])
          self.rb3.config(text = self.questions_answers[qnum][3])
          self.rb4.config(text = self.questions_answers[qnum][4])


#confirm button for the questions window to be better 
  def test_progress(self):#pass the users choice
    print(asked)

    global score#score which is to be accessed to everyone 
    scr_label = self.score_label#shhowing the score because it will be different each time a question is answered 
    choice = self.var.get()#get the users choice
    if len(asked)>9:#to determine it its the last question to end the quiz after
      if choice ==self.questions_answers[qnum][6]:#cheking the qnum has the correct answer that is stored in index 6
        score+=1#adding a point afth=er each correct answer 
        scr_label.configure(text=score)#it will change the score to the new score each time 
        self.confirm_button.config(text="confirm")#will change the test on the button to confirm
        self.endScreen()#to open endScreen when quiz is completed 
      
      else:
        print(choice)
        score+=0#score will stay the same if the questions is answered incorrectly 
        scr_label.configure(text="Incorrect the answer was:  " +self.questions_answers[qnum][5])#sayin the incorrect answer the the question that the end user put wrong 
        self.confirm_button.config(text="Confirm")#will change the test on the button to confirm
        self.endScreen()#to open endScreen when quiz is completed 

    else:
      if choice == 0:#if the user doesnt select and option
        self.confirm_button.config(text="Pick an option")#then the confirm button will say please try again until the questions is answered and an option is selected
        choice=self.var.get()#still get the answer if they chose it
           
      else:#if choice is correct
        if choice ==self.questions_answers[qnum][6]:#if the choice is correct
          score+=1
          scr_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
          self.question_setup()#to move on to the next question

        else:#if the choice was incorrect
          print(choice)
          score+=0
          scr_label.configure(text="Incorrect! The answer was:" +self.questions_answers[qnum][5])#telling the correct answer 
          self.confirm_button.config(text="Confirm")
          self.question_setup()#moving to the next question

  def endScreen(self):
    root.withdraw()
    name = names_list[0]
    file = open("leaderBoard.txt", "a")#opens highscores, text file in append mode
    if name == "admin_reset":#to wipe scores in the list, admin enters with the name
      file = open("leaderBoard.txt", "w")
    
    else:
      file.write( str(score))#turns the success rate into a string 
      file.write(" - ")#writes into the text file
      file.write(name+"\n")#writes the names into the text files and goes to a new line (\n)
      file.close()#closes the file

    inputFile = open("leaderBoard.txt", 'r')#opens the high score files in read mode 
    lineList = inputFile.readlines()#linelist equals the each lines in the lists
    lineList.sort()#sorts the line alphabetically
    top=[]#display top scores 
    top5=(lineList[-5:])#the last 10 values in the list for top 10
    for line in top5:
      point=line.split(" - ")
      top.append((int(point[0]), point[1]))
    file.close()#closes the files 
    top.sort()
    top.reverse()
    return_string = " Your final score is: "
    for i in range (len(top)):
      return_string += "{} - {}\n".format(top[i][0], top[i][1])
      print(return_string)#for testing to show on the console
      
    open_endscreen = End(root)
    open_endscreen.listLabel.config(text=return_string)#this will config the label in the end screen class which is displaying the names of the top 5

#end window         
class End:
  def __init__(self, parent): # this function is called every time the class is being used to Create a new object
    background ="#BBD0FF"
    self.end_box = Toplevel(root)
    self.end_box.title("End Box")

    self.end_frame = Frame(self.end_box, pady=40, padx=45, bg=background)
    self.end_frame.grid()
    
    #end heading 
    end_heading = Label (self.end_frame, text='YAY! You have now Completed the quiz!', font=("Comic Sans MS", "11"), bg=background, pady=15)
    end_heading.grid(row=0)
      
    #exit button to end the quiz 
    exit_button = Button (self.end_frame, text='Exit quiz', width=10, font=("Comic Sans MS", "11"), command=self.close_end, pady=10, padx=10)
    exit_button.grid(row=4, pady=20, padx=5, sticky=E)

    #if 1st place is available/ what they got 
    self.listLabel = Label(self.end_frame, text="You are in 1st place!", font=("Comic Sans MS", "11"), width=40, bg=background, padx=10, pady=10)
    self.listLabel.grid(row=2)

  def close_end(self):
    self.end_frame.destroy()
    self.end_box.destroy()
    root.withdraw()

#Entry
if __name__=="__main__":
      root = Tk() #creating a window
      root.title("Greek History")
      Create_object= Create(root)  #object 1
      root.mainloop()
      #keep looping so window stays on

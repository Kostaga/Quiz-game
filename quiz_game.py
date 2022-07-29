import tkinter
import random
#show rules only once

questions = [
    "How many lives is a cat said to have?",
    "According to George Orwell, who is watching us?",
    "Which is the oldest Pokemon in the game universe?",
    "Who was the original drummer for The Beatles?",
    "In which video did Michael Jackson first perform his famous moonwalk in 1983?",
    "Immigrant Song was a hit for which band in 1970?",
    "What year was star wars released",
    "What year did Elvis Presley die",
    "What is the name of the largest country in the world?",
    "How many States does the United States consist of?",
    "What is Earth's largest continent?",
    "How many hearts does an octopus have?",
    "The unicorn is the national animal of which country?",
    "What is the nearest planet to the sun?",
    "How many teeth does an adult human have?",
    "Which of the following is used in pencils?",
    "Nuclear sizes are expressed in a unit named",
    "Light from the Sun reaches us in nearly",
    "For which of the following disciplines is Nobel Prize awarded?",
    "First China War was fought between",
    "How many drummers have played for the famous band- AC/DC?",
    "What year did Disneyland open?",
    "What is the name of the largest ocean in the world?",
    "What does Pokémon mean?",
    "How many times per second can a honey bee flap its wings?"

]

answers = [
    ["Nine", "Six", "Seven", "One"],
    ["Angels", "Big Brother", "God", "Loved ones"],
    ["Arceus", "Rhydon", "Mewtwo", "Kyogre"],
    ["Buddy Rich", "Neil Peart", "Ringo Starr", "Pete Best"],
    ["Man in the mirror", "Beat it", "Billie Jean", "Thriller"],
    ["Jimi Hendrix", "Rolling Stones", "AC/DC", "Led Zeppelin"],
    ["March 28, 1997", "June 14 1996", "November 25 1997", "April 7 1998 "],
    ["January 15 1977", "August 16, 1977", "September 12 1978", "July 19 1979"],
    ["China", "India", "Russia", "USA"],
    ["95", "30", "50", "72"],
    ["South America","North America","Africa","Asia"],
    ["4","2","3","8"],
    ["Sweden","Scotland","Luxembourg","Denmark"],
    ["Venus","Mercury","Earth","Saturn"],
    ["48","25","32","36"],
    ["Silicon","Phosphorous","Charcoal","Graphite"],
    ["Fermi","Angstrom","Newton","Tesla"],
    ["2 minutes", "4 minutes", "8 minutes", "16 mintues"],
    ["Physics and Chemistry", "Physiology or Medicine", "Literature, Peace and Economics", "All of the above"],
    ["China and Britain","China and France", "China and Egypt", "China and Greek"],
    ["4","3","7","12"],
    ["1949","1955","1963","1947"],
    ["Atlantic Ocean","Pacific Ocean","Indian Ocean","Arctic Ocean"],
    ["Nothing","Pocket Monsters","Little creatures","Pets"],
    ["600","100","200","400"]




]

correct_answers = ["Nine", "Big Brother", "Arceus", "Pete Best", "Billie Jean", "Led Zeppelin",
                    "March 28, 1997", "August 16, 1977", "Russia", "50","2","Scotland","Mercury","32","Graphite","Fermi","8 minutes","All of the above",
                   "China and Britain","12","1955","Pacific Ocean","Pocket Monsters","200","Asia"]

indexes = []
quest = 1
def generate():
    global indexes
    while (len(indexes)<10):
        rand = random.randint(0,24)
        if (rand not in indexes):
            indexes.append(rand)



def rules():
    w3 = tkinter.Label(root, bd=5, width=100, fg="yellow", bg="black",
                           text="This quiz contains 10 questions\n Answer 5 of them correct and win!", font=("Arial", 20,))
    w3.pack(side="bottom")
    w2.config(state="disabled")

#start button is pressed
def start():
    w1.destroy()
    w2.destroy()
    button_start.destroy()
    button_exit.destroy()
    image.destroy()
    generate()
    start_quiz()

def win_play_again():
    global win_image, you_win, button_start, button_exit,score,quest
    you_win.destroy()
    button_start.destroy()
    button_exit.destroy()
    win_image.destroy()
    score_label.destroy()
    quest = 1
    generate()
    start_quiz()

def lose_play_again():
    global lose_image, you_lose, button_start, button_exit, score, quest
    lose_image.destroy()
    you_lose.destroy()
    button_start.destroy()
    button_exit.destroy()
    score_label.destroy()
    quest = 1
    generate()
    start_quiz()

def submit():
    global r1,r2,r3,r4,question,quest,score_label,score
    #last question
    if (quest==10):
        # check if user answer is the same with correct answer
        correct()
        # show results
        end()
    elif (quest<10):
        # check if user answer is the same with correct answer
        correct()
        #change questions and answers to next
        question.config(text = questions[indexes[quest]])
        #answer 1
        r1.config(text = answers[indexes[quest]][0])
        r1.config(variable=var)
        #answer 2
        r2.config(text=answers[indexes[quest]][1])
        #answer 3
        r3.config(text=answers[indexes[quest]][2])
        #answer 4
        r4.config(text=answers[indexes[quest]][3])

        #next question
        quest += 1

def correct():
    global answers,indexes,quest,correct_answers,score,x
    x = var.get()
    if (answers[indexes[quest - 1]][x - 1] in correct_answers):
        score += 1
        score_label.config(text=f"Score: {score}", font=("Arial", 20,))


def end():
    #end results
    global sub,score,win_image, you_win, button_start, button_exit, lose_image, you_lose,indexes
    #destroy buttons and question label
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    question.destroy()
    sub.destroy()
    indexes = []
    if (score>=5):
        win_image = tkinter.Label(root, image=win)
        win_image.pack(side="top", pady=(50, 0))
        you_win = tkinter.Label(root, text="You win!", width=50, font=("Arial", 40, "bold"), bd=5)
        you_win.pack(side="top", pady=(50, 50))

        button_start = tkinter.Button(root, command=win_play_again, text="PLAY AGAIN", font=("Arial", 30, "bold"), bd=5,
                                      bg="light green")
        button_exit = tkinter.Button(root, command=root.destroy, text="EXIT", font=("Arial", 30, "bold"), bd=5,
                                     bg="red")
        button_start.pack(side="top")
        button_exit.pack(pady=(50, 50), side="top")
    else:
        lose_image = tkinter.Label(root, image=lose)
        lose_image.pack(side="top", pady=(50, 0))
        you_lose = tkinter.Label(root, text="You lose.Try again and win!", width=50, font=("Arial", 40, "bold"), bd=5)
        you_lose.pack(side="top", pady=(50, 50))

        button_start = tkinter.Button(root, command=lose_play_again, text="PLAY AGAIN", font=("Arial", 30, "bold"), bd=5,
                                      bg="light green")
        button_exit = tkinter.Button(root, command=root.destroy, text="EXIT", font=("Arial", 30, "bold"), bd=5,
                                     bg="red")
        button_start.pack(side="top")
        button_exit.pack(pady=(50, 50), side="top")


def start_quiz():
    global question,r1,r2,r3,r4,score,score_label
    score = 0
    question = tkinter.Label(root, text=questions[indexes[0]],font=("Arial",20,), width=100, height=2, bg="light grey",justify="center")
    question.pack(pady=(50,30),side="top")
    global var
    var = tkinter.IntVar()
    r1 = tkinter.Radiobutton(root, text=answers[indexes[0]][0], variable=var, value=1, font=("Arial",20))
    r1.pack(pady=(100,0))
    r2 = tkinter.Radiobutton(root, text=answers[indexes[0]][1], variable=var, value=2, font=("Arial", 20))
    r2.pack()
    r3 = tkinter.Radiobutton(root, text=answers[indexes[0]][2], variable=var, value=3, font=("Arial", 20))
    r3.pack()
    r4 = tkinter.Radiobutton(root, text=answers[indexes[0]][3], variable=var, value=4, font=("Arial", 20))
    r4.pack()
    global sub
    sub = tkinter.Button(root, text="Submit", font=("Arial",30,"bold"),bd=5,bg="yellow", command=submit)
    sub.pack(pady=(0,200),side="bottom")
    score_label = tkinter.Label(root, text = f"Score: {score}", font=("Arial",20,))
    score_label.pack(pady=(0,20),side="bottom")


#---------
root = tkinter.Tk()
root.title("Quiz game")
win = tkinter.PhotoImage(file="youwin2.png")
lose = tkinter.PhotoImage(file="youlose.png")
logo = tkinter.PhotoImage(file="quiz.png")

window_width = 1200
window_height = 900

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')



#images and labels
w1 = tkinter.Label(root, text="Welcome to QuizGame!",font=("Arial",20,"bold"))
image = tkinter.Label(root, image=logo)

w1.pack()
image.pack(pady=(50,0))

#buttons
w2 = tkinter.Button(root, command=rules,bd=1, bg="#E6E6E5", text="Read the rules and click start once you are ready",font=("Arial",20,"bold"))
button_start = tkinter.Button(root, command=start, text="START", font=("Arial",30,"bold"),bd=5,bg="light green")
button_exit = tkinter.Button(root, command=root.destroy, text="EXIT", font=("Arial",30,"bold"),bd=5, bg="red")
w2.pack(pady=(50,50),side="top")
button_start.pack(side="top")
button_exit.pack(pady=(50,50),side="top")



root.mainloop()


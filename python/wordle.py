import turtle, random

word_list = ['which', 'their', 'would', 'there', 'could', 'other', 'about', 'great', 'these', 'after', 'first', 'never', 'where', 'those', 'shall', 'being', 'might', 'every', 'think', 'under', 'found', 'still', 'while', 'again', 'place', 'young', 'years', 'three', 'right', 'house', 'whole', 'world', 'thing', 'night', 'going', 'heard', 'heart', 'among', 'asked', 'small', 'woman', 'whose', 'quite', 'words', 'given', 'taken', 'hands', 'until', 'since', 'light']

answer = random.choice(word_list) #choose random word from list above

y = 250 #y location on grid

def draw_square(x,y,color): #takes in x,y coordinates and a color
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):  #for loop to draw the square
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

def input_guess(prompt):
    my_input = turtle.textinput("5 letter word", prompt)
    if my_input == None: #submitting nothing or blank guess
        return "    "
    elif len(my_input) != 5: #sends the first 5 characters
        return my_input[0:5]
    else:
        return my_input.lower() #converts guess to all lowercase letters

def check_guess(my_input, answer, y):
    count = 0 #setting count for the loop below
    x = -250 #x location on grid
    for i in my_input:
        if i == answer[count]: #letter in correct spot = green square
            draw_square(x,y,"green")
        elif i in answer: #letter in word but not in correct spot = yellow square
            draw_square(x,y,"yellow")
        else: #letter guessed is not in word
            draw_square(x,y,"red")
        count += 1
        x += 75 #move x coordinate right by 75
    turtle.penup()
    turtle.goto(x,y-25)
    turtle.write(my_input, font = ("Verdana", 15, "normal"))

#main
for i in range(6): #starting the game
    guess_prompt = "What is guess " + str(i+1) + "?"
    my_input = input_guess(guess_prompt)
    check_guess(my_input, answer, y)
    y -= 75 #move y coordinate down by 75
    if my_input == answer:
        turtle.penup()
        turtle.goto(-300,-200)
        turtle.write("Well Done!", font=("Verdana", 42, "normal"))
        break
else: #only runs if you have used all your guesses without guessing correct word
    turtle.penup()
    turtle.goto(-300,-250)
    turtle.write(answer, font=("Verdana", 42, "normal"))
turtle.done() #needed for some Python editors

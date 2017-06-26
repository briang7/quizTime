
question_number = ["1", "2", "3", "4"]


easy_quiz = """__1__ is grounded in arithmetic, so it's __2__ to know how programming __3__ do simple math. Thankfully, Python follows the same math __4__ people do."""

easy_answers = ["programming", "important", "languages", "rules"]


medium_quiz = """Programmers use __1__ to represent __2__ in their code. This makes code __3__ to read by telling others what values mean. It also makes code easier to write by cutting down on potentially complicated numbers that __4__ in our code.""" 

medium_answers = ["variables", "values", "easier", "repeat"]


hard_quiz = """__1__ are an important concept in computer __2__. Loops let us __3__ blocks of code many times which can be really useful when we have to __4__ tasks."""

hard_answers = ["loops", "programming", "run", "repeat"]




def choose_level():    
    #"""This takes raw input from the user and makes sure that they are choosing a provided difficulty.  It then outputs that choice."""
    levels = ["easy", "medium", "hard"]
    choice = raw_input("Choose difficulty: easy, medium, hard: ").lower()
    while choice not in levels:
        print ("Choose again!")
        choice = raw_input("Choose difficulty: easy, medium, hard: ").lower()
    print ("            You've choosen " + choice + "!")
    return choice

def retrieve_quiz_and_answers(choice):
    #This prints the choosen quiz and outputs the choosen quiz and answers.
    if choice == "easy":
        print easy_quiz
        return (easy_quiz, easy_answers)
    if choice == "medium":
        print medium_quiz
        return (medium_quiz, medium_answers)
    else:
        print hard_quiz
        return (hard_quiz, hard_answers)


def ask_question(quiz, answers):
    #This does a lot lol.  It took me forever to get this right.  It takes the choosen string quiz and splits it up into a list.  Then it searches for the number using the num_in_question
    #function.  If it finds a number it asks the user to fill in the blank.  Then I have a while loop checking the answer with the choosen answers.  Once they get it right the quiz is printed with the correct answer
    #showing.  And it loops through again until there are no more numbers left.  Appending everthing to the replaced list and using join to turn it back into a string.
    replaced = []
    question = quiz.split()
    for word in question:
        number = num_in_question(word, question_number)
        if number != None:
            user_answer = raw_input("       What is blank " + number + "? ").lower()
            while user_answer != answers[int(number)-1]:
                print ("Try again!")
                user_answer = raw_input("       What is blank " + number + "? ").lower()
            
            word = word.replace("__" + number + "__", user_answer)
            replaced.append(word)
            the_rest = question[replaced.index(word)+1:]
            the_rest = " ".join(the_rest)
            new = " ".join(replaced) 
            print new + " " + the_rest
        else:
            replaced.append(word)
    
               


def num_in_question(word, question_number):
    #This takes the word from the for loop inside of ask_questions and checks to see if it matches the numbers from question_number using another for loop.
    for num in question_number:
        if num in word:
            return num
    return None


    

    
def play_game():
   #This brings everything together, initiating the game.
    choice = choose_level()
    quiz, answers = retrieve_quiz_and_answers(choice)
    ask_question(quiz, answers)
    print ("        Congratulations!!! You have finished the quiz")
             

play_game()



from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    Score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    imput = simpledialog.askstring(title='None', prompt="What is 5-3")
    #      // 3.  Use an if statement to check if their answer is correct
    if imput == "2":
        Score +=1
    #      // 4.  if the user's answer was correct, add one to their score 
    else:
        Score =-1

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above
    imput2 = simpledialog.askstring(title='None', prompt="What is 10-8")
    if imput == "2":
        Score +=1
    else:
        Score = -1

    imput3 = simpledialog.askstring(title='None', prompt="What is -4+6")
    if imput == "2":
       Score +=1
    else:
        Score = -1

    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    print("Your score is", Score)
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
    window.mainloop()



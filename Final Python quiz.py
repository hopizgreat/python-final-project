#store the questions in a variable named questions
questions = ["What should you do before trusting AI information?"]
#store the multiple choices for the questions
choices = ["A. trust AI", "B. verify wih reliable sources", "C. share without checking"]
#store the correct answer
correct_answers = ["B"]
#store the feedback to show when the user answers incorrectly
feed_back = ["AI can make mistakes, so information should be verified using reliable sources."]

#1st function asks the user the questions and asks for an input
def ask_question(question, choices):
    print(questions)
    #the code below is used to go over and print every choices of the questions
    for choice in choices:
        print(choice)
    #asks the user to choose an answer
    user_answer = input("Enter A, B, or C: ")
    return user_answer

#the secodn function checks whether the users answer is correct or not
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False



def quiz():
    questions = {
        "What is the capital of France?": "paris",
        "What is 5 + 7?": "12",
        "Which programming language is known for web development?": "javascript",
        "Who wrote 'Harry Potter'?": "jk rowling",
        "What is the square root of 64?": "8"
    }
    
    score = 0
    
    print("Welcome to the Quiz!\n")
    
    for question, answer in questions.items():
        user_answer = input(question + " ").lower()
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer is:", answer)
    
    print(f"\nYour final score is {score}/{len(questions)}")
    
if __name__ == "__main__":
    quiz()

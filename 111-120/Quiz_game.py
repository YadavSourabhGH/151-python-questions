# Quiz Game - Simple multiple choice quiz
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris",
        "choices": ["London", "Paris", "Berlin", "Madrid"]
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answer": "Jupiter",
        "choices": ["Mars", "Venus", "Jupiter", "Saturn"]
    },
    # More questions can be added here
]

score = 0

# Ask the questions and display the choices
for question_data in quiz_questions:
    question = question_data["question"]
    choices = question_data["choices"]

    print("\n" + question)
    for i in range(len(choices)):
        print(str(i+1) + ". " + choices[i])

    user_answer = input("Enter your answer: ")

    if user_answer == question_data["answer"]: # score
        score += 1
        print("Correct!")
    else:
        print("Wrong!")

print("Final score: " + str(score) + "/" + str(len(quiz_questions)))

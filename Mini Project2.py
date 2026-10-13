print("Welcome to the Python Quiz Game!")
print("--------------------------------")

score = 0

questions = [
    {
        "question": "1. Which language are we learning?",
        "options":["A. Java,", "B. Python","C. C++","D. HTML"],
        "answer":"B"
    },
    {
        "question":"2. Which functions displays output in Python?",
        "options":["A. input()","B. scan()","C. print()","D. show()"],
        "answer":"C"
    },
    {
        "question":"3. Which symbol is used for comments in Python?",
        "options":["A. //","B. #","C. /*","D. @@"],
        "answer":"B"
    },
    {
        "question":"4. Which data type stores True or False?",
        "options":["A. int","B. str","C. list","D. bool"],
        "answer":"D"
    },
    {
        "question":"5. Which keyword is used for a condition?",
        "options":["A. if","B. repeat","C. define","D. print"],
        "answer":"A"
    }
]

for item in questions:
    print("\n" + item["question"])
    
    for option in item["options"]:
        print(option)
        
    answer = input("Enter your answer (A/B/C/D): ").upper().strip()
    
    if answer == item["answer"]:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")
        print("Correct answer:", item["answer"])
        
print("\n----------------------------------")
print("Quiz completed!")
print("Your score:",score,"out of", len(questions))

percentage = (score/ len(questions)) * 100
print("Your percentage:",percentage,"%")

if percentage >= 80:
    print("Excellent work!")
elif percentage >60:
    print("Good Job")
elif percentage >=40:
    print("Keep practising!")
else:
    print("Don't give up! Try again. ")            
        
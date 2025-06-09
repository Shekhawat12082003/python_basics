def quiz():
    questions = [
        {
            "question": "What is the output of 3 + 2 * 2?",
            "options": ["5", "10", "7", "8"],
            "answer": "7"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["func", "define", "def", "function"],
            "answer": "def"
        },
        {
            "question": "What data type is this: [1, 2, 3]?",
            "options": ["Dictionary", "Tuple", "List", "Set"],
            "answer": "List"
        }
    ]
    score = 0
    for i,q in enumerate(questions,1):
        print(f"Question {i}:{q['question']}")
        for idx,options in enumerate(q["options"],1):
            print(f"{idx}:{options}")
        try:
           choice = int(input("Enter your Choice"))
           if q["options"][choice-1]==q["answer"]:
            print("Correct")
            score+=1
           else:
            print("wrong answer")
        except (ValueError, IndexError):
            print("⚠️ Invalid input. Moving to next question.")

    print(f"\n🎉 Quiz Over! You scored {score} out of {len(questions)}")
quiz()

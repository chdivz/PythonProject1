score = 0 
questions = [
    {
        "question" : "What is the capital of India",
        "options" : ["a)Delhi, b)Assam, c)Kerala, d)TamilNadu"],
        "answer" : "a"
    },
    {
        "question" : "Which is the national animal of India",
        "options" : ["a)Lion, b)Tiger, c)Kangaroo, d)Elephant"],
        "answer" : "b"
    },
    {
        "question" : "Which is the national bird of India",
        "options" : ["a)Cock, b)Duck, c)Ostrich, d)Peacock"],
        "answer" : "d"
    },
    {
        "question" : "What is the currency of India",
        "options" : ["a)Rupee, b)Dirham, c)Dolar, d)Aud"],
        "answer" : "a"
    },
    {
        "question" : "which is the smallest number given option",
        "options" : ["a)7, b)5, c)1, d)3"],
        "answer" : "c"
    }
]

for qus in questions:
    print("\n" + qus["question"])
    for option in qus["options"]:
        print(option)

    uans = input("Please select correct answer A/B/C/B").lower()

    if uans == qus["answer"]:
        print("correct")
        score += 1
    else:
         print("wrong")

print("Quiz Finished!")
print(f"Your Score is: {score} out of {len(questions)}")


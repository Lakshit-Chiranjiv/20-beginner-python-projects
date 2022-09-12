questions = {
    "q1": {
        "ques": "What is capital of India?",
        "opt": ['Kolkata','Mumbai','Delhi','Chennai'],
        "ans": 2
    },
    "q2": {
        "ques": "What is capital of USA?",
        "opt": ['Washington DC','Mumbai','Delhi','Chennai'],
        "ans": 0
    },
    "q3": {
        "ques": "What is capital of Canada?",
        "opt": ['Kolkata','Mumbai','Delhi','Toronto'],
        "ans": 3
    },
    "q4": {
        "ques": "What is capital of Russia?",
        "opt": ['Moscow','Mumbai','Delhi','Chennai'],
        "ans": 0
    },
    "q5": {
        "ques": "What is capital of Australia?",
        "opt": ['Kolkata','Canberra','Delhi','Chennai'],
        "ans": 1
    },
}

score = 0

for key,value in questions.items():
    print(value['ques'])
    for i in value['opt']:
        print(i)
    
    ans = int(input('\nEnter answer(1/2/3/4) : '))
    
    if ans-1 == value['ans']:
        print("Correct")
        score += 1
    else:
        print("Wrong")

    print(f"score: {score}")

print(f"\nFinal score : {score}")      

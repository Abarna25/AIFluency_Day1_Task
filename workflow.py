MARKS = {
    "abarna":92,
    "priya":85,
    "kavin":78,
    "rahul":88
}

QUESTIONS = [
    "What is Abarna's mark?",
    "Who scored highest?",
    "What is the average mark?",
    "Which students scored above 85?"
]

print("=== RULE BASED WORKFLOW ===")

for q in QUESTIONS:

    q = q.lower()

    if "abarna" in q:
        answer = f"Abarna scored {MARKS['abarna']}"

    elif "highest" in q:
        student = max(MARKS,key=MARKS.get)
        answer = f"{student} scored highest with {MARKS[student]}"

    elif "average" in q:
        avg = sum(MARKS.values())/len(MARKS)
        answer = f"Average = {avg}"

    elif "above 85" in q:
        students = [s for s,m in MARKS.items() if m>85]
        answer = str(students)

    else:
        answer = "No rule found"

    print("Q:",q)
    print("A:",answer)
    print("-"*50)
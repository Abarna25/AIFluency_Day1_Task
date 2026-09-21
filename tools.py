MARKS = {
    "abarna":92,
    "priya":85,
    "kavin":78,
    "rahul":88
}

def get_mark(student):
    return MARKS.get(student.lower(),"Student not found")

TOOLS = [
    {
        "type":"function",
        "function":{
            "name":"get_mark",
            "description":"Get mark of student",
            "parameters":{
                "type":"object",
                "properties":{
                    "student":{
                        "type":"string"
                    }
                },
                "required":["student"]
            }
        }
    }
]

TOOL_FUNCTIONS = {
    "get_mark":get_mark
}
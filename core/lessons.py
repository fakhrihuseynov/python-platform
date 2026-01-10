def get_lessons():
    return [
        {
            "id": "lesson-variables",
            "title": "Variables & Types",
            "example": "x = 42\nname = 'Fakhri'\nprint(type(x), type(name))",
            "challenge": "Assign a number to a variable and print its type.",
        },
        {
            "id": "lesson-lists",
            "title": "Lists & Methods",
            "example": "nums = [1,2,3]\nnums.append(4)\nprint(nums)",
            "challenge": "Create a list and append two items, then print it.",
        },
        {
            "id": "lesson-functions",
            "title": "Functions & Return",
            "example": "def add(a:int,b:int)->int:\n    return a+b\nprint(add(2,3))",
            "challenge": "Write a function greet(name) that returns 'Hello, <name>'.",
        },
    ]

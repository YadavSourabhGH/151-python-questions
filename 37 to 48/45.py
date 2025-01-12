# Create a dictionary with student names as keys and their grades as values. Prompt the user for a name and display the grade.

student_grades = {
    "Chaitanya": "A",
    "Sourabh": "B",
    "Vinayak": "C",
    "shashank": "D",
    "Yash": "E",
    "Soham": "F",
    "Ronak": "G",
    "Sujal": "H",
    "Rohan": "I",
    "Tanishq": "J"
}

name = input("Enter a student name: ")

if name in student_grades:
    print(f"The grade of {name} is {student_grades[name]}")
else:
    print("Student not found in the dictionary.")
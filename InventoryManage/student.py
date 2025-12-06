    #  1. Collections & Filtering
    # - Create a dictionary of students with their marks.
    # - Filter out students who scored below 40.
    # - Find the student with the highest marks using max().
    # - Return all students who scored above average.


students = {
    "Alice": 96,
    "Bob": 42,
    "Charlie": 37,
    "David": 90,
    "Eve": 55,
    "Frank": 28
}
below_40 = {name: marks for name, marks in students.items() if marks < 40}
passing_students = {name: marks for name, marks in students.items() if marks >= 40}
highest_scorer = max(students, key=students.get)
# print(students.values())
# print(sum(students.values())/ len(students))
average_marks = sum(students.values()) / len(students)
above_average_students = {name: marks for name, marks in students.items() if marks > average_marks}

print(f"Students scoring below 40: {below_40}")
print(f"Passing Students: {passing_students}")
print(f"Highest Scorer: {highest_scorer} with marks {students[highest_scorer]}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Students scoring above average: {above_average_students}")


def divide(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError: 
        return "Error: Division by zero is not allowed."
    except ArithmeticError: 
        return "Error: An arithmetic error occurred."
    except Exception as e: 
        return f"An error occurred: {e}"
    finally: 
        return f"An unexpected error occurred: {a} / {b}"
    
print(divide(10,0))
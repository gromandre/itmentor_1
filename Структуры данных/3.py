def find_students_with_grade_above(students, grade):

    result = {
        id: students[id] for id, info in students.items()
        if all(num >= grade for num in info['grades'])
    }

    return result

def create_set(students):   # result = []
    # for id, info in students.items():
    #     result+=info["grades"]
    # return set(result)

    return {grade for info in students.values() for grade in info['grades']}

students = {
    1: {
        "name": "Ivan",
        "age": 18,
        "grades": [5, 4, 5]
    },
    2: {
        "name": "Maria",
        "age": 19,
        "grades": [3, 4, 4]
    },
    3: {
        "name": "Pavel",
        "age": 18,
        "grades": [5, 5, 5]
    },
    4: {
        "name": "Anna",
        "age": 20,
        "grades": [4, 4, 3]
    }
}

print(find_students_with_grade_above(students, 4))
#print(create_set(students))
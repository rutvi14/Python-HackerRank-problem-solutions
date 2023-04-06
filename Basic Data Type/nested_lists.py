if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Sort the list based on grades
    sort_students = sorted(students, key=lambda x: x[0])
    
    # Sort the list based on grades
    sorted_students = sorted(students, key=lambda x: x[1])

    # Find the second lowest grade
    second_lowest_grade = sorted(set([x[1] for x in sorted_students]))[1]

    # Iterate over the sorted list to print the names of all students who have the second lowest grade
    for name, grade in sort_students:
        if grade == second_lowest_grade:
            print(name)

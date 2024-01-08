if __name__ == '__main__':
    student_data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_data.append([name,score])
        student_data.sort(key = lambda x : x[1])
        
    second_lowest_score = None
    for student in student_data:
        if student[1] > student_data[0][1]:
            second_lowest_score = student[1]
            break
        
    if second_lowest_score is not None:
        second_lowest_students = [student[0] for student in student_data if student[1] == second_lowest_score]
        for student in second_lowest_students:
            print(student)
        
        
        
           
        

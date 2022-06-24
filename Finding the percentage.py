if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    scores_list = student_marks[query_name]

    average_score = 0
    
    for i in scores_list:
        average_score += i
    
    format = "{:.2f}".format(average_score/3)
    
    print(format)


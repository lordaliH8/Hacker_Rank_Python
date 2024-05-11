if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = 0
    tmp = student_marks[query_name]
    for i in tmp:
        avg = avg +i
    print('{:.2f}'.format(float(avg/len(tmp))))

if __name__ == '__main__':
    students = []
    scores = []
    min = 20
    ret = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        students.append([name,score])
    tmp = set(scores)
    min = sorted(list(tmp))[1]


    for student in students:
        if student[1] == min :
            ret.append(student[0])
    for j in sorted(ret):
        print(j)

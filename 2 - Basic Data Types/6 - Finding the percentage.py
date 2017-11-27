if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    query_scores = student_marks[query_name]
    sumscores = 0
    for e in query_scores:
        sumscores += e
    sco= len(query_scores)
    average = sumscores/sco
    c = format(average, '.2f') #round the average at the second decimal
    print c
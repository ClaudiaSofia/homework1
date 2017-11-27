students = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    l = [name,score]
    students.append(l) #create a list of students
students.sort(key=lambda x: x[1])  #sort them in order of score, from the lower to the higher  
z  = students[0][1] #find the lower score
while students[0][1] ==z:
    del students[0] #delete all the students that have the lower score
slow= students[0][1] #Second LOWer score
lower_students = []
for student in students:
    if student[1]==slow: #find all the students that have the second lower score
        lower_students.append(student) #and add them in a list
lower_students.sort(key=lambda x: x[0]) #sort the list in alphabetic order
for stu in lower_students: 
    print stu[0]  #print each name in a new line

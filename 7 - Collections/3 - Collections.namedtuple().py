from collections import namedtuple
N= int(input())
fields = ",".join(raw_input().split())
av= 0.00
for i in range(N):
    students= namedtuple("students", fields)
    field1, field2, field3,field4 = raw_input().split()
    student = students(field1,field2,field3,field4)
    av += int(student.MARKS)

print av/N
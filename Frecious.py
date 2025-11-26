
student_num = int(input ("ENTERN NOMBER OF STUDENTS A HAVE A MISSINGACTIVITY: "))

student= {}

if student_num == 0:
    print("ALL STUDENT COMPLETE ACTIVITY")

else:
    for i in range(student_num):
        print ("STUDENT", i + 1)

    name = input ("ENTER STUDENT NAME:")
    missing = input ("ENTER STUDENT MISSING:")

    student[name] = missing

    print()
    print("STUDENT HAVE A MISSING ACTIVITY")
    for name, missing in student. items():
        print("NAME:", name)
        print("MISSING", missing)
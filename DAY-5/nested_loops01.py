subjects = "PYTHON,CSS,JAVA,HTML,JS,SQL,PHP,C++"
subjectList = subjects.split(",")

for i in subjectList:
    print("\nSubject Name:", i)
    for j in i: # nested loop
        print(j, end="|")
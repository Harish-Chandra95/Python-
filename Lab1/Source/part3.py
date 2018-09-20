python_students = input('Enter the list of students attending python class separated by comma: ')
webappStudents = input('Enter the list of students attending web technologies class separated by comma: ')


python_students = python_students.split(',') #splitting the space separated value into pythonstudents list
webappStudents = webappStudents.split(',')# splitting the values separated by space into webapp list

print('"list of students attending python but not web application"')

#calculating the symmetric difference between python stu and webaapp students using sets
print(list(set(python_students).symmetric_difference(set(webappStudents)))) #using the symmetric_differeence function

names = input("Enter names separated by commas: ").title().split(',')  # get and process input for a list of names
assignments = input("Enter assignment counts separated by commas: ").split(',')  # a list of the number of assignments
grades = input("Enter grades separated by commas: ").split(',')  # get and process input for a list of grades
potential_grade = []
for assignment, grade in zip(assignments, grades):
    assignment_grade = 2*int(assignment)+int(grade)
    potential_grade.append(assignment_grade)
# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade, pg in zip(names, assignments, grades, potential_grade):
    print(message.format(name, assignment, grade, pg))


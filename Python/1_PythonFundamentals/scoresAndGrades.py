print "Scores and Grades"
def Grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score < 60:
        return 'F'

for i in range(10):
    score = raw_input("Please enter your number score and press Enter: ")
    if score == '':
        print "no input"
    else:
        print "Score: " + str(score) + "; Your grade is " + Grade(int(score))

print "End of program. Bye!"

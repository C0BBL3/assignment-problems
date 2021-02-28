convertLetterToNumber letter
    | letter == "A" = 4
    | letter == "B" = 3
    | letter == "C" = 2
    | letter == "D" = 1
    | letter == "F" = 0

calcGPA [] = error "No Grades to find GPA of."
calcGPA grades = map (convertLetterToNumber) (grades)
calcGPA gpa = ( sum grades ) / length grades


main = print (calcGPA ["A", "B", "B", "C", "C", "C", "D", "F"])
""" working-with-lists.py
    This Python script shows how you can manipulate lists.

    Author: Andres Hernandez G.
    Email: andres.hernandezg@udem.edu
    Institution: Universidad de Monterrey
    First created: Sun 26 Jan, 2020
"""

grades = [100, 90.5, 90.3, 76, 54]
print('\nGrades: ', grades)

# indexing lists
print(grades[0])
print(grades[-1])
print(grades[0:3])
print(grades[1] + 6)
print(grades[-3:-1])

nested_grades = [100, 89, 74, [39, 75, 10]]
print(nested_grades)
print(nested_grades[2])
print(nested_grades[3])
print(nested_grades[3][1])

print(len(grades))
print(len(nested_grades))
mix_of_grades_and_courses = ['artificial intelligence',
                             2, 'supply chain', 90]
print(mix_of_grades_and_courses)
print(mix_of_grades_and_courses[0])
print(mix_of_grades_and_courses[-1])
print(type(mix_of_grades_and_courses))
print(len(mix_of_grades_and_courses))
mix_of_grades_and_courses.append('hi there')
print(mix_of_grades_and_courses)
mix_of_grades_and_courses.pop()
print(mix_of_grades_and_courses)
mix_of_grades_and_courses.insert(1, 'changed')
print(mix_of_grades_and_courses)
print(len(mix_of_grades_and_courses))
mix_of_grades_and_courses.insert(10, 2)
print(mix_of_grades_and_courses)
print(grades.__dir__())

print(grades + grades)
print(2*grades)
print(3*grades)
print(grades[1]+grades[2])
print(grades[0:2] + grades[2:4])

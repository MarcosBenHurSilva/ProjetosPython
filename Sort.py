# sort() method   = used with lists
# sort() function = used with iterables

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

name = lambda names: names[0]
grade = lambda grades: grades[1]
age = lambda ages: ages[2]

# students.sort(key=name)
# students.sort(key=grade)
# students.sort(key=age)

sorted_students_name = sorted(students, key=name)
sorted_students_grade = sorted(students, key=grade)
sorted_students_age = sorted(students, key=age)

# for i in students:
#     print(i)

for i in sorted_students_age:
    print(i)

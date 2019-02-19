students = {
	'cohort 1': 34,
	'cohort 2': 42,
	'cohort 3': 22
}

students["cohort 4"] = 43

for cohorts, number in students.items():
	print("{}: {} students".format(cohorts, number))


print(students.keys())

for cohorts, size in students.items():
	students[cohorts] =  size * 1.05

print(students)


students.pop("cohort 2")
print(students)


total_num_stud = 0
for students, number in students.items():
	total_num_stud += number

	print("The number of students in {} is {}.".format(students, number))
	


	


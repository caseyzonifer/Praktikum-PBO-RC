#122140054_Casey Manurung

# data siswa
students = [
    {'name': 'Ceb', 'grade': 90},
    {'name': 'Sebastian', 'grade': 80},
    {'name': 'Popowi', 'grade': 80},
    {'name': 'Janggar', 'grade': 75},
    {'name': 'Proboro', 'grade': 85},
]

# mengulang data siswa
for i in range(len(students)):
    print('student name ',i+1,': ', students[i]['name'],)
    print('student grade ',i+1,': ', students[i]['grade'])
print('')

# dictionary siswa 
grade_dict = {student['name']: student['grade'] for student in students}

# hasil dictionary
print("Resulting grade dictionary:")
print(grade_dict)

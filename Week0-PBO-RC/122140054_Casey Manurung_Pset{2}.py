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

# Mengurutkan data
urutkan_berdasarkan = input("Urutkan berdasarkan (name/grade): ")
urutkan = input("Urutkan data ter (Terbesr/Terkecil) urutkan: ")

if urutkan.lower() == "terbesar":
    for i in range(len(students)):
        for n in range(i):
            if students[i][urutkan_berdasarkan] > students[n][urutkan_berdasarkan]:
                tmp = students[n]
                students[n] = students[i]
                students[i] = tmp
elif urutkan.lower() == "terkecil":
    for i in range(len(students)):
        for n in range(i):
            if students[i][urutkan_berdasarkan] < students[n][urutkan_berdasarkan]:
                tmp = students[n]
                students[n] = students[i]
                students[i] = tmp
print('')

# dictionary siswa 
grade_dict = {student['name']: student['grade'] for student in students}

# hasil dictionary
print("Resulting grade dictionary:")
print(grade_dict)

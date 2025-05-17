Y = int(input('Макс. возраст: '))
X = input('Город: ').strip()
with open('klinika.txt', encoding='utf-8') as f:
    s = f.readlines()
    count = 0
    for patient in s:
        age = int(patient.split(' ')[2])
        city = patient.split(' ')[3]
        if age < Y and city == X:
            count += 1
print(f'Количество пациентов младше {Y} лет из города {X}: {count}')

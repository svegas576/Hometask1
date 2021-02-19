subj = {}

with open('labs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
print(f'Общее количество часов по предмету - {subj}')
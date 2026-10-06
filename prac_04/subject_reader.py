FILENAME = "subject_data.txt"

def main():
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)

def load_subjects(filename):
    subjects = []
    with open(filename, "r") as input_file:
        for line in input_file:
            parts = line.strip().split(",")
            subject_code = parts[0]
            lecturer = parts[1]
            number_of_students = int(parts[2])
            subject = [subject_code, lecturer, number_of_students]
            subjects.append(subject)
    return subjects

def display_subjects(subjects):
    for subject in subjects:
        subject_code = subject[0]
        lecturer = subject[1]
        number_of_students = subject[2]
        print(f"{subject_code} is taught by {lecturer} and has {number_of_students} students")


main()
"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    concatenated_list = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        concatenated_list.append(parts)
    input_file.close()
    return concatenated_list


def print_subject_details(data):
    """Print subject details with string length handling."""
    max_lecturer_width = max(len(parts[1]) for parts in data)
    max_students_width = max(len(str(parts[2])) for parts in data)
    for parts in data:
        subject = parts[0]
        lecturer = parts[1]
        number_of_students = parts[2]
        print(
            f"{subject} is taught by {lecturer:{max_lecturer_width}} and has {number_of_students:{max_students_width}} "
            f"students")


main()

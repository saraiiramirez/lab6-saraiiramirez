from grades_manager import add_student, avg_by_student


def main():
    print("Welcome to the Student Grades Manager!\n")

    my_grades = {}

    while True:
        print("Select an option:")
        print("1. Add a student")
        print("2. Print student grade averages")
        print("3. Exit")

        option = input()

        if option == "1":
            my_grades = add_student(my_grades)

        elif option == "2":
            print("Select an option:")
            print("a. Display all students")
            print("b. Display selected students")

            sub_option = input()

            if sub_option == "a":
                avg_by_student(my_grades)

            elif sub_option == "b":
                names = input("Enter student names (comma-separated): ")
                keys = [name.strip() for name in names.split(",")]
                avg_by_student(my_grades, keys)

            else:
                print("Invalid option selected!")

        elif option == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option selected!")

if __name__ == "__main__":
    main()
import grades_manager as gm 

def main():
    print("Welcome to the Student Grades Manager!")
    
    my_grades = {}
    
    while True:
        print("\nSelect an option:")
        print("1. Add a student")
        print("2. Print student grade averages")
        print("3. Exit")
        
        choice = input().strip()
        
        if choice == '1':
            print()
            my_grades = gm.add_student(my_grades)
            
        elif choice == '2':
            print("\nSelect an option:")
            print("a. Display all students")
            print("b. Display selected students")
            
            sub_choice = input().strip().lower()
            
            if sub_choice == 'a':
                print()
                gm.avg_by_student(my_grades)
                
            elif sub_choice == 'b':
                names_input = input("\nEnter student names (comma-separated):\n")
                names_list = [n.strip() for n in names_input.split(',')]
                print()
                gm.avg_by_student(my_grades, names_list)
                
            else:
                print("\nInvalid option selected!")
                
        elif choice == '3':
            print("\nGoodbye!")
            break
            
        else:
            print("\nInvalid option selected!")


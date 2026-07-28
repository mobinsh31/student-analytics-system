from data import scores, student_names, course_names
from analytics import (
    calculate_student_averages,
    calculate_course_averages,
    get_best_student,
    get_worst_student,
    get_best_course,
    get_worst_course,
    get_failed_student,
    get_top_N_students,
    student_report,
    get_class_statistics
)


def main():
    while True:

        print("\n" + "=" * 50)

        choice = input("""
========== Student Analytics System ==========

1. Show Student Averages
2. Show Course Averages
3. Show Best Student
4. Show Worst Student
5. Show Best Course
6. Show Worst Course
7. Show Failed Students
8. Show Top N Students
9. Show Student Report
10. Show Class Statistics
0. Exit

Choose an option:
""").strip()

        print()

        if choice == '1':
            averages = calculate_student_averages(scores)

            print("========== Student Averages ==========\n")

            for name, average in zip(student_names, averages):
                print(f"{name:<15}: {average:.2f}")

        elif choice == '2':
            averages = calculate_course_averages(scores)

            print("========== Course Averages ==========\n")

            for name, average in zip(course_names, averages):
                print(f"{name:<15}: {average:.2f}")

        elif choice == '3':
            name, average = get_best_student(scores, student_names)

            print("========== Best Student ==========\n")
            print(f"Name    : {name}")
            print(f"Average : {average:.2f}")

        elif choice == '4':
            name, average = get_worst_student(scores, student_names)

            print("========== Worst Student ==========\n")
            print(f"Name    : {name}")
            print(f"Average : {average:.2f}")

        elif choice == '5':
            name, average = get_best_course(scores, course_names)

            print("========== Best Course ==========\n")
            print(f"Course  : {name}")
            print(f"Average : {average:.2f}")

        elif choice == '6':
            name, average = get_worst_course(scores, course_names)

            print("========== Worst Course ==========\n")
            print(f"Course  : {name}")
            print(f"Average : {average:.2f}")

        elif choice == '7':
            failed_students = get_failed_student(scores, student_names)

            print("========== Failed Students ==========\n")

            if len(failed_students) == 0:
                print("All students passed successfully! 🎉")
            else:
                print(f"Total Failed Students : {len(failed_students)}\n")

                for name, average in failed_students:
                  print(f"{name:<20} Average : {average:.2f}")
        elif choice == '8':
            try:
                n = int(input("Enter N: "))

                if n <= 0:
                    print("N must be greater than zero.")

                elif n > len(student_names):
                    print(f"There are only {len(student_names)} students.")

                else:
                    top_students = get_top_N_students(scores, student_names, n)

                    print("\n========== Top Students ==========\n")

                    for name, average in top_students:
                        print(f"{name:<15}: {average:.2f}")

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == '9':

            student_name = input("Enter student name: ").strip()

            report = student_report(
                scores,
                student_names,
                course_names,
                student_name
            )

            if report is None:
                print("Student not found.")

            else:
                print("\n========== Student Report ==========\n")

                print(f"Name : {report['name']}")

                print("\nScores:")

                for course, score in report["scores"].items():
                    print(f"{course:<15}: {score}")

                print(f"\nAverage : {report['average']:.2f}")
                print(f"Rank    : {report['rank']}")

        elif choice == '10':

            statistics = get_class_statistics(scores)

            print("========== Class Statistics ==========\n")

            print(f"Number of Students     : {statistics['number_of_students']}")
            print(f"Number of Courses      : {statistics['number_of_courses']}")
            print(f"Overall Class Average  : {statistics['overall_average']:.2f}")
            print(f"Conditional Students   : {statistics['conditional_students']}")
            print(f"Passed Students        : {statistics['passed_students']}")

        elif choice == '0':
            print("\nThank you for using Student Analytics System!")
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
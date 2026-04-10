from data_loader import load_data
from analyzer import calculate_average, highest_score, lowest_score
from visualizer import plot_scores, plot_distribution
from student import Student

def show_menu():
    print("\n===== Student Analyzer =====")
    print("1. Show all students")
    print("2. Show statistics")
    print("3. Show grades")
    print("4. Show charts")
    print("5. Exit")

def main():
    df = load_data("students.csv")

    if df is None:
        return
    
    print("\nDataset Preview:")
    print(df.head())

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nStudents:")
            print(df)

        elif choice == "2":
            avg = calculate_average(df)
            print(f"\nAverage Score: {avg:.2f}")
            print("Highest Score:", highest_score(df))
            print("Lowest Score:", lowest_score(df))

        elif choice == "3":
            print("\nStudent Grades:")
            for _, row in df.iterrows():
                s = Student(row["Name"], row["Score"])
                print(f"{s.name}: {s.get_grade()}")

        elif choice == "4":
            plot_scores(df)
            plot_distribution(df)

        elif choice == "5":
            print("Thank you for you checking. ^_^ Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
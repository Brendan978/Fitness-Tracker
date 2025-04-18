from storage import init_db
from tracker import log_workout  # Import the function to log a workout

def main():
    init_db()
    print("Welcome to the Python Fitness Tracker!\n")

    while True:
        print("=== Menu ===")
        print("1. Log a Workout")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            log_workout()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
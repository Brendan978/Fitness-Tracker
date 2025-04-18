from storage import insert_workout, insert_exercise
from utils import get_int_input

def log_workout():
    print("\n--- Log a New Workout ---")
    date = input("Date (YYYY-MM-DD): ")
    workout_type = input("Workout Type (e.g., Cardio, Strength): ")
    duration = get_int_input("Duration (minutes): ")

    calories = None
    while True:
        calories_input = input("Calories burned (optional): ")
        if not calories_input:
            break
        try:
            calories = int(calories_input)
            break
        except ValueError:
            print("Please enter a valid number or leave blank.")

    notes = input("Notes (optional): ")
    workout_id = insert_workout(date, workout_type, duration, calories, notes)

    print("\n--- Add up to 6 Exercises ---")
    for i in range(6):
        add_more = input(f"Add exercise {i+1}? (y/n): ").lower()
        if add_more != 'y':
            break

        name = input("Exercise name: ")
        sets = get_int_input("Number of sets: ")
        reps = get_int_input("Reps per set: ")
        weight = get_int_input("Weight used (lbs): ")

        insert_exercise(workout_id, name, sets, reps, weight)

    print("✅ Workout and exercises logged!\n")

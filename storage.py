import sqlite3
import os

DB_PATH = os.path.join("data", "workouts.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            type TEXT NOT NULL,
            duration INTEGER NOT NULL,
            calories INTEGER,
            notes TEXT
        )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        workout_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        sets INTEGER,
        reps INTEGER,
        weight INTEGER,
        FOREIGN KEY (workout_id) REFERENCES workouts(id)
    )
""")

    conn.commit()
    conn.close()

def insert_workout(date, workout_type, duration, calories, notes):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO workouts (date, type, duration, calories, notes)
        VALUES (?, ?, ?, ?, ?)
    """, (date, workout_type, duration, calories, notes))
    workout_id = cursor.lastrowid  # Capture the new row's ID
    conn.commit()
    conn.close()
    return workout_id  # So we can use it to link exercises

def insert_exercise(workout_id, name, sets, reps, weight):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO exercises (workout_id, name, sets, reps, weight)
        VALUES (?, ?, ?, ?, ?)
    """, (workout_id, name, sets, reps, weight))
    conn.commit()
    conn.close()

import json
import os

DATA_FILE = "student_records.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    roll = input("Enter Roll Number: ").strip()
    data = load_data()
    if roll in data:
        print("Student record already exists.")
        return
    name = input("Enter Name: ").strip()
    course = input("Enter Course: ").strip()
    try:
        marks = float(input("Enter Marks (0-100): "))
    except ValueError:
        print("Invalid marks entered.")
        return

    data[roll] = {"name": name, "course": course, "marks": marks}
    save_data(data)
    print(f"Record for {name} saved successfully.")

def view_records():
    data = load_data()
    if not data:
        print("No records found.")
        return
    print("\n--- Student Database ---")
    for roll, info in data.items():
        print(f"Roll: {roll} | Name: {info['name']} | Course: {info['course']} | Marks: {info['marks']}")
    print("------------------------\n")

def main():
    while True:
        print("\n1. Add Student\n2. View Records\n3. Exit")
        choice = input("Select an option (1-3): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_records()
        elif choice == "3":
            print("Exiting system.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
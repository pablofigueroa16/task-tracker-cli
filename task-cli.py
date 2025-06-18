import sys
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    new_id = 1 if not tasks else tasks[-1]["id"] + 1
    now = datetime.now().isoformat()

    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarea agregada exitosamente (ID: {new_id})")

def main():
    args = sys.argv[1:]
    if not args:
        print("Por favor, especificá un comando.")
        return

    command = args[0]

    if command == "add":
        if len(args) < 2:
            print("Falta la descripción de la tarea.")
            return
        description = args[1]
        add_task(description)
    else:
        print("Comando no reconocido:", command)

if __name__ == "__main__":
    main()

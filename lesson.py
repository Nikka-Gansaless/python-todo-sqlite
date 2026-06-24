import sqlite3
connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

cursor.execute("""             
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT 
)   
""")
connection.commit()

def add_task():
    x = input("название: ")
    cursor.execute("""
    INSERT INTO tasks (title)
    VALUES (?)
    """, (x,) )
    connection.commit()

def show_task():
    cursor.execute("SELECT id, title FROM tasks")
    rows = cursor.fetchall()
    if not rows:
        print("список пуст")
    else:
        for i in rows:
            print(f"{i[0]}) {i[1]}")

def update_tusks():
    number = int(input("введите номер записи который хотите обновить: "))
    str = input("введите обновленную задачу: ")
    cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (str, number))
    connection.commit()



def delate_task():
    number = int(input("Введите номер задачи: "))
    cursor.execute("DELETE FROM tasks WHERE id = ?", (number,))
    connection.commit()

while 0 == 0:
    command = input("введите команду: ").strip().lower()
    if command == "показать список":
        show_task()
    elif command == "добавить задачу":
        add_task()
    elif command == "удалить задачу":
        delate_task()
    elif command == "обновить запись":
        update_tusks()
        


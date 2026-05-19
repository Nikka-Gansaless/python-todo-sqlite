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

cursor.execute("""
INSERT INTO tasks (title)
VALUES ("Купить хлеб")                             
""")
connection.commit()


task = [] 

def add_task():
    x = input("название: ")
    task.append(x)

def show_task():
    if not task:
        print("список пуст")
    else:    
        for index, i in enumerate(task):
            print(f"{index+1}) {i}")

def delate_task():
    number = int(input("Введите номер задачи"))
    task.pop(number-1)  

while 0 == 0:
    command = input("введите команду: ").strip().lower()
    if command == "показать список":
        show_task()
    elif command == "добавить задачу":
        add_task()
    elif command == "удалить задачу":
        delate_task()
        


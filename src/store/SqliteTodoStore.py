import sqlite3
from model.todo import Todo

class SqliteTodoStore:

    def __init__(self, db_path="data/todos.db"):
        # 如果文件不存在，会自动创建一个空文件。
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        
        self._create_table()

    def _create_table(self):
        self.conn.execute(""" 
        CREATE TABLE IF NOT EXISTS todos(
            todo_id INTEGER PRIMARY KEY,
            title TEXT,
            completed BOOLEAN,
            completed_at DATE,
            user_id INTEGER  )""")
        self.conn.commit()   # commit代表真正写进硬盘

    # 现在的save是全量覆盖，先清空数据库，再把内存的todos写进去。
    def save(self, todos):
        self.conn.execute('DELETE FROM todos')

        for todo in todos:
            self.conn.execute("""
                INSERT INTO todos (todo_id, title, completed, user_id) 
                VALUES(?, ?, ?, ?)
            """,
                (todo.todo_id, todo.title, todo.completed, todo.user_id))
        
        self.conn.commit()


    def load(self):
        cursor = self.conn.execute("""SELECT todo_id,title,
        completed,completed_at,user_id FROM todos""")
        #获取所选择的列数据的所有行；返回的是元祖列表。
        rows = cursor.fetchall()

        todos = []
        for row in rows:
            todo = Todo(*row)
            todos.append(todo)

        return todos


    def list_by_user(self,user_id):
        cursor = self.conn.execute("""
            SELECT todo_id,title,completed,completed_at,user_id FROM todos
            WHERE user_id = ?
        """, 
            (user_id,))
        rows=cursor.fetchall()
        return [Todo(*row) for row in rows]



        
            

import sqlite3
from app.model.todo import Todo

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

    
    def add(self,title,user_id):
        cursor = self.conn.execute("""
            INSERT INTO todos (title,completed,completed_at,user_id)
            VALUES(?, ?, ?, ?)
        """, (title,False,None,user_id))
        # SQL自动生成id,因此不需要insert todo_id。

        self.conn.commit()
        return cursor.lastrowid

    # 相当于读取功能，读取对应user_id的数据。
    def list_by_user(self,user_id):
        cursor = self.conn.execute("""
            SELECT todo_id,title,completed,completed_at,user_id FROM todos
            WHERE user_id = ?
        """, 
            (user_id,))
        rows=cursor.fetchall()
        return [Todo(*row) for row in rows]
    
    # 更新complete状态
    def toggle_completed(self,todo_id):
        todo = self.find_todo(todo_id)
        if not todo:
            return None   # 表示没找到
        
        new_completed = not todo.completed

        cursor = self.conn.execute("""
            UPDATE todos
            SET completed = ?
            WHERE todo_id = ?
        """, (new_completed,todo_id))

        self.conn.commit()
        if cursor.rowcount == 0:
            return None   # 没更新成功
        return new_completed
    
    # 更新title
    def update_title(self,title,todo_id):
        cursor = self.conn.execute("""
            UPDATE todos
            SET title = ?
            WHERE todo_id = ?                                                 
        """, (title,todo_id))
        self.conn.commit()
        return cursor.rowcount > 0
    
    # 更新completed_at
    def update_completed_at(self,completed_at,todo_id):
        cursor = self.conn.execute("""
            UPDATE todos
            SET completed_at = ?
            WHERE todo_id = ?                           
        """, (completed_at,todo_id))
        self.conn.commit()
        return cursor.rowcount > 0


    def delete(self,todo_id,user_id):
        cursor = self.conn.execute("""
            DELETE FROM todos
            WHERE todo_id = ? AND user_id = ?                  
        """, (todo_id,user_id))
        self.conn.commit()
        return cursor.rowcount > 0


    def find_todo(self,todo_id):
        cursor = self.conn.execute("""
            SELECT todo_id,title,completed,completed_at,user_id
            FROM todos
            WHERE todo_id=?               
        """, (todo_id,))
        row = cursor.fetchone()
        if row:
            return Todo(*row)
        return None
        
            

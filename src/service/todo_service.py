from model.todo import Todo
from datetime import datetime 

class TodoService:
    def __init__(self,store):
        self.store = store
        self.todos = store.load()
        if not self.todos:
            self.next_id = 1
        else:
            self.next_id = max((todo.todo_id for todo in self.todos)) + 1

    def add(self,title,user_id):
        todo = Todo(
            todo_id=self.next_id, 
            title=title,
            user_id=user_id)
        self.next_id += 1

        self.todos.append(todo)
        self.store.save(self.todos)

    def remove(self,todo_id,user_id):
        todo = self.find_todo(todo_id)
        if not todo:
            return False
        
        if todo.user_id != user_id:
            return False

        self.todos.remove(todo)
        self.store.save(self.todos)
        return True

    def find_todo(self,todo_id):
        for todo in self.todos:
            if todo.todo_id == todo_id:
                return todo
        return None
           

    # 列出对应用户的todos
    def get_user_todos(self,user_id):
        return self.store.list_by_user(user_id)
        
    

    def complete(self,todo_id,user_id):
        todo = self.find_todo(todo_id)

        if not todo:
            return False

        if todo.user_id != user_id:
            return False

        if todo.completed:
            todo.completed = False
            todo.completed_at = None
        else:
            todo.completed = True
            todo.completed_at = datetime.now().date()
        self.store.save(self.todos)
        return todo.completed

    # 更新此id的内容为title
    def update(self,todo_id,title,user_id):
        todo = self.find_todo(todo_id)
        if not todo:
            return False
        
        if todo.user_id != user_id:
            return False

        todo.title = title
        self.store.save(self.todos)
        return True

    def delete_all(self):
        self.todos.clear()
        self.store.save(self.todos)




    

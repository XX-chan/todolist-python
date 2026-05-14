from model.todo import Todo
from datetime import datetime 

class TodoService:
    def __init__(self,store):
        self.store = store
        

    def add(self,title,user_id):
        if title and user_id:
            return self.store.add(title,user_id)

    def remove(self,todo_id,user_id):
        todo = self.store.find_todo(todo_id)
        if not todo:
            return False
        
        if todo.user_id != user_id:
            return False

        return self.store.delete(todo_id,user_id)



    # 列出对应用户的todos
    def get_user_todos(self,user_id):
        return self.store.list_by_user(user_id)
        
    
    # complete状态变化和completed_at 变化
    def complete(self,todo_id,user_id):
        todo = self.store.find_todo(todo_id)

        if not todo:
            return False

        if todo.user_id != user_id:
            return False
        
        new_status = self.store.toggle_completed(todo_id)
        if new_status is not None:
            if new_status:
                todo.completed_at = datetime.now().date()
            else:
                todo.completed_at = None
        return self.store.update_completed_at(todo.completed_at,todo_id)
            
    

    # 更新此id的内容为title
    def edit(self,todo_id,title,user_id):
        todo = self.store.find_todo(todo_id)
        if not todo:
            return False
        
        if todo.user_id != user_id:
            return False

        return self.store.update_title(title,todo_id)




    

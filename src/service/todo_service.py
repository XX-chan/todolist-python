from model.todo import Todo

class TodoService:
    def __init__(self,store):
        self.store = store
        self.todos = store.load()
        if not self.todos:
            self.next_id = 1
        else:
            self.next_id = max((todo.id for todo in self.todos)) + 1

    def add(self,title):
        todo = Todo(self.next_id, title)
        self.next_id += 1

        self.todos.append(todo)
        self.store.save(self.todos)

    def remove(self,id):
        todo = self.find_todo(id)

        if not todo:
            return False

        self.todos.remove(todo)
        self.store.save(self.todos)
        return True

    def find_todo(self,id):
        for todo in self.todos:
            if todo.id == id:
                return todo
        return None
           
            
    def list(self):
        return self.todos
    
    def complete(self,id):
        todo = self.find_todo(id)

        if not todo:
            return False
        
        todo.completed = True
        self.store.save(self.todos)
        return True

    # 更新此id的内容为title
    def update(self,id,title):
        todo = self.find_todo(id)

        if not todo:
            return False
        
        todo.title = title
        self.store.save(self.todos)
        return True

    def delete_all(self):
        self.todos.clear()
        self.store.save(self.todos)




    

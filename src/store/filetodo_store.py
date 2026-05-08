from pathlib import Path
from model.todo import Todo

class FileTodoStore:
    def __init__(self,txt_path = "data/todos.txt"):
        self.file = Path(txt_path)
        #创建目录
        self.file.parent.mkdir(parents=True, exist_ok=True)


    def save(self, todos):
        with open(self.file, "w", encoding = "utf-8") as f:
            for todo in todos:
                #将todo对象转换为字符串
                line = f"{todo.id}|{todo.title}|{todo.completed}\n"
                f.write(line)


    def load(self):
        todos = []
        if not self.file.exists():
            return todos
        
        with open(self.file, "r", encoding = "utf-8") as f:
            for line in f:
                id, title, completed = line.strip().split("|")
                todo = Todo(int(id), title, completed == "True")
                todos.append(todo)
        return todos



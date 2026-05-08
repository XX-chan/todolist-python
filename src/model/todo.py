class Todo:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"[{'√' if self.completed else ' '}] {self.id}: {self.title}"
    
    
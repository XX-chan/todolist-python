class Todo:
    def __init__(self, todo_id, title, completed=False, completed_at=None,user_id=None):
        self.todo_id = todo_id
        self.title = title
        self.completed = completed
        self.completed_at = completed_at
        self.user_id = user_id


    def __repr__(self):
        return f"[{' √ ' if self.completed else '   '}] {self.todo_id}: {self.title} {self.completed_at}"
    
    
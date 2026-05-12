class Todo:
    def __init__(self, id, title, completed=False, completed_at=None):
        self.id = id
        self.title = title
        self.completed = completed
        self.completed_at = completed_at


    def __repr__(self):
        return f"[{' √ ' if self.completed else '   '}] {self.id}: {self.title} {self.completed_at}"
    
    
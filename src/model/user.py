class User:
    def __init__(self, user_id, username, password_hash, created_at=None):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.created_at = created_at

    
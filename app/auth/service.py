from model.user import User
from auth.store import SqliteUserStore
from werkzeug.security import generate_password_hash,check_password_hash

class AuthService:
    def __init__(self,store):
        self.user_store=store
    
    def register(self,username,password):
        password_hash = generate_password_hash(password)
        user = User(None,username,password_hash)
        self.user_store.add(user)
        return "login_page"
    
    # 如果账号密码正确，返回user，否则返回None。
    def login(self,username, password):
        user = self.user_store.get_by_username(username)
        if user and check_password_hash(user.password_hash,password):
            return user
        return None





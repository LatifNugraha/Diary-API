from database import db
from models.user import User
from datetime import datetime

def create_user(data):
    u = User(
        username=data["username"],
        email=data["email"],
        password_hash=data["password"],  # replace with hashed value in prod
        full_name=data.get("full_name")
    )
    db.session.add(u)
    db.session.commit()
    return u

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def update_user(user_id, data):
    u = User.query.get(user_id)
    if not u:
        return None
    u.username = data.get("username", u.username)
    u.email = data.get("email", u.email)
    if "password" in data:
        u.password_hash = data["password"]
    u.full_name = data.get("full_name", u.full_name)
    u.updated_at = datetime.utcnow()
    db.session.commit()
    return u

def delete_user(user_id):
    u = User.query.get(user_id)
    if not u:
        return False
    db.session.delete(u)
    db.session.commit()
    return True

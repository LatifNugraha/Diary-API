from database import db
from models.mood import Mood

def create_mood(data):
    m = Mood(
        name=data["name"],
        icon=data.get("icon"),
        description=data.get("description")
    )
    db.session.add(m)
    db.session.commit()
    return m

def get_all_moods():
    return Mood.query.all()

def get_mood_by_id(mood_id):
    return Mood.query.get(mood_id)

def update_mood(mood_id, data):
    m = Mood.query.get(mood_id)
    if not m:
        return None
    m.name = data.get("name", m.name)
    m.icon = data.get("icon", m.icon)
    m.description = data.get("description", m.description)
    db.session.commit()
    return m

def delete_mood(mood_id):
    m = Mood.query.get(mood_id)
    if not m:
        return False
    db.session.delete(m)
    db.session.commit()
    return True

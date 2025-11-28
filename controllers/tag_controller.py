from database import db
from models.tag import Tag

def create_tag(data):
    t = Tag(
        name=data["name"],
        description=data.get("description"),
        color=data.get("color")
    )
    db.session.add(t)
    db.session.commit()
    return t

def get_all_tags():
    return Tag.query.all()

def get_tag_by_id(tag_id):
    return Tag.query.get(tag_id)

def update_tag(tag_id, data):
    t = Tag.query.get(tag_id)
    if not t:
        return None
    t.name = data.get("name", t.name)
    t.description = data.get("description", t.description)
    t.color = data.get("color", t.color)
    db.session.commit()
    return t

def delete_tag(tag_id):
    t = Tag.query.get(tag_id)
    if not t:
        return False
    db.session.delete(t)
    db.session.commit()
    return True

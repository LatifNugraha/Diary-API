from database import db
from models.content import Content
from datetime import datetime

def create_content(data):
    c = Content(
        title=data.get("title"),
        text=data["text"],
        image_url=data.get("image_url"),
        location=data.get("location")
    )
    db.session.add(c)
    db.session.commit()
    return c

def get_all_contents():
    return Content.query.all()

def get_content_by_id(content_id):
    return Content.query.get(content_id)

def update_content(content_id, data):
    c = Content.query.get(content_id)
    if not c:
        return None
    c.title = data.get("title", c.title)
    c.text = data.get("text", c.text)
    c.image_url = data.get("image_url", c.image_url)
    c.location = data.get("location", c.location)
    c.updated_at = datetime.utcnow()
    db.session.commit()
    return c

def delete_content(content_id):
    c = Content.query.get(content_id)
    if not c:
        return False
    db.session.delete(c)
    db.session.commit()
    return True

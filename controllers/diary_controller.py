from database import db
from models.diary_entry import DiaryEntry
from models.tag import Tag
from datetime import datetime

def create_entry(data):
    # expect: user_id, content_id, mood_id (optional), tag_ids (optional list)
    entry = DiaryEntry(
        user_id=data["user_id"],
        content_id=data["content_id"],
        mood_id=data.get("mood_id")
    )

    if "tag_ids" in data and isinstance(data["tag_ids"], (list, tuple)):
        tags = Tag.query.filter(Tag.id.in_(data["tag_ids"])).all()
        entry.tags = tags

    db.session.add(entry)
    db.session.commit()
    return entry

def get_all_entries():
    return DiaryEntry.query.all()

def get_entry_by_id(entry_id):
    return DiaryEntry.query.get(entry_id)

def update_entry(entry_id, data):
    e = DiaryEntry.query.get(entry_id)
    if not e:
        return None
    e.user_id = data.get("user_id", e.user_id)
    e.content_id = data.get("content_id", e.content_id)
    e.mood_id = data.get("mood_id", e.mood_id)
    if "tag_ids" in data and isinstance(data["tag_ids"], (list, tuple)):
        tags = Tag.query.filter(Tag.id.in_(data["tag_ids"])).all()
        e.tags = tags
    e.updated_at = datetime.utcnow()
    db.session.commit()
    return e

def delete_entry(entry_id):
    e = DiaryEntry.query.get(entry_id)
    if not e:
        return False
    db.session.delete(e)
    db.session.commit()
    return True

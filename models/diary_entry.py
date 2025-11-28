from database import db
from datetime import datetime
from models.entry_tag import entry_tags

class DiaryEntry(db.Model):
    __tablename__ = "diary_entries"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content_id = db.Column(db.Integer, db.ForeignKey("contents.id"), nullable=False)
    mood_id = db.Column(db.Integer, db.ForeignKey("moods.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # Koneksi
    tags = db.relationship("Tag", secondary=entry_tags, backref=db.backref("entries", lazy="dynamic"))

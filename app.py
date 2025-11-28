from flask import Flask
import pymysql
from config import Config
from database import db

app = Flask(__name__)
app.config.from_object(Config)

# ===== BUAT DATABASE =====
conn = pymysql.connect(
    host=Config.DB_HOST,
    user=Config.DB_USER,
    password=Config.DB_PASSWORD
)
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.DB_NAME}")
conn.close()

# ===== INIT ORM =====
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}/{Config.DB_NAME}"
)
db.init_app(app)

# ===== IMPORT MODELS =====
from models.user import User
from models.content import Content
from models.mood import Mood
from models.tag import Tag
from models.diary_entry import DiaryEntry
from models.entry_tag import entry_tags

# ===== BUAT TABLES =====
with app.app_context():
    db.create_all()

# ===== REGISTER ROUTES =====
from routes.user_routes import user_bp
from routes.content_routes import content_bp
from routes.mood_routes import mood_bp
from routes.tag_routes import tag_bp
from routes.diary_routes import diary_bp

app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(content_bp, url_prefix="/contents")
app.register_blueprint(mood_bp, url_prefix="/moods")
app.register_blueprint(tag_bp, url_prefix="/tags")
app.register_blueprint(diary_bp, url_prefix="/diary")

if __name__ == "__main__":
    app.run(debug=True)

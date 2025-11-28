class Config:
    DB_USER = "root"
    DB_PASSWORD = ""
    DB_HOST = "localhost"
    DB_PORT = 3306
    DB_NAME = "db_diary"

    # initial URI points to server (no specific db) for DB creation step
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

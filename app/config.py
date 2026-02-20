import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:454678@localhost:5432/todo_list_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
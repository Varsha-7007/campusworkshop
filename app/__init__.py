"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host=" dpg-chaa7jm7avj5o48bgo40-a.oregon-postgres.render.com",
        database="todo_nlet",
        user="todo_nlet_user",
        password="z25JGwuDXps8uddKH7x3MUqnjMs5MVS3")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

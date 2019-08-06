#encoding:utf-8
from app import create_app, db
from flask_migrate import Migrate
from app.models import User, Post

app = create_app()
migrate = Migrate(app, db)


# 设定shell 上下文，避免每次调试的时候多次import
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

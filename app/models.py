from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
import bleach
from markdown import markdown
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True,unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    body = db.Column(db.Text)
    html_body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    type = db.Column(db.Enum('post', 'review'), default='post')
    age = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

    @staticmethod
    def on_body_change(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'h4', 'h5', 'p', 'hr', 'img',
			'video', 'div', 'iframe', 'br', 'span', 'src', 'class']

        allowed_attrs = {'*': ['class'],
                         'a': ['href', 'rel'],
                         'img': ['src', 'alt']}

        html_body = markdown(value, output_format='html', extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables', 'markdown.extensions.toc'])
        html_body = bleach.clean(html_body, tags=allowed_tags, strip=True, attributes=allowed_attrs)
        html_body = bleach.linkify(html_body)
        target.html_body = html_body


db.event.listen(Post.body, 'set', Post.on_body_change)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

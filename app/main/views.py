from app.main import bp
from flask import render_template
from app import admin
from app.models import User, Post, db
from flask_admin import form
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


@bp.route('/')
def hello_world():
    posts = Post.query.filter_by(type='post')
    return render_template('index.html', title='Essay', posts=posts)

@bp.route('/review')
def show_reviews():
    posts = Post.query.filter_by(type='review')
    return render_template('index.html', title='Review', posts=posts)


@bp.route('/p/<int:id>')
def get_blog(id):
    post = Post.query.get(id)
    return render_template('post.html', post=post)


# flask-admin 自定义定制view

# list 过滤
# class MicroBlogModelView(ModelView):
#    column_exclude_list = ['password_hash', 'html_body']
# admin.add_view(MicroBlogModelView(User, db.session))
# admin.add_view(MicroBlogModelView(Post, db.session))


# create form 过滤，filter
class MyBaseForm(form.BaseForm):
    def do_something(self):
        pass


class MyModelView(ModelView):
    form_base_class = MyBaseForm
    form_excluded_columns = ('password_hash', 'html_body')
    column_exclude_list = ['password_hash', 'html_body']

# 控制访问后台页面的权限，经过认证的才能访问
    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Post, db.session))
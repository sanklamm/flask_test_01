from flask import Flask, redirect, url_for, current_app
from config import Config
#from app import db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_admin import Admin, helpers, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_user import UserManager, current_user
from flask_babelex import Babel

print("--------------- HI ------------")
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
# for login
login = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    
    # for debugging
    # app.debug = True
    # toolbar = DebugToolbarExtension(app)
    
    # for login
    login.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app import models#, create_app
    # db.create_all(app=create_app())
    # db.session.commit()
    # if not models.Role.query.filter_by(name="Admin").first:
    #     role_admin = models.Role('Admin')
    #     db.session.add(role_admin)
    #     db.session.commit()
    # if not models.Role.query.filter_by(name="User").first:
    #     role_user = models.Role('User')
    #     db.session.add(role_user)
    #     db.session.commit()
    # if not models.User.query.filter_by(password="MTS61PWD").first:
    #     role_ = Role.query.filter_by(name="Admin").first()
    #     admin_user = models.User(password="MTS61PWD", used=False)
    #     admin_user.roles = [role_,]
    #     db.session.add(admin_user)
    #     db.session.commit()


    # Initialize Flask-BabelEx
    # babel = Babel(app)

    # from app import routes

    # class MyModelView(ModelView):
    # # Allow only admins to access Admin views
    #     def is_accessible(self):
    #         if not current_user.is_authenticated: return False
    #         return current_user.has_roles('Admin')

    # class MyAdminIndexView(AdminIndexView):
    #     @expose('/')
    #     def index(self):
    #         if not current_user.is_authenticated:
    #             return redirect(url_for('login'))
    #         return super(MyAdminIndexView, self).index()

    # admin = Admin(app, name='Backend', index_view=MyAdminIndexView(), template_mode='bootstrap3')
    # admin.add_view(MyModelView(models.Question, db.session))
    # admin.add_view(MyModelView(models.Answer, db.session))
    # admin.add_view(MyModelView(models.User, db.session))
    return app
    
from app import models

# Setup Flask-User and specify the User data-model
# user_manager = UserManager(app, db, models.User)

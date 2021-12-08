from app import create_app
from app.views import app_views

# create Flask app
app = create_app('dev')

# regist blueprint
app.register_blueprint(app_views)

# run flask app
if __name__ == '__main__':
    app.run()

from flask import Flask
from app.api.views import api_blueprint
from app.posts.views import post_blueprint


app = Flask(__name__)

app.register_blueprint(api_blueprint)
app.register_blueprint(post_blueprint)

app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    app.run()
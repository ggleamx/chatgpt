from flask import Flask
from routes.chatgpt_route import chatgpt_route

def create_app():
    app = Flask(__name__)
    app.register_blueprint(chatgpt_route)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

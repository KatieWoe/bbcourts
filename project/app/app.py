from flask import Flask

app = Flask(__name__)

from core.routes import core
app.register_blueprint(core)




if __name__ == '__main__':
    app.run(debug=True)
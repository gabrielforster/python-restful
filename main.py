from flask import Flask
from flask_restful import Api, Resource

app = app = Flask(__name__)
api = Api(app)

from languages import Languages
from teacher import Teachers

api.add_resource(Languages, '/languages')
api.add_resource(Teachers, '/teachers')

if __name__ == "__main__":
    app.run(debug=True)

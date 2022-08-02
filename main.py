from flask import Flask
from flask_restful import Api

app = app = Flask(__name__)
api = Api(app)

from languages import Languages
from teacher import Teachers
from students import Students

api.add_resource(Languages, '/languages')
api.add_resource(Teachers, '/teachers')
api.add_resource(Students, '/students')

if __name__ == "__main__":
    app.run(debug=True)

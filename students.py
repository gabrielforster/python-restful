from flask_restful import Resource
from utils import isAdult


students = [
    {
        'name': 'Gabriel',
        'lastname': 'Rocha',
        'isAdult': isAdult(18),
    },
    {
        'name': 'Leonardo',
        'lastname': 'Rafaelli',
        'isAdult': isAdult(17),
    }
]

class Students(Resource):
    def get(self):
        return students
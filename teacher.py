from flask_restful import Resource

teachers =[
    {
        'name': 'Luciano',
        'age': 30,
        'lesson': 'System Development'
    },
    {
        'name': 'Karen',
        'age': 29,
        'lesson': 'Mobile App development'
    }
]

class Teachers(Resource):
    def get(self):
        return teachers
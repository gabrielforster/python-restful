from flask_restful import Resource

languages = [
    {
        'name': 'Javascript',
        'type': 'dynamic',
        'description': 'Just javascript, fvck'
    },
    {
        'name': 'Typescript',
        'type': 'typed',
        'description': 'Javascript with types'
    },
    {
        'name': 'Java',
        'type': 'idk',
        'description': 'this sucks'
    },
    {
        'name': 'python',
        'type': 'dynamic',
        'description': 'much better than java'
    }
    ]

class Languages(Resource):
    def get(self):
        return languages

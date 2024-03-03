
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, fields, marshal_with


app = Flask(__name__)
api = Api(app)


class HelloRest(Resource):

    def get(self):
        return {"key": "value"}, 200, {"header_info": "value"}

    def post(self):
        return "method Post"

data_base = ["Apple", "Amazone", "Alphabet", "Microsoft"]

parser = reqparse.RequestParser()
parser.add_argument('page', type=int, location="args")
parser.add_argument('parag', type=int, location="args", help="Must be str! Error")

class Companies(Resource):

    def get(self):
        my_list_comp = ["Compan-1","Compan-2","Compan-3"]
        args = parser.parse_args()
        print(args)
        response = dict()
        for i, elem in enumerate(data_base, 1):
            response[i] = elem
        response['my_comp'] = my_list_comp[args["page"]]
        return response

    def post(self, value):
        data_base.append(value)
        print(data_base)
        return "Successful POST", 200

    def put(self):
        import json
        data = json.loads(request.data)
        # print(data)
        company = data.get('company')
        position = data.get('position') - 1
        print(position, company)

        data_base.remove(company)
        data_base.insert(position, company)
        return "Successful UPDATE", 200

    def delete(self, value):
        data_base.remove(value)
        return "Successful DELETE", 200


data_fish = ["Carp","Dorado","Perch"]

structure_fish = {
    "name": fields.String,
    "size": fields.String,
}


class Fish:

    def __init__(self, name, size):
        self.name = name
        self.size = size


class GetFish(Resource):

    @marshal_with(structure_fish)
    def get(self):
        fish = Fish("Carp", "30cm")
        return fish


api.add_resource(HelloRest, "/")
api.add_resource(Companies, "/companies", "/companies/<value>")
api.add_resource(GetFish, "/fish")

if __name__ == "__main__":
    app.run(debug=True)
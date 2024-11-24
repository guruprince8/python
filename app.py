from flask import Flask, jsonify, request
from waitress import serve
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        return jsonify({'message': 'hello world'})

    def post(self):
        data = request.get_json()
        return jsonify({'data': data})


class Square(Resource):
    def get(self, num):
        return jsonify(({'square': num ** 2}))


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = 'hello world'
        return jsonify({'data': data})


api.add_resource(Hello, '/hello')
api.add_resource(Square, '/square/<int:num>')


context = ('./certs/tomcat.crt', './certs/tomcat.key')
#serve(app, host="0.0.0.0", port=5001, url_scheme='https')
app.run(debug=True, port=5001, host="0.0.0.0", ssl_context=context)

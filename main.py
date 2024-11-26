from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from waitress import serve
from web.default import DefaultRouter
from web.hello import HelloRouter
from web.square import SquareRouter
from web.ml import MLRouter
from web.wiki import WikiRouter
from web.dsa import DSARouter
from web.file import FileRouter
from dsa import ArrayStructure


app = Flask(__name__)
api = Api(app)
asr = ArrayStructure()
print(asr.data)


api.add_resource(HelloRouter, '/hello')
api.add_resource(SquareRouter, '/square/<int:num>')
api.add_resource(MLRouter, '/ml')
api.add_resource(WikiRouter, '/wiki')
api.add_resource(DSARouter, '/dsa')
api.add_resource(FileRouter, '/file')
api.add_resource(DefaultRouter, "/")


if __name__ == '__main__':
    context = ('./certs/tomcat.crt', './certs/tomcat.key')
    #serve(app, host="0.0.0.0", port=5001, url_scheme='https')
    app.run(debug=True, port=5001, host="0.0.0.0", ssl_context=context)
    #app.run(debug=True, port=5001, host="0.0.0.0")

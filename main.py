from flask import Flask
from flask_restful import  Api,Resource


app = Flask(__name__)
api = Api(app)

names = {"syam":{"Age":22,"Study":"B.Tech"},
         "Manoj":{"Age":21,"Study":"B.Tech Cse"}}

"""class HelloWorld(Resource):
    @app.route("/")
    def get(self,name):
        print(name+"jkdbcvfh")
        return names[name]
    def post(self):
        return {'data':"Posted Successfully"}


api.add_resource(HelloWorld,"/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug = True)"""

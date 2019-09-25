from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from views import Quote

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(Quote, '/')

if __name__ == "__main__":
    app.run()

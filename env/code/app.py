import os

from flask import Flask
from flask_restful import Api
from resources.task import Task,TaskList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

api.add_resource(Task,'/task/<string:name>')
api.add_resource(TaskList,'/tasks/')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

import os

from flask import Flask
from flask_restful import Api
from resource.task import Task,TaskList

app = Flask(__name__)
# later add the db configuration here

api = Api(app)

api.add_resource(Task,'/task/<string:name>')
api.add_resource(TaskList,'/tasks/')

if __name__ == '__main__':
    app.run(debug=True)

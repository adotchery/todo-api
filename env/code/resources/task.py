from flask_restful import Resource
from models.task import TaskModel

class Task(Resource):
    def get(self):
        return {"message":"Hello World"}

class TaskList(Resource):
    def get(self):
        return {"message":"whats up"}
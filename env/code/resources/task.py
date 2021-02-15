from flask_restful import Resource, reqparse
from models.task import TaskModel

class Task(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('task',
        type=str,
        required=True,
        help="This field can not be left blank!"
    )
    parser.add_argument('day',
        type=str,
        required=True,
        help="This field can not be left blank!"
    )
    # parser.add_argument('reminder',
    #     type=bool,
    #     required=True,
    #     help="This field can not be left blank!"
    # )

    def get(self):
        return {"message":"Hello World"}

    def post(self):
        data = Task.parser.parse_args()
        task = TaskModel(task=data['task'], day=data['day']) #reminder=data['reminder']
        task.save_to_db()
        return {"message":"new task created"}

class TaskList(Resource):
    def get(self):
        return list(map(lambda x: x.json(), TaskModel.query.all()))
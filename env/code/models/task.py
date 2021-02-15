from db import db

class TaskModel(db.Model):
    
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250))
    day = db.Column(db.String(200))
    # reminder = db.Column(db.Boolean)

    def __init__(self,task, day):
        self.task = task
        self.day = day
        # self.reminder = bool

    def json(self):
        return {"text": self.task, "day": self.day}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


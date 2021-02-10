from db import db

class TaskModel(db.Model):
    
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(160))
    day = db.Column(db.String(160))
    reminder = db.Column(db.Boolean)

    def __init__(self,text,day,reminder):
        self.text = text
        self.day = day
        self.reminder = reminder

    def json(self):
        return {"text": self.text, "day": self.day}

    


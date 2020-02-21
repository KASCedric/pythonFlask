import json

from sqlalchemy import event, DDL

from src import db


class Cedric(db.Model):
    """Model for Cedric table."""

    __tablename__ = 'cedric'

    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(db.String(64), index=False, unique=False, nullable=True)

    prenom = db.Column(db.String(64), index=False, unique=False, nullable=True)

    age = db.Column(db.Integer, index=False, unique=False, nullable=True)

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_data):
        j_str = str(json_data).replace("\'", "\"")
        json_dict = json.loads(j_str)
        return cls(**json_dict)

    def __repr__(self):
        return "<Cedric {}>".format(self.id)


initialization_ddl = DDL(
    """
    INSERT INTO cedric (id, prenom, nom, age) 
    VALUES 
    (1,"cedric", "kuassivi", 22);
    """
)

event.listen(Cedric.__table__, 'after_create', initialization_ddl)
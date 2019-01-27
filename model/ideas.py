from app import db
from passlib.hash import pbkdf2_sha256 as sha256
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import time
import uuid

def generate_uuid():
    value = str(uuid.uuid4().hex)
    return value[:9]

class IdeasModel(db.Model):

    __tablename__ = 'ideas'
    id = db.Column(db.String, primary_key=True, unique=True, default=generate_uuid)
    content = db.Column(db.String(255), nullable=False)
    impact = db.Column(db.Integer, nullable=False)
    ease = db.Column(db.Integer, nullable=False)
    confidence = db.Column(db.Integer, nullable=False)
    average_score = db.Column(db.Float, nullable=False)
    CreateAt = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except SQLAlchemyError as err:
            print(err)
            return False

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first_or_404()

    @classmethod
    def return_by_id(cls, id):
        def to_json(x):
            return {
                'id': x.id,
                'content': x.content,
                'impact': x.impact,
                'ease': x.ease,
                'confidence': x.confidence,
                'average_score': x.average_score,
                'created_at': time.mktime(x.CreateAt.timetuple())
            }

        return to_json(cls.query.filter_by(id=id).first_or_404())

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'id': x.id,
                'content': x.content,
                'impact': x.impact,
                'ease': x.ease,
                'confidence': x.confidence,
                'average_score': x.average_score,
                'created_at': time.mktime(x.CreateAt.timetuple())
            }
        return list(map(lambda x: to_json(x), IdeasModel.query.all()))

    @classmethod
    def return_by_page(cls, page):
        def to_json(x):
            return {
                'id': x.id,
                'content': x.content,
                'impact': x.impact,
                'ease': x.ease,
                'confidence': x.confidence,
                'average_score': x.average_score,
                'created_at': time.mktime(x.CreateAt.timetuple())
            }
        return list(map(lambda x: to_json(x), IdeasModel.query.paginate(page=page,
                                                                        per_page=10).items))

    @classmethod
    def delete_by_id(cls, id):
        user = cls.query.filter_by(id=id).first_or_404()
        try:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'Idea: {}, deleted.'.format(user.id)}, 200
        except SQLAlchemyError as err:
            print(err)
            return {'message': 'Something went wrong'}, 404

    @classmethod
    def update_by_id(cls, id, content, impact, ease, confidence):
        user = cls.query.filter_by(id=id).first_or_404()
        user.content = content
        user.impact = int(impact)
        user.ease = int(ease)
        user.confidence = int(confidence)
        user.average_score = (int(impact) + int(ease) + int(confidence))/3
        try:
            db.session.commit()
            def to_json(x):
                return {
                    'content': x.content,
                    'impact': x.impact,
                    'ease': x.ease,
                    'confidence': x.confidence
                }
            return to_json(cls.query.filter_by(id=id).first_or_404())
        except SQLAlchemyError as err:
            print(err)
            return {'message': 'Can\'t update data'}, 404

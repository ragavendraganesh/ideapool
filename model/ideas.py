from app import db
from passlib.hash import pbkdf2_sha256 as sha256
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import func


class UserModel(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(255), nullable=False)
    impact = db.Column(db.Integer, nullable=False)
    ease = db.Column(db.Integer, nullable=False)
    confidence = db.Column(db.Integer, nullable=False)
    average_score = db.Column(db.Integer, nullable=False)
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
                'created_at': x.CreateAt
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
                'created_at': x.CreateAt
            }
        return list(map(lambda x: to_json(x), UserModel.query.all()))

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
    def update_passowrd_by_id(cls, id, password):
        user = cls.query.filter_by(id=id).first_or_404()
        user.password = cls.generate_hash(password=password)
        try:
            db.session.commit()
            return {'message': 'Pasword from user: {}, updated.'.format(user.name)}, 200
        except SQLAlchemyError as err:
            print(err)
            return {'message': 'Can\'t update Password'}, 404

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

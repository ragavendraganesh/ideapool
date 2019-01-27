from flask_restful import Resource, reqparse
from flask import jsonify
from model.user import UserModel
# from model.auth import RevokedTokenModel
from sqlalchemy.exc import IntegrityError
import time, os
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)
import string
from random import *
import re
from libgravatar import Gravatar

parseUserCreate = reqparse.RequestParser()
parseUserCreate.add_argument('name', help='This field cannot be blank', required=True)
parseUserCreate.add_argument('email', help='This field cannot be blank', required=True)
parseUserCreate.add_argument('password', help='This field cannot be blank')

parseUserCreateNoPassword = reqparse.RequestParser()
parseUserCreateNoPassword.add_argument('email', help='This field cannot be blank', required=True)


parserUserUpdate = reqparse.RequestParser()
parserUserUpdate.add_argument('id', help='This field cannot be blank', required=True)
parserUserUpdate.add_argument('name', help='This field cannot be blank', required=True)
parserUserUpdate.add_argument('email', help='This field cannot be blank')
parserUserUpdate.add_argument('password', help='This field cannot be blank')

min_char = 8
max_char = 12
allchar = string.ascii_letters + string.punctuation + string.digits


def gravatar_gen(email):
    default = "http://icons.iconarchive.com/icons/papirus-team/papirus-status/256/avatar-default-icon.png"
    size = 40
    gravatar = Gravatar(email)
    gravatar_url = gravatar.get_image(size=size, default=default)
    return gravatar_url

def validate(password):
    if len(password) < 8:
        return {"error"}
    elif re.search('[0-9]',password) is None:
        return {"error"}
    elif re.search('[A-Z]',password) is None:
        return {"error"}
    elif re.search('[a-z]',password) is None:
        return {"error"}
    else:
        return {"success"}


class UserRegistration(Resource):
    def post(self):
        data = parseUserCreate.parse_args()
        validate_password = validate(password=data["password"])
        if "error" in validate_password:
            return {"error": "Password should be at least 8 characters, " \
                             "including 1 uppercase letter, 1 lowercase letter, " \
                             "and 1 number"}, 417
        new_user = UserModel(
            name=data["name"],
            email=data['email'],
            password=UserModel.generate_hash(data['password']),
            avatar_url=gravatar_gen(data["email"])
        )
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['email'])
            refresh_token = create_refresh_token(identity = data['email'])
            return {
                       'jwt': access_token,
                       'refresh_token': refresh_token
                   }, 201
        except:
            return {'message': 'Something went wrong '}, 500

    @jwt_required
    def get(self, id=None):
        if id is None:
            return UserModel.return_all()
        else:
            return UserModel.return_by_id(id)


class UserDetails(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return UserModel.return_by_email(email=current_user)

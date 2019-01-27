from flask_restful import Resource, reqparse
from flask import jsonify
from model.ideas import IdeasModel
# from model.auth import RevokedTokenModel
from sqlalchemy.exc import IntegrityError
import time, os
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)
import string
from random import *
import re
from libgravatar import Gravatar

parseIdeasCreate = reqparse.RequestParser()
parseIdeasCreate.add_argument('content', help='This field cannot be blank', required=True)
parseIdeasCreate.add_argument('impact', help='This field cannot be blank', required=True)
parseIdeasCreate.add_argument('ease', help='This field cannot be blank', required=True)
parseIdeasCreate.add_argument('confidence', help='This field cannot be blank', required=True)

parseUserCreateNoPassword = reqparse.RequestParser()
parseUserCreateNoPassword.add_argument('email', help='This field cannot be blank', required=True)

parseGetIdeas = reqparse.RequestParser()
parseGetIdeas.add_argument('page', help='This field cannot be blank')

parseIdeasUpdate = reqparse.RequestParser()
parseIdeasUpdate.add_argument('content', help='This field cannot be blank', required=True)
parseIdeasUpdate.add_argument('impact', help='This field cannot be blank', required=True)
parseIdeasUpdate.add_argument('ease', help='This field cannot be blank', required=True)
parseIdeasUpdate.add_argument('confidence', help='This field cannot be blank', required=True)

min_char = 8
max_char = 12
allchar = string.ascii_letters + string.punctuation + string.digits

def validate_number(impact, ease, confidence):
    for number in [impact, ease, confidence]:
        if number < 1 or number > 10:
            return "error"
    return "success"



class Ideas(Resource):
    @jwt_required
    def post(self):
        data = parseIdeasCreate.parse_args()
        content = data["content"]
        impact = int(data["impact"])
        ease = int(data["ease"])
        confidence = int(data["confidence"])
        validate_digits = validate_number(impact=impact,
                                            ease=ease,
                                            confidence=confidence)
        if "error" in validate_digits:
            return {"error": "Impact, Ease & Confidence values " \
                             "requires integer between 1 to 10, " \
                             "10 being the highest impact"}, 417
        average_score = (impact + ease + confidence)/3
        new_idea = IdeasModel(
            content=content,
            impact=impact,
            ease=ease,
            confidence=confidence,
            average_score=average_score
        )
        try:
            new_idea.save_to_db()
            return IdeasModel.return_by_id(id=new_idea.id), 201
        except:
            return {'message': "Something went wrong"}, 500


    @jwt_required
    def get(self, id=None):
        try:
           data = parseGetIdeas.parse_args()
        except:
            data = ""
            pass
        if "page" in data:
            return IdeasModel.return_by_page(page=int(data["page"])), 200
        else:
            return IdeasModel.return_by_page(page=1), 200

    @jwt_required
    def delete(self, id):
        if id:
            return IdeasModel.delete_by_id(id), 204
        else:
            return {'message': 'ID cannot be empity'}, 404

    @jwt_required
    def put(self, id):
        data = parseIdeasUpdate.parse_args()
        validate_digits = validate_number(impact=int(data["impact"]),
                                          ease=int(data["ease"]),
                                          confidence=int(data["confidence"]))
        if "error" in validate_digits:
            return {"error": "Impact, Ease & Confidence values " \
                             "requires integer between 1 to 10, " \
                             "10 being the highest impact"}, 417
        if id:
            return IdeasModel.update_by_id(id=id,
                                           content=data["content"],
                                           impact=int(data["impact"]),
                                           ease=int(data["ease"]),
                                           confidence=int(data["confidence"])), 200
        else:
            return {'message': 'ID cannot be empity'}, 404

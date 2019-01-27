from flask_restful import Resource, reqparse
from model.user import UserModel
from model.auth import RevokedTokenModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

parserUserLogin = reqparse.RequestParser()
parserUserLogin.add_argument('email', help ='This field cannot be blank', required = True)
parserUserLogin.add_argument('password', help ='This field cannot be blank', required = True)

parserRefreshToken = reqparse.RequestParser()
parserRefreshToken.add_argument('refresh_token', help ='This field cannot be blank', required = True)


class UserLogin(Resource):
    def post(self):
        data = parserUserLogin.parse_args()
        current_user = UserModel.find_by_email(email=data['email'])

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['email'])}, 401

        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['email'])
            refresh_token = create_refresh_token(identity = data['email'])
            return {
                       'jwt': access_token,
                       'refresh_token': refresh_token
                   }, 201
        else:
            return {'message': 'Wrong credentials'}, 401

    def delete(self):
        data = parserRefreshToken.parse_args()
        refresh_token = data['refresh_token']
        try:
            revoked_token = RevokedTokenModel(jti = refresh_token)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}, 204
        except:
            return {'message': 'Something went wrong'}, 500

class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    #@jwt_refresh_token_required
    def post(self):
        data = parserRefreshToken.parse_args()
        #current_user = get_jwt_identity()
        access_token = create_access_token(identity = data["refresh_token"])
        return {'jwt': access_token}

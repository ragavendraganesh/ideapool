from app import app, jwt, api_flask, db
import model.auth as auth_model
from repository.auth import *
from repository.user import *
from repository.ideas import *
import secrets


api_flask.add_resource(UserRegistration, '/users')
api_flask.add_resource(UserLogin, '/access-tokens')
api_flask.add_resource(UserLogoutAccess, '/logout/access')
api_flask.add_resource(UserLogoutRefresh, '/logout/refresh')
api_flask.add_resource(TokenRefresh, '/access-tokens/refresh')
api_flask.add_resource(UserDetails, '/me')
api_flask.add_resource(Ideas, '/ideas', '/ideas/<string:id>')


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return auth_model.RevokedTokenModel.is_jti_blacklisted(jti)


if __name__ == '__main__':
    port = os.getenv('PORT')
    #createDatabase()
    app.run(host='0.0.0.0', port=port, use_reloader=True, debug=True)

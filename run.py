from app import app, jwt, api_flask, db
import model.auth as auth_model
from repository.auth import *
from repository.user import *
import secrets


api_flask.add_resource(UserRegistration, '/registration')
api_flask.add_resource(UserLogin, '/access-tokens')
api_flask.add_resource(UserLogoutAccess, '/logout/access')
api_flask.add_resource(UserLogoutRefresh, '/logout/refresh')
api_flask.add_resource(TokenRefresh, '/access-tokens/refresh')
api_flask.add_resource(Users, '/users', '/users/<int:id>')
api_flask.add_resource(UserDetails, '/me')


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return auth_model.RevokedTokenModel.is_jti_blacklisted(jti)


def createDatabase():
    if not os.path.isfile(os.getcwd() + '/login-flask-restfull.db'):
        try:
            db.create_all()
            """
            admin_psw = secrets.token_hex(nbytes=16)
            new_user = UserModel(
                name="admin",
                surname="of system",
                cpf="11111111111",
                email="admin@admin.com",
                password=UserModel.generate_hash(admin_psw),
            )
            new_user.save_to_db()
            print("\nuser: admin | password: {admin_psw}\n")
            """
        except Exception as e:
            print(e)


if __name__ == '__main__':
    createDatabase()
    app.run(host='0.0.0.0', use_reloader=True, debug=True)

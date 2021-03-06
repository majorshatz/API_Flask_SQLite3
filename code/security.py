from user import User
#compare strings
from werkzeug.security import safe_str_cmp

def authenticate(username,password):
    user=User.find_by_username(username)#changed to use def from user
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    #payload contents of jwt token
    user_id=payload['identity']
    return User.find_by_id(user_id)

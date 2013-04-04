from getpass import getpass
from models.user import User

class LoginController:
  def login(self):
    username = raw_input('Username:')
    password = getpass('Password:')
    user = User.find_by_username(username)
    return user and user.authenticate(password)

  def show(self):
    pass

import os


class User(object):
    """Encapsulates the attributes of an user"""
    def __init__(self):
        self._user = None
        self._pwd = None
        self._logged_in = False
        self.get_credentials()

    def get_credentials(self):
        self._user = raw_input('Enter user name >> ')
        self._user = str(self._user)

        # Validate user
        if not PasswordManager.is_user_exists(self._user):
            return 0

        self._pwd = raw_input('Enter password >> ')
        self._pwd = str(self._pwd)

    def login(self):
        if not self._user or not self._pwd:
            print("Cannot login unless you enter a valid username or password!")
            return 0

        # Validate password
        if not PasswordManager.is_password_valid(self._user, self._pwd):
            return 0

        # Set login flag
        self._logged_in = True

        print("Logged in as user: {}".format(self._user))
        return 1

    def get_name(self):
        return self._user

    def is_logged_in(self):
        if not self._logged_in:
            print("User '{}' is not logged in.".format(self._user))
            return False

        print("User '{}' logged in.".format(self._user))
        return True

    def logout(self):
        if not self.is_logged_in():
            return 0

        # Clear user credentials
        self._logged_in = False

        print ("Logged out successfully!")
        return 1


class PasswordManager(object):
    """Encapsulates password related operations"""
    password_file = 'passwords.csv'

    def __init__(self):
        self.load_password_file()

    @staticmethod
    def load_password_file():
        if not os.path.exists(PasswordManager.password_file):
            open(PasswordManager.password_file, 'w').close()
        return 1

    @staticmethod
    def create_user():
        username = raw_input('Enter user name >> ')
        password = raw_input('Enter user password >> ')

        credentials = "\n{username},{password}".format(username=username,
                                                       password=password)

        try:
            with open(PasswordManager.password_file, 'a') as file_obj:
                file_obj.write(credentials)
                print("Password successfully saved!")
                return 1
        except Exception as e:
            print("Failed to create password:")
            print(e)
            return 0

    @staticmethod
    def is_user_exists(username):
        if username in open(PasswordManager.password_file).read():
            return True

        print("User does not exist: {}".format(username))
        return False

    @staticmethod
    def is_password_valid(username, password):
        with open(PasswordManager.password_file) as file_obj:
            for line in file_obj:
                if username in line:
                    pwd = line.rstrip('\n').split(',')[1]
                    if pwd == password:
                        return True
                    else:
                        print("Password doesn't match!")
                        return False


class FileMonitor(object):
    def __init__(self, filename):
        self._cached_stamp = 0
        self._filename = filename
        self._counter = 0

    def monitor(self):
        """Polls the file for any modification"""
        stamp = os.stat(self._filename)

        if stamp != self._cached_stamp or not self._counter:
            self._cached_stamp = stamp
            self._counter += 1
            return True

        return False

if __name__ == '__main__':
    while True:
        user = User()
        user.login()
        user.logout()
        user.is_logged_in()
        user.login()
        user.is_logged_in()
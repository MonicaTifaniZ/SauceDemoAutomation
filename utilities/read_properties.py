import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\LoginConfig.ini")

class Read_Config:
    @staticmethod
    def get_url_web():
        url = config.get('login user info','url_web')
        return url
    
    @staticmethod
    def get_username():
        username = config.get('login user info','username')
        return username
    
    @staticmethod
    def get_password():
        password = config.get('login user info','password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('login user info','invalid_username')
        return invalid_username
    
    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('login user info','invalid_password')
        return invalid_password

    @staticmethod
    def get_invalid_credential():
        error_invalid_credential = config.get('login user info','ERROR_INVALID_CREDENTIALS')
        return error_invalid_credential

    @staticmethod
    def get_error_username_required():
        error_username_required = config.get('login user info', 'ERROR_USERNAME_REQUIRED')
        return error_username_required

    @staticmethod
    def get_error_password_required():
        error_password_required = config.get('login user info', 'ERROR_PASSWORD_REQUIRED')
        return error_password_required
import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

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
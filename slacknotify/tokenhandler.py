import keyring

class TokenHandler():
    '''
    Utility class to wrap token functions.
    '''
    
    def __init__(self, token=None):
        self.system = 'jupyter_to_slack_bot'
        self.user = 'token'
        if token is not None:
            self.set_token(token)


    def check_token(self):
        token = keyring.get_password(self.system, self.user)
        if token is None:
            print('Token not set')
        else:
            print('Token = {}'.format(token))
    

    def get_token(self):
        token = keyring.get_password(self.system, self.user)
        if token == None:
            raise Exception('\nSlack Bot User OAuth Access Token is not set.\nPlease set it with TokenHandler().set_token()')
        return token
    
    
    def set_token(self, token):
        keyring.set_password(self.system, self.user, token)
        
    
    def delete_token(self):
        try:
            keyring.delete_password(self.system, self.user)
            print('Token deleted')
        except Exception as e:
            print('Nothing to delete')
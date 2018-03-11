from slackclient import SlackClient
from .tokenhandler import TokenHandler

class SlackNotify():

    def __init__(self, name):
        token = TokenHandler().get_token()
        self.sc = SlackClient(token)
        self.name = name
        self.id = self.get_id(name)
        if self.id is None:
            raise Exception('Can\'t find user {}'.format(name))
            

    def get_id(self, name):
        response = self.sc.api_call("users.list")
        
        if not response['ok']:
            raise Exception('API error: {}\nCheck if your Bot User OAuth Access Token is correct'.format(response['error']))
            
        user_list = response['members']
        for user in user_list:
            profile = user['profile']

            if profile['display_name'] != '':
                if profile['display_name'] == name:
                    return user['id']

            elif profile['real_name'] == name:
                return user['id']

        return None

    def send(self, text, user=None):
        if user is None:
            user = self.id
        self.sc.api_call(
            "chat.postMessage",
            channel=user,
            text=text,
            as_user='True'
        )
        
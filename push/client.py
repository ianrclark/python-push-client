import hashlib
from pusher.pusher import Pusher

__author__ = 'gcumming'

class PushClient:

    @staticmethod
    def channel_for_user(user_id, salt):
        return hashlib.md5(':'.join([unicode(user_id), salt])).hexdigest()

    def __init__(self, channel_salt, app_id=None, key=None, secret=None, **options):
        self.channel_salt = channel_salt
        self.pusher = Pusher(app_id, key, secret)

    def send_to_user(self, user_id, event_name, data):
        channel = PushClient.channel_for_user(user_id, self.channel_salt)
        self.pusher.trigger([channel], event_name, data)

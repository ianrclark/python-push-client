import hashlib
import unittest
from push.client import PushClient


class TestClient(unittest.TestCase):

    def test_channel(self):
        salt = PushClient.channel_for_user("12345","salty salt")
        expected = hashlib.md5("12345:salty salt").hexdigest()
        self.assertEqual(salt, expected)

        salt = PushClient.channel_for_user(12345, "salty salt")
        self.assertEqual(salt, expected)


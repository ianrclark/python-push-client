import ConfigParser
import argparse
import os
from push.client import PushClient


def main():
    parser = argparse.ArgumentParser(description='Send a sample push message')

    parser.add_argument('user_id', type=unicode,
                       help='user_id to send to')
    parser.add_argument('event_name', type=unicode,
                       help='Event Name')
    parser.add_argument('payload', type=unicode,
                       help='Payload to send')

    args = parser.parse_args()

    config = ConfigParser.ConfigParser()
    config.read(['pusher.cfg', os.path.expanduser('~/.pusher.cfg')])
    if config.has_section("Pusher"):
        config.get("Pusher", "app_id")
        client = PushClient(config.get("Pusher", "salt"),
                   app_id=config.get("Pusher", "app_id"),
                   key=config.get("Pusher", "key"),
                   secret=config.get("Pusher", "secret"))

        client.send_to_user(args.user_id, args.event_name, args.payload)

    else:
        print("No pusher config was found, looking for pusher.cfg or ~/.pusher.cfg")
        quit(code=-2)

if __name__ == '__main__':
    main()
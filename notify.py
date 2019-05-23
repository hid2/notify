import json

import requests


def discord_notify(url, message):
    """
    Discord send message.

    Args:
        url (str): discord webhook url.
        message (str): message.
    """
    if url:
        requests.post(url,
                      data={'content': message})


def slack_notify(url, message):
    """
    Slack send message.

    Args:
        url (str): slack incoming-webhook url.
        message (str): message.
    """
    if url:
        requests.post(url,
                      data=json.dumps({'text': message}))


def line_notify(token, message):
    """
    LINE send message.

    Args:
        token (str): line notify token.
        message (str): message.
    """
    LINE_NOTIFY_URL = 'https://notify-api.line.me/api/notify'
    if token:
        requests.post(LINE_NOTIFY_URL,
                      headers={'Authorization': 'Bearer {}'.format(token)},
                      data={'message': '\n{}'.format(message)})


if __name__ == '__main__':
    # example
    DISCORD_URL = ''
    SLACK_URL = ''
    LINE_TOKEN = ''
    discord_notify(DISCORD_URL, 'Discord test message\nDiscord Hello.')
    slack_notify(SLACK_URL, 'Slack test message\nSlack Hello.')
    line_notify(LINE_TOKEN, 'LINE test message\nLINE Hello.')

from slacker import Slacker

def slack_notify(text=None, channel='#it_news', username='알림봇', attachments=None):
    token = "xxxxxxxx"
    slack = Slacker(token)
    slack.chat.post_message(
      text=text,
      channel=channel,
      username=username,
      attachments=attachments
    )



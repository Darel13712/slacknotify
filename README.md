# SlackNotify
This is a simple package to send yourself a message in slack from python.

You need to have a Slack Bot User installed in your Slack workspace.

## Installation
`pip install slacknotify`

## Usage
First time you launch it you have to set up your Slack Bot User OAuth Access Token. Otherwise just initialize it with your name in Slack. It checks your display name and if it is absent checks real name.

```
from slacknotify import SlackNotify, TokenHandler
handler = TokenHandler()
handler.set_token('slack_token')
notify = SlackNotify('username')
notify.send('Hello from python!')
```
You can use TokenHandler class to manage your token and delete it.
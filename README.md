Discord Utility Bot

A multi-purpose Discord bot built with discord.py, featuring reminders, polls, user info lookup, and moderation tools.

Features:
   1) !remind <minutes> <message> — Sends you a DM reminder after a specified number of minutes.
   2) !poll <question>? <choice1> <choice2> ... — Creates a poll with up to 10 options, automatically adding numbered reactions for voting.
   3) !userinfo [@user] — Displays info about a server member, including join date, roles, and avatar. Defaults to the command author if no user is mentioned.
   4) !clear <amount> — Bulk-deletes a specified number of messages from a channel. Requires the "Manage Messages" permission.

Technologies Used:
   1) Python 3
   2) discord.py
   3) python-dotenv

Notes:
   This bot requires the Message Content Intent to be enabled in the Discord Developer Portal, and the Manage Messages permission for the !clear command to function correctly.

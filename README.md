Discord Utility Bot

A multi-purpose Discord bot built with discord.py, featuring reminders, polls, user info lookup, and moderation tools. Built as a portfolio project to demonstrate Python and API integration skills.

Features


!remind <minutes> <message> — Sends you a DM reminder after a specified number of minutes.
!poll <question>? <choice1> <choice2> ... — Creates a poll with up to 10 options, automatically adding numbered reactions for voting.
!userinfo [@user] — Displays info about a server member, including join date, roles, and avatar. Defaults to the command author if no user is mentioned.
!clear <amount> — Bulk-deletes a specified number of messages from a channel. Requires the "Manage Messages" permission.


Setup


Clone the repository:


bash   git clone https://github.com/malliaras/discord-bot.git
   cd discord-bot


Create a virtual environment and activate it:


bash   python3 -m venv discordbot-env
   source discordbot-env/bin/activate


Install dependencies:


bash   pip install -r requirements.txt


Create a .env file in the project root with your bot token:


   TOKEN=your_discord_bot_token_here


Run the bot:


bash   python3 bot.py

Technologies Used


Python 3
discord.py
python-dotenv


Notes

This bot requires the Message Content Intent to be enabled in the Discord Developer Portal, and the Manage Messages permission for the !clear command to function correctly.

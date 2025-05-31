🧪 Test-Bot
Test-Bot is an experimental Telegram-boot based on Aiogram 3, created for the sake of tests, experiments and funny rakes. If you are looking for the perfect code - you are not at the address, but if you want to see how the asynchronous bot on Python works - welcome!

🚀 Opportunities
Asynchronous work on the basis of Aiogram 3
Database connection via SQLALCHEMY (ASYNC)

Telegram ID registration of users

Flexible architecture: routers, separate modules, database

Logging off the bot (so as not to forget that it has turned off)

Great platform for experiments and training

🛠️ Fast start
Clon the repository:

Bash
_Git Clone https: // github.
COM/NATSUNESH/Test-BOT.GIT_
CD Test-Bot
Set the dependencies:

Bash
Pip Install -r Requirements.txt
Set up a bot token

Insert your Telegram Bot Token into Main.py (or, if not laziness, bring it to the environment variables).

Launch the bot:

Bash
Python Main.py
If you see the Bot Is Off, then you pressed Ctrl+C and everything works as planned!
📦 Project structure
Main.py - entrance point, launch of the bot, initialization of the base

App/handler - routers and team handlers

App/Database/Models.py - asynchronous models and functions for working with database

REQUESS.PY - functions for working with users (for example, adding by TG_ID)

🧩 Code example
`
Async Def set_user (tg_id):
Async with async_Session () As Session:
        User = AWAIT SESSION.SCALAR (Select (user) .where (user.tg_id == tg_id))
        if not user:
            session.add (user (tg_id = tg_id))
            AWAIT SESSION.commit ()
`
🤔 Why do you need it?
Learn to write asynchronous bots on python

Experiment with Aiogram 3 architecture
Check integration with the database

Just indulge

📝 License
MIT - do what you want, just do not forget about tokens!

💬 Feedback
If you suddenly want to improve something or just write "Hello"-create Issue or Pull Request.


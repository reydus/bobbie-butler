Bobbie Butler 
=====================

Bobbie Butler is a Python-based bot for Matrix rooms.
It is based on Shawnanastasio's [python-matrix-bot-api](https://github.com/shawnanastasio/python-matrix-bot-api)

Requires the [matrix-python-sdk](https://github.com/matrix-org/matrix-python-sdk).

Running
--------

This bot uses Python3. I recommend running this bot by using the Python environment included by activating it:

```
source venv/bin/activate
```

Then run the bot by using:

```
python start.py
```

Alternatively, use `nohup` to run in the background. Output will be found in `bobbie.log`:

```
nohup python -u start.py > bobbie.log &
```
Capabilities
------------

Currently, this bot is being developed and it is logged in as @bot:reyd.us sometimes. For
testing purposes, you can use Shawnanastasio's tests

    Test it out by adding it to a group chat and doing one of the following:
    1. Say "Hi"
    2. Say !echo this is a test!
    3. Say !d6 to get a random size-sided die roll result


Contributing
------------
I am quite new at making bots to work on the Matrix ecosystem.
If you know of any improvements, solutions or other concerns, why not text me at @reydus:reyd.us?
You are more than welcome to submit pull requests.

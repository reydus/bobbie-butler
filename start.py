#!/usr/bin/env python3
import wikipedia
import random
import yaml
from matrix_bot_api.matrix_bot_api import MatrixBotAPI
from matrix_bot_api.mregex_handler import MRegexHandler
from matrix_bot_api.mcommand_handler import MCommandHandler

# Load configuration from YAML

config = open('config.yaml', 'r')
config = yaml.load(config, Loader=yaml.FullLoader)
USERNAME = config["username"]
PASSWORD = config["password"]
SERVER = config["homeserverUrl"]


def hi_callback(room, event):
    # Somebody said hi, let's say Hi back
    print("Someone greeted me.")
    room.send_text("Hi, " + event['sender'])


def echo_callback(room, event):
    args = event['content']['body'].split()
    args.pop(0)

    # Echo what they said back
    room.send_text(' '.join(args))


def dieroll_callback(room, event):
    # someone wants a random number
    args = event['content']['body'].split()

    # we only care about the first arg, which has the die
    die = args[0]
    die_max = die[2:]

    # ensure the die is a positive integer
    if not die_max.isdigit():
        room.send_text('{} is not a positive number!'.format(die_max))
        return

    # and ensure it's a reasonable size, to prevent bot abuse
    die_max = int(die_max)
    if die_max <= 1 or die_max >= 1000:
        room.send_text('dice must be between 1 and 1000!')
        return

    # finally, send the result back
    result = random.randrange(1,die_max+1)
    room.send_text(str(result))
def wikipedia_callback(room, event):
    args = event['content']['body'].split()
    args.pop(0) #Erase command call, leave page name.
    args = " ".join(args)
    if args == "":
        room.send_text(event["sender"]+": If you want to inquiry about a Wikipedia page, you should probably tell me which one by typing ;wikipedia <name of the page>")
        return None
    
    try:
        print("Received wikipedia enquiry for page "+args)
        text = wikipedia.summary(args, sentences = 3)
        print("Which narrates..."+text)
        room.send_text(text)
    except wikipedia.exceptions.DisambiguationError as err:
        options = err
        options = str(options).split("\n")
        options.pop(0)
        room.send_text("Ambiguous page, try typing a more exact page title? Perhaps you meant "+str(options[0:3])[1:-1])
    
def main():
    # Create an instance of the MatrixBotAPI
    bot = MatrixBotAPI(USERNAME, PASSWORD, SERVER)
    #general_command_handler = MRegexHandler(";", commandHandler)

    # Add a regex handler waiting for the word Hi
    hi_handler = MRegexHandler("Hi", hi_callback)
    bot.add_handler(hi_handler)

    # Add a regex handler waiting for the echo command
    echo_handler = MCommandHandler("echo", echo_callback)
    bot.add_handler(echo_handler)

    # Add a regex handler waiting for the die roll command
    dieroll_handler = MCommandHandler("d", dieroll_callback)
    bot.add_handler(dieroll_handler)

    wikipedia_handle = MCommandHandler("wikipedia",wikipedia_callback)
    bot.add_handler(wikipedia_handle)
    # Start polling
    bot.start_polling()

    # Infinitely read stdin to stall main thread while the bot runs in other threads
    while True:
        abc = "abc" # MODIFIED


if __name__ == "__main__":
    main()

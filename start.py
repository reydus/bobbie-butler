

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
    args = args.pop(0) #Erase command call, leave page name.
    page = "_".join(args) # Join using underscores.
    page = ""

def commandHandler(room, event):
    #args = event['content']['body'].split()

    if event['content']['body'][0] != ";":  # Exit Handler if first character isn't ";"
        return None
    
    args = event['content']['body'].split()
    command = args[0][1:]   # skip ";" at the beginning.
    args.remove(";"+command)
    print("Detected command "+command+" with args "+args)

def main():
    # Create an instance of the MatrixBotAPI
    bot = MatrixBotAPI(USERNAME, PASSWORD, SERVER)
    general_command_handler = MRegexHandler(";", commandHandler)

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
    # Start polling
    bot.start_polling()

    # Infinitely read stdin to stall main thread while the bot runs in other threads
    while True:
        input()


if __name__ == "__main__":
    main()

import math
import requests
import json

commands = {
    "hi": "Says hi. hi",
    "say": "Says something. say *[message]",
    "dosquareroot": "Does the square root of a (rational) (real) number. dosquareroot *[message]",
    "ipinfo": "Looks up an IP Address. ipinfo *[message]",
    "ascii_figure": "Prints an ASCII. ascii_figure",
    "creator": "Prints creator. creator.",
    "help": "Prints list of commands if you type number, or a specific one. [command]"
}

def help(command, data):
    if (command == " "):
        for item in commands:
            data["channel"].sendMessage("{command}:   {help}".format(command = item, help = commands[item]))
    
    else:
        data["channel"].sendMessage("{command}:   {help}".format(command = command, help = commands[command]))

def hi(command, data):
    data["channel"].sendMessage("Hello, there")

def say(to_say, data):
    data["channel"].sendMessage(to_say)

def dosquareroot(number, data):
    data["channel"].sendMessage(math.sqrt(int(number)))

def ascii_figure(command, data):
    for line in open("ascii.txt", "r").readlines():
        data["channel"].sendMessage(line)

def ipinfo(ipaddr, data):
    json_ar = json.loads(requests.get("https://ipinfo.io/{ip}".format(ip = ipaddr)).text)

    for key in json_ar:
        data["channel"].sendMessage("{key}:{value}".format(key = key, value = json_ar[key]))



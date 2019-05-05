import os
import sys

import csv
from io import StringIO
#import csv

import json

import threading
from libqchatterpy import *
import libqchatterpy.QChatterUser
import libqchatterpy.QChatterChannel 

import math
import readline
import commands

def on_message(login, channel):
    while True:
        try:
            messages = json.loads(login.obtainUserMessageFromChannel(channel.channel))
            if (messages == 50000):
                continue

            for message in messages:
                if (str(message) != "50000"):
                    json_decode = message
                    title = json_decode["title"]
                    title_status = json_decode["title_status"]
                    content = json_decode["content"]
                    #Decoding information

                    if (title != login.username):
                        if (content.startswith("$")):
                            f = StringIO(content)
                            reader = csv.reader(f, delimiter=' ')
                            command = []
                            # Using CSV to parse, allows us to enclose text with quotes for spaces.

                            for item in reader:
                                command.append(item)
                            # No other way to convert csvreader object into list ):

                            command = command[0] # for some reason it is in an array

                            if (command[1] not in commands.commands): # if the command is not in the command list
                                channel.sendMessage("Command not found.")
                                continue

                            data = {
                                "channel": channel,
                                "login": login,
                                "title": title,
                                "title_status": title_status,
                                "content": content
                            } # Pass these objects/string to our function as a dictionary for neat packaging.


                            exec_s = "commands.{function}({args}data)" # Build the function
                            function = command[1]

                            args = ""

                            for item in command[2:]:
                                args = args + '"' + item + '",'
                            
                            if (args == ""):
                                args = '" ",'

                            #print(exec_s.format(function = function, args = args))
                            exec(exec_s.format(function = function, args = args)) # Execute it. Hopefully it has not been hijacked. It ONLY allows commands from a certain file.
                            # DANGER ONE FUCK UP AND YOU COULD BE RM -RF'D 
                            
                            

        except Exception as ex:
                print(ex)
                pass

username = "bot" # A public bot account. Don't misuse! Create your own using QChatterPyClient and the --register-bot argument. Or register with cURL. 
password = "3313"

r_channel = input("Channel: ")

login = libqchatterpy.QChatterUser.QChatterUser(username, password)
channel = libqchatterpy.QChatterChannel.QChatterChannel(r_channel, login)

login.joinChannel(channel.channel)

threading._start_new_thread(on_message, (login, channel,))
readline.parse_and_bind("tab: complete")
while True:
    to_execute = input("cmd>")

    data = {
        "channel": channel,
        "login": login,
        "title": login.username,
        "title_status": 2,
        "content": to_execute
    } # Pass these objects/string to our function as a dictionary for neat packaging.
    
    try:
        exec(to_execute)
    except Exception as ex:
        print(ex)
        pass

